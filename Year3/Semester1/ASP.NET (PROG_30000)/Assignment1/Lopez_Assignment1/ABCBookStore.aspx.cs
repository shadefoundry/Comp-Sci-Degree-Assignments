using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Data;
using System.Configuration;
namespace Lopez_Assignment1
{
    public partial class ABCBookStore : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            showDatabase();
            btn_showSearchControls.Visible = true;
            btn_hideSearchControls.Visible = false;
            lbl_searchByTitle.Visible = false;
            lbl_searchByCatagory.Visible = false;
            lbl_searchByPrice.Visible = false;
            txt_searchByName.Visible = false;
            txt_searchByPrice.Visible = false;
            ddl_searchByCategory.Visible = false;
            btn_searchDatabase.Visible = false;
        }

        private void cry(string message)
        {
            this.AlertBoxMessage.InnerText = message;
            this.AlertBox.Visible = true;
        }

        protected void btn_searchByName_Click(object sender, EventArgs e)
        {
            hideDatabase();
            string bookName = txt_searchByName.Text.ToString();
            string category = ddl_searchByCategory.SelectedItem.Text;
            string p = txt_searchByPrice.Text.ToString();
            int price;
            //try to parse string to int
            bool result = Int32.TryParse(p, out price);
            if (result == true)
            {
                //if it works we get an int
                price = Int32.Parse(p);
                System.Diagnostics.Debug.WriteLine("name :" + bookName + "\ncategory " + category + "\nprice " + price);
            }
            else
            {
                //otherwise give up and set the price to 0
                price = 0;
            }

            string commandString = buildSearchCommand(bookName, category, price);
            string conString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
            using (SqlConnection con = new SqlConnection(conString))
            {
                try
                {
                    con.Open();
                    SqlCommand cmd = new SqlCommand(commandString, con);
                    //declare and bind data source
                    grid_searchResults.DataSource = cmd.ExecuteReader();
                    grid_searchResults.DataBind();
                    con.Close();
                    grid_searchResults.Visible = true;
                    lbl_tableTitle.Text = "Search Results:";
                }
                catch (Exception we)
                {
                    //you should never get here
                    showDatabase();
                    cry("He's dead, Jim!\nSomething went wrong!\n");
                }
            }
        }

        private void refreshGridView(GridView _gridView)
        {
            string command = "select * from Books";
            string conString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
            using (SqlConnection con = new SqlConnection(conString))
            {
                try
                {
                    con.Open();
                    //redind data source, effectively refreshing it.
                    Books.SelectCommand = command;
                    _gridView.DataBind();
                    con.Close();
                }
                catch (Exception we)
                {
                    //you should never see this
                    cry("He's dead, Jim!\nSomething went wrong!\n" + we.ToString());
                }
            }
        }

        private string buildSearchCommand(string _bookName, string _category, int _price)
        {
            string cmd = "select * from Books where ";
            if (_bookName != "") { cmd += "Title = '" + _bookName + "' and "; }
            if (_category != "None")
            {
                cmd += "Category = '" + _category + "' and Price > " + _price;
            }
            else { cmd += "price > " + _price; }

            return cmd;
        }

        private string buildInsertCommand(int _isbn, string _bookName, string _author, string _publishDate, string _publisher, string _category, int _pgCount, int _price)
        {
            //returns a string with the insert command done so I don't need to clutter up my onclick method
            string cmd = "insert into Books (ID, Title, Author, PublishingDate, Publisher, Category, PageCount, Price)" +
                " values ('" + _isbn + "','" + _bookName + "','" + _author + "','" + _publishDate + "','" + _publisher + "','" + _category + "','" + _pgCount + "','" + _price + "');";
            return cmd;
        }

        protected void btn_showSearchControls_Click(object sender, EventArgs e)
        {
            //hide this button, show the search controls and new button
            showSearch();
        }

        private void showSearch()
        {
            btn_showSearchControls.Visible = false;
            btn_hideSearchControls.Visible = true;
            lbl_searchByTitle.Visible = true;
            lbl_searchByCatagory.Visible = true;
            lbl_searchByPrice.Visible = true;
            txt_searchByName.Visible = true;
            txt_searchByPrice.Visible = true;
            ddl_searchByCategory.Visible = true;
            btn_searchDatabase.Visible = true;
            
        }

        protected void btn_hideSearchControls_Click(object sender, EventArgs e)
        {
            //hide search controls and this button. Show old button.
            hideSearch();
        }

        private void hideSearch()
        {
            lbl_tableTitle.Text = "";
            grid_searchResults.Visible = false;
            lbl_searchByTitle.Visible = false;
            lbl_searchByCatagory.Visible = false;
            lbl_searchByPrice.Visible = false;
            txt_searchByName.Visible = false;
            txt_searchByPrice.Visible = false;
            ddl_searchByCategory.Visible = false;
            btn_searchDatabase.Visible = false;
            btn_hideSearchControls.Visible = false;
            btn_showSearchControls.Visible = true;
        }

        protected void btn_insertIntoDatabase_Click(object sender, EventArgs e)
        {
            string bookName, author, publishDate, publisher, category;
            int pgCount, price, isbn;

            Boolean fine = checkValues();
            if (fine == true)
            {
                //set values
                bookName = txt_bookTitle.Text.ToString();
                author = txt_author.Text.ToString();
                publishDate = txt_publishDate.Text.ToString();
                publisher = ddl_publisher.SelectedItem.Text.ToString();
                category = ddl_category.SelectedItem.Text.ToString();
                pgCount = Int32.Parse(txt_pgCount.Text.ToString());
                price = Int32.Parse(txt_price.Text.ToString());
                isbn = Int32.Parse(txt_isbn.Text.ToString());
                //construct command
                string commandString = buildInsertCommand(isbn, bookName, author, publishDate, publisher, category, pgCount, price);
                string conString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
                using (SqlConnection con = new SqlConnection(conString))
                {
                    try
                    {
                        //try to actually insert the new command
                        con.Open();
                        SqlCommand cmd = new SqlCommand(commandString, con);
                        //try to execute the command
                        cmd.ExecuteNonQuery();
                        con.Close();
                        refreshGridView(grid_BookList);
                    }
                    catch (Exception we)
                    {
                        //if we fail, cry about it
                        cry("Error inserting.\nEnsure that all forms are populated and that there are no duplicate ISBNs\n");
                    }
                }

            }
            else
            {
                //throw an error
                cry("Something went wrong! There's an invalid or missing input!");
            }
        }

        private Boolean checkValues()
        {
            /*
             Go through all fields for insert and check if they're empty.
             If anything's empty, return false.
             If something can't be converted, return false.
             If everything's fine, return true
             */
            int p, q, r;
            bool r1 = Int32.TryParse(txt_pgCount.Text.ToString(), out p);
            bool r2 = Int32.TryParse(txt_price.Text.ToString(), out q);
            bool r3 = Int32.TryParse(txt_isbn.Text.ToString(), out r);
            string bookName = txt_bookTitle.Text.ToString();
            string author = txt_author.Text.ToString();
            string publishDate = txt_publishDate.Text.ToString();
            string publisher = ddl_publisher.SelectedItem.Text.ToString();
            string category = ddl_category.SelectedItem.Text.ToString();
            if (r1 == false || r2 == false || r3 == false || bookName == "" || author == "" || publishDate == "" || publisher == "" || category == "None")
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        protected void btn_closeAlert_Click(object sender, EventArgs e)
        {
            AlertBox.Visible = false;
        }

        protected void btn_proceed_Click(object sender, EventArgs e)
        {
            div_landingPage.Visible = false;
            div_main.Visible = true;
        }

        protected void btn_back_Click(object sender, EventArgs e)
        {
            Response.Redirect(Request.Url.AbsoluteUri);
        }

        protected void btn_showDatabase_Click(object sender, EventArgs e)
        {
            showDatabase();
        }

        private void showDatabase()
        {
            hideSearch();
            lbl_tableTitle.Text = "Current Database:";
            btn_showDatabase.Visible = false;
            btn_hideDatabase.Visible = true;
            grid_BookList.Visible = true;
        }

        protected void btn_hideDatabase_Click(object sender, EventArgs e)
        {
            hideDatabase();
        }

        private void hideDatabase()
        {
            lbl_tableTitle.Text = "";
            btn_showDatabase.Visible = true;
            btn_hideDatabase.Visible = false;
            grid_BookList.Visible = false;
        }
    }
}