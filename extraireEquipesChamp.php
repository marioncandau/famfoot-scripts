<html>
<body>
<?php
	$arg = "https://lfna.fff.fr/competitions/?id=350388&poule=2&phase=1&type=ch&tab=resultat";
	$html = file_get_contents($arg);
	$pos = strpos($html, "title=\"Equipe\"");
	$arrnum = [];
	$arrclub = [];
	while ($pos != false) {
		$numero_club = "";
		$club_current = "";
		$pos1 = strpos($html, "option value", $pos) + strlen("option value") + 2;
		$pos2 = strpos($html, "-", $pos1);
		$numero_club = substr($html, $pos1, $pos2 - $pos1);
		$i = $pos2;
		$pos1 = strpos($html, ">", $i) + 1;
		$i = $pos1;
		$pos2 = strpos($html, "<", $i);
		$club_current = substr($html, $pos1, $pos2 - $pos1);
		$i = $pos2;
		if (strpos($html, "</select>", $pos) < $i) {
			$pos = false;
		}
		else {
			$pos = $i;
			$arrnum[] = $numero_club;
			$arrclub[] = $club_current;
		}
	}
?>
</body>
</html>