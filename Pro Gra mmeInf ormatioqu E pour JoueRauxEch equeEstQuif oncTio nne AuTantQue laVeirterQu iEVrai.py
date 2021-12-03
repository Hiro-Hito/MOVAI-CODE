import time
taille = 8

def placer_pion():
    global plateau
    for x in range(8):
        plateau[1][x] = '♟'
        plateau[6][x] = '♙'
    
    plateau[0][0] = '♜';plateau[7][7] = '♖';plateau[0][7] = '♜';plateau[7][0] = '♖' ;plateau[0][1] = '♞';plateau[7][6] = '♘';plateau[0][6] = '♞';plateau[7][1] = '♘';plateau[0][2] = '♝';plateau[7][5] = '♗';plateau[0][5] = '♝'#Tout ca pour rien!!! cheh
    plateau[7][2] = '♗';plateau[0][3] = '♛';plateau[7][3] = '♕';plateau[7][4] = '♔';plateau[0][4] = '♚'
    
def creation_plateau():
    global plateau
    plateau = [[' ']*taille for _ in range(taille)]
    placer_pion()
    return plateau

def afficher_plateau():
    global plateau;print('-------------------------------------');print('| x | a | b | c | d | e | f | g | h |')
    print('-------------------------------------')
    for x in range(taille):
        texte = '| ' + str(8-x) +' | '
        for y in range(taille):
            texte = texte + str(plateau[x][y]) + ' | '
        print(texte);print('-------------------------------------')



def lettre_to_chiffre(test):
    if test == 'a':return 0
    elif test == 'b':return 1
    elif test == 'c':return 2
    elif test == 'd':return 3
    elif test == 'e':return 4
    elif test == 'f':return 5
    elif test == 'g':return 6
    elif test == 'h':return 7
    else:return -1
######  ######
def type_pion(test_x,test_y):
    global plateau
    if plateau[test_x][test_y] == '♟': return ('noir','pion')
    elif plateau[test_x][test_y] == '♜': return ('noir','tour')
    elif plateau[test_x][test_y] == '♞': return ('noir','cavalier')
    elif plateau[test_x][test_y] == '♝': return ('noir','fou')
    elif plateau[test_x][test_y] == '♛': return ('noir','dame')
    elif plateau[test_x][test_y] == '♚': return ('noir','roi')
    elif plateau[test_x][test_y] == '♙': return ('blanc','pion')
    elif plateau[test_x][test_y] == '♖': return ('blanc','tour')
    elif plateau[test_x][test_y] == '♘': return ('blanc','cavalier')
    elif plateau[test_x][test_y] == '♗': return ('blanc','fou')
    elif plateau[test_x][test_y] == '♕': return ('blanc','dame')
    elif plateau[test_x][test_y] == '♔': return ('blanc','roi')
    else: return (None,None)

