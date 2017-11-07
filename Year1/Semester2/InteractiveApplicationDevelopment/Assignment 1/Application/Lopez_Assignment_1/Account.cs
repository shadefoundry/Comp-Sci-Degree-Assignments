using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    public class Account
    {
        public int ACCOUNT_TYPE_CHECQUING = 1;
        public int ACCOUNT_TYPE_SAVINGS = 2;
        public double TYPE_DEPOSIT = 1.0;
        public double TYPE_WITHDRAWAL = 2.0;
        public int _acctNo = -1;
        public string _acctHolderName = "";
        public double _balance = 0.0;
        double _annualIntrRate = 0.0;
        public List<double> _transactionList = new List<double>();
        //returns the int _acctNo
        public int GetAccountNumber(int _acctNo) {
            return _acctNo;
        }
        //returns the string _acctHolderName
        public string GetAcctHolderName() { return _acctHolderName; }
        public double GetBalance() { return _balance;}
        public double GetAnnualIntrRate() { return _annualIntrRate; }
        public void SetAnnualIntrRate(double newAnnualIntrRatePercentage) { _annualIntrRate = newAnnualIntrRatePercentage / 100; }
        public double GetMonthlyIntrRate() { return _annualIntrRate / 12; }

        public List<double> GetTransactionList() {
            return _transactionList;
        }

        public void Deposite(double amount) {
            //raise the custom exception that tells us you cant use negatives
            if (amount < 0) {
                throw new InvalidTransaction("Invalid amount provided. Cannot deposit a negative amount.");
            }
            //change the balance
            double oldBalance = _balance;
            _balance += amount;
        }

        public double Withdraw(double amount) {
            if (amount < 0) {
                throw new InvalidTransaction("Invalid amount provided. Cannot withdraw a negative amount.");
            }
            if (amount > _balance) {
                throw new InvalidTransaction("Insufficient funds. Cannot withdraw the provided amount.");
            }
            //change the balance
            double oldBalance = _balance;
            _balance += amount;

            //record the transaction
            _transactionList.Add(TYPE_WITHDRAWAL);
            _transactionList.Add(amount);
            _transactionList.Add(oldBalance);
            _transactionList.Add(_balance);
            //return the new balance
            return _balance;
        }

        public string PredictStatement(float mondep, float monWithdr)
        {
            int month = 1;
            double predictedBalance = _balance;
            double predictedInterest = 0;
            string stm = "\n============ Programming Principles Bank Statement ================\n\nAccount Number: {0}\nName:\t\t{1}\n";

            while (month <= 12) {
                predictedBalance = predictedBalance + mondep - monWithdr;
                double monthlyInterest = predictedBalance * GetMonthlyIntrRate();
                predictedInterest = predictedInterest + monthlyInterest;
                stm = stm + ("\nMonth {0}:\n\tBalance: {1}\n\tInterest: {2}\n");
                month = month + 1;
            }
            predictedBalance = predictedBalance + predictedInterest;
            stm = stm + "\n\nEnd of Year Balance:{0}";
            stm = stm + "\n\n================================================================";

            return stm;
        }
        //TODO implement Load and Save functions in account.cs
        public void Load() { }
        public void Save() { }
    }
    //Exception for when an invalid value is entered (does nothing)
    class InvalidValue: Exception
    { public InvalidValue(string message): base(message) { } }
    //Exception for when an invalid transaction happens (does nothing)
    class InvalidTransaction: Exception
    {
        public InvalidTransaction(string message): base(message) {}
    }
}
