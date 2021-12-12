<?php

$data = file_get_contents("http://localhost/refactory_b5/json/data.json");
$dataParse = json_decode($data);

$tanggal = '16 Januari 2020';
echo "Semua barang yang dibeli pada ".$tanggal." : ";

echo "<ol style='height:10px'>";
foreach ($dataParse as $beli){
	if ($beli->purchased_at == '16012020'){
		echo "<li style='height:10px'> {$beli->name} </li><br>";
	}else{
		echo "Tidak ada barang yang di beli pada tanggal ".$tanggal;
		break;
	}
}
echo "</ol>";
?>