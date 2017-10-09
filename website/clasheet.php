<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
<meta charset="utf-8">
</head>
</html>

<?php
include("header1.html");
$con = mysql_connect("localhost","root","");
if(!$con){
	die("cannont connect". mysql_error());
	}
	mysql_select_db("major",$con);
	$sql = "SELECT id,name,day1,day2,day3,day4,day5,day6 FROM atnd";
	$myData = mysql_query($sql,$con);
	echo "<table>
	<tr>
	<th>id</th>
	<th>name</th>
	<th>day1</th>
	<th>day2</th>
	<th>day3</th>
	<th>day4</th>
	<th>day5</th>
	<th>day6</th>
	</tr>";
	while($record = mysql_fetch_array($myData))
	{
		echo "<tr>";
		echo "<td>" . $record['id'] . "</td>";
		echo "<td>" . $record['name'] . "</td>";
		echo "<td>" . $record['day1'] . "</td>";
		echo "<td>" . $record['day2'] . "</td>";
		echo "<td>" . $record['day3'] . "</td>";
		echo "<td>" . $record['day4'] . "</td>";
		echo "<td>" . $record['day5'] . "</td>";
		echo "<td>" . $record['day6'] . "</td>";

		
		echo "</tr>";
	}
	echo "</table>";

	mysql_close($con);
?>