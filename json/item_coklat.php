<?php

$data = file_get_contents("http://localhost/refactory_b5/json/data.json");
$dataParse = json_decode($data);
//echo '<pre>'; echo print_r($dataParse); echo '</pre>';

echo "Semua item dengan warna coklat : ";

echo "<ol style='height:10px'>";
foreach ($dataParse as $coklat){
	if ($coklat->tags[2] == "brown"){
		echo "<li style='height:10px'> {$coklat->name} </li><br>";
	}else{
		break;
	}
}
echo "</ol>";

?>