def condition(x,y,a,b):
    global plateau;jeu_possible = [];type_pion_depart = type_pion(x,y);type_pion_arriver = type_pion(a,b)
    if type_pion_depart[1] == 'pion':
        if type_pion_depart[0] == 'blanc':
                #Tout est nickel pour le pion
            if type_pion_arriver[0] == None:
                if a == x - 1 and b == y:
                    return True
                elif a == x - 2 and b == y and plateau[x-1][y] == ' ' and x == 6:
                    return True
                else:
                    return False

            elif type_pion_arriver[0] == 'noir':
                if a == x - 1 and b == y + 1 or a == x - 1 and b == y - 1:
                    return True
                else:
                    return False

        elif type_pion_depart[0] == 'noir':
            #Tout est nickel pour le pion
            if type_pion_arriver[0] == None:
                if a == x + 1 and b == y:
                    return True
                elif a == x + 2 and b == y and plateau[x+1][y] == ' ' and x == 1:
                    return True
                else:
                    return False
            elif type_pion_arriver[0] == 'blanc':
                if a == x + 1 and b == y + 1 or a == x + 1 and b == y - 1:
                    return True
                else:
                    return False

        #Tout est nickel pour le pion
        elif type_pion_depart[0] == type_pion_arriver[0]:
            return False

        #Tout est nickel pour le pion
        elif type_pion_depart[0] != type_pion_arriver[0]:
            if a == x - 1 and b == y + 1 or a == x - 1 and b == y - 1:
                return True
            else:
                return False
        """
        Pour savoir quoi ce nom d'équipe c'est simple le leadeur s'appelle T'choupie et le guitariste s'appelle Peepoodoo e apres c'est des amis

        Porquoi T'choupi parce je lui resemble et Peepoodoo c'etait un malentendu qui est rester
        
        """
    #Tout est nickel pour le pion
    elif type_pion_depart[1] == 'tour':
        for interation_x in range (-1,2,2):
            test_x = x + interation_x
            while 0 <= test_x <= 7:
                test_piece = type_pion(test_x,y)
                if test_piece[0] == None:
                    jeu_possible.append([test_x,y])
                elif test_piece[0] != type_pion_depart[0]:
                    jeu_possible.append([test_x,y])
                    break
                elif test_piece[0] == type_pion_depart[0]:
                    break
                test_x += interation_x
        for interation_y in range (-1,2,2):
            test_y = y + interation_y
            while 0 <= test_y <= 7:
                test_piece = type_pion(x,test_y)
                if test_piece[0] == None:
                    jeu_possible.append([x,test_y])
                elif test_piece[0] != type_pion_depart[0]:
                    jeu_possible.append([x,test_y])
                    break
                elif test_piece[0] == type_pion_depart[0]:
                    break
                test_y += interation_y
        if [a,b] in jeu_possible:
            return True
        else:
            return False
    
    #Tout est nickel pour le pion
    elif type_pion_depart[1] == 'fou':
        for interation_x in range (-1,2,2):
            for interation_y in range (-1,2,2):
                test_x = x + interation_x
                test_y = y + interation_y
                while 0 <= test_x <= 7 and 0 <= test_y <= 7:
                    test_piece = type_pion(test_x,test_y)
                    if test_piece[0] == None:
                        jeu_possible.append([test_x,test_y])
                    elif test_piece[0] != type_pion_depart[0]:
                        jeu_possible.append([test_x,test_y])
                        break
                    elif test_piece[0] == type_pion_depart[0]:
                        break
                    test_x += interation_x
                    test_y += interation_y
        if [a,b] in jeu_possible:
            return True
        else:
            return False
    
    #Tout est nickel pour le pion
    elif type_pion_depart[1] == 'dame':
        for interation_x in range (-1,2,2):
            test_x = x + interation_x
            while 0 <= test_x <= 7:
                test_piece = type_pion(test_x,y)
                if test_piece[0] == None:
                    jeu_possible.append([test_x,y])
                elif test_piece[0] != type_pion_depart[0]:
                    jeu_possible.append([test_x,y])
                    break
                elif test_piece[0] == type_pion_depart[0]:
                    break
                test_x += interation_x
        for interation_y in range (-1,2,2):
            test_y = y + interation_y
            while 0 <= test_y <= 7:
                test_piece = type_pion(x,test_y)
                if test_piece[0] == None:
                    jeu_possible.append([x,test_y])
                elif test_piece[0] != type_pion_depart[0]:
                    jeu_possible.append([x,test_y])
                    break
                elif test_piece[0] == type_pion_depart[0]:
                    break
                test_y += interation_y
        
        '''

        Des boucle pourquoi faire ?

        '''
        interation_x = -1
        interation_y = -1
        test_x = x + interation_x
        test_y = y + interation_y
        while 0 <= test_x <= 7 and 0 <= test_y <= 7:
            test_piece = type_pion(test_x,test_y)
            if test_piece[0] == None:
                jeu_possible.append([test_x,test_y])
            elif test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([test_x,test_y])
                break
            elif test_piece[0] == type_pion_depart[0]:
                break
            test_x += interation_x
            test_y += interation_y


        interation_x = -1
        interation_y = 1
        test_x = x + interation_x
        test_y = y + interation_y
        while 0 <= test_x <= 7 and 0 <= test_y <= 7:
            test_piece = type_pion(test_x,test_y)
            if test_piece[0] == None:
                jeu_possible.append([test_x,test_y])
            elif test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([test_x,test_y])
                break
            elif test_piece[0] == type_pion_depart[0]:
                break
            test_x += interation_x
            test_y += interation_y


        interation_x = 1
        interation_y = -1
        test_x = x + interation_x
        test_y = y + interation_y
        while 0 <= test_x <= 7 and 0 <= test_y <= 7:
            test_piece = type_pion(test_x,test_y)
            if test_piece[0] == None:
                jeu_possible.append([test_x,test_y])
            elif test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([test_x,test_y])
                break
            elif test_piece[0] == type_pion_depart[0]:
                break
            test_x += interation_x
            test_y += interation_y



        interation_x = 1
        interation_y = 1
        test_x = x + interation_x
        test_y = y + interation_y
        while 0 <= test_x <= 7 and 0 <= test_y <= 7:
            test_piece = type_pion(test_x,test_y)
            if test_piece[0] == None:
                jeu_possible.append([test_x,test_y])
            elif test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([test_x,test_y])
                break
            elif test_piece[0] == type_pion_depart[0]:
                break
            test_x += interation_x
            test_y += interation_y





        if [a,b] in jeu_possible:
            return True
        else:
            return False
            """
            Ne pas oubliez d'aller cherche ma fille a l ecole de la rue des Potiers a boulogne Y aller a 13H96 et aller chercher un bouquet de fleur a mon ammande euh femme qui s'appelle karima
            
            Ne pas oublier la commande McDonad pour la nuit de l'informatice

            Yirmyahu \ DofSekai — Aujourd’hui à 18:59
            Maxi best of : 
            Tripple burger avec beacon 
            Grand frite
            Coca sans glaçon
            Avec les chaussettes noel 
            戦空 — Aujourd’hui à 19:00
            Menu maxi best of Mc chicken
            Ice tea 
            Grand frites. 
            +Chaussette
            Master_Zorigh — Aujourd’hui à 19:02
            Maxi best-of :
            Chicken Big Tasty
            Frites
            Ice Tea Green Tea SANS GLACONS 
            + Chaussettes ! 
            Yirmyahu \ DofSekai — Aujourd’hui à 19:04
            Pour Romain (je paye) :
            Maxi best of 
            Tripple cheese becon 
            Grand potatoes sauce creamy de luxe
            Ice tea
            Macfleury oreo beurre de cacahouète avec cacahouète
            + chausette !
            MissWeasley — Aujourd’hui à 19:05
            Maxi best-of : 9 nuggets (sauce creamy deluxe) ,
            frites (may), 
            Coca
            CalydwΣn — Aujourd’hui à 19:06
            Un petit ranch parce que je suis radin => 2€
            Eloïse — Aujourd’hui à 19:18
            Florence: Sundea Caramel Daim

            Question a pas oubliez 

            Première question :

            Supposons que vous connaissiez une femme qui est enceinte, mais qui a déjà huit enfants, dont trois sourds, deux aveugles et un mentalement attardé. De plus, cette femme a la syphilis. Lui recommanderiez-vous d’avorter ?

            Répondez mentalement, puis lisez la seconde question.

            Deuxième question :

            Il est temps d’élire le Président du Monde, et votre vote sera déterminant. Voici les données concernant les trois principaux candidats :

            – Le candidat A est associé à des politiciens véreux et consulte des astrologues. Il a eu deux maîtresses. Il fume comme une cheminée d’usine et boit huit à dix martinis par jour.

            – Le candidat B a déjà été viré deux fois, il dort jusqu’à midi, fumait de l’opium au collège et boit un quart de litre de whisky chaque soir.

            – Le candidat C est un héros de guerre médaillé. Il est végétarien, boit une bière occasionnellement et n’a jamais eu d’histoires extra-conjugales.

            Parmi ces trois candidats, lequel choisiriez-vous (honnêtement) ? Faites d’abord votre choix, ne trichez pas, puis lisez la réponse ci-dessous.

            Le candidat A est Franklin D. Roosevelt.
            Le candidat B est Winston Churchill.
            Le candidat C est Adolf Hitler.

            Comme quoi, il faut toujours se méfier des personnes qui ont une vie trop saine…

            Au fait, s’agissant de la question de l’avortement : si vous avez répondu « oui », vous venez de tuer Beethoven…


            """



    #Tout est nickel pour le pion
    elif type_pion_depart[1] == 'cavalier':
        if x+1 < 8 and y+2 < 8:
            test_piece = type_pion(x+1,y+2)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x+1,y+2])
        if x-1 >= 0 and y+2 < 8:
            test_piece = type_pion(x-1,y+2)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x-1,y+2])
        if x+1 < 8 and y-2 >= 0:
            test_piece = type_pion(x+1,y-2)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x+1,y-2])
        if x-1 >= 0 and y-2 >= 0:
            test_piece = type_pion(x-1,y-2)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x-1,y-2])
        if x+2 < 8 and y-1 >= 0:
            test_piece = type_pion(x+2,y-1)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x+2,y-1])
        if x+2 < 8 and y+1 < 8:
            test_piece = type_pion(x+2,y+1)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x+2,y+1])
        if x-2 >= 0 and y-1 >= 0:
            test_piece = type_pion(x-2,y-1)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x-2,y-1])
        if x-2 >= 0 and y+1 < 8:
            test_piece = type_pion(x-2,y+1)
            if test_piece[0] != type_pion_depart[0]:
                jeu_possible.append([x-2,y+1])

        if [a,b] in jeu_possible:
            return True
        else:
            return False

    #Tout est nickel pour le pion
    elif type_pion_depart[1] == 'roi':
        for interation_x in range (-1,2):
            for interation_y in range (-1,2):
                test_piece = type_pion(x+interation_x,y+interation_y)
                if interation_x == 0 and interation_y == 0:
                    continue
                if 0 <= x+interation_x <= 7 and 0 <= y+interation_y <= 7:
                    jeu_possible.append([x+interation_x,y+interation_y])
        if [a,b] in jeu_possible:
            return True
        else:
            return False

