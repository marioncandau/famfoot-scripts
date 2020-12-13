#coding: utf-8
from __future__ import unicode_literals
import urllib.request
import hashlib
import time
import famfoot

def extractEquipes(html):
    f = open("equipes.txt", "w", encoding = "utf-8")
    page = html
    pos = page.find("title=\"Equipe\"")
    while(pos != -1):
        numero_club = ""
        club_current = ""
        pos1 = page.find("option value", pos) + len("option value") + 2

        i = pos1
        while(page[i] != '-'):
            numero_club += page[i]
            i = i + 1

        pos1 = page.find(">", i) + 1
        i = pos1
        while(page[i] != '<'):
            club_current += page[i]
            i = i + 1
        print(numero_club + " - " + club_current)
        
        if (page.find("</select>", pos) < i):
            pos = -1
        else:
            pos = i
            f.write(numero_club + " - " + club_current + "\n")
        
    f.close

#arg = sys.argv[1]
arg = "https://lfna.fff.fr/competitions/?id=350388&poule=1&phase=1&type=ch&tab=resultat"

try: 
    response = urllib.request.urlopen(arg)
except:
    print("erreur on line: " + arg)
    time.sleep(40)
    response = urllib.request.urlopen(arg)
if(response != 0):
    html = str(response.read())
    extractEquipes(html)
            





