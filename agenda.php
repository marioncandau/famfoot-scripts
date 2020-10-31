<?php 

try
{
	$pdo_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;
	$bdd = new PDO('mysql:host=localhost;dbname=famfoot_db', 'marion', 'mySqlfoTbal:8', $pdo_options);
}
catch (Exception $e)
{
	 die('Erreur : ' . $e->getMessage());
}

$fp = fopen ("resultats_famfoot.txt", "wb");

$query = $bdd->query("SELECT * FROM champ_aqu WHERE tri > 5 ORDER BY tri");
while($row = $query->fetch()) {
	$lien = $row['lien'];
	$nom_champ = $row['nom'];
	$prefix = $row['prefix'];
	$slug = $row['slug'];
	$query2 = $bdd->query("SELECT * FROM poules_aqu WHERE championnat = $lien");
	while($row2 = $query2->fetch()) {
		$nom_poule = $row2['nom'];
		$numero = $row2['numero'];
		$phase = $row2['phase'];
		if($row['coupe'] == false) {
			fwrite($fp, "/* $nom_champ - $nom_poule\n");
			fwrite($fp, "0$slug\n");
			fwrite($fp, "https://$prefix.fff.fr/competitions/?id=$lien&poule=$numero&phase=$phase&type=ch&tab=calendar\n");
		}
		else {
			if($nom_poule != "") {
				fwrite($fp, "*  $nom_champ - $nom_poule\n");
				fwrite($fp, "0$slug\n");
			}
			else {
				fwrite($fp, "*  $nom_champ\n");
				fwrite($fp, "0$slug\n");
			}
			fwrite($fp, "https://$prefix.fff.fr/competitions/?id=$lien&poule=$numero&phase=$phase&type=cp&tab=resultat\n");
		}
	}	
}

fclose($fp);

if($bdd){
    $bdd = NULL;
}

echo shell_exec("python3 agenda.py 2>&1"); 

try
{
	$pdo_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;
	$bdd = new PDO('mysql:host=localhost;dbname=famfoot_db', 'marion', 'mySqlfoTbal:8', $pdo_options);
}
catch (Exception $e)
{
	 die('Erreur : ' . $e->getMessage());
}

$fp = fopen("agenda.json", "rb");
$datep = fopen("date_agenda.json", "rb");

if($datep) {
	$query = $bdd->query("TRUNCATE TABLE date_agenda");
	$datepcontent = substr(fgets($datep), 1, -1);
	if($datepcontent != "") {
		$buffer = explode(", ", $datepcontent);
		for ($i = 0; $i < count($buffer); $i++) {
			$query = $bdd->query("INSERT INTO date_agenda (date) VALUES (".$buffer[$i].")");
		}
	}
}


if ($fp)
{
	while (!feof($fp))
	{
		$buffer = fgets($fp);
		$j = json_decode($buffer);
		if($j != NULL) {
			$query = $bdd->query("SELECT * FROM matchs WHERE matchid = ".$j->{'numero'});
			if($row = $query->fetch()) {
				if((($j->{'score'} != " ?") and (($row['score'] == " ?") or ($row['score'] == "Report&eacute;") or ($row['score'] == "Report&eacute")  or ($row['score'] == "Non jou&eacute;"))) or (($j->{'score'} == " ?") and (($row['score'] == 'Report&eacute') or ($row['score'] == 'Report&eacute;') or ($row['score'] == "Non jou&eacute;")))) {
					$q = $bdd->query("UPDATE matchs SET date = '".$j->{'date'}."', score = '".$j->{'score'}."', forfait_equipe1 = ".$j->{'forfait1'}.", forfait_equipe2 = ".$j->{'forfait2'}.", forfaitgeneral1 = ".$j->{'forfaitgeneral1'}.", forfaitgeneral2 = ".$j->{'forfaitgeneral2'}." WHERE matchid = ".$j->{'numero'});
				}
				else {
					$q = $bdd->query("UPDATE matchs SET date = '".$j->{'date'}."', equipe1='".$j->{'equipe1'}."', equipe2='".$j->{'equipe2'}."', equipe1_id=".$j->{'equipe1_id'}.", equipe2_id=".$j->{'equipe2_id'}." WHERE matchid = ".$j->{'numero'});
				}
			}
			else {
				$q2 = $bdd->query("INSERT INTO matchs (matchid, competition, compet_slug, date, journee, equipe1, equipe2, equipe1_id, equipe2_id, forfait_equipe1, forfait_equipe2, forfaitgeneral1, forfaitgeneral2, place1, place2, score, coupe) VALUES (".$j->{'numero'}.", '".$j->{'competition'}."', '".$j->{'compet_slug'}."', '".$j->{'date'}."', ".$j->{'journee'}.", '".$j->{'equipe1'}."', '".$j->{'equipe2'}."', ".$j->{'equipe1_id'}.", ".$j->{'equipe2_id'}.", ".$j->{'forfait1'}.", ".$j->{'forfait2'}.", ".$j->{'forfaitgeneral1'}.", ".$j->{'forfaitgeneral2'}.", ".$j->{'place1'}.", ".$j->{'place2'}.", '".$j->{'score'}."', ".$j->{'coupe'}.")");
			}
		}
	}
	fclose($fp);
}

?>
<meta http-equiv="Refresh" content="0;url=https://www.famfoot.fr/agenda">