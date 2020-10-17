#coding: utf-8
from __future__ import unicode_literals
import urllib.request
import hashlib
import time
import famfoot

def build_tab_res(html, url, g, bonnedate, champ_name, coupe, slug):
    result = 0;
    c = [];
    b = 0;
    for date in bonnedate:
        c.append(famfoot.retrieve_date(html, date, coupe));
        if(c[-1] != ""):
            result = 1;
    for date in c:
        if(date != ""):
            a = famfoot.gather_matchs(html, date, url, coupe, 1);
            for t in a:
                t.competition = champ_name
                t.compet_slug = slug
                g.write("{");
                datetow = str(t.date.encode('utf-8'))[2:-1].replace("\\xc3\\xa9", "&eacute;")
                g.write('"date": "' + datetow + '",  ');
                g.write('"journee": ' + str(t.journee) + ', ')
                if(datetow not in datew):
                    datew.append(datetow);
                g.write('"numero": ' + str(t.numero) + ', ');
                g.write('"equipe1": "' + t.equipe1.replace("\\xc3\\xa9", "&eacute;").upper().replace("\\XC3\\X89", "&Eacute;").replace("\\XC3\\X88", "&Egrave;").replace("\\xc3\\xa8", "&egrave;") + '", ');
                g.write('"equipe2": "' + t.equipe2.replace("\\xc3\\xa9", "&eacute;").upper().replace("\\XC3\\X89", "&Eacute;").replace("\\XC3\\X88", "&Egrave;").replace("\\xc3\\xa8", "&egrave;") + '", ');
                g.write('"equipe1_id": ' + str(t.equipe1_id) + ', ')
                g.write('"equipe2_id": ' + str(t.equipe2_id) + ', ')
                g.write('"score": "' + t.score + '", ');
                g.write('"forfait1": ' + str(int(t.forfait1)) + ', ');
                g.write('"forfait2": ' + str(int(t.forfait2)) + ', ');
                g.write('"forfaitgeneral1": ' + str(int(t.forfaitgeneral1)) + ', ');
                g.write('"forfaitgeneral2": ' + str(int(t.forfaitgeneral2)) + ', ');
                g.write('"competition": "' + str(t.competition.encode('utf-8'))[2:-1].replace("\\xc3\\xa9", "&eacute;").replace("\\xc3\\xa8", "&egrave;") + '", ');
                g.write('"compet_slug": "' + t.compet_slug + '", ');
                g.write('"place1": ' + str(t.place1) + ', ');
                g.write('"place2": ' + str(t.place2)+ ', ');
                g.write('"lien": "' + t.lien[:-1] + '", ');
                g.write('"coupe": ' + str(int(t.coupe)));
                g.write("}\n");
                
f = open("resultats_famfoot.txt", "r", encoding = "utf-8");
g = open("resultat.json", "w");
datefile = open("date_resultat.json", "w");

datew = [];


for line in f:
    if(line[0] == '/'):
        champ_name = line[3:-1];
        response = 0;
        coupe = 0;
    elif(line[0] == '*'):
        champ_name = line[3:-1];
        coupe = 1;
        response = 0;
    elif(line[0] == 'C'):
        h = open(line[:-1], "r");
        response = h.readlines();
        h.close();
    elif(line[0] == '0'):
        slug = line[1:-1];
    elif(line[0] == 'h'):
        try:
            req = urllib.request.Request(line, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            response = urllib.request.urlopen(req);
        except:
            print("erreur on line: " + line);
            time.sleep(40);
            response = urllib.request.urlopen(req);
        if(response != 0):
            html = str(response.read().decode('utf-8'));
            if(coupe == 1):
                k = famfoot.retrieve_tour(html);
                champ_name = champ_name + " - " + k;
            g = open("resultat.json", "a");
            bonnedate = famfoot.previous_week_end();
            build_tab_res(html, line, g, bonnedate, champ_name, coupe, slug);
            g.close();

datefile.write(str(datew));
g.close();
f.close();
datefile.close();