def deplacement():
    global plateau;joue_blanc = True;gagner = False
    while gagner == False:
        print("De :");print('Position en X :');X = abs(8-int(input()));print('Position en Y :');Y = str(input());print("\nA :");print('Position en X :');A = abs(8-int(input()));print('Position en Y :');B = str(input())
        Y = lettre_to_chiffre(Y);B = lettre_to_chiffre(B)
        if Y == -1 or 0 > X or 7 < X:
            print('\nLa case de départ n\'existe pas\n')
            time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)#J'aime la precison
        elif B == -1 or 0 > A or 7 < A:
            print('\nLa case d\'arriver n\'existe pas\n')
            time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)#J'aime la precison
        else:
            type_pion_depart = type_pion(X,Y)
            if joue_blanc == True and type_pion_depart[0] == 'blanc':
                print('Ca marche')
                coup = condition(X,Y,A,B)
                if coup == True:
                    pion = plateau[X][Y];plateau[X][Y] = ' ';plateau[A][B] = pion;afficher_plateau();joue_blanc = False
                else:
                    print('\nCoup impossible\n')
                    time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)#J'aime la precison
                    afficher_plateau()
            elif joue_blanc == False and type_pion_depart[0] == 'noir':
                coup = condition(X,Y,A,B)
                if coup == True:
                    pion = plateau[X][Y] ;plateau[X][Y] = ' ';plateau[A][B] = pion;afficher_plateau();joue_blanc = True
                else:
                    print('\nCoup impossible\n')
                    time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001);afficher_plateau()#J'aime la precison
            elif type_pion_depart[0] == None:
                print('\nCase sans pion\n')
                time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)#J'aime la precison
                afficher_plateau()
            else:
                print('\nCe n\'est pas a ce joueur de jouer\n')
                time.sleep(10.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)#J'aime la precison
                afficher_plateau()

if __name__ == "__main__":
    global plateau;plateau = creation_plateau();afficher_plateau();deplacement()