<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <form action="displayAll.php" method="post">
            <input type="submit" name="diaplay" value="Display All Values"><br>
        </form>
        
        <form action="displayByID.php" method="post">
            <br>Display by ID Number:<br><input type="range" name="idNo" min="1" max="5"><br>
            <input type="submit" name="submit">
        </form>
        <form action="displayByName.php" method="post">
            <br>Search by First Name:<br><input type="text" name="firstName"><br>
            <input type="submit" name="submit">
        </form>
    </body>
</html>
