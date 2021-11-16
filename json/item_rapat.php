<?php

$data = file_get_contents("http://localhost/refactory_b5/json/data.json");
$dataParse = json_decode($data);

echo "Semua item di Ruang Rapat :";

echo "<ol style='height:10px'>";
foreach ($dataParse as $key => $rapat){
	if ($rapat->placement->name == "Meeting Room"){
		echo "<li style='height:10px'> {$rapat->name} </li><br>";
}}
echo "</ol>";
?>