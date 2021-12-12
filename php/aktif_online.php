<?php
function durasi($datefrom){
	$timestamp = is_numeric($datefrom) ? $datefrom : strtotime($datefrom);		// membuat kondisi agar semua menjadi integer
	$current_time = time();
	$diff = $current_time - ($timestamp-(6*3600));
	$intervals = array('year'=>31556926, 'month'=>2629744, 'week'=>604800, 'day'=>86400, 'hour'=>3600, 'minute'=>60);

	if($diff<60){
		$rntval = $diff . ' detik yang lalu';
	}
	if($diff>=60 && $diff<$intervals['hour']){
		$diff = floor($diff/$intervals['minute']);
		$rntval = $diff.' menit yang lalu';
	}
	if($diff>=$intervals['hour'] && $diff<$intervals['day']){
		$diff = floor($diff/$intervals['hour']);
		$rntval = $diff.' jam yang lalu';
	}
	if($diff>=$intervals['day'] && $diff<$intervals['week']){
		$diff = floor($diff/$intervals['day']);
		$rntval = $diff == 1 ? 'kemarin' : $diff.' hari yang lalu';
	}
	if($diff>=$intervals['week'] && $diff<$intervals['month']){
		$diff = floor($diff/$intervals['week']);
		$rntval = $diff.' minggu yang lalu';
	}
	if($diff>=$intervals['month'] && $diff<$intervals['year']){
		$diff = floor($diff/$intervals['month']);
		$rntval = $diff.' bulan yang lalu';
	}
	if($diff>=$intervals['year']){
		$diff = floor($diff/$intervals['year']);
		$rntval = $diff.' tahun yang lalu';
	}
	return $rntval;
}

// eksekusi
$tgl1 = '2021-11-23';
$tgl2 = '2021-11-18 19:25:33';

echo durasi($tgl1).'<br>';
echo durasi($tgl2);
?>