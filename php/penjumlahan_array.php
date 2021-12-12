<?php
//Input: [3, 5, 2, -4, 8, 11]
//penjumlahan = 7

//Output: [[11, -4], [2, 5]]

//note : 11, -4 dan 2, 5 adalah hasil penjumlahan 7

#############################################################

$arr = [3, 5, 2, -4, 8, 11];
$lenArr = count($arr);

for ($i=0; $i<=$lenArr-1; $i++){	// 3,55,222,-4-4-4-4,88888
	for ($j=0; $j<=$i; $j++)		// 3,35,352,352-4,352-48
	{
		$jumlah = $arr[$i] + $arr[$j];
		
		if ($jumlah == 7){
			echo "[{$arr[$i]}, {$arr[$j]}]<br>";  // hasil masih belum bentuk array
		}
}}
//  endfor


?>