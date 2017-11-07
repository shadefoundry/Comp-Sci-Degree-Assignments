"""Defines the Account class and used by the BankingApplication module."""

from TransactionModule import Transaction


class InvalidTransaction(Exception): 
    """Exception class used when an invalid trasaction is performed"""
    pass

class InvalidValue(Exception): 
    """Exception class used when an invalid value is detected"""
    pass

class Account:
    """
    Defines a bank account its associated attributes and operations.

    Attributes:
        _acctNo         : int   -- the account number, read-only attribute
        _acctHolderName : str   -- the name of the account holder, read-only attribute
        _balance        : float -- the account balance that gets affected by withdrawls and deposits
        _annualIntrRate : float -- the annual interest rate applicable on the balance
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation
    """constant representing a checquing account type"""
    ACCOUNT_TYPE_CHECQUING = 1

    """constant representing a savings account type"""
    ACCOUNT_TYPE_SAVINGS = 2

    def __init__(self, acctNo=-1, acctHolderName=''):
        """
        Initialize the account object with its attributes.

        The account constructor requires the caller to supply an account number and
        the name of the account holder in order to create an account. 

        NOTE: the constructor assigns default values to each parameter allowing the code
        not to supply them (i.e. acct = Account()). If the calling code does not supply
        values for the two parameters they will receive these default values. This is used
        when the accounts are created from data files 
        
        Arguments:
            acctNo          : int   -- the account number, required parameter
            acctHolderName  : str   -- the name of the account holder, required parameter
        """
        self._acctNo = acctNo
        self._acctHolderName = acctHolderName
        self._balance = 0.0
        self._annualIntrRate = 0.0
        self._transactionList = []

    def getAccountNumber(self):
        """Return the account number."""
        return self._acctNo

    def getAcctHolderName(self):
        """Return the account holder's name"""
        return self._acctHolderName

    def getBalance(self):
        """Return the balance in the account"""
        return self._balance
    
    def getAnnualIntrRate(self):
        """Return the annuaul interest rate on the account"""
        return self._annualIntrRate

    def setAnnualIntrRate(self, newAnnualIntrRatePercentage):
        """
        Change the annual interest rate on the account

        Arguments:
            newAnnualIntrRatePercentage: float -- the annual interest as a percentage (e.g. 3%)
        """
        self._annualIntrRate = newAnnualIntrRatePercentage / 100

    def getMonthlyIntrRate(self):
        """Calculate and return the monthly interest rate on the account"""
        return self._annualIntrRate / 12

    def getTransactionList(self):
        """Returns the list of transactions performed on this account"""
        return self._transactionList

    def deposit(self, amount):
        """Deposit the given amount in the account and return the new balance
        Arguments:
            amount - the amount to be deposited
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """

        #check that the amount is positive
        if amount < 0:
            raise InvalidTransaction( 'Invalid amount provided. Cannot deposit a negative amount.')
        
        #change the balance
        oldBalance = self._balance
        self._balance += amount

        #record the transaction
        self._transactionList.append(Transaction(Transaction.TYPE_DEPOSIT, amount, oldBalance, self._balance))

        #provide the new balance to the caller to avoid a getBalance() call
        return self._balance

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account and return teh new balance
        Arguments:
            amount - the amount to be withdrawn, cannot be negative or greater than available balance             
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """
        #pylint: disable=no-self-use, unused-argument
        if amount < 0:
            raise InvalidTransaction('Invalid amount provided. Cannot withdraw a negative amount.')

        if amount > self._balance:
            raise InvalidTransaction('Insufficient funds. Cannot withdraw the provided amount.')

        #change the balance
        oldBalance = self._balance
        self._balance -= amount
        
        #record the transaction
        self._transactionList.append(Transaction(Transaction.TYPE_WITHDRAWAL, amount, oldBalance, self._balance))

        #provide the new balance to the caller to avoid a getBalance() call
        return self._balance

    def predictStatement(self, monDep, monWithdr):
        """
        Calculate a monthly statement given the monthly deposits and withdrawals. 
        
        Arguments:
            monDep      : float -- monthly deposited amount (e.g. income)
            monWithdr   : float -- mothly withdrawal amount (e.g. bills)
        Return:
            statement : str
        """
        #start to predict balance and interest with the first month of the interest rate period (1 year)
        #and the current balance. The interest at the start of the period is zero. 
        month = 1
        predictedBalance = self._balance
        predictedInterest = 0
        stm = '\n============ Programming Principles Bank Statement ================\n\nAccount Number: {0}\nName:\t\t{1}\n'. \
                format(self._acctNo, self._acctHolderName)

        #repeat calculating predicted balance and interest for as long as there are months left in the year
        while month <= 12:
            #update the predicted balance with the monthly deposit and monthly withdrawal
            predictedBalance = predictedBalance + monDep - monWithdr

            #update the predicted interest which is calculated on balance only (no compounding)
            monthlyInterest = predictedBalance * self.getMonthlyIntrRate()
            predictedInterest = predictedInterest + monthlyInterest

            #update the statement
            stm = stm + '\nMonth {0}:\n\tBalance: {1}\n\tInterest: {2}\n'.format(month, predictedBalance, predictedInterest)

            #go to the next month
            month = month + 1
        
        #compute the final balance by adding the interest and complete the statement
        predictedBalance = predictedBalance + predictedInterest
        stm = stm + '\n\nEnd of Year Balance:{0}'.format(predictedBalance) 
        stm = stm + '\n\n================================================================' 
        
        return stm

    def load(self, file):
        """Load the account information from the given file. The file is assumed opened
        Arguments:
            file - the file containing the account information
        """
        #read the account properties in the same order they were saved
        self._acctNo = int(file.readline().rstrip('\n'))
        self._acctHolderName = file.readline().rstrip('\n')
        self._balance = float(file.readline().rstrip('\n'))
        self._annualIntrRate = float(file.readline().rstrip('\n'))

        #read the transaction list
        transCount = int(file.readline().rstrip('\n'))
        for iTrans in range(transCount):
            trans = Transaction()
            trans.load(file)
            self._transactionList.append(trans)
        

    def save(self, file):
        """Save the account information in the given file. The file is assumed opened
        Arguments:
            file - the file to contain the account information
        """
        #write the account properties, one per line
        file.write(str(self._acctNo) + '\n')
        file.write(str(self._acctHolderName) + '\n')
        file.write(str(self._balance) + '\n')
        file.write(str(self._annualIntrRate) + '\n')

        #write the number of transactions and the list of transactions
        file.write(str(len(self._transactionList)) + '\n')
        for trans in self._transactionList:
            trans.save(file)