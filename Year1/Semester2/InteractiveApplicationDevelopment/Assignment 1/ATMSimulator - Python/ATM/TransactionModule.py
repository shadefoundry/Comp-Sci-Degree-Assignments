class Transaction:
    """Represents a banking transaction performed on a bank account. Two transaction types are supported: deposit and withdrawal
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation

    """Constant that represents a deposit transaction"""
    TYPE_DEPOSIT = 1

    """Constant that represents a withdrawal transaction"""
    TYPE_WITHDRAWAL = 2

    """Represents a banking transaction"""
    def __init__(self, type=0, amount=0.0, originalBalance=0.0, newBalance=0.0):
        """Constructor that allows the initialization of the transaction field variables
        
        NOTE: the constructor assigns default values to each parameter allowing the code
        not to supply them (i.e. trans = Transaction()). If the calling code does not supply
        values for the two parameters they will receive these default values. This is used
        when the accounts are created from data files 
        """

        self._type = type
        self._amount = amount
        self._originalBalance = originalBalance
        self._newBalance = newBalance

    def getType(self):
        """Return the type of transaction"""
        return self._type

    def getAmount(self):
        """Return the amount that was involved in the transaction"""
        return self._amount

    def getOriginalBalance(self):
        """Return the original balance before the transaction was performed"""
        return self._originalBalance

    def getNewBalance(self):
        """Return the balance after the transaction was performed"""
        return self._newBalance

    def __str__(self):
        """Default built-in method that is called automatically when a transaction object is printed"""
        trans = "Withdrawal" if self._type == Transaction.TYPE_WITHDRAWAL else "Deposit"
        return '{0}: Amount = {1}, Original Balance = {2}, New Balance = {3}'.format(trans, self._amount, self._originalBalance, self._newBalance)

    def load(self, file):
        """Load the the transaction information from the given file
        Arguments:
            file - the file containing the encoded transaction data. The file is assumed opened and pointing to the transaction data
        """
        #load the encoded information
        transInfo = file.readline().rstrip('\n')

        #decode the information
        transPartList = transInfo.split('~')
        
        #assign the transaction properties
        self._type = transPartList[0]
        self._amount = float(transPartList[1])
        self._originalBalance = float(transPartList[2])
        self._newBalance = float(transPartList[3])

    def save(self, file):
        """Save the transaction information into the given file
        Arguments:
            file - the file where the transaction information needs to be saved
        """
        #we would like the entire transaction to be written on one line so the information
        #needs to be encoded
        transInfo = '{0}~{1}~{2}~{3}'.format(self._type, self._amount, self._originalBalance, self._newBalance)
        file.write(transInfo + '\n')
