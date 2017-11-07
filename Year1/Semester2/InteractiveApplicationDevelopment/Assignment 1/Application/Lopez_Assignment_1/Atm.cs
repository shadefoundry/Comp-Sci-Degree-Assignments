using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class Atm:Account
    {
        //create the bank the atm works with
        Bank _bank = new Bank();
        //create the MAIN MENU options
        int SELECT_ACCOUNT_OPTION = 1;
        int CREATE_ACCOUNT_OPTION = 2;
        int EXIT_ATM_APPLICATION_OPTION = 3;
        //create the ACCOUNT MENU options
        int CHECK_BALANCE_OPTION = 1;
        int WITHDRAW_OPTION = 2;
        int DEPOSIT_OPTION = 3;
        int DISPLAY_TRANSACTIONS = 4;
        int EXIT_ACCOUNT_OPTIONS = 5;
        public void Start() {
            bool _start = true;
            while (_start == true){ int selectedOption = ShowMainMenu();
                if (selectedOption == SELECT_ACCOUNT_OPTION) {
                    int acct = SelectAccount();
                    if (acct != 0)
                    {
                        ManageAccount(acct);
                    }
                    else if (selectedOption == CREATE_ACCOUNT_OPTION)
                    {
                        OnCreateAccount();
                    }
                    else if (selectedOption == EXIT_ATM_APPLICATION_OPTION)
                    {
                        _bank.SaveAccountData();
                    }
                    else { Console.WriteLine("Please enter a valid option\n"); }
                }
            }
        }

        public int ShowMainMenu() {
            while (true)
            {
                try
                {
                    Console.WriteLine("\nMain Menu\n\n1: Select Account\n2: Create Account\n3: Exit\n\nEnter a choice:  ");
                    string choice = Console.ReadLine();
                    int _choice = int.Parse(choice);
                    return _choice;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Invalid value. Please enter a valid option.\n");
                }
            }
        }

        public int ShowAccountMenu() {
            while (true) {
                try
                {
                    Console.WriteLine("\nAccount Menu\n\n1: Check Balance\n2: Withdraw\n3: Deposit\n4: Display Transactions\n5: Exit\n\nEnter a choice: ");
                    int _choice = Convert.ToInt32(Console.ReadLine());
                    return _choice;
                }
                catch {
                    throw new InvalidValue("Please enter a valid menu option \n");
                }
            }
        }

        public void OnCreateAccount() {
            while (true) {
                try
                {
                    //get the name of account holder from user
                    string clientName = PromptForClientName();
                    //get initial deposit from user
                    double initDepositAmount = PromptForDepositeAmount();
                    //get annual interest rate
                    double annIntrRate = PromptForAnnualIntrRate();
                    //get account type from the user
                    int accType = PromptForAccountType();
                    //open the account
                    Account newAccount = new Account();
                    _bank.OpenAccount(clientName, accType);
                    //set the other account properties
                    newAccount.Deposite(initDepositAmount);
                    newAccount.SetAnnualIntrRate(annIntrRate);
                    //now the account has been successfully created and added to the bank
                    //the method is done
                    return;
                }
                catch (InvalidValue e) {
                    Console.WriteLine(e);
                }
                catch (OperationCancel e) {
                    Console.WriteLine(e);
                    return;//user has cancelled the creation of the account
                }
            }
        }

        public int SelectAccount() {
            while (true) {
                try {
                    int accNoInput = Convert.ToInt32(Console.ReadLine());
                    string _accNoInput = Convert.ToString(accNoInput);
                    //check to see if the user gave up and is cancelling the operation
                    if (_accNoInput.Length == 0) {
                        return 0;
                    }
                    //create a flat int of accNoInput so that we dont have a loop of readLines.
                    int acctNo = accNoInput;
                    //obtain the account required by the user from the bank
                    int acct = _bank.FindAccounts(acctNo);
                    if (acct != 0)
                    {
                        return acct;
                    }
                    else {
                        Console.WriteLine("The account was not found. Please select another account.");
                    }
                }
                catch (InvalidValue) {
                    //the use entered an invalid id, ex: abc
                    Console.WriteLine("Please enter a valid account number (ex: 100)\n");
                }
            }
        }

        public void ManageAccount(int account) {
            while (true) {
                int selAcctMenuOpt = ShowAccountMenu();
                if (selAcctMenuOpt == CHECK_BALANCE_OPTION) { OnCheckBalance(account); }
                else if (selAcctMenuOpt == WITHDRAW_OPTION) { OnWithdraw(account); }
                else if (selAcctMenuOpt == DEPOSIT_OPTION) { OnDeposite(account); }
                else if (selAcctMenuOpt==DISPLAY_TRANSACTIONS) { OnDisplayTransactions(account); }
                else if (selAcctMenuOpt==EXIT_ACCOUNT_OPTIONS) { return; }
                else{ Console.WriteLine("Please enter a valid menu option"); }
            }
        }

        public string PromptForClientName() {
            Console.WriteLine("Enter client name. Press [Enter] to cancel");
            string clientName = Console.ReadLine();
            if (clientName.Length == 0) {
                //user cancelled account creation
                throw new OperationCancel("User selected to cancel current operation");
            }
            return clientName;
        }

        public double PromptForDepositeAmount() {
            while (true) {
                try
                {
                    double initAmount = Convert.ToDouble(Console.ReadLine());
                    if (initAmount >= 0) { return initAmount; }
                    else { Console.WriteLine("Cannot create an account with negative initial balance, please enter valid amount."); }
                }
                catch (InvalidValue err) { Console.WriteLine(err); }
            }
        }

        public double PromptForAnnualIntrRate() {
            while (true) {
                try {
                    double intrRate = Convert.ToDouble(Console.ReadLine());
                    if (intrRate >= 0) { return intrRate; }
                    else { Console.WriteLine("Cannot read an account with a negative interest rate."); }
                }
                catch (InvalidValue err) { Console.WriteLine(err); }
            }
            
        }

        public int PromptForAccountType() {
            while (true) {
                Console.WriteLine("Please enter the account type [c/s] for chequing/savings respectively: ");
                string accTypeInput = Console.ReadLine();
                //the python code supports the letter c, and like 2 different spellings of chequing
                //We don't care though, we're going to force the user to input c/s or nothing.
                if (accTypeInput == "c") { return ACCOUNT_TYPE_CHECQUING; }
                else if (accTypeInput == "s") { return ACCOUNT_TYPE_SAVINGS; }
                else { Console.WriteLine("Answer not supported. Please enter one of supported answers [c/s]"); }
            }
        }

        public void OnCheckBalance(int account) {
            Console.WriteLine("The balance is " + GetBalance());
        }

        public void OnDeposite(int account) {
            while (true) {
                try
                {
                    Console.WriteLine("Enter amount to deposite. Press [ENTER] to exit.");
                    string inputAmount = Console.ReadLine();
                    //test for empty input in case the user pressed [enter] to give up
                    if (inputAmount.Length > 0)
                    {
                        double amount = Convert.ToDouble(inputAmount);
                        //check amount and raise errors if value is invalid will be checked in the catch below
                        Deposite(amount);
                    }
                    return;
                }
                catch (InvalidValue)
                {
                    //user must have entered invalid amount if we get to this
                    Console.WriteLine("Invalid entry. Enter a number for your amount.");
                }
                catch (InvalidTransaction err) {
                    //account must have refused to deposite amount.
                    Console.WriteLine(err);
                }
            }
        }

        public void OnWithdraw(int account) {
            while (true) {
                try
                {
                    Console.WriteLine("Please enter an amount to withdraw or hit [ENTER]] to exit: ");
                    string inputAmount = Console.ReadLine();
                    //check if we entered [enter]
                    if (inputAmount.Length > 0)
                    {
                        double amount = Convert.ToDouble(inputAmount);
                        // the account itself is responsible for checking the amount and raising any errors if the withdraw
                        // is not possible like negative amounts and balance overruns
                        Withdraw(amount);
                    }
                    return;
                }
                catch (InvalidValue)
                {
                    //user entered invalid, ex: abc
                    Console.WriteLine("Invalid entry. enter number for amount.");
                }
                catch (InvalidTransaction err) {
                    //account must have refused to withdraw entered amount. probably something like a negative
                    Console.WriteLine(err);
                }
            }
        }

        public void OnDisplayTransactions(int account) {
            Console.WriteLine("\n========= TRANSACTION LIST ==============\n");

            //display account type
            Console.WriteLine("Account No: " + GetAccountNumber(account));

            //display client name
            Console.WriteLine("Client: " + GetAcctHolderName());

            //display list of transactions performed on account
            foreach (double trans in GetTransactionList()) {
                Console.WriteLine(trans);
            }
        }
    }
}