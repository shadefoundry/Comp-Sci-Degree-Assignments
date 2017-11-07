using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lopez_Assignment_1
{
    class Application
    {
        static void Main()
        {
            //create an application object
            Application app = new Application();
            //run the app
            app.Run();
            //Console.ReadKey();
        }
        private void Run()
        {
            try
            {
                Console.WriteLine("Surprise! No errors!");
                //create the bank for a more real-life like implementation
                Bank _bank = new Bank();
                _bank.LoadAccountData();
                //create an ATM and link it to the bank
                Atm _atm = new Atm();
                //start the ATM machine
                _atm.Start();
            }
            catch (Exception exception)
            {
                Console.WriteLine("An error occurred with the following message: ", exception);
            }
        }
    }
}
