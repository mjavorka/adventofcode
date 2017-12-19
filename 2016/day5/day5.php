<?php

$input = 'ojvtpuvg';
$idx = 0;
$password = [];
while (sizeof($password) < 8) {
	$hash = md5($input . $idx);
	$idx++;
	if (substr($hash, 0, 5) === "00000") {
		$id = substr($hash, 5, 1);
		if (! is_numeric($id)) {
			continue;
		}
		$id = (int) $id;
		if ($id < 8 && ! isset($password[$id])) {
			$password[$id] = substr($hash, 6, 1);
		}
	}
}
ksort($password);
foreach ($password as  $char) {
	echo $char;
}
echo "\n";

