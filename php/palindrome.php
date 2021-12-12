<?php
$array = ['radar','Malam','kasur ini rusak','Ibu Ratna antar ubi','Malas', 'Makan nasi goreng','Balonku ada lima'];

// membuat fungsi
function Palindrome($string){
	// strrev() = membalikan string
	if (strrev($string) == $string){
		return true;
	}else{
		return false;
	}
}
// eksekusi
foreach ($array as $kata){
	// strtolower = string ke lowercase
	if(Palindrome(strtolower($kata))){
		echo "<table><th style='width:150px; text-align:left'>".$kata."</th>";
		echo "<th> # --> Palindrom </th></table>";
	}else {
		echo "<table><th style='width:150px; text-align:left'>".$kata."</th>";
		echo "<th> # --> Bukan Palindrom </th></table>";
	}
}
?>
