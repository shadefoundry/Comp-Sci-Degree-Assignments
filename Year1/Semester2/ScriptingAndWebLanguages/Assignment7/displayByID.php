<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Assignment_7";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
$idNo = filter_input(INPUT_POST, "idNo",FILTER_VALIDATE_INT);
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM `assignment_7` WHERE IDNumber='$idNo'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
     echo "<table border=1><tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Date of Birth</th></tr>";
     // output data of each row
     while($row = $result->fetch_assoc()) {
     echo "<tr><td>" . $row["IDNumber"]. "</td><td>" . $row["FirstName"]. "</td><td>" . $row["LastName"]. "</td><td>" . $row["BirthDate"]. "</td></tr>";
     }
     echo "</table>";
} else {
     echo "No results with ID $idNo";
}

$conn->close();
?>