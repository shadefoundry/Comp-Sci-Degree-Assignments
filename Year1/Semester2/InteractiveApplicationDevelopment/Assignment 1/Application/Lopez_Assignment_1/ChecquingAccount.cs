using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class ChecquingAccount: Account
    {
        double MAX_INTEREST_RATE = 1.0;
        double OVERDRAFT_LIMIT = 500;
        int acctNo = -1;
        string acctHolderName = "";
        Account _ChecquingAccount = new ChecquingAccount();
        //different name because im too lazy to set things up in a non-dirty way
        //should all work the same though
        public void setAnnualIntrRate(double newAnnualInterRatePercentage) {
            //check to ensure the annual intrerest rate is valid for a checking account
            if (newAnnualInterRatePercentage > MAX_INTEREST_RATE) {
                //if the new annual interest rate is too damn high, we throw an exception.
                throw new ArgumentOutOfRangeException("A checquing account cannot have an interest rate greater than {0}",System.Convert.ToString(MAX_INTEREST_RATE)); }
            //use the account class to set the annual interest rate
            SetAnnualIntrRate(newAnnualInterRatePercentage);
        }
        public double Withdraw(double amount) {
            if (amount < 0) {
                throw new ArgumentOutOfRangeException("Invalid amount provided. Cannot withdraw a negative amount.");
            }
            if (amount > _balance + OVERDRAFT_LIMIT) {
                throw new ArgumentOutOfRangeException("Insufficient funds. Cannot withdraw the provided amount.");
            }
            //change the balance
            double oldBalance = _balance;
            _balance -= amount;
            //record the transaction, apparently I don't get to do them all on one line -.-
            _transactionList.Add(TYPE_WITHDRAWAL);
            _transactionList.Add(amount);
            _transactionList.Add(oldBalance);
            _transactionList.Add(_balance);
            //provide the new balance
            return _balance;

        }
    }
}
