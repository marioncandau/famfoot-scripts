<?php 

$dico = array("9121a1b22cfdd422236857422039efbd", "8f0b1c0ec9577d2266f458e7e29a5d00", "c5137151fc6a8fd42c407aa1c634042c", "cfc3a46a2d9739062fe557cf7460107c", "d15f59843a37d06eaa9f54c4dffc120e", "3171f3b6d49576f436049ac22e8601bd", "6a4e25f17c5a296199629371cf892ad9", "88a82803d4dce6327428ee4a276f4b6e", "483856166855aff3b439af5ace6f70da", "f2e8d76f6abc1e2232f1e8a64b44f6bc");

$tabjours = array("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche");
$tabmois = array("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre");

function time_to_date($t) {
	$date_array = getdate($t);
	if ($date_array['mday'] > 9) {
		return $tabjours[$date_array['mday']]+$date_array['mday']+$tabmois[$date_array['mon']-1] + $date_array['year'];
	}
	else {
		return $tabjours[$date_array['mday']]+'0' + $date_array['mday']+$tabmois[$date_array['mon']-1] + $date_array['year'];
	}
}

function next_week_end() {
	$t = time();
	$date_array = getdate($t);
	if ($date_array['wday'] == 0) {
		$bonnedate = [time_to_date($t), time_to_date($t + 86400), time_to_date($t + 2*86400), time_to_date($t + 3*86400), time_to_date($t + 4*86400), time_to_date($t + 5*86400), time_to_date($t + 6*86400)];
	}
	else if ($date_array['wday'] == 1) {
		$bonnedate = [time_to_date($t - 86400), time_to_date($t), time_to_date($t + 86400), time_to_date($t + 2*86400), time_to_date($t + 3*86400), time_to_date($t + 4*86400), time_to_date($t + 5*86400)];
	}
	else if ($date_array['wday'] == 2) {
		$bonnedate = [time_to_date($t - 2*86400), time_to_date($t-86400), time_to_date($t), time_to_date($t + 86400), time_to_date($t + 2*86400), time_to_date($t + 3*86400), time_to_date($t + 4*86400)];
	}
	else if ($date_array['wday'] == 3) {
		$bonnedate = [time_to_date($t - 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t), time_to_date($t + 86400), time_to_date($t + 2*86400), time_to_date($t + 3*86400)];
	}
	else if ($date_array['wday'] == 4) {
		$bonnedate = [time_to_date($t - 4*86400), time_to_date($t- 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t), time_to_date($t + 86400), time_to_date($t + 2*86400)];
	}
	else if ($date_array['wday'] == 5) {
		$bonnedate = [time_to_date($t - 5*86400), time_to_date($t- 4*86400), time_to_date($t - 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t), time_to_date($t + 86400)];
	}
	else if ($date_array['wday'] == 6) {
		$bonnedate = [time_to_date($t - 6*86400), time_to_date($t- 5*86400), time_to_date($t - 4*86400), time_to_date($t - 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t)];
	}
	return $bonnedate;
}

function previous_week_end() {
	$t = time();
	$date_array = getdate($t);
	if ($date_array['wday'] == 0) {
		$bonnedate = [time_to_date($t - 86400), time_to_date($t - 2*86400), time_to_date($t -3*86400), time_to_date($t -4*86400), time_to_date($t -5*86400), time_to_date($t -6*86400), time_to_date($t -7*86400)];
	}
	else if ($date_array['wday'] == 1) {
		$bonnedate = [time_to_date($t - 2*86400), time_to_date($t - 3*86400), time_to_date($t - 4*86400), time_to_date($t -5*86400), time_to_date($t -6*86400), time_to_date($t -7*86400), time_to_date($t -8*86400)];
	}
	else if ($date_array['wday'] == 2) {
		$bonnedate = [time_to_date($t - 3*86400), time_to_date($t-4*86400), time_to_date($t - 5*86400), time_to_date($t -6*86400), time_to_date($t -7*86400), time_to_date($t -8*86400), time_to_date($t -9*86400)];
	}
	else if ($date_array['wday'] == 3) {
		$bonnedate = [time_to_date($t - 4*86400), time_to_date($t -5*86400), time_to_date($t -6*86400), time_to_date($t - 7*86400), time_to_date($t - 8*86400), time_to_date($t -9*86400), time_to_date($t -10*86400)];
	}
	else if ($date_array['wday'] == 4) {
		$bonnedate = [time_to_date($t -5*86400), time_to_date($t- 6*86400), time_to_date($t - 7*86400), time_to_date($t - 8*86400), time_to_date($t - 9*86400), time_to_date($t - 10*86400), time_to_date($t - 11*86400)];
	}
	else if ($date_array['wday'] == 5) {
		$bonnedate = [time_to_date($t - 5*86400), time_to_date($t- 4*86400), time_to_date($t - 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t), time_to_date($t + 86400)];
	}
	else if ($date_array['wday'] == 6) {
		$bonnedate = [time_to_date($t - 6*86400), time_to_date($t- 5*86400), time_to_date($t - 4*86400), time_to_date($t - 3*86400), time_to_date($t - 2*86400), time_to_date($t - 86400), time_to_date($t)];
	}
	return $bonnedate;
}

