# -*- coding: utf-8 -*-

import unicodedata

ALPHA = "abcdefghijklmnopqrstuvwxyz" ;

def PosCharInString(char, string):
    cpt = 0 ;
    for i in string:
        if i==char:
            return cpt;
        cpt = cpt+1 ;
    return 26 ; 
        

def Enleve_Accents(txt):
    ch1 = u"àâçéèêëîïôùûüÿ"
    ch2 = u"aaceeeeiiouuuy"
    s = ""
    for c in txt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s

def Get_nth_field(ligne,nb):
    switch = '0' ;
    retour = "" ;
    i_nb = 0 ;
    for i in ligne:
        if (i!='\t'):
            if (switch=='0'):
                switch='1'    ;
                i_nb = i_nb+1 ;
            if (switch=='1'):
                if (i_nb == nb and i != '\n'):
                    retour=retour+i ;
        else:
            if (switch=='1'):
                switch='0';
    return retour ;

def Get_nth_word(ligne,nb):
    switch = '0' ;
    retour = "" ;
    i_nb = 0 ;
    for i in ligne:
        if (i!=' '):
            if (switch=='0'):
                switch='1'    ;
                i_nb = i_nb+1 ;
            if (switch=='1'):
                if (i_nb == nb and i != '\n'):
                    retour=retour+i ;
        else:
            if (switch=='1'):
                switch='0';
    return retour ;


def Get_nb_words(ligne):
    switch = '1' ;
    nb_lg = 0 ;
    for i in ligne:
        if i==' ':
            switch='1';
        else:
            if switch=='1':
                nb_lg=nb_lg+1;
                switch='0';
    return nb_lg ;
                
        
def Print_DB(DB):
    for i in DB:
        print(i);

def Create_DB(file):
    op_file = open(file,'r');
    DB = [] ;
    for i in op_file:
        tmp = [] ;
        tmp = [Get_nth_field(i,1),Get_nth_field(i,2),Get_nth_field(i,3)]
        DB.append(tmp);
    return DB ; 

def sort_DB_Goal(DB):
    length = len(DB);
    Sort_DB = DB.copy() ;
    Output_DB = [] ; 
    for i in range(length):
        mmax = 0 ; lmax = 0 ;
        for j in range(length):
            if int(Sort_DB[j][2])>mmax:
                mmax = int(Sort_DB[j][2]); 
                lmax = j ;
        Output_DB.append(Sort_DB[lmax].copy());
        Sort_DB[lmax][2] = 0 ; 
    return Output_DB ;

def sort_DB_Alpha(DB):
    length = len(DB);
    Sort_DB = DB.copy() ;
    for i in range(length):
        mmin = "wwww" ; lmin = 0 ;
        for j in range(i,length):
            tmp = Sort_DB[j][0];
            tmp = Get_nth_word(tmp,2);
            tmp = Enleve_Accents(tmp).lower();
            if tmp < mmin:
                mmin = tmp ;
                lmin = j ;
        tmp = Sort_DB[i] ;
        Sort_DB[i] = Sort_DB[lmin] ;
        Sort_DB[lmin] = tmp ; 
    return Sort_DB ;

def Generate_HTML(DB, file):
    B = sort_DB_Alpha(DB);
    B = sort_DB_Goal(B);
    Print_DB(B);
    op_file = open(file,'w');
    cpt=1;
    cpt2=1;
    old_score=0;
    op_file.write("<table> \n");
    op_file.write("<tbody> \n");
    op_file.write("<tr> \n");
    op_file.write("<td class=\"cla\"></td> \n");
    op_file.write("<td class=\"nom\">Joueuse</td> \n");
    op_file.write("<td class=\"club\">Club</td> \n");
    op_file.write("<td class=\"buts\">Buts</td> \n");
    op_file.write("<td>Buts ce week-end</td> \n");
    op_file.write("</tr> \n");
    for i in B:
        if old_score != i[2]:
            cpt=cpt2;
            old_score = i[2];
            print("DEBUG "+str(i));
        
        cpt2=cpt2+1 ;
        op_file.write("<tr> \n")
        op_file.write(" <td class=\"cla\"> ");
        op_file.write(str(cpt));        
        op_file.write(" </td> \n");
        op_file.write(" <td class=\"nom\"> ");
        op_file.write(i[0]);        
        op_file.write(" </td> \n")       
        op_file.write(" <td class=\"club\"> ");
        op_file.write(i[1]);        
        op_file.write(" </td> \n")
        op_file.write(" <td class=\"buts\"> ");
        op_file.write(i[2]);        
        op_file.write(" </td> \n")
        op_file.write(" <td> </td> \n")
        op_file.write("</tr> \n");

    op_file.write("</tbody> \n");
    op_file.write("</table> \n");
    op_file.close();
    
if __name__=="__main__":
    B = Create_DB("BDD_R2Sud.txt");
    Generate_HTML(B,"generated_file_R2Sud.htm");
    print("Done");
