<html>
<body>
<?php
	$arg = "https://gironde.fff.fr/recherche-clubs/?scl=2588&tab=teams";
	$html = file_get_contents($arg);
	$pos = strpos($html, "calendrier-competition");
	$arrnum = [];
	while ($pos != false) {
		$numero_compet = "";
		$pos1 = strpos($html, "competition=", $pos) + strlen("competition=");
		if ($pos1 < $pos) {
			$pos = false;
		}
		else {
			$pos2 = strpos($html, "&", $pos1);
			$numero_compet = substr($html, $pos1, $pos2 - $pos1);
			$pos = $pos2;
			$arrnum[] = $numero_compet;
		}
	}
	for ($i = 0; $i < count($arrnum); $i++) {
		echo $arrnum[$i];
		echo "<br />";
	}
?>
</body>
</html>