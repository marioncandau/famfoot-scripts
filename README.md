# famfoot-scripts

Ce repository contient les scripts nécessaires pour famfoot.

Quand on clique sur le bouton "Actualiser les matchs" sur https://famfoot.fr/agenda/ le fichier agenda.php est appelé. Il remplit le fichier resultats_famfoot.txt avec la liste des liens menant aux calendriers sur les sites des districts/de la ligue. Il appelle agenda.py afin de générer agenda.json et date_agenda.json. Le premier contient la liste des matchs à jouer le prochain week-end et l'autre les dates de ce week-end. A partir des infos du JSON, on remplit la table matchs dans la BDD. Cette table est utilisée pour afficher les matchs de l'agenda.

Les fichiers resultats.php, resultats.py, resultats.json et date_resultat.json sont utilisés de la même façon pour créer les résultats (donc le week-end précédent). 

famfoot.py contient ls fonctions python communes aux 2 scripts agenda.py et resultats.py. 

Les fichiers famfoot_fff.py et api_fff.py sont un projet d'API du site de la fff où à partir d'une compétition en entrée, on répondrait le JSON des résultats, de l'agenda, du calendrier complet et du classement. 

Le dossier "classement des buteuses" contient les scripts pour générer les classements des buteuses, qui sont ensuite copiés-collés dans des articles wordpress. 

