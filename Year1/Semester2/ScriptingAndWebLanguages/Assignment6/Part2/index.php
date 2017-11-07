<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "login";
$UserPassword = filter_input(INPUT_POST, "newPass",FILTER_SANITIZE_STRING);
$NewPassword = filter_input(INPUT_POST, "verify",FILTER_SANITIZE_STRING);
try {
$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
// set the PDO error mode to exception
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$sql = "UPDATE data SET Pass='$UserPassword' WHERE UserID=1";
// Prepare statement
$stmt = $conn->prepare($sql);

// execute the query
$stmt->execute();

// echo a message to say the UPDATE succeeded
if($UserPassword == $NewPassword){echo "Your password has been updated to $UserPassword";}
else{echo"Passwords do now match!";}
}
catch(PDOException $e)
{
echo $sql . "<br>" . $e->getMessage();
}

$conn = null;
?>