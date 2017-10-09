<?php
$con = mysql_connect("localhost","root","");
if(!$con){
	die("cannont connect". mysql_error());
	}
	mysql_select_db("major",$con);
$user = $_POST['username'];
$pass = $_POST['password'];
$sql = "SELECT username,password FROM teacherl WHERE username = '".$user."' and password = '".$pass."'";
$myData = mysql_query($sql,$con);
$row = mysql_fetch_array($myData);
 if ($row['username'] == $user && $row['password'] == $pass)
 {
 	header("location:tvteacher.php");
 }
 else
 {
 	header("location: tlogin.php");
 }
 mysql_close($con);
?>