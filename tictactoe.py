import numpy as np

def valide_move(grille=None, move=None):
    ''' Renvoie True si le mouvement est valide et False sinon
    '''
    if move is not None and grille is not None:
        if len(move) != 3 or move[0] not in [0, 1] or move[1] not in [0, 1, 2] or move[2] not in [0, 1, 2]:
            return False
        else:
            return grille[move[1], move[2]] == ' '
    
def end_game(grille):
    ''' Calcule si le jeu est fini ou non
    '''
    if len(grille[grille != ' ']) == 9:
        return True
    else:
        # on test les lignes et les colonnes
        for i in range(3):
            symbol_ligne = grille[i, 0] * (grille[i, 0] != ' ') + '#' * (grille[i, 0] == ' ')
            symbol_colonne = grille[0, i] * (grille[0, i] != ' ') + '#' * (grille[0, i] == ' ')
            ligne_complete = sum(grille[i, :] == symbol_ligne) == 3
            colonne_complete = sum(grille[:, i] == symbol_colonne) == 3 
            if ligne_complete or colonne_complete:
                return True
        # on test les 2 diagonales
        diag1 = sum(np.diag(grille) == grille[0, 0] * (grille[0, 0] != ' ') + '#' * (grille[0, 0] == ' ')) == 3
        diag2 = sum(np.fliplr(grille).diagonal() == grille[2, 0] * (grille[2, 0] != ' ') + '#' * (grille[2, 0] == ' ')) == 3
        if diag1 or diag2:      
            return True


def prettify_grille(grille):
    res = "  _   _   _ \n"
    for line in grille:
        res += f"| {line[0]} | {line[1]} | {line[2]} |\n"
    
    return res+"  ‾   ‾   ‾ "
  

def update_grille(grille=None, move=None):
    '''Update la grille en fonction du move
    args:
        move : liste (int) de taille 3, move[0] = id joueur, move[1] = coordonnée x, move[2] = coordonnée y. 
    '''
    if grille is None:
        grille = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    else:
        if move is None:
            return grille
        else:
            symbol = 'X' * (move[0] == 1) + 'O' * (move[0] == 0)
            if valide_move(grille, move):
                grille[move[1], move[2]] = symbol
            else:
                raise ValueError("La case est déjà prise")
    return grille


def tictactoe():
    ''' Fonction implémentant le jeu tictactoe à 2 joueurs
    '''
    grille = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    game_ended = False
    joueur = 0
    while not game_ended:
        print(prettify_grille(grille))
        print("Choisir la ligne")
        coord_x = int(input())
        print("Choisir la colonne")
        coord_y = int(input())
        move = [joueur, coord_x, coord_y]
        try:
            update_grille(grille, move)
        except ValueError as error:
            while not valide_move(grille, move):
                print(error)
                print("Choisir la ligne")
                coord_x = int(input())
                print("Choisir la colonne")
                coord_y = int(input())
                move = [joueur, coord_x, coord_y]
            update_grille(grille, move)
        game_ended = end_game(grille)
        joueur = 1 - joueur
    print(prettify_grille(grille))
    print(f"Le joueur {1 - joueur} a gagné !!!")
