<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Assignment_7";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT IDNumber, FirstName, LastName, BirthDate FROM Assignment_7";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
     echo "<table border=1><tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Date of Birth</th></tr>";
     // output data of each row
     while($row = $result->fetch_assoc()) {
     echo "<tr><td>" . $row["IDNumber"]. "</td><td>" . $row["FirstName"]. "</td><td>" . $row["LastName"]. "</td><td>" . $row["BirthDate"]. "</td></tr>";
     }
     echo "</table>";
} else {
     echo "No results in database";
}

$conn->close();
?>  