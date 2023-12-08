import numpy as np

def valide_move(grille=None, move=None):
    ''' Renvoie True si le mouvement est valide et False sinon
    '''
    if move is not None and grille is not None:
        return grille[move[1], move[2]] == ' '
    
def end_game(grille):
    ''' Calcule si le jeu est fini ou non
    '''
    if len(grille[grille != ' ']) == 9:
        return True
    else:
        # on test les lignes et les colonnes
        for i in range(3):
            symbol_ligne = grille[i, 0]
            symbol_colonne = grille[0, i]
            ligne_complete = sum(grille[i, :] == symbol_ligne) == 3
            colonne_complete = sum(grille[:, i] == symbol_colonne) == 3 
            if ligne_complete or colonne_complete:
                return True
        # on test les 2 diagonales
        diag1 = sum(np.diag(grille) == grille[0, 0]) == 3
        diag2 = sum(np.fliplr(grille).diagonal() == grille[2, 0]) == 3
        if diag1 or diag2:      
            return True
            

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
    return grille


Grille = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
Move = [0, 1, 1]
print(update_grille(Grille, Move))