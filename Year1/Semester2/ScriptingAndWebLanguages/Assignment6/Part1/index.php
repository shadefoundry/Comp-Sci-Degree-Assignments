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
        <?php
        $user='root';
        $pass='';
        $db='registration';
        $db = new mysqli('localhost',$user,$pass,$db) or die("Unable to connect to database.");
        $firstName = filter_input(INPUT_POST, "firstName", FILTER_VALIDATE_INT);
        $lastName = filter_input(INPUT_POST, "lastName", FILTER_VALIDATE_INT);
        $address = filter_input(INPUT_POST, "address", FILTER_VALIDATE_INT);
        $city = filter_input(INPUT_POST, "city", FILTER_VALIDATE_INT);
        $state = filter_input(INPUT_POST, "state", FILTER_VALIDATE_INT);
        $zip = filter_input(INPUT_POST, "zip", FILTER_VALIDATE_INT);
        $home = filter_input(INPUT_POST, "homePhone", FILTER_VALIDATE_INT);
        $work = filter_input(INPUT_POST, "workPhone", FILTER_VALIDATE_INT);
        $fax = filter_input(INPUT_POST, "faxNumber", FILTER_VALIDATE_INT);
        $url = filter_input(INPUT_POST, "url", FILTER_VALIDATE_INT);
        $siteName = filter_input(INPUT_POST, "linkName", FILTER_VALIDATE_INT);
        $email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_INT);
        $sql="INSERT INTO `userdata`(`UserNo`, `FirstName`, `LastName`, `Address`, `City`, `State`, `Zip`, `HomePhone`, `WorkPhone`, `Fax`, `WebsiteURL`, `WebsiteName`, `Email`) VALUES (null,$firstName,$lastName,$address,$city,$state,$zip,$home,$work,$fax,$url,$siteName,$email)";
        ?>
    </body>
</html>
