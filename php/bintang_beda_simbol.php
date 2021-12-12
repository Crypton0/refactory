<?php

$arr = ['*','#','$','%'];
$lenArr = count($arr);

$simbol = ['*','*','*','*'];

for ($i=0; $i<=$lenArr-1; $i++){	// 1,22,333,4444
	for ($j=0; $j<=$i; $j++)		// 1,12,123,1234
	{
	echo "{$arr[$i]} {$arr[$j]}<br>";
	

}}
// endfor
?>