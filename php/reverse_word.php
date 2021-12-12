<?php
$string = "I am A Great human";
$array = explode(" ", strrev($string));
$revArray = array_reverse($array);
$newArray = implode(" ", $revArray);

echo $newArray;


?>