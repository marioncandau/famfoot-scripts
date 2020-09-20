#coding: utf-8
from __future__ import unicode_literals
import urllib.request
import hashlib
import time

#<div class="score_match">
score_match = "<div class=\"score_match\">" ;

# Dico

dico = {}
dico["9121a1b22cfdd422236857422039efbd"] = 0 ;
dico["8f0b1c0ec9577d2266f458e7e29a5d00"] = 1 ;
dico["c5137151fc6a8fd42c407aa1c634042c"] = 2 ;
dico["cfc3a46a2d9739062fe557cf7460107c"] = 3 ;
dico["d15f59843a37d06eaa9f54c4dffc120e"] = 4 ;
dico["3171f3b6d49576f436049ac22e8601bd"] = 5 ;
dico["6a4e25f17c5a296199629371cf892ad9"] = 6 ;
dico["88a82803d4dce6327428ee4a276f4b6e"] = 7 ;
dico["483856166855aff3b439af5ace6f70da"] = 8 ;
dico["f2e8d76f6abc1e2232f1e8a64b44f6bc"] = 9 ;

tabjours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'];
tabmois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre'];

class matchClass:
    def __init__(self):
        self.date = ""
        self.numero = 0
        self.equipe1 = ""
        self.equipe2 = ""
        self.score = ""
        self.forfait1 = False
        self.forfait2 = False
        self.forfaitgeneral1 = False
        self.forfaitgeneral2 = False
        self.competition = ""
        self.compet_slug = "";
        self.place1 = 0
        self.place2 = 0
        self.lien = 0;
        self.coupe = 0;

def time_to_date(t):
    if(t.tm_mday > 9):
        return str((tabjours[t.tm_wday]+str(t.tm_mday)+tabmois[t.tm_mon-1]+str(t.tm_year)).encode('utf-8'));
    else:
        return str((tabjours[t.tm_wday]+"0" + str(t.tm_mday)+tabmois[t.tm_mon-1]+str(t.tm_year)).encode('utf-8')); 

def next_week_end():
    t2 = time.time();
    t = time.localtime(t2);
    if(t.tm_wday == 0):
        bonnedate = [time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400)), time_to_date(time.localtime(t2 + 6*86400)), time_to_date(time.localtime(t2 + 7*86400))]; 
    elif(t.tm_wday == 1):
        bonnedate = [time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400)), time_to_date(time.localtime(t2 + 6*86400))];
    elif(t.tm_wday == 2):
        bonnedate = [time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400))];
    elif(t.tm_wday == 3):
        bonnedate = [time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400))];
    elif(t.tm_wday == 4):
        bonnedate = [time_to_date(time.localtime(t2 - 4*86400)),time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)),time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400))];
    elif(t.tm_wday == 5):                                                                                                                                                                                                                                                                                      
        bonnedate = [time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)),time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400))];
    elif(t.tm_wday == 6):
        bonnedate = [time_to_date(time.localtime(t2 - 6*86400)),time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)),time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400))];

    return bonnedate;

def previous_week_end():
    t2 = time.time();
    t = time.localtime(t2);
    if(t.tm_wday == 0):
        bonnedate = [time_to_date(time.localtime(t2)), time_to_date(time.localtime(t2 - 86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400))]; 
    elif(t.tm_wday == 1):
        bonnedate = [time_to_date(time.localtime(t2 - 86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 -6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400))];
    elif(t.tm_wday == 2):
        bonnedate = [time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)), time_to_date(time.localtime(t2 - 9*86400))];
    elif(t.tm_wday == 3):
        bonnedate = [time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)), time_to_date(time.localtime(t2 - 9*86400)), time_to_date(time.localtime(t2 - 10*86400))];
    elif(t.tm_wday == 4):
        bonnedate = [time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)),time_to_date(time.localtime(t2 - 9*86400)), time_to_date(time.localtime(t2 - 10*86400)), time_to_date(time.localtime(t2 - 11*86400))];
    elif(t.tm_wday == 5):                                                                                                                                                                                                                                                                                      
        bonnedate = [time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)),time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400))];
    elif(t.tm_wday == 6):
        bonnedate = [time_to_date(time.localtime(t2 - 6*86400)),time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)),time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400))];

    return bonnedate;

