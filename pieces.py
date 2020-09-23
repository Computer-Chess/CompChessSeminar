import numpy as np
from itertools import product

class Piece:
    @classmethod
    def get_possible_moves(self, startRow, startCol, nRows, nCols):
        table = np.zeros(shape=(nRows, nCols))
        table[startRow, startCol] = 1
        return np.flip(table, 0)

class Knight(Piece):
    @classmethod
    def get_possible_moves(self, startRow, startCol, nRows, nCols):
        table = super().get_possible_moves(startRow, startCol, nRows, nCols)
        table = np.flip(table, 0)

        for minor, major in product((1,-1), (2,-2)):
            if startRow+minor in range(nRows) and startCol+major in range(nCols):
                table[startRow+minor, startCol+major] = 1
            if startRow+major in range(nRows) and startCol+minor in range(nCols):
                table[startRow+major, startCol+minor] = 1
        
        return np.flip(table, 0)
        

class Rook(Piece):
    @classmethod
    def get_possible_moves(self, startRow, startCol, nRows, nCols):
        table = super().get_possible_moves(startRow, startCol, nRows, nCols)
        table = np.flip(table, 0)

        # Horizontal moves
        for j in range(nCols):
            table[startRow, j] = 1
        # Vertical moves
        for i in range(nRows):
            table[i, startCol] = 1
        
        return np.flip(table, 0)

class Bishop(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        table = super().get_possible_moves(startRow, startCol, nRows, nCols)
        table = np.flip(table, 0)

        ## Right diagonal
        rs = max([startRow-startCol,0])
        cs = max([startCol-startRow,0])
        
        while rs < nRows and cs < nCols:
            table[rs,cs] = 1
            rs +=1
            cs +=1
        
        ## Left diagonal
        rs = max([(startRow+startCol) - nRows+1, 0])
        cs = min([startCol+startRow, nCols-1])
        
        while rs < nRows and cs >= 0:
            table[rs,cs] = 1
            rs +=1
            cs -=1
        
        return np.flip(table, 0)

class Queen(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        rook_table = Rook.get_possible_moves(startRow, startCol, nRows, nCols)
        bishop_table = Bishop.get_possible_moves(startRow, startCol, nRows, nCols)

        return np.logical_or(rook_table, bishop_table).astype(float)

class King(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        table = super().get_possible_moves(startRow, startCol, nRows, nCols)
        table = np.flip(table, 0)
        
        for i, j in product((1,0), repeat=2):
            table[startRow+i, startCol+j] = int(startRow+i in range(nRows) and startCol+j in range(nCols))
            table[startRow-i, startCol+j] = int(startRow-i in range(nRows) and startCol+j in range(nCols))
            table[startRow+i, startCol-j] = int(startRow+i in range(nRows) and startCol-j in range(nCols))
            table[startRow-i, startCol-j] = int(startRow-i in range(nRows) and startCol-j in range(nCols))
        
        return np.flip(table, 0)
