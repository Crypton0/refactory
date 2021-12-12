<?php  
function leapYear($year){
	return checkdate(2, 29, $year);  
}
// eksekusi
for($year=1900; $year<2020+1; $year++){  
	If (leapYear($year)){
		echo $year.', ';
	}
}
?>