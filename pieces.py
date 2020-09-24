import numpy as np
from itertools import product

class Piece:
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        board = np.zeros(shape=(nRows, nCols))
        return np.flip(board, 0)

    @classmethod
    def self_discount(cls, board, startRow, startCol):
        board[startRow, startCol] = 0
        return board

class Knight(Piece):
    @classmethod
    def get_possible_moves(self, startRow, startCol, nRows, nCols):
        board = super().get_possible_moves(startRow, startCol, nRows, nCols)
        board = np.flip(board, 0)

        for minor, major in product((1,-1), (2,-2)):
            if startRow+minor in range(nRows) and startCol+major in range(nCols):
                board[startRow+minor, startCol+major] = 1
            if startRow+major in range(nRows) and startCol+minor in range(nCols):
                board[startRow+major, startCol+minor] = 1

        board = super().self_discount(board, startRow, startCol)
        
        return np.flip(board, 0)
        

class Rook(Piece):
    @classmethod
    def get_possible_moves(self, startRow, startCol, nRows, nCols):
        board = super().get_possible_moves(startRow, startCol, nRows, nCols)
        board = np.flip(board, 0)

        # Horizontal moves
        for j in range(nCols):
            board[startRow, j] = 1
        # Vertical moves
        for i in range(nRows):
            board[i, startCol] = 1

        board = super().self_discount(board, startRow, startCol)

        return np.flip(board, 0)

class Bishop(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        board = super().get_possible_moves(startRow, startCol, nRows, nCols)
        board = np.flip(board, 0)

        ## Right diagonal
        rs = max([startRow-startCol,0])
        cs = max([startCol-startRow,0])
        
        while rs < nRows and cs < nCols:
            board[rs,cs] = 1
            rs +=1
            cs +=1
        
        ## Left diagonal
        rs = max([(startRow+startCol) - nRows+1, 0])
        cs = min([startCol+startRow, nCols-1])
        
        while rs < nRows and cs >= 0:
            board[rs,cs] = 1
            rs +=1
            cs -=1

        board = super().self_discount(board, startRow, startCol)

        return np.flip(board, 0)

class Queen(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        rook_board = Rook.get_possible_moves(startRow, startCol, nRows, nCols)
        bishop_board = Bishop.get_possible_moves(startRow, startCol, nRows, nCols)
        
        board = np.logical_or(rook_board, bishop_board).astype(float)
        board = super().self_discount(np.flip(board, 0), startRow, startCol)

        return np.flip(board, 0)

class King(Piece):
    @classmethod
    def get_possible_moves(cls, startRow, startCol, nRows, nCols):
        board = super().get_possible_moves(startRow, startCol, nRows, nCols)
        board = np.flip(board, 0)
        
        for i, j in product((1,0), repeat=2):
            if startRow+i in range(nRows) and startCol+j in range(nCols):
                board[startRow+i, startCol+j] = 1
            if startRow-i in range(nRows) and startCol+j in range(nCols):
                board[startRow-i, startCol+j] = 1
            if startRow+i in range(nRows) and startCol-j in range(nCols):
                board[startRow+i, startCol-j] = 1
            if startRow-i in range(nRows) and startCol-j in range(nCols):
                board[startRow-i, startCol-j] = 1

        board = super().self_discount(board, startRow, startCol)

        return np.flip(board, 0)
