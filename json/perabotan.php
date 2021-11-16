<?php

$data = file_get_contents("http://localhost/refactory_b5/json/data.json");
$dataParse = json_decode($data);

echo "Semua perabotan : ";

echo "<ol style='height:10px'>";
foreach ($dataParse as $perabotan){
	if ($perabotan->type == true){
		echo "<li style='height:10px'> {$perabotan->name} </li><br>";
}}
echo "</ol>";
?>