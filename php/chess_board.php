<?php

// catur kotak berwarna

$size = 8;
echo "<table align=center border=1 cellspacing=0>";
	for ($x=1; $x<=$size; $x++) {  // baris  $x=12345678
		echo "<tr>";
		
		for ($y=1; $y<=$size; $y++) {  // kolom  $y=12345678 (8x)
			if (($x+$y) %2 > 0){  // x+y = 2-9, 3-10, 4-11, 5-12, 6-13, 7-14, 8-15, 9-16
				echo "<td width=50 height=50  bgcolor=black></td>";
			}else{
				echo "<td width=50 height=50 bgcolor=white></td>";
		}}
		echo "</tr>";
	}
echo "</table><br><br>";

######################################################################################################

// catur menggunakan simbol

$size = 8;
$string = "&nbsp;";  // kode untuk spasi
echo '<center>';
for ($baris=1; $baris<=$size; $baris++){  // baris  $x=12345678
	for ($kolom=1; $kolom<=$size; $kolom++){  // kolom  $y=12345678 (8x)
		if(($baris+$kolom) %2 == 0){  // baris+kolom = 2-9, 3-10, 4-11, 5-12, 6-13, 7-14, 8-15, 9-16
			echo "#";
		}
		else if(($baris+$kolom) %2 ==1){
			echo "*";  // ganti dengan $string
	}}
	echo "<br>";
}
echo '</center>';

######################################################################################################

"<!-- <center> ilustrasi <br>
2  3  4  5  6  7  8  9 <br>
3  4  5  6  7  8  9  10 <br>
4  5  6  7  8  9  10 11 <br>
5  6  7  8  9  10 11 12 <br>
6  7  8  9  10 11 12 13 <br>
7  8  9  10 11 12 13 14 <br>
8  9  10 11 12 13 14 15 <br>
9  10 11 12 13 14 15 16 <br>
</center> -->";

?>