function gather_matchs($page, $date) {
	$matchs_list = [];
	$header = strpos($page, $date);
	$pos = $header;
	$club_current = "";
	$score_current = "";
	$l = strlen($page);
	while (pos != -1) {
		$pos1 = strpos($page, "equipe1", $pos);
		$i = strpos($page, "class=\"name", $pos1);
		$i = strpos(">", $i) + 3;
		while ($page[$i] == " ") {
			$i = $i + 1;
		}
		while($page[i] != '<') {
			if(($club_current != "") or ($page[i] != " ")) {
				$club_current += $page[i];
			}
			$i = $i + 1;
		}
		while($club_current[-1] == " ") {
			$club_current = substr($club_current, 0, strlen($club_current)-1);
		}
		if($club_current != 'empt') {
			$m = strpos($page,"<div class=\"forfeit\">", $i + 1);
			$k = strpos($page, "</div>", $m);
			if(strpos($page, "Forfait g", $m, $k) != -1) {
				$club_current += " (Forfait g&eacute;n&eacute;ral)";
			}
			else if (strpos($page, "Forfait", $m, $k) != -1) {
				$club_current += " (Forfait)";
			}	
		}
		$matchs_list[] = $date;
		$matchs_list[] = $club_current;
		$club_current ="";
		
		$i = strpos($page, "<div class=\"score_match\">", $i);
		$score_current = get_score($i, $page);
		if(($score_current == " ?") or (score_current == "")) {
			$pos3 = strpos($page, "Report", $i);
			if (($pos3 < $i + 100) and ($pos3 != -1)) {
				$score_current = "Report&eacute;";
			}
			$pos3 = strpos($page, "Non-jou", $i);
			if (($pos3 < $i + 100) and ($pos3 != -1)) {
				$score_current = "Non jou&eacute;";
			}
			$pos3 = strpos($page, "serve", $i);
			if (($pos3 < $i + 100) and ($pos3 != -1)) {
				$score_current = "R&eacute;serve";
			}
			$pos3 = strpos($page, "Arr", $i);
			if (($pos3 < $i + 100) and ($pos3 != -1)) {
				$score_current = "Arr&ecirc;t&eacute;";
			}
		}
		$matchs_list[] = $score_current;
		$score_current = "";
		
		$pos1 = strpos($page, "equipe2", $i);
		$i = strpos($page, "class=\"name", $pos1);
		$i = strpos($page, ">", $i) + 3;
		while ($page[$i] == " ") {
			$i = $i + 1;
		}
		while($page[i] != '<') {
			if(($club_current != "") or ($page[i] != " ")) {
				$club_current += $page[i];
			}
			$i = $i + 1;
		}
		while($club_current[-1] == " ") {
			$club_current = substr($club_current, 0, strlen($club_current)-1);
		}
		if($club_current != 'empt') {
			$m = strpos($page,"<div class=\"forfeit\">", $i + 1);
			$k = strpos($page, "</div>", $m);
			if(strpos($page, "Forfait g", $m, $k) != -1) {
				$club_current += " (Forfait g&eacute;n&eacute;ral)";
			}
			else if (strpos($page, "Forfait", $m, $k) != -1) {
				$club_current += " (Forfait)";
			}	
		}
		$matchs_list[] = $club_current;
		$club_current ="";
		$pos = strpos($page, $date, $i);
	}
	return $matchs_list;
}

