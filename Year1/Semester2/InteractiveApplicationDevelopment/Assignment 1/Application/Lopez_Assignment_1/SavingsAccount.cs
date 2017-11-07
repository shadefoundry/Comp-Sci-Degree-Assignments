using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class SavingsAccount: Account
    {
        int acctNo = -1;
        string acctHolderName = "";
        double MATCHING_DEPOSIT_RATIO = 0.5;
        double MIN_INTEREST_RATE = 3.0;
        public void SetAnnualIntrRate(double newAnnualIntrRatePercentage) {
            //check to see if the interest rate is valid
            if (newAnnualIntrRatePercentage < MIN_INTEREST_RATE) {
                throw new InvalidValue("A savings account cannot have an interest rate less than " + MIN_INTEREST_RATE);
            }
            //set the annual intrest rate from the base class
            SetAnnualIntrRate(newAnnualIntrRatePercentage);
        }
        public void Deposit(double amount) {
            Deposite(amount + amount * MATCHING_DEPOSIT_RATIO);
        }
    }
}
