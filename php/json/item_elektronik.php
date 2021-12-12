<?php

$data = file_get_contents("http://localhost/refactory_b5/json/data.json");
$dataParse = json_decode($data);

echo "Semua perangkat elektronik : ";

echo "<ol style='height:10px'>";
foreach ($dataParse as $elekronik){
	if ($elekronik->type == "electronic"){
		echo "<li style='height:10px'> {$elekronik->name} </li><br>";
}}
echo "</ol>";
?>