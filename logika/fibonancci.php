<?php

function nearestFibonacci($num){
	if ($num == 0){
		echo 0;
		return;
	}

	$bilangan1 = 0;
	$bilangan2 = 1;
	$bilangan3 = $bilangan1 + $bilangan2;

	// Iterasi sampai suku ketiga 
	// kurang dari atau sama dengan num
	while ($bilangan3 <= $num){
		// meng-update bilangan yang sudah ada
		$bilangan1 = $bilangan2;
		$bilangan2 = $bilangan3;
		$bilangan3 = $bilangan1 + $bilangan2;
	}
	// abs = absolute, akan selalu menghasilkan angka positif
	// menyimpan angka Fibonacci yang memiliki selisih lebih kecil dengan input
	if (abs($bilangan3 - $num) >=
		abs($bilangan2 - $num)){
		$hasil = 'Fibonacci terdekat dengan '.$num.' adalah = '.$bilangan2;
	}else{
		$hasil = 'Fibonacci terdekat dengan '.$num.' adalah = '.$bilangan3;
	}
	echo $hasil;
}

// eksekusi
$input = 18;
nearestFibonacci($input);

?>