def gather_matchs(page, date, link, coupe, isRes):
    matchs_list = [];
    header = page.find(date);
    pos = header;
    club_current = "";
    score_current = "";
    length = len(page);
    html_class = html_classement(link)
    while(pos != -1):
        match = matchClass()
        match.lien = link;
        match.coupe = coupe;
        pos1 = page.rfind("match_id=", 0, pos) + len("match_id=");
        pos2 = min(page.find("\"", pos1), page.find("&", pos1));
        match.numero = int(page[pos1:pos2]);
        pos = pos1;
        pos1 = page.find("equipe1", pos);
        i = page.find("class=\"name", pos1);
        i = page.find(">", i) + 3;
        while(page[i] == " "):
            i = i + 1;
        
        while(page[i] != '<'):
            if (club_current != "" or page[i] != " "):
                club_current += page[i];
            i = i + 1;
        while(club_current[-1] == " "):
            club_current = club_current[:-1];
        if(club_current != 'empt'):
            if(coupe == 0 and isRes == 0):
                match.place1 = add_classement(club_current, html_class);
            m = page.find("<div class=\"forfeit\">", i + 1);
            k = page.find("</div>", m);
            if (page.find("Forfait g", m, k) != -1):
                match.forfaitgeneral1 = 1
            elif (page.find("Forfait", m, k) != -1):
                match.forfait1 = 1
        match.date = date
        if(club_current == "empt"):
            club_current = "Exempt";
        match.equipe1 = club_current;
        club_current = "";

        #recuperer le score
        i = page.find(score_match, i);
        score_current = get_score(i, page);
        if (score_current == " ?" or score_current == ""):
            pos3 = page.find("Report", i);
            if (pos3 < i + 100 and pos3 != -1):
                score_current = "Report&eacute;";
            pos3 = page.find("Non-jou", i);
            if (pos3 < i + 100 and pos3 != -1):
                score_current = "Non jou&eacute;";
            pos3 = page.find("serve", i);
            if (pos3 < i + 100 and pos3 != -1):
                score_current = "R&eacute;serve";
            pos3 = page.find("Arr", i);
            if (pos3 < i + 100 and pos3 != -1):
                score_current = "Arr&ecirc;t&eacute;";
        match.score = score_current;
        score_current = "";
            
        pos1 = page.find("equipe2", i);
        i = page.find("class=\"name", pos1);
        i = page.find(">", i) + 3;
        while(page[i] == " "):
            i = i + 1;
        while(page[i] != '<'):
            if (club_current != "" or page[i] != " "):
                club_current += page[i];
            i = i + 1;
        while(club_current[-1] == " "):
            club_current = club_current[:-1];
        if(club_current != "empt"):
            if(coupe == 0 and isRes == 0):
                match.place2 = add_classement(club_current, html_class);
            m = page.find("<div class=\"forfeit\">", i + 1);
            k = page.find("</div>", m);
            if (page.find("Forfait g", m, k) != -1):
                match.forfaitgeneral2 = 1
            elif (page.find("Forfait", m, k) != -1):
                match.forfait2 = 1
        if(club_current == "empt"):
            club_current = "Exempt";
        match.equipe2 = club_current;
        matchs_list.append(match);
        club_current = "";
        pos = page.find(date, i);
        
    return matchs_list;


