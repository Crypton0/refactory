<?php
//Input: [3, 5, 2, -4, 8, 11]
//penjumlahan = 7

//Output: [[11, -4], [2, 5]]

//note : 11, -4 dan 2, 5 adalah hasil penjumlahan 7

#############################################################

$data = [3, 5, 2, -4, 8, 11];
$jumlah = 7;

// eksekusi
$lendata = count($data);
$hasil = [];

for ($i=0; $i<=$lendata-1; $i++){	// 3,55,222,-4-4-4-4,88888
	for ($j=0; $j<=$i; $j++)		// 3,35,352,352-4,352-48
	{
		if ($data[$i] + $data[$j] == $jumlah){
			array_push($hasil, [$data[$i], $data[$j]]);
		}
}}

$output = json_encode($hasil);		// convert ke json sekaligus merapikan
print_r($output);


?>