function retrieve_date($page, $bonnedate, $coupe) {
	$header = strpos($page, "module-club");
	if (coupe == 0) {
			$pos = strpos($page, "<br/></span><br/>", $header) + strlen("<br/></span><br/>") + 11;
	}
	else {
		$pos = strpos($page, "<div class=\"date\">", $header) + strlen("<div class=\"date\">") + 2;
	}
	$l = strlen($page);
	$date_current = "";
	$date_format = "";
	$i = $pos;
	while (($i < $l) and ($i != -1)) {
		while (($page[$i] != '-') or ($page[i] != ' ')) {
			if (($date_current != "") or ($page[$i] != " ")) {
				$date_current += $page[$i];
			}
			if ($page[$i] != " ") {
				$date_format += $page[$i];
			}
			$i = $i + 1;
		}
		if ($coupe == 0) {
			$pos = strpos("<br/></span><br/>", $i);
		}
		else {
			$pos = strpos("<div class=\"date\">", $i);
		}
		$i = $pos;
		if($date_format == $bonnedate) {
			while ($date_current[-1] == ' ') {
				$date_current = substr($date_current, 0, strlen($date_current)-1);
			}
			return $date_current;
		}
		else {
			$date_format = "";
			$date_current = "";
		}
		if ($i == -1) {
			return "";
		}
		if ($coupe == 0) {
			$i = $pos + strlen("<br/></span><br/>") + 2;
		}
		else {
			$i = $pos + strlen("<div class=\"date\">") + 2;
		}
	}
	return "";
}

function retrieve_champ($page) {
	$pos = strpos($page, "<div class=\"info\"><h1>") + strlen("<div class=\"info\"><h1>");
	$pos1 = strpos($page, "<div class=\"marge\">");
	$champ = "";
	for ($i = pos; $i < $pos1; $i++) {
		$champ = $page[$i];
	}
	$pos = strlen("</h1>&#xA0") + 1;
	
	if (substr($champ, strlen($champ)-$pos) == "</h1>&#xA0;") {
		$champ = substr($champ, 0, -$pos);
	}
	return $champ;
}

function retrieve_tour($page) {
	$pos = strpos($page, "<div class=\"date_tour\">") + strlen("<div class=\"date_tour\">") + 2;
	$pos1 = strpos($page, "</div>", $pos);
	$tour = "";
	$i = $pos;
	while ($page[$i] == " ") {
		$i = $i + 1;
	}
	for ($j = $i; $j < $pos1; $j++) {
		$tour = $page[$j];
	}
	
	return $tour;
}

function retrieve_ligue($url) {
	$i = 7;
	$ligue = "";
	while ($url[$i] != '.') {
		$ligue = $url[$i];
		$i = $i + 1;
	}
	return $ligue;
}

function get_score($i, $page) {
	$tmp_score = "";
	$upper_bound = strpos($page, "</div>", $i);
	$http_pos_0 = $http_pos_1 = 0;
	$ptr = $i;
	$nb = 0;
	while ($http_pos_0 != -1) {
		$old_http_pos_1 = $http_pos_1;
		$http_pos_0 = strpos($page, "http", $ptr, $upper_bound);
		$http_pos_1 = strpos($page, ".png", $ptr, $upper_bound);
		if($http_pos_0 == -1) {
			if($tmp_score == "") {
				$tmp_score = " ?";
			}
			return $tmp_score;
		}
		if (($nb >= 1) and (strpos($page, "-", $old_http_pos_1, $http_pos_0) != -1)) {
			$tmp_score += "-";
		}
		$current_img = substr($page, $http_pos_0, $http_pos_1+4 - $http_pos_0);
		$ptr = $http_pos_1 + 4;
		$file = file_get_contents($current_img);
		$md5 = md5($file);
		$nb +=1;
		for ($i = 0; $i < 10; $i++) {
			if($dico[$i] == $md5) {
				$tmp_score = $i;
				break;
			}
		}
	}
}


?>