def retrieve_date(page, bonnedate, coupe):
    header=page.find("module-club");
    if (coupe == 0):
        pos=page.find("<br/></span><br/>",header) + len("<br/></span><br/>") + 11;
    else:
        pos = page.find("<div class=\"date\">", header) + len("<div class=\"date\">") + 2;
    length = len(page);
    date_current = "";
    date_format = "";
    i = pos;
    while(i < length and i != -1):
        while(page[i] != '-' and page[i] != '<'):
            if (date_current != "" or page[i] != " "):
                date_current+=page[i];
            if(page[i] != ' '):
                date_format += page[i];
            i = i + 1;
        if(coupe == 0):
            pos=page.find("<br/></span><br/>", i);
        else:
            pos = page.find("<div class=\"date\">", i);
        i = pos;
        if((str(date_format.replace("é", "e")) == str(str(bonnedate))[2:-1]) or (str(date_format.replace("û", "u")) == str(str(bonnedate))[2:-1])):
            while(date_current[-1] == ' '):
                date_current = date_current[:-1];
            return date_current;
        else:
            date_format = "";
            date_current = "";
        if(i == -1):
            return "";
        if(coupe == 0):
            i = pos + len("<br/></span><br/>") + 2;
        else:
            i = pos + len("<div class=\"date\">") + 2;
    return "";

def retrieve_champ(page):
    pos=page.find("<div class=\"info\"><h1>") + len("<div class=\"info\"><h1>");
    pos1=page.find("<div class=\"marge\">");
    champ = "";
    for i in range(pos, pos1):
        champ+=page[i];
    pos = len("</h1>&#xA0")+1; 

    if(champ[len(champ)-pos:] == "</h1>&#xA0;"):
        champ = champ[:-pos];
    return champ;

def retrieve_tour(page):
    pos=page.find("<div class=\"date_tour\">") + len("<div class=\"date_tour\">") + 2;
    pos1=page.find("</div>", pos);
    tour = "";
    i = pos;
    while(page[i] == " "):
        i = i + 1;
    for j in range(i, pos1):
        tour+=page[j];
    
    return tour;

def retrieve_ligue(url):
    i = 7;
    ligue = "";
    while(url[i] != '.'):
        ligue+=url[i];
        i = i + 1;
    return ligue;

def get_score(i, page):
    tmp_score = "" ;
    upper_bound = page.find("</div>",i) ;
    http_pos_0 = http_pos_1 = 0 ;
    ptr = i ;
    nb = 0 ;
    # On récupère toutes les images.
    while(http_pos_0 != -1):
        old_http_pos_1 = http_pos_1 ;
        http_pos_0 = page.find("http", ptr, upper_bound) ;
        http_pos_1 = page.find(".png", ptr, upper_bound) ;
        if http_pos_0 == -1:
            if(tmp_score == ""):
                tmp_score = " ?";
            return tmp_score;
        # On vérifie s'il y a un tiret entre les images
        if nb >= 1 and page.find("-", old_http_pos_1, http_pos_0) != -1:
            tmp_score += "-" ;
        current_img = page[http_pos_0:http_pos_1+4] ;
        ptr = http_pos_1+4 ;
        # On charge l'image
        file = urllib.request.urlopen(current_img).read() ;
        md5  = hashlib.md5() ;
        md5.update(file) ;
        hash_img = md5.hexdigest() ;
        nb+= 1 ;
        tmp_score += str(dico[hash_img]) ;
    return tmp_score;

def html_classement(link):
    i = len(link) - 1;
    while(link[i] != "="):
        i = i - 1
    link = link[0:i] + "=ranking";
    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    response = urllib.request.urlopen(req);
    html = str(response.read().decode('utf-8'));
    return(html)

def add_classement(club, html):
    res = club;
    pos = html.find(club);
    pos = pos - len(club) - 120;
    pos = html.find('<td class="ranking-tab-content">', pos);
    if(pos != -1):
        pos = pos + len('<td class="ranking-tab-content">');
        i = pos
        while(html[i] != '<'):
            i = i + 1;
        if(pos < i):
            res = html[pos:i];
    if(res == club):
        res = 0
    return(res);



