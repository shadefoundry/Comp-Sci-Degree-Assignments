using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class Bank: Account
    {
        List<int> _accountList = new List<int>();
        int DEFAULT_ACCT_NO_START = 100;
        //TODO: Implement Load and Save methods for Bank.cs
        //load the account data from a file
        public void LoadAccountData() {}
        //save account data to file
        public void SaveAccountData() { }
        public void CreateDefaultAccounts()
        {
            for (int iAccount = 1; iAccount <= 10; iAccount++)
            {
                //create a new default account with the required properties
                Account newDefAcct = new Account();
                int AccValue = DEFAULT_ACCT_NO_START + iAccount;
                //deposite some dosh
                newDefAcct.Deposite(100);
                //set the (rather high) default interest rate
                newDefAcct.SetAnnualIntrRate(2.5);
                //add the account to the list
                _accountList.Add(AccValue);
            }
        }
        public int FindAccounts(int _acctNo) {
            foreach (int acct in _accountList){
                if (GetAccountNumber(acct) == _acctNo)
                {
                    return acct;
                }
            }
            //if the program got to this point then no account with given number exists
            return 0;
        }
        public int DetermineAccountNumber(){
            while (true){
                try
                {
                    int acctNoInput = 0;
                    Console.WriteLine("Please Enter the Account Number [100 - 1000] or press [ENTER] to cancel: ");
                    acctNoInput = Convert.ToInt32(Console.ReadLine());

                    if (acctNoInput == 0) {
                        throw new OperationCancel("User selected to terminate the progra after invalid input");
                    }
                    _acctNo = acctNoInput;
                    if (_acctNo < 100 || _acctNo > 1000) {
                        throw new InvalidValue("The account entered is not valid. Please enter a valid number");
                    }
                    for (int account = 1; account <= _accountList.Count; account++) {
                        if (_acctNo == GetAccountNumber(account)) {
                            throw new InvalidValue("The account number entered already exists. Enter another number.");
                        }
                    }
                    return _acctNo;
                }
                catch (InvalidValue err) { Console.WriteLine(err); }
                catch (ArgumentException err) { Console.WriteLine(err); }
                
            }
        }
        public string OpenAccount(string clientName, int acctType) {
            int acctNo = DetermineAccountNumber();

            if (acctType == ACCOUNT_TYPE_CHECQUING) {
                Account newAccount = new ChecquingAccount();
                newAccount._acctHolderName = clientName;
            }
            else if (acctType == ACCOUNT_TYPE_SAVINGS) {
                Account newAccount = new SavingsAccount();
                newAccount._acctHolderName = clientName;
            }
            _accountList.Add(DetermineAccountNumber());
            return clientName;
        }
    }
    class OperationCancel : Exception {
        public OperationCancel(string message): base(message) { }
    }
}
