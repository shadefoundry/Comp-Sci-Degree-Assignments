<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ABCBookStore.aspx.cs" Inherits="Lopez_Assignment1.ABCBookStore" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title></title>
    <style type="text/css">
        .auto-style1 {
            height: 23px;
            width: 353px;
        }
        .auto-style3 {
            height: 23px;
            width: 255px;
        }
        .auto-style4 {
            width: 353px;
        }
        .auto-style5 {
            width: 255px;
        }
    </style>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>
<body>
    <div class="container-fluid">
        <form id="form1" runat="server">
            <div runat="server" id="AlertBox" class="jumbotron alert-danger" visible="false">
                <div runat="server" id="AlertBoxMessage"></div>
                <hr class="my-4">
                <asp:Button ID="btn_closeAlert" type="button" class="btn btn-primary" runat="server" Text="Dismiss Alert" OnClick="btn_closeAlert_Click" />
            </div>
            <div runat="server" class="jumbotron" id="div_landingPage">
                <p class="lead">Programmed By: Kevin Lopez<br />
                Student ID: 991395035<br />
                Section: Friday Section, 2:00pm to 5:00pm<br />
                Instructor: Syed Tanbeer<br /></p>
                <hr class="my-4">
                <asp:Button ID="btn_proceed" type="button" class="btn btn-primary" runat="server" Text="Proceed to Main Site" OnClick="btn_proceed_Click" />
            </div>
            <div runat="server" class="jumbotron" id="div_main" visible="false">
                <h3>ABC Bookstore</h3>
                <hr class="my-4">
                <table style="width: 100%;">
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_bookTitle" CssClass="h4" runat="server" Text="Title"></asp:Label></td>
                        <td class="auto-style4">
                            <asp:TextBox ID="txt_bookTitle" class="form-control" runat="server"></asp:TextBox></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="Label2" CssClass="h4" runat="server" Text="Author(s)"></asp:Label></td>
                        <td class="auto-style4">

                            <asp:TextBox ID="txt_author" class="form-control" runat="server"></asp:TextBox>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style3">
                            <asp:Label ID="lbl_isbn" CssClass="h4" runat="server" Text="ISBN"></asp:Label>
                        </td>
                        <td class="auto-style1">
                            <asp:TextBox ID="txt_isbn" class="form-control" runat="server"></asp:TextBox>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_publishDate" CssClass="h4" runat="server" Text="Publish Date"></asp:Label>
                        </td>
                        <td class="auto-style4">
                            <asp:TextBox ID="txt_publishDate" class="form-control" runat="server"></asp:TextBox>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_publisher" CssClass="h4" runat="server" Text="Publisher"></asp:Label>
                        </td>
                        <td class="auto-style4">
                            <asp:DropDownList ID="ddl_publisher" class="btn btn-secondary dropdown-toggle" type="button" runat="server">
                                <asp:ListItem Selected="True">International</asp:ListItem>
                                <asp:ListItem>Canadian</asp:ListItem>
                            </asp:DropDownList>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_category" CssClass="h4" runat="server" Text="Category"></asp:Label>
                        </td>
                        <td class="auto-style4">
                            <asp:DropDownList ID="ddl_category" class="btn btn-secondary dropdown-toggle" type="button" runat="server">
                                <asp:ListItem Selected="True">None</asp:ListItem>
                                <asp:ListItem>Children</asp:ListItem>
                                <asp:ListItem>Comics</asp:ListItem>
                                <asp:ListItem>Drama</asp:ListItem>
                                <asp:ListItem>Games</asp:ListItem>
                                <asp:ListItem>Health</asp:ListItem>
                                <asp:ListItem>Journals</asp:ListItem>
                                <asp:ListItem>Poetry</asp:ListItem>
                                <asp:ListItem>Sci-Fi</asp:ListItem>
                                <asp:ListItem>Travel</asp:ListItem>
                            </asp:DropDownList>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_pgCount" CssClass="h4" runat="server" Text="Page Count"></asp:Label>
                        </td>
                        <td class="auto-style4">
                            <asp:TextBox ID="txt_pgCount" class="form-control" runat="server"></asp:TextBox>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Label ID="lbl_price" CssClass="h4" runat="server" Text="Price"></asp:Label>
                        </td>
                        <td class="auto-style4">
                            <asp:TextBox ID="txt_price" class="form-control" runat="server"></asp:TextBox>
                        </td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="auto-style5">
                            <asp:Button ID="btn_insertIntoDatabase" type="button" class="btn btn-primary" runat="server" OnClick="btn_insertIntoDatabase_Click" Text="Insert" />
                        </td>
                        <td></td>
                    </tr>
                </table>
                <hr class="my-4">
                <asp:Button ID="btn_showSearchControls" type="button" class="btn btn-primary" runat="server" OnClick="btn_showSearchControls_Click" Text="Show Search Controls" />
                <asp:Button ID="btn_hideSearchControls" type="button" class="btn btn-primary" runat="server" OnClick="btn_hideSearchControls_Click" Text="Hide Search Controls" />
                <br />
                <asp:Label ID="lbl_searchByTitle" runat="server" Text="Search Book Name"></asp:Label>
                <asp:TextBox ID="txt_searchByName" runat="server"></asp:TextBox>
                <br />
                <asp:Label ID="lbl_searchByCatagory" runat="server" Text="Search By Category"></asp:Label>
                <asp:DropDownList ID="ddl_searchByCategory" runat="server">
                    <asp:ListItem Selected="True">None</asp:ListItem>
                    <asp:ListItem>Children</asp:ListItem>
                    <asp:ListItem>Comics</asp:ListItem>
                    <asp:ListItem>Drama</asp:ListItem>
                    <asp:ListItem>Games</asp:ListItem>
                    <asp:ListItem>Health</asp:ListItem>
                    <asp:ListItem>Journals</asp:ListItem>
                    <asp:ListItem>Poetry</asp:ListItem>
                    <asp:ListItem>Sci-Fi</asp:ListItem>
                    <asp:ListItem>Travel</asp:ListItem>
                </asp:DropDownList>
                <br />
                <asp:Label ID="lbl_searchByPrice" runat="server" Text="Price Greater Than"></asp:Label>
                <asp:TextBox ID="txt_searchByPrice" runat="server"></asp:TextBox>
                <br />
                <asp:Button ID="btn_searchDatabase" type="button" class="btn btn-primary" runat="server" OnClick="btn_searchByName_Click" Text="Search" />
                <hr class="my-4">
                <asp:Button ID="btn_showDatabase" type="button" class="btn btn-primary" runat="server" OnClick="btn_showDatabase_Click" Text="Show Database" />
                <asp:Button ID="btn_hideDatabase" type="button" class="btn btn-primary" runat="server" OnClick="btn_hideDatabase_Click" Text="Hide Database" />
                <br />
                <asp:Label ID="lbl_tableTitle" CssClass="h4" runat="server"></asp:Label>
                <asp:GridView ID="grid_BookList" runat="server" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="ID" DataSourceID="Books" CellPadding="3" AllowPaging="True" BackColor="White" BorderColor="#CCCCCC" BorderStyle="None" BorderWidth="1px">
                    <Columns>
                        <asp:CommandField ShowDeleteButton="True" ShowEditButton="True" />
                        <asp:BoundField DataField="ID" HeaderText="ID" ReadOnly="True" SortExpression="ID" />
                        <asp:BoundField DataField="Title" HeaderText="Title" SortExpression="Title" />
                        <asp:BoundField DataField="Author" HeaderText="Author" SortExpression="Author" />
                        <asp:BoundField DataField="PublishingDate" HeaderText="PublishingDate" SortExpression="PublishingDate" />
                        <asp:BoundField DataField="Publisher" HeaderText="Publisher" SortExpression="Publisher" />
                        <asp:BoundField DataField="Category" HeaderText="Category" SortExpression="Category" />
                        <asp:BoundField DataField="PageCount" HeaderText="PageCount" SortExpression="PageCount" />
                        <asp:BoundField DataField="Price" HeaderText="Price" SortExpression="Price" />
                    </Columns>
                    <FooterStyle BackColor="White" ForeColor="#000066" />
                    <HeaderStyle BackColor="#006699" Font-Bold="True" ForeColor="White" />
                    <PagerStyle BackColor="White" ForeColor="#000066" HorizontalAlign="Left" />
                    <RowStyle ForeColor="#000066" />
                    <SelectedRowStyle BackColor="#669999" Font-Bold="True" ForeColor="White" />
                    <SortedAscendingCellStyle BackColor="#F1F1F1" />
                    <SortedAscendingHeaderStyle BackColor="#007DBB" />
                    <SortedDescendingCellStyle BackColor="#CAC9C9" />
                    <SortedDescendingHeaderStyle BackColor="#00547E" />
                </asp:GridView>
                <asp:SqlDataSource ID="Books" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [Books] WHERE [ID] = @ID" InsertCommand="INSERT INTO [Books] ([ID], [Title], [Author], [Publishing Date], [Publisher], [Category], [Page Count], [Price], [ISBN]) VALUES (@ID, @Title, @Author, @Publishing_Date, @Publisher, @Category, @Page_Count, @Price, @ISBN)" SelectCommand="SELECT * FROM [Books]" UpdateCommand="UPDATE [Books] SET [Title] = @Title, [Author] = @Author, [Publishing Date] = @Publishing_Date, [Publisher] = @Publisher, [Category] = @Category, [Page Count] = @Page_Count, [Price] = @Price, [ISBN] = @ISBN WHERE [ID] = @ID">
                    <DeleteParameters>
                        <asp:Parameter Name="ID" Type="Int32" />
                    </DeleteParameters>
                    <InsertParameters>
                        <asp:Parameter Name="ID" Type="Int32" />
                        <asp:Parameter Name="Title" Type="String" />
                        <asp:Parameter Name="Author" Type="String" />
                        <asp:Parameter DbType="Date" Name="Publishing_Date" />
                        <asp:Parameter Name="Publisher" Type="String" />
                        <asp:Parameter Name="Category" Type="String" />
                        <asp:Parameter Name="Page_Count" Type="Int32" />
                        <asp:Parameter Name="Price" Type="Int32" />
                        <asp:Parameter Name="ISBN" Type="Int32" />
                    </InsertParameters>
                    <UpdateParameters>
                        <asp:Parameter Name="Title" Type="String" />
                        <asp:Parameter Name="Author" Type="String" />
                        <asp:Parameter DbType="Date" Name="Publishing_Date" />
                        <asp:Parameter Name="Publisher" Type="String" />
                        <asp:Parameter Name="Category" Type="String" />
                        <asp:Parameter Name="Page_Count" Type="Int32" />
                        <asp:Parameter Name="Price" Type="Int32" />
                        <asp:Parameter Name="ISBN" Type="Int32" />
                        <asp:Parameter Name="ID" Type="Int32" />
                    </UpdateParameters>
                </asp:SqlDataSource>
                <asp:GridView ID="grid_searchResults" runat="server" CellPadding="3" ForeColor="Black" GridLines="Vertical" BackColor="White" BorderColor="#999999" BorderStyle="Solid" BorderWidth="1px">
                    <AlternatingRowStyle BackColor="#CCCCCC" />
                    <FooterStyle BackColor="#CCCCCC" />
                    <HeaderStyle BackColor="Black" Font-Bold="True" ForeColor="White" />
                    <PagerStyle BackColor="#999999" ForeColor="Black" HorizontalAlign="Center" />
                    <SelectedRowStyle BackColor="#000099" Font-Bold="True" ForeColor="White" />
                    <SortedAscendingCellStyle BackColor="#F1F1F1" />
                    <SortedAscendingHeaderStyle BackColor="#808080" />
                    <SortedDescendingCellStyle BackColor="#CAC9C9" />
                    <SortedDescendingHeaderStyle BackColor="#383838" />
                </asp:GridView>
                <br />
                <asp:Button ID="btn_back" class="btn btn-success" runat="server" Text="Return to Landing Page" OnClick="btn_back_Click" />
            </div>
        </form>
    </div>
</body>
</html>
