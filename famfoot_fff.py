#coding: utf-8
from __future__ import unicode_literals
import urllib.request
import hashlib
import time
import datetime

# in development

#<div class="score_match">
score_match = "<div class=\"score_match\">" 
title_box = "<div class=\"title_box\">"

# Dico

dico = {}
dico["9121a1b22cfdd422236857422039efbd"] = 0 
dico["8f0b1c0ec9577d2266f458e7e29a5d00"] = 1 
dico["c5137151fc6a8fd42c407aa1c634042c"] = 2 
dico["cfc3a46a2d9739062fe557cf7460107c"] = 3 
dico["d15f59843a37d06eaa9f54c4dffc120e"] = 4 
dico["3171f3b6d49576f436049ac22e8601bd"] = 5 
dico["6a4e25f17c5a296199629371cf892ad9"] = 6 
dico["88a82803d4dce6327428ee4a276f4b6e"] = 7 
dico["483856166855aff3b439af5ace6f70da"] = 8 
dico["f2e8d76f6abc1e2232f1e8a64b44f6bc"] = 9 

tabjours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
tabmois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
        

def time_to_date(t):
    if(t.tm_mday > 9):
        return str((tabjours[t.tm_wday]+str(t.tm_mday)+tabmois[t.tm_mon-1]+str(t.tm_year)).encode('utf-8'))
    else:
        return str((tabjours[t.tm_wday]+"0" + str(t.tm_mday)+tabmois[t.tm_mon-1]+str(t.tm_year)).encode('utf-8')) 

def next_week_end():
    t2 = time.time()
    t = time.localtime(t2)
    if(t.tm_wday == 0):
        bonnedate = [time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400)), time_to_date(time.localtime(t2 + 6*86400)), time_to_date(time.localtime(t2 + 7*86400))] 
    elif(t.tm_wday == 1):
        bonnedate = [time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400)), time_to_date(time.localtime(t2 + 6*86400))]
    elif(t.tm_wday == 2):
        bonnedate = [time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400)), time_to_date(time.localtime(t2 + 5*86400))]
    elif(t.tm_wday == 3):
        bonnedate = [time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400)), time_to_date(time.localtime(t2 + 4*86400))]
    elif(t.tm_wday == 4):
        bonnedate = [time_to_date(time.localtime(t2 - 4*86400)),time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)),time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400)), time_to_date(time.localtime(t2 + 3*86400))]
    elif(t.tm_wday == 5):     
        bonnedate = [time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)),time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400))]
    elif(t.tm_wday == 6):
        bonnedate = [time_to_date(time.localtime(t2 - 6*86400)),time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)),time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400))]

    return bonnedate

def previous_week_end():
    t2 = time.time()
    t = time.localtime(t2)
    if(t.tm_wday == 0):
        bonnedate = [time_to_date(time.localtime(t2)), time_to_date(time.localtime(t2 - 86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400))] 
    elif(t.tm_wday == 1):
        bonnedate = [time_to_date(time.localtime(t2 - 86400)), time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 -6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400))]
    elif(t.tm_wday == 2):
        bonnedate = [time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)), time_to_date(time.localtime(t2 - 9*86400))]
    elif(t.tm_wday == 3):
        bonnedate = [time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)), time_to_date(time.localtime(t2 - 9*86400)), time_to_date(time.localtime(t2 - 10*86400))]
    elif(t.tm_wday == 4):
        bonnedate = [time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 6*86400)), time_to_date(time.localtime(t2 - 7*86400)), time_to_date(time.localtime(t2 - 8*86400)),time_to_date(time.localtime(t2 - 9*86400)), time_to_date(time.localtime(t2 - 10*86400)), time_to_date(time.localtime(t2 - 11*86400))]
    elif(t.tm_wday == 5):         
        bonnedate = [time_to_date(time.localtime(t2 - 5*86400)),time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)), time_to_date(time.localtime(t2 - 2*86400)),time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400)), time_to_date(time.localtime(t2 + 2*86400))]
    elif(t.tm_wday == 6):
        bonnedate = [time_to_date(time.localtime(t2 - 6*86400)),time_to_date(time.localtime(t2 - 5*86400)), time_to_date(time.localtime(t2 - 4*86400)), time_to_date(time.localtime(t2 - 3*86400)),time_to_date(time.localtime(t2 - 2*86400)), time_to_date(time.localtime(t2 - 86400)), time_to_date(t), time_to_date(time.localtime(t2 + 86400))]

    return bonnedate

