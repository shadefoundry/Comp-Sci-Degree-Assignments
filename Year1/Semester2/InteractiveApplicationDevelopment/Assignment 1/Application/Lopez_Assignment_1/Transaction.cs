using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class Transaction
    {
        public int TYPE_DEPOSIT = 1;
        public int TYPE_WITHDRAWAL = 2;
        public int _type = 0;
        double _amount = 0.0;
        double _originalBalance = 0.0;
        double _newBalance = 0.0;
        public int getType()
        {
            return _type;
        }
        public double GetAmount()
        {
            return _amount;
        }
        public double GetOriginalBalance()
        {
            return _originalBalance;
        }
        public double GetNewBalance()
        {
            return _newBalance;
        }
        //TODO: implement auto called method below
        public void Load()
        {
            //Not implemented due to a lack of understanding of file i/o as well as
            //a lack of time.
        }
        public void Save()
        {
            //Not implemented due to a lack of understanding of file i/o as well as
            //a lack of time.
        }
    }
}