def gather_matchs(html, date, coupe):
    all = dict()
    calendrier = dict()
    calendrier.journees = []
    classement = dict()
    agenda = dict()
    resultats = dict()
    matchs = []
    journee_num = 0
    journee_nom = ""

    pos = html.find("<div id=\"match-list")
    while(pos != -1):
        pos1 = html.find(title_box, pos)
        pos2 = html.find("<h4>", pos)
        if pos1 < pos2:
            if matchs != []:
                journee = dict()
                if coupe == 0:
                    journee.numero = journee_num
                else:
                    journee.nom = journee_nom
                journee.matchs = matchs
                calendrier.journees.append(journee)
            if coupe == 0:
                journee_num = retrieve_journee(html, pos1)
            else:
                journee_nom = retrieve_tour(html, pos1)
            pos = pos1
        else:
            date = parse_date(html, pos2)
            pos = pos2

        pos = html.find("eqleft", pos)
        equipe_dom = parse_equipe(html, pos)
        pos = html.find("class=\"score\"")
        score = get_score(html, pos)
        pos = html.find("eqright", pos)
        equipe_ext = parse_equipe(html, pos)
        pos = html.find("href=\"/match/")
        match_id = get_id(html, pos)
        match = dict()
        match.date = dict()
        match.date.lisible = date
        match.date.timestamp = time.mktime(datetime.datetime.strptime(date, "%A %d %B %Y - %H:%M").timetuple())
        match.equipes = dict()
        match.equipes.dom = equipe_dom
        match.equipes.ext = equipe_ext
        match.score = score
        match.id = match_id

    all.calendrier = calendrier
    all.classement = classement
    all.resultats = resultats
    all.agenda = agenda
    return all


def retrieve_date(page, bonnedate, coupe):
    header=page.find("module-club")
    if (coupe == 0):
        pos=page.find("<br/></span><br/>",header) + len("<br/></span><br/>") + 11
    else:
        pos = page.find("<div class=\"date\">", header) + len("<div class=\"date\">") + 2
    length = len(page)
    date_current = ""
    date_format = ""
    i = pos
    while(i < length and i != -1):
        while(page[i] != '-' and page[i] != '<'):
            if (date_current != "" or page[i] != " "):
                date_current+=page[i]
            if(page[i] != ' '):
                date_format += page[i]
            i = i + 1
        if(coupe == 0):
            pos=page.find("<br/></span><br/>", i)
        else:
            pos = page.find("<div class=\"date\">", i)
        i = pos
        if((str(date_format.replace("é", "e")) == str(str(bonnedate))[2:-1]) or (str(date_format.replace("û", "u")) == str(str(bonnedate))[2:-1])):
            while(date_current[-1] == ' '):
                date_current = date_current[:-1]
            return date_current
        else:
            date_format = ""
            date_current = ""
        if(i == -1):
            return ""
        if(coupe == 0):
            i = pos + len("<br/></span><br/>") + 2
        else:
            i = pos + len("<div class=\"date\">") + 2
    return ""

def retrieve_tour(page):
    pos=page.find("<div class=\"date_tour\">") + len("<div class=\"date_tour\">") + 2
    if(pos == len("<div class=\"date_tour\">") + 1):
        return ""
    pos1=page.find("</div>", pos)
    tour = ""
    i = pos
    while(page[i] == " "):
        i = i + 1
    k = pos1-1
    while(page[k] == " "):
        k = k - 1
    for j in range(i, k+1):
        tour+=page[j]
    
    return tour

def get_score(i, page):
    tmp_score = "" 
    upper_bound = page.find("</div>",i) 
    http_pos_0 = http_pos_1 = 0 
    ptr = i 
    nb = 0 
    # On récupère toutes les images.
    while(http_pos_0 != -1):
        old_http_pos_1 = http_pos_1 
        http_pos_0 = page.find("http", ptr, upper_bound) 
        http_pos_1 = page.find(".png", ptr, upper_bound) 
        if http_pos_0 == -1:
            if(tmp_score == ""):
                tmp_score = " ?"
            tmp_score += get_penalty(i, page)
            return tmp_score
        # On vérifie s'il y a un tiret entre les images
        if nb >= 1 and page.find("-", old_http_pos_1, http_pos_0) != -1:
            tmp_score += "-" 
        current_img = page[http_pos_0:http_pos_1+4] 
        ptr = http_pos_1+4 
        # On charge l'image
        file = urllib.request.urlopen(current_img).read() 
        md5  = hashlib.md5() 
        md5.update(file) 
        hash_img = md5.hexdigest() 
        nb+= 1 
        tmp_score += str(dico[hash_img]) 

    tmp_score += get_penalty(i, page)
    return tmp_score

def get_penalty(i, page):
    penaltypos = page.find('<div class="score_match_penalty">',i) + len('<div class="score_match_penalty">')
    while(page[penaltypos] == ' ' or page[penaltypos] == '\n'):
        penaltypos+=1
    endpenaltypos = page.find("</div>", penaltypos)
    while(page[endpenaltypos-1] == ' '):
        endpenaltypos-=1
    penalty = page[penaltypos-1:endpenaltypos]
    return penalty

def retrieve_journee(linkmatch):
    pos = linkmatch.find('Journ')+ len('Journee ')
    pos1 = pos
    while (linkmatch[pos1] != " "):
        pos1 = pos1 + 1

    jour = int(linkmatch[pos:pos1])
    return(jour)
    
    



