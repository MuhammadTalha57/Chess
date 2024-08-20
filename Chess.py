from configparser import ConfigParser
from Pieces import *
from Stopwatch import Stopwatch
import flet as ft
from math import dist, sqrt

config = ConfigParser()

class Chess:
    time_limit = 0
    timed = False
    @classmethod
    def readTime(cls):
        config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")
        cls.time_limit = int(config.get('SETTINGS', 'time limit'))
        cls.timed = str(config.get('SETTINGS', 'timed'))
        if(cls.timed == "True"):
            cls.timed = True
        else:
            cls.timed = False

    def initialize(self):
        self.wking = WhiteKing([7,4], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wking.png", "wk")
        self.wqueen = WhiteQueen([7,3], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wqueen.png","wq")
        self.wbishop2 = WhiteBishop([7,2], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wbishop.png", "wB")
        self.wbishop1 = WhiteBishop([7,5], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wbishop.png", "wb")
        self.wknight2 = WhiteKnight([7,1], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wknight.png", "wK")
        self.wknight1 = WhiteKnight([7,6], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wknight.png", "wK")
        self.wrook2 = WhiteRook([7,0], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wrook.png", "wr")
        self.wrook1 = WhiteRook([7,7], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wrook.png", "wr")

        self.wpawn1 = WhitePawn([6,0], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 1)
        self.wpawn2 = WhitePawn([6, 1], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 2)
        self.wpawn3 = WhitePawn([6, 2], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 3)
        self.wpawn4 = WhitePawn([6, 3], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 4)
        self.wpawn5 = WhitePawn([6, 4], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 5)
        self.wpawn6 = WhitePawn([6, 5], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 6)
        self.wpawn7 = WhitePawn([6, 6], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 7)
        self.wpawn8 = WhitePawn([6, 7], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png", "wp", 8)

        self.bking = BlackKing([0,4], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bking.png", "bk")
        self.bqueen = BlackQueen([0,3], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bqueen.png", "bq")
        self.bbishop2 = BlackBishop([0,2], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bbishop.png", "bb")
        self.bbishop1 = BlackBishop([0,5], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bbishop.png", "bB")
        self.bknight2 = BlackKnight([0,1], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bknight.png", "bK")
        self.bknight1 = BlackKnight([0,6], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bknight.png", "bK")
        self.brook2 = BlackRook([0,0], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\brook.png", "br")
        self.brook1 = BlackRook([0,7], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\brook.png", "br")

        self.bpawn1 = BlackPawn([1, 0], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 1)
        self.bpawn2 = BlackPawn([1, 1], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 2)
        self.bpawn3 = BlackPawn([1, 2], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 3)
        self.bpawn4 = BlackPawn([1, 3], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 4)
        self.bpawn5 = BlackPawn([1, 4], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 5)
        self.bpawn6 = BlackPawn([1, 5], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 6)
        self.bpawn7 = BlackPawn([1, 6], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 7)
        self.bpawn8 = BlackPawn([1, 7], "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png", "bp", 8)

        self.white_pieces = [self.wking, self.wqueen, self.wbishop2, self.wbishop1, self.wknight2, self.wknight1,
                           self.wrook2, self.wrook1, self.wpawn1, self.wpawn2, self.wpawn3, self.wpawn4, self.wpawn5,
                           self.wpawn6, self.wpawn7, self.wpawn8]

        self.white_pawns = [self.wpawn1, self.wpawn2, self.wpawn3, self.wpawn4, self.wpawn5, self.wpawn6, self.wpawn7, self.wpawn8]

        self.black_pieces = [self.bking, self.bqueen, self.bbishop2, self.bbishop1, self.bknight2, self.bknight1,
                                 self.brook2, self.brook1, self.bpawn1, self.bpawn2, self.bpawn3, self.bpawn4,
                                 self.bpawn5, self.bpawn6, self.bpawn7, self.bpawn8]

        self.black_pawns = [self.bpawn1, self.bpawn2, self.bpawn3, self.bpawn4, self.bpawn5, self.bpawn6, self.bpawn7, self.bpawn8]


        self.white_positions = [obj.pos for obj in self.white_pieces]
        self.black_positions = [obj.pos for obj in self.black_pieces]


        self.selected_piece = None
        self.white_turn = True
        self.gameEnd = False

        self.invalidBlackKingMoves = []
        self.invalidWhiteKingMoves = []
        self.blackRestrictedPieces = dict()
        self.whiteRestrictedPieces = dict()
        self.whiteMoves = []
        self.whiteBeatMoves = []
        self.blackMoves = []
        self.blackBeatMoves = []
        self.whiteTempMoves = []
        self.blackTempMoves = []

        self.wkingBeater = []
        self.bkingBeater = []
        self.wkingBeaterPath = []
        self.bkingBeaterPath = []

        # FOr 50-Move rule
        self.moves = 0

        # Threefold repetition
        self.threeFoldPawns = []
        r1 = ["br", "bK", "bb", "bq", "bk", "bB", "bK", "br"]
        r2 = ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"]
        r = ["_", "_", "_", "_", "_", "_", "_", "_"]
        r7 = ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]
        r8 = ["wr", "wK", "wB", "wq", "wk", "wb", "wK", "wr"]
        self.currentPosition = [r1.copy(), r2.copy(), r.copy(), r.copy(), r.copy(), r.copy(), r7.copy(), r8.copy()]
        temp = ""
        for i in self.currentPosition:
            temp += "".join(i)
        temp += "W"
        self.positions = {temp: 1}

        self.moveCalculator()

        self.readTime()
        if(self.timed):
            self.clock.setTime(self.time_limit*60)
            self.clock.start()
            self.board.w_clock_cont.content.opacity = 1
            self.board.b_clock_cont.content.opacity = 1
            self.board.w_clock_cont.content = ft.Text(
                value='{:02d}:{:02d}'.format(self.clock.wTime // 60, self.clock.wTime % 60),
                size=20,
                weight=ft.FontWeight.BOLD)
            self.board.b_clock_cont.content = ft.Text(
                value='{:02d}:{:02d}'.format(self.clock.bTime // 60, self.clock.bTime % 60), size=20,
                weight=ft.FontWeight.BOLD)
            self.board.page.update()
        else:
            self.board.w_clock_cont.content.opacity = 0
            self.board.b_clock_cont.content.opacity = 0
        self.board.page.update()

    def __init__(self, board):
        self.board = board
        self.clock = Stopwatch(self.time_limit*60, self)

    def whitePieceAtPos(self, pos:list):
        if(pos in self.white_positions):
            for p in self.white_pieces:
                if(pos == p.pos):
                    return p
        return None
    def blackPieceAtPos(self, pos:list):
        if(pos in self.black_positions):
            for p in self.black_pieces:
                if(pos == p.pos):
                    return p
        return None

    def isEmptyBlock(self, pos: list):
        return pos not in self.white_positions and pos not in self.black_positions

    def checkWhiteenPassant(self, piece, pos):
        if (isinstance(piece, WhitePawn) and pos[0] == 4):
            if (piece.firstMove):
                piece.en_passant = True
                piece.firstMove = False

    def checkBlackenPassant(self, piece, pos):
        if (isinstance(piece, BlackPawn) and pos[0] == 3):
            if (piece.firstMove):
                piece.en_passant = True
                piece.firstMove = False

    def updateWhiteenPassant(self):
        for p in self.white_pawns:
            if(p.en_passant):
                p.en_passant = False

    def updateBlackenPassant(self):
        for p in self.black_pawns:
            if(p.en_passant):
                p.en_passant = False

    def updateRookMoved(self, color: str):
        if(color == 'White'):
            if (isinstance(self.selected_piece, WhiteRook)):
                if (not self.selected_piece.moved):
                    self.selected_piece.moved = True
        else:
            if (isinstance(self.selected_piece, BlackRook)):
                if (not self.selected_piece.moved):
                    self.selected_piece.moved = True

    def updateKingMoved(self, color: str):
        if (color == 'White'):
            if (isinstance(self.selected_piece, WhiteKing)):
                if (not self.selected_piece.moved):
                    self.selected_piece.moved = True
        else:
            if (isinstance(self.selected_piece, BlackKing)):
                if (not self.selected_piece.moved):
                    self.selected_piece.moved = True

    def updateWhitePositions(self, old: list, new: list):
        self.white_positions[self.white_positions.index(old)] = new

    def updateBlackPositions(self, old: list, new: list):
        self.black_positions[self.black_positions.index(old)] = new

    def checkCheckmate(self):
        self.wking.check =  False
        self.bking.check = False
        for p in self.black_pieces:
            if(self.wking.pos in p.beat_moves):
                self.wking.check = True
                break

        for p in self.white_pieces:
            if(self.bking.pos in p.beat_moves):
                self.bking.check = True
                break

    def checkWhiteCastle(self):
        if(not self.wking.moved and not self.wking.check):
            if(self.wrook1 in self.white_pieces):
                if(not self.wrook1.moved):
                    if(self.isEmptyBlock([7,5]) and self.isEmptyBlock([7,6])):
                        if([7,5] not in self.blackMoves and [7,6] not in self.blackMoves):
                            self.wking.moves.append([7,6])

            if (self.wrook2 in self.white_pieces):
                if(not self.wrook2.moved):
                    if (self.isEmptyBlock([7, 1]) and self.isEmptyBlock([7, 2]) and self.isEmptyBlock([7, 3])):
                        if ([7, 1] not in self.blackMoves and [7, 2] not in self.blackMoves and [7, 3] not in self.blackMoves):
                            self.wking.moves.append([7, 2])

    def checkBlackCastle(self):
        if (not self.bking.moved and not self.bking.check):
            if(self.brook1 in self.black_pieces):
                if (not self.brook1.moved):
                    if (self.isEmptyBlock([0, 5]) and self.isEmptyBlock([0, 6])):
                        if ([0, 5] not in self.whiteMoves and [0, 6] not in self.whiteMoves):
                            self.bking.moves.append([0, 6])

            if(self.brook2 in self.black_pieces):
                if (not self.brook2.moved):
                    if (self.isEmptyBlock([0, 1]) and self.isEmptyBlock([0, 2]) and self.isEmptyBlock([0, 3])):
                        if ([0, 1] not in self.whiteMoves and [0, 2] not in self.whiteMoves and [0,3] not in self.whiteMoves):
                            self.bking.moves.append([0, 2])
    def blockClicked(self, pos: list, b):


        if(self.white_turn):

            if(self.selected_piece == None):
                p = self.whitePieceAtPos(pos)
                if(p == None):  # No piece selected
                    pass
                else:
                    self.selected_piece = p
                    temp = [p.pos] + p.moves + p.beat_moves
                    self.board.selectBlocks(temp)

            else:
                if (pos in self.selected_piece.moves):
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()

                    if (isinstance(self.selected_piece, WhitePawn)):
                        self.moves = 0
                    else:
                        self.moves += 1

                    # Pawn Promotion
                    if(isinstance(self.selected_piece, WhitePawn) and pos[0] == 0):
                        self.board.move(p, pos, m, b, False, True)
                        return

                    castling = False
                    if(isinstance(self.selected_piece, WhiteKing) and p == [7, 4] and (pos == [7,6] or pos == [7,2]) ):
                        castling = True
                        if(pos == [7, 6]):
                            self.wrook1.pos = [7,5]
                            self.updateWhitePositions([7,7], [7,5])
                        else:
                            self.wrook2.pos = [7,3]
                            self.updateWhitePositions([7, 0], [7, 3])

                    self.selected_piece.pos = pos

                    self.updateWhitePositions(p, pos)
                    self.checkWhiteenPassant(self.selected_piece, pos)

                    self.updateBlackenPassant()

                    # For Castling
                    self.updateRookMoved("White")
                    self.updateKingMoved("White")

                    self.moveCalculator()

                    if (castling):
                        self.updatePosition(old = p, new = pos, castling=True)
                    else:
                        self.updatePosition(old = p, new = pos)


                    self.white_turn = False
                    self.selected_piece = None

                    self.board.move(p, pos, m, b, castling, False)

                elif(pos in self.selected_piece.beat_moves):
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.moves = 0

                    if (isinstance(self.selected_piece, WhitePawn) and pos[0] == 0):
                        beatedPiece = self.blackPieceAtPos(pos)
                        self.black_pieces.remove(beatedPiece)
                        self.black_positions.remove(beatedPiece.pos)
                        try:
                            self.black_pawns.remove(beatedPiece)
                        except:
                            pass

                        self.board.beat(p, pos, m, b, False, True)
                        return

                    self.selected_piece.pos = pos

                    # Castling
                    self.updateRookMoved("White")
                    self.updateKingMoved("White")

                    beatedPiece = self.blackPieceAtPos(pos)
                    enPassant = False
                    if(beatedPiece == None):
                        enPassant = True
                        beatedPiece = self.blackPieceAtPos([pos[0] + 1, pos[1]])

                    self.black_pieces.remove(beatedPiece)
                    self.black_positions.remove(beatedPiece.pos)
                    try:
                        self.black_pawns.remove(beatedPiece)
                    except:
                        pass

                    self.updateBlackenPassant()

                    self.updateWhitePositions(p, pos)

                    self.moveCalculator()

                    if (enPassant):
                        self.updatePosition(old=p, new=pos, enPassant=True, ePos=[pos[0] + 1, pos[1]])
                    else:
                        self.updatePosition(old=p, new=pos, beat=True)

                    self.selected_piece = None

                    self.white_turn = False

                    self.board.beat(p, pos, m, b, enPassant, False)

                elif (pos == self.selected_piece.pos or self.whitePieceAtPos(pos) == None ):  # clicked on selected piece or non-white piece or
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.selected_piece = None
                    temp = [p] + m + b
                    self.board.deselectBlocks(temp)

                else:
                    p, m , b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.selected_piece = self.whitePieceAtPos(pos)
                    temp = [p] + m + b
                    self.board.deselectBlocks(temp)
                    temp = [pos] + self.selected_piece.moves + self.selected_piece.beat_moves
                    self.board.selectBlocks(temp)

        else:

            if (self.selected_piece == None):
                p = self.blackPieceAtPos(pos)
                if (p == None):  # No piece selected
                    pass
                else:
                    self.selected_piece = p
                    temp = [p.pos] + p.moves + p.beat_moves
                    self.board.selectBlocks(temp)
            else:
                if (pos in self.selected_piece.moves):
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    if (isinstance(self.selected_piece, BlackPawn)):
                        self.moves = 0
                    else:
                        self.moves += 1

                    if(isinstance(self.selected_piece, BlackPawn) and pos[0] == 7):
                        self.board.move(p, pos, m, b, False, True)
                        return

                    castling = False
                    if(isinstance(self.selected_piece, BlackKing) and p == [0, 4] and (pos == [0,6] or pos == [0, 2])):
                        castling = True
                        if (pos == [0, 6]):
                            self.brook1.pos = [0, 5]
                            self.updateBlackPositions([0, 7], [0, 5])
                        else:
                            self.brook2.pos = [0, 3]
                            self.updateBlackPositions([0, 0], [0, 3])

                    self.selected_piece.pos = pos

                    self.checkBlackenPassant(self.selected_piece, pos)

                    self.updateWhiteenPassant()

                    # Castling
                    self.updateRookMoved("Black")
                    self.updateKingMoved("Black")

                    self.updateBlackPositions(p, pos)

                    self.moveCalculator()

                    if (castling):
                        self.updatePosition(old = p, new = pos, castling = True)
                    else:
                        self.updatePosition(old = p, new = pos)

                    self.white_turn = True

                    self.selected_piece = None

                    self.board.move(p, pos, m, b, castling, False)

                elif (pos in self.selected_piece.beat_moves):
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.moves = 0

                    if (isinstance(self.selected_piece, BlackPawn) and pos[0] == 7):
                        beatedPiece = self.whitePieceAtPos(pos)
                        self.white_pieces.remove(beatedPiece)
                        self.white_positions.remove(beatedPiece.pos)
                        try:
                            self.white_pawns.remove(beatedPiece)
                        except:
                            pass

                        # self.updatePosition(old = p, new = pos, beat = True)

                        del beatedPiece
                        self.board.beat(p, pos, m , b, False, True)
                        return

                    self.selected_piece.pos = pos

                    # Castling
                    self.updateRookMoved("Black")
                    self.updateKingMoved("Black")

                    beatedPiece = self.whitePieceAtPos(pos)
                    enPassant = False
                    if (beatedPiece == None):
                        enPassant = True
                        beatedPiece = self.whitePieceAtPos([pos[0] - 1, pos[1]])


                    self.white_pieces.remove(beatedPiece)
                    self.white_positions.remove(beatedPiece.pos)
                    try:
                        self.white_pawns.remove(beatedPiece)
                    except:
                        pass

                    self.updateWhiteenPassant()

                    self.updateBlackPositions(p, pos)

                    self.moveCalculator()

                    if (enPassant):
                        self.updatePosition(old=p, new=pos, enPassant=True, ePos=[pos[0] - 1, pos[1]])
                    else:
                        self.updatePosition(old=p, new=pos, beat=True)

                    self.white_turn = True

                    self.selected_piece = None

                    self.board.beat(p, pos, m, b, enPassant, False)

                elif (pos == self.selected_piece.pos or self.blackPieceAtPos(pos) == None):  # clicked on selected piece or non-black piece
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.selected_piece = None
                    temp = [p] + m + b
                    self.board.deselectBlocks(temp)

                else:
                    p, m, b = self.selected_piece.pos.copy(), self.selected_piece.moves.copy(), self.selected_piece.beat_moves.copy()
                    self.selected_piece = self.blackPieceAtPos(pos)
                    temp = [p] + m + b
                    self.board.deselectBlocks(temp)
                    temp = [pos] + self.selected_piece.moves + self.selected_piece.beat_moves
                    self.board.selectBlocks(temp)

    def getPoints(self, p1: list, p2: list):
        x1, y1 = p1
        x2, y2 = p2
        if(x1 > x2):
            maxX = x1
            minX = x2
        else:
            maxX = x2
            minX = x1
        if (y1 > y2):
            maxY = y1
            minY = y2
        else:
            maxY = y2
            minY = y1
        points = []
        if(y1 - y2 == 0):   # Horizontal Line
            for x in range(minX+1, maxX):
                points.append([x, y1])
        elif(x1 - x2 == 0): # Vertical Line
            for y in range(minY+1, maxY):
                points.append([x1, y])
        else:   # Diagonal
            m = (y2-y1) // (x2 - x1)
            c = y1 - (m*x1)
            for x in range(minX+1, maxX):
                points.append([x, (m*x) + c])
        return points
    def WPmoveCalculate(self, piece: WhitePawn):
        i,j = piece.pos
        if(self.isEmptyBlock([i-1,j])):
            piece.moves.append([i-1,j])
            if(self.isEmptyBlock([i-2, j]) and i == 6):
                piece.moves.append([i-2, j])

        if(i-1 >= 0 and i-1 <= 7  and j-1 >= 0 and j-1 <= 7):
            if(self.blackPieceAtPos([i-1, j-1])):
                piece.beat_moves.append([i-1, j-1])
                if(isinstance(self.blackPieceAtPos([i - 1, j - 1]), BlackKing)):
                    self.bkingBeater.append(piece)
            elif(self.whitePieceAtPos([i-1, j-1])):
                self.whiteTempMoves.append([i-1, j-1])
            else:
                self.invalidBlackKingMoves.append([i-1, j-1])

        if (i - 1 >= 0 and i - 1 <= 7 and j + 1 >= 0 and j + 1 <= 7):
            if (self.blackPieceAtPos([i - 1, j + 1])):
                piece.beat_moves.append([i - 1, j + 1])
                if(isinstance(self.blackPieceAtPos([i - 1, j + 1]), BlackKing)):
                    self.bkingBeater.append(piece)
            elif(self.whitePieceAtPos([i-1, j+1])):
                self.whiteTempMoves.append([i-1, j+1])
            else:
                self.invalidBlackKingMoves.append([i - 1, j + 1])

        # En passant
        if(i == 3):
            if(isinstance(self.blackPieceAtPos([i, j-1]), BlackPawn)):
                if(self.blackPieceAtPos([i, j-1]).en_passant):
                    piece.beat_moves.append([i-1, j-1])
                    self.threeFoldPawns.append("wp"+str(piece.no)+"l")

            if (isinstance(self.blackPieceAtPos([i, j + 1]), BlackPawn)):
                if (self.blackPieceAtPos([i, j + 1]).en_passant):
                    piece.beat_moves.append([i - 1, j + 1])
                    self.threeFoldPawns.append("wp" + str(piece.no) + "r")

    def BPmoveCalculate(self, piece: BlackPawn):
        i, j = piece.pos
        if(self.isEmptyBlock([i+1, j])):
            piece.moves.append([i+1, j])
            if(self.isEmptyBlock([i+2, j]) and i == 1):
                piece.moves.append([i+2, j])

        if(i+1 >= 0 and i+1 <= 7 and j-1 >= 0 and j-1 <= 7):
            if(self.whitePieceAtPos([i+1, j-1])):
                piece.beat_moves.append([i+1, j-1])
                if(isinstance(self.whitePieceAtPos([i + 1, j - 1]), WhiteKing)):
                    self.wkingBeater.append(piece)
            elif(self.blackPieceAtPos([i+1, j-1])):
                self.blackTempMoves.append([i+1, j-1])
            else:
                self.invalidWhiteKingMoves.append([i+1, j-1])

        if(i+1 >= 0 and i+1 <= 7 and j+1 >= 0 and j + 1 <= 7):
            if (self.whitePieceAtPos([i + 1, j + 1])):
                piece.beat_moves.append([i + 1, j + 1])
                if (isinstance(self.whitePieceAtPos([i + 1, j + 1]), WhiteKing)):
                    self.wkingBeater.append(piece)
            elif(self.blackPieceAtPos([i+1, j+1])):
                self.blackTempMoves.append([i+1, j+1])
            else:
                self.invalidWhiteKingMoves.append([i + 1, j + 1])

        # En passant
        if (i == 4):
            if (isinstance(self.whitePieceAtPos([i, j - 1]), WhitePawn)):
                if (self.whitePieceAtPos([i, j - 1]).en_passant):
                    piece.beat_moves.append([i + 1, j - 1])
                    self.threeFoldPawns.append("bp" + str(piece.no) + "l")

            if (isinstance(self.whitePieceAtPos([i, j + 1]), WhitePawn)):
                if (self.whitePieceAtPos([i, j + 1]).en_passant):
                    piece.beat_moves.append([i + 1, j + 1])
                    self.threeFoldPawns.append("bp" + str(piece.no) + "r")

    def WRcheckBlackSelfCheck(self, piece: WhiteRook, pos: list, way: str):
        tempPiece = self.blackPieceAtPos(pos)

        if(way == "Up"):
            r, j = pos
            r -= 1
            while(r >= 0 and r <= 7):
                if( [r, j] in self.black_positions):
                    if([r,j] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif([r, j] in self.white_positions):
                    break
                elif(pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, j])
                r -= 1

        elif(way == "Down"):
            r, j = pos
            r += 1
            while(r <= 7):
                if([r, j] in self.black_positions):
                    if([r,j] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, j] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, j])
                r += 1

        elif(way == "Right"):
            i, c = pos
            c += 1
            while(c <= 7 and c >= 0):
                if([i,c] in self.black_positions):
                    if([i,c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):
                    self.invalidBlackKingMoves.append([i, c])

                c += 1

        elif(way == "Left"):
            i, c = pos
            c -= 1
            while(c >= 0 and c <= 7):
                if([i ,c] in self.black_positions):
                    if([i, c] ==self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([i, c])
                c -= 1

    def WRmoveCalculate(self, piece: WhiteRook):
        i, j = piece.pos
        # Up
        r = i-1
        while(r >= 0 and r <= 7):
            if(self.blackPieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.blackPieceAtPos([r, j]), BlackKing)):
                    self.bkingBeater.append(piece)
                # Logic for Black self check
                self.WRcheckBlackSelfCheck(piece, [r,j], "Up")
                break
            elif(self.whitePieceAtPos([r, j])):
                self.whiteTempMoves.append([r,j])
                break
            elif(self.isEmptyBlock([r,j])):
                piece.moves.append([r,j])
                self.invalidBlackKingMoves.append([r, j])

            r -= 1

        # Down
        r = i + 1
        while(r <= 7 and r >= 0):
            if (self.blackPieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.blackPieceAtPos([r, j]), BlackKing)):
                    self.bkingBeater.append(piece)
                # Logic for Black self check
                self.WRcheckBlackSelfCheck(piece, [r, j], "Down")
                break
            elif (self.whitePieceAtPos([r, j])):
                self.whiteTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])
                self.invalidBlackKingMoves.append([r , j])
            r += 1

        # Right
        c = j + 1
        while(c <= 7 and c >= 0):
            if(self.blackPieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.blackPieceAtPos([i, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WRcheckBlackSelfCheck(piece, [i, c], "Right")
                break
            elif(self.whitePieceAtPos([i, c])):
                self.whiteTempMoves.append([i, c])
                break
            elif(self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidBlackKingMoves.append([i,c])

            c += 1

        # Left
        c = j - 1
        while(c >= 0 and c <= 7):
            if(self.blackPieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.blackPieceAtPos([i, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WRcheckBlackSelfCheck(piece, [i,c], "Left")
                break
            elif(self.whitePieceAtPos([i, c])):
                self.whiteTempMoves.append([i, c])
                break
            elif(self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidBlackKingMoves.append([i, c])

            c -= 1

    def BRcheckWhiteSelfCheck(self, piece: BlackRook, pos: list, way: str):
        tempPiece = self.whitePieceAtPos(pos)

        if(way == "Up"):
            r, j = pos
            r -= 1
            while(r >= 0 and r <= 7):
                if( [r, j] in self.white_positions):
                    if([r,j] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, j] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, j])
                r -= 1

        elif(way == "Down"):
            r, j = pos
            r += 1
            while(r <= 7 and r >= 0):
                if([r, j] in self.white_positions):
                    if([r,j] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, j] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, j])
                r += 1

        elif(way == "Right"):
            i, c = pos
            c += 1
            while(c <= 7 and c >= 0):
                if([i,c] in self.white_positions):
                    if([i,c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([i, c])

                c += 1

        elif(way == "Left"):
            i, c = pos
            c -= 1
            while(c >= 0 and c <= 7):
                if([i ,c] in self.white_positions):
                    if([i, c] ==self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([i, c])

                c -= 1

    def BRmoveCalculate(self, piece: BlackRook):
        i, j = piece.pos
        # Up
        r = i - 1
        while (r >= 0 and r <= 7):
            if (self.whitePieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.whitePieceAtPos([r, j]), WhiteKing)):
                    self.wkingBeater.append(piece)
                # Logic for Black self check
                self.BRcheckWhiteSelfCheck(piece, [r, j], "Up")
                break
            elif (self.blackPieceAtPos([r, j])):
                self.blackTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])
                self.invalidWhiteKingMoves.append([r, j])

            r -= 1

        # Down
        r = i + 1
        while (r <= 7 and r >= 0):
            if (self.whitePieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.whitePieceAtPos([r, j]), WhiteKing)):
                    self.wkingBeater.append(piece)
                # Logic for Black self check
                self.BRcheckWhiteSelfCheck(piece, [r, j], "Down")
                break
            elif (self.blackPieceAtPos([r, j])):
                self.blackTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])
                self.invalidWhiteKingMoves.append([r, j])
            r += 1

        # Right
        c = j + 1
        while (c <= 7 and c >= 0):
            if (self.whitePieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.whitePieceAtPos([i, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BRcheckWhiteSelfCheck(piece, [i, c], "Right")
                break
            elif (self.blackPieceAtPos([i, c])):
                self.blackTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidWhiteKingMoves.append([i, c])

            c += 1

        # Left
        c = j - 1
        while (c >= 0 and c <= 7):
            if (self.whitePieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.whitePieceAtPos([i, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BRcheckWhiteSelfCheck(piece, [i, c], "Left")
                break
            elif (self.blackPieceAtPos([i, c])):
                self.blackTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidWhiteKingMoves.append([i, c])

            c -= 1

    def WhiteKnightMoves(self,piece: WhiteKnight, move: list):
        if(move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7):
            if(self.blackPieceAtPos(move)):
                piece.beat_moves.append(move)
                if (isinstance(self.blackPieceAtPos([move[0], move[1]]), BlackKing)):
                    self.bkingBeater.append(piece)
            elif(self.whitePieceAtPos(move)):
                self.whiteTempMoves.append(move)
            else:
                piece.moves.append(move)
                self.invalidBlackKingMoves.append(move)

    def WKnmoveCalculate(self, piece: WhiteKnight):
        i, j = piece.pos
        temp = [[i-1, j+2], [i-1, j-2], [i+1, j-2], [i+1, j+2], [i-2, j-1], [i-2, j+1], [i+2, j+1], [i+2, j-1]]
        for move in temp:
            self.WhiteKnightMoves(piece, move)

    def BlackKnightMoves(self, piece: BlackKnight, move: list):
        if (move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7):
            if (self.whitePieceAtPos(move)):
                piece.beat_moves.append(move)
                if (isinstance(self.whitePieceAtPos([move[0], move[1]]), WhiteKing)):
                    self.wkingBeater.append(piece)
            elif(self.blackPieceAtPos(move)):
                self.blackTempMoves.append(move)
            else:
                piece.moves.append(move)
                self.invalidWhiteKingMoves.append(move)

    def BKnmoveCalculate(self, piece: BlackKnight):
        i, j = piece.pos
        temp = [[i-1, j+2], [i-1, j-2], [i+1, j-2], [i+1, j+2], [i-2, j-1], [i-2, j+1], [i+2, j+1], [i+2, j-1]]
        for move in temp:
            self.BlackKnightMoves(piece, move)

    def WBcheckBlackSelfCheck(self, piece: WhiteBishop, pos: list, way: str):
        tempPiece = self.blackPieceAtPos(pos)
        r, c = pos
        if(way == 'tl'):
            r -= 1
            c -= 1
            while(r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if([r,c] in self.black_positions):
                    if([r,c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif([r,c] in self.white_positions):
                    break
                elif(pos == self.bking.pos):


                    self.invalidBlackKingMoves.append([r, c])
                r -= 1
                c -= 1
        elif(way == 'tr'):
            r -= 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r -= 1
                c += 1
        elif(way == 'bl'):
            r += 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r += 1
                c -= 1
        elif(way == 'br'):
            r += 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r += 1
                c += 1

    def WBmoveCalculate(self, piece: WhiteBishop):
        i, j = piece.pos

        #Top left
        r, c = i-1, j-1
        while(r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if(self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r,c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WBcheckBlackSelfCheck(piece, [r, c], 'tl')

                break
            elif(self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif(self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r -= 1
            c -= 1

        # Top right
        r, c = i - 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WBcheckBlackSelfCheck(piece, [r, c], 'tr')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r -= 1
            c += 1

        # Bottom left
        r, c = i + 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WBcheckBlackSelfCheck(piece, [r, c], 'bl')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r += 1
            c -= 1

        #Bottom Right
        r, c = i + 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WBcheckBlackSelfCheck(piece, [r, c], 'br')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r += 1
            c += 1

    def BBcheckWhiteSelfCheck(self, piece: BlackBishop, pos: list, way: str):
        tempPiece = self.whitePieceAtPos(pos)
        r, c = pos
        if (way == 'tl'):
            r -= 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r -= 1
                c -= 1
        elif (way == 'tr'):
            r -= 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r -= 1
                c += 1
        elif (way == 'bl'):
            r += 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r += 1
                c -= 1
        elif (way == 'br'):
            r += 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r += 1
                c += 1

    def BBmoveCalculate(self, piece: BlackBishop):
        i, j = piece.pos

        # Top left
        r, c = i - 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BBcheckWhiteSelfCheck(piece, [r, c], 'tl')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r -= 1
            c -= 1

        # Top right
        r, c = i - 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BBcheckWhiteSelfCheck(piece, [r, c], 'tr')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r -= 1
            c += 1

        # Bottom left
        r, c = i + 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BBcheckWhiteSelfCheck(piece, [r, c], 'bl')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r += 1
            c -= 1

        # Bottom Right
        r, c = i + 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BBcheckWhiteSelfCheck(piece, [r, c], 'br')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r += 1
            c += 1

    def WQcheckBlackSelfCheck(self, piece: WhiteQueen, pos: list, way: str):
        tempPiece = self.blackPieceAtPos(pos)

        if (way == "Up"):
            r, j = pos
            r -= 1
            while (r >= 0 and r <= 7):
                if ([r, j] in self.black_positions):
                    if ([r, j] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, j] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, j])
                r -= 1

        elif (way == "Down"):
            r, j = pos
            r += 1
            while (r <= 7 and r >= 0):
                if ([r, j] in self.black_positions):
                    if ([r, j] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, j] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, j])
                r += 1

        elif (way == "Right"):
            i, c = pos
            c += 1
            while (c <= 7 and c >= 0):
                if ([i, c] in self.black_positions):
                    if ([i, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([i, c])

                c += 1

        elif (way == "Left"):
            i, c = pos
            c -= 1
            while (c >= 0 and c <= 7):
                if ([i, c] in self.black_positions):
                    if ([i, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([i, c])

                c -= 1

        r, c = pos
        if (way == 'tl'):
            r -= 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])

                r -= 1
                c -= 1
        elif (way == 'tr'):
            r -= 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r -= 1
                c += 1
        elif (way == 'bl'):
            r += 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r += 1
                c -= 1
        elif (way == 'br'):
            r += 1
            c += 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.black_positions):
                    if ([r, c] == self.bking.pos):
                        self.blackRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,c] in self.white_positions):
                    break
                elif (pos == self.bking.pos):

                    self.invalidBlackKingMoves.append([r, c])
                r += 1
                c += 1

    def WQmoveCalculate(self, piece: WhiteQueen):
        i, j = piece.pos

        # Up
        r = i - 1
        while (r >= 0 and r <= 7):
            if (self.blackPieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.blackPieceAtPos([r, j]), BlackKing)):
                    self.bkingBeater.append(piece)
                # Logic for Black self check
                self.WQcheckBlackSelfCheck(piece, [r, j], "Up")
                break
            elif (self.whitePieceAtPos([r, j])):
                self.whiteTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])

                self.invalidBlackKingMoves.append([r, j])

            r -= 1

        # Down
        r = i + 1
        while (r <= 7 and r >= 0):
            if (self.blackPieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.blackPieceAtPos([r, j]), BlackKing)):
                    self.bkingBeater.append(piece)
                # Logic for Black self check
                self.WQcheckBlackSelfCheck(piece, [r, j], "Down")
                break
            elif (self.whitePieceAtPos([r, j])):
                self.whiteTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])

                self.invalidBlackKingMoves.append([r, j])
            r += 1

        # Right
        c = j + 1
        while (c <= 7 and c >= 0):
            if (self.blackPieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.blackPieceAtPos([i, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [i, c], "Right")
                break
            elif (self.whitePieceAtPos([i, c])):
                self.whiteTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])

                self.invalidBlackKingMoves.append([i, c])

            c += 1

        # Left
        c = j - 1
        while (c >= 0 and c <= 7):
            if (self.blackPieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.blackPieceAtPos([i, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [i, c], "Left")
                break
            elif (self.whitePieceAtPos([i, c])):
                self.whiteTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])

                self.invalidBlackKingMoves.append([i, c])

            c -= 1

        # Top left
        r, c = i - 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [r, c], 'tl')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r -= 1
            c -= 1

        # Top right
        r, c = i - 1, j + 1
        while (r >= 0 and c <= 7 and r <= 7 and c >= 0):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [r, c], 'tr')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r -= 1
            c += 1

        # Bottom left
        r, c = i + 1, j - 1
        while (r <= 7 and c >= 0 and r >= 0 and c <= 7):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [r, c], 'bl')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r += 1
            c -= 1

        # Bottom Right
        r, c = i + 1, j + 1
        while (r >= 0 and c <= 7 and r <= 7 and c >= 0):
            if (self.blackPieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.blackPieceAtPos([r, c]), BlackKing)):
                    self.bkingBeater.append(piece)

                self.WQcheckBlackSelfCheck(piece, [r, c], 'br')

                break
            elif (self.whitePieceAtPos([r, c])):
                self.whiteTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])

                self.invalidBlackKingMoves.append([r, c])

            r += 1
            c += 1

    def BQcheckWhiteSelfCheck(self, piece: BlackQueen, pos: list, way: str):
        tempPiece = self.whitePieceAtPos(pos)

        if (way == "Up"):
            r, j = pos
            r -= 1
            while (r >= 0 and r <= 7):
                if ([r, j] in self.white_positions):
                    if ([r, j] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,j] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, j])
                r -= 1

        elif (way == "Down"):
            r, j = pos
            r += 1
            while (r <= 7 and r >= 0):
                if ([r, j] in self.white_positions):
                    if ([r, j] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r,j] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, j])
                r += 1

        elif (way == "Right"):
            i, c = pos
            c += 1
            while (c <= 7 and c >= 0):
                if ([i, c] in self.white_positions):
                    if ([i, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([i, c])

                c += 1

        elif (way == "Left"):
            i, c = pos
            c -= 1
            while (c >= 0 and c <= 7):
                if ([i, c] in self.white_positions):
                    if ([i, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([i, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([i, c])

                c -= 1

        r, c = pos
        if (way == 'tl'):
            r -= 1
            c -= 1
            while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r -= 1
                c -= 1
        elif (way == 'tr'):
            r -= 1
            c += 1
            while (r >= 0 and c <= 7 and r <= 7 and c >= 0):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r -= 1
                c += 1
        elif (way == 'bl'):
            r += 1
            c -= 1
            while (r >= 0 and c <= 7 and r <= 7 and c >= 0):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r += 1
                c -= 1
        elif (way == 'br'):
            r += 1
            c += 1
            while (r >= 0 and c <= 7 and r <= 7 and c >= 0):
                if ([r, c] in self.white_positions):
                    if ([r, c] == self.wking.pos):
                        self.whiteRestrictedPieces.update({tempPiece: piece})
                    break
                elif ([r, c] in self.black_positions):
                    break
                elif (pos == self.wking.pos):
                    self.invalidWhiteKingMoves.append([r, c])
                r += 1
                c += 1

    def BQmoveCalculate(self, piece: BlackQueen):
        i, j = piece.pos
        # Up
        r = i - 1
        while (r >= 0 and r <= 7):
            if (self.whitePieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.whitePieceAtPos([r, j]), WhiteKing)):
                    self.wkingBeater.append(piece)
                # Logic for Black self check
                self.BQcheckWhiteSelfCheck(piece, [r, j], "Up")
                break
            elif (self.blackPieceAtPos([r, j])):
                self.blackTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])
                self.invalidWhiteKingMoves.append([r, j])

            r -= 1

        # Down
        r = i + 1
        while (r <= 7 and r >= 0):
            if (self.whitePieceAtPos([r, j])):
                piece.beat_moves.append([r, j])
                if (isinstance(self.whitePieceAtPos([r, j]), WhiteKing)):
                    self.wkingBeater.append(piece)
                # Logic for Black self check
                self.BQcheckWhiteSelfCheck(piece, [r, j], "Down")
                break
            elif (self.blackPieceAtPos([r, j])):
                self.blackTempMoves.append([r, j])
                break
            elif (self.isEmptyBlock([r, j])):
                piece.moves.append([r, j])
                self.invalidWhiteKingMoves.append([r, j])
            r += 1

        # Right
        c = j + 1
        while (c <= 7 and c >= 0):
            if (self.whitePieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.whitePieceAtPos([i, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [i, c], "Right")
                break
            elif (self.blackPieceAtPos([i, c])):
                self.blackTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidWhiteKingMoves.append([i, c])

            c += 1

        # Left
        c = j - 1
        while (c >= 0 and c <= 7):
            if (self.whitePieceAtPos([i, c])):
                piece.beat_moves.append([i, c])
                if (isinstance(self.whitePieceAtPos([i, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [i, c], "Left")
                break
            elif (self.blackPieceAtPos([i, c])):
                self.blackTempMoves.append([i, c])
                break
            elif (self.isEmptyBlock([i, c])):
                piece.moves.append([i, c])
                self.invalidWhiteKingMoves.append([i, c])

            c -= 1

        # Top left
        r, c = i - 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [r, c], 'tl')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r -= 1
            c -= 1

        # Top right
        r, c = i - 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [r, c], 'tr')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r -= 1
            c += 1

        # Bottom left
        r, c = i + 1, j - 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [r, c], 'bl')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r += 1
            c -= 1

        # Bottom Right
        r, c = i + 1, j + 1
        while (r >= 0 and c >= 0 and r <= 7 and c <= 7):
            if (self.whitePieceAtPos([r, c])):
                piece.beat_moves.append([r, c])
                if (isinstance(self.whitePieceAtPos([r, c]), WhiteKing)):
                    self.wkingBeater.append(piece)

                self.BQcheckWhiteSelfCheck(piece, [r, c], 'br')

                break
            elif (self.blackPieceAtPos([r, c])):
                self.blackTempMoves.append([r, c])
                break

            elif (self.isEmptyBlock([r, c])):
                piece.moves.append([r, c])
                self.invalidWhiteKingMoves.append([r, c])

            r += 1
            c += 1

    def WKmoveCalculate(self, piece: WhiteKing):
        i, j = piece.pos
        temp = [ [i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1] ]

        for move in temp:
            r, c = move
            if(dist(self.bking.pos, move) == 1 or dist(self.bking.pos, move) == sqrt(2)):
                continue

            if(r >= 0 and r <= 7 and c >= 0 and c <= 7):
                if(self.blackPieceAtPos(move) and move not in self.blackTempMoves):
                    self.wking.beat_moves.append(move)
                elif(self.isEmptyBlock(move) and move not in self.invalidWhiteKingMoves):
                    self.wking.moves.append(move)
                elif(self.whitePieceAtPos(move)):
                    self.whiteTempMoves.append(move)

    def BKmoveCalculate(self, piece: BlackKing):
        i, j = piece.pos
        temp = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j],
                [i + 1, j + 1]]

        for move in temp:
            r, c = move
            if (dist(self.wking.pos, move) == 1 or dist(self.wking.pos, move) == sqrt(2)):
                continue
            if (r >= 0 and r <= 7 and c >= 0 and c <= 7):
                if (self.whitePieceAtPos(move) and move not in self.whiteTempMoves):
                    self.bking.beat_moves.append(move)
                elif (self.isEmptyBlock(move) and move not in self.invalidBlackKingMoves):
                        self.bking.moves.append(move)
                elif(self.blackPieceAtPos(move)):
                    self.blackTempMoves.append(move)


    def restrictBlackMoves(self):
        for bPiece, wPiece in self.blackRestrictedPieces.items():
            i, j = self.bking.pos
            x, y = bPiece.pos
            m, n = wPiece.pos
            tempMoves = bPiece.moves.copy()
            tempBeatMoves = bPiece.beat_moves.copy()
            bPiece.moves.clear()
            bPiece.beat_moves.clear()

            if ([m, n] in tempBeatMoves):
                bPiece.beat_moves.append([m, n])
            if(self.wking.pos in tempBeatMoves):
                bPiece.beat_moves.append(self.wking.pos)
            for move in self.getPoints([i,j], [m, n]):
                if(move in tempMoves):
                    bPiece.moves.append(move)

    def restrictWhiteMoves(self):
        for wPiece, bPiece in self.whiteRestrictedPieces.items():
            i, j = self.wking.pos
            x, y = wPiece.pos
            m, n = bPiece.pos
            tempMoves = wPiece.moves.copy()
            tempBeatMoves = wPiece.beat_moves.copy()
            wPiece.moves.clear()
            wPiece.beat_moves.clear()

            if([m , n] in tempBeatMoves):
                wPiece.beat_moves.append([m, n])
            if(self.bking.pos in tempBeatMoves):
                wPiece.beat_moves.append(self.bking.pos)
            for move in self.getPoints([i, j], [m, n]):
                if(move in tempMoves):
                    wPiece.moves.append(move)

    def restrictMovesIfChecked(self):
        path = []
        if(self.wking.check):
            path = self.getPoints(self.wking.pos, self.wkingBeater[0].pos)
            doubleCheck = len(self.wkingBeater) == 2
            for piece in self.white_pieces:
                if(isinstance(piece, WhiteKing)):
                    continue
                elif(doubleCheck):   # Double Check
                    piece.moves.clear()
                    piece.beat_moves.clear()
                else:
                    if(self.wkingBeater[0].pos in piece.beat_moves):
                        piece.beat_moves = [self.wkingBeater[0].pos]
                    else:
                        piece.beat_moves.clear()
                    temp = []
                    for move in piece.moves:
                        if(move in path):
                            temp.append(move)
                    piece.moves = temp

            if(doubleCheck):
                self.whiteMoves = [m for m in self.wking.moves]
                self.whiteBeatMoves = [bm for bm in self.wking.beat_moves]

        elif(self.bking.check):
            path = self.getPoints(self.bking.pos, self.bkingBeater[0].pos)
            doubleCheck = len(self.bkingBeater) == 2
            for piece in self.black_pieces:
                if (isinstance(piece, BlackKing)):
                    continue
                elif (doubleCheck):  # Double Check
                    piece.moves.clear()
                    piece.beat_moves.clear()
                else:
                    if (self.bkingBeater[0].pos in piece.beat_moves):
                        piece.beat_moves = [self.bkingBeater[0].pos]
                    else:
                        piece.beat_moves.clear()
                    temp = []
                    for move in piece.moves:
                        if (move in path):
                            temp.append(move)
                    piece.moves = temp

            if (doubleCheck):
                self.blackMoves = [m for m in self.bking.moves]
                self.blackBeatMoves = [bm for bm in self.bking.beat_moves]

    def moveCalculator(self):
        self.whiteTempMoves.clear()
        self.blackTempMoves.clear()
        self.whiteRestrictedPieces.clear()
        self.blackRestrictedPieces.clear()
        self.whiteMoves.clear()
        self.whiteBeatMoves.clear()
        self.blackMoves.clear()
        self.blackBeatMoves.clear()
        self.invalidWhiteKingMoves.clear()
        self.invalidBlackKingMoves.clear()
        self.wkingBeater.clear()
        self.bkingBeater.clear()
        self.threeFoldPawns.clear()

        for piece in self.white_pieces:
            piece.moves.clear()
            piece.beat_moves.clear()
            if(isinstance(piece, WhiteKing)):
                continue
            elif(isinstance(piece, WhitePawn)):
                self.WPmoveCalculate(piece)
            elif (isinstance(piece, WhiteRook)):
                self.WRmoveCalculate(piece)
            elif (isinstance(piece, WhiteKnight)):
                self.WKnmoveCalculate(piece)
                tempPiece = piece
            elif (isinstance(piece, WhiteBishop)):
                self.WBmoveCalculate(piece)
            elif (isinstance(piece, WhiteQueen)):
                self.WQmoveCalculate(piece)

        for piece in self.black_pieces:
            piece.moves.clear()
            piece.beat_moves.clear()
            if (isinstance(piece, BlackKing)):
                continue
            elif (isinstance(piece, BlackPawn)):
                self.BPmoveCalculate(piece)
            elif (isinstance(piece, BlackRook)):
                self.BRmoveCalculate(piece)
            elif (isinstance(piece, BlackKnight)):
                self.BKnmoveCalculate(piece)
            elif (isinstance(piece, BlackBishop)):
                self.BBmoveCalculate(piece)
            elif (isinstance(piece, BlackQueen)):
                self.BQmoveCalculate(piece)

        self.restrictWhiteMoves()
        self.restrictBlackMoves()

        self.WKmoveCalculate(self.wking)
        self.BKmoveCalculate(self.bking)

        self.checkCheckmate()

        self.restrictMovesIfChecked()

        for p in self.white_pieces:
            self.whiteMoves.extend(p.moves)
            self.whiteBeatMoves.extend(p.beat_moves)

        for p in self.black_pieces:
            self.blackMoves.extend(p.moves)
            self.blackBeatMoves.extend(p.beat_moves)

        self.checkWhiteCastle()
        self.checkBlackCastle()

        self.gameEnd = self.checkGameEnd()
        if(self.gameEnd):
            self.board.gameEnd = True
            self.board.resultContainer.visible = True
            self.board.resignBtn.disabled = True

    def checkGameEnd(self):
        if(not self.white_turn):
            if(self.whiteMoves == [] and self.whiteBeatMoves == []):
                if(self.wking.check):
                    self.board.result.value = "Black Won"
                    self.board.reason.value = "through Checkmate"
                else:
                    self.board.result.value = "Game Drawn"
                    self.board.reason.value = "through Stalemate"
                return True

        else:
            if(self.blackMoves == [] and self.blackBeatMoves == []):
                if(self.bking.check):
                    self.board.result.value = "White Won"
                    self.board.reason.value = "through Checkmate"
                else:
                    self.board.result.value = "Game Drawn"
                    self.board.reason.value = "through Stalemate"
                return  True


        # Insuficient Material
        if(len(self.white_pieces) == 1 and len(self.black_pieces) == 1):
            print("Game drawn through Insufficient material (K vs K)")
            self.board.result.value = "Game Drawn"
            self.board.reason.value = "through Insufficient material"
            return True

        if(len(self.white_pieces) == 1 and len(self.black_pieces) == 2):
            flag = any(isinstance(piece, BlackKnight) for piece in self.black_pieces) or any(isinstance(piece, BlackBishop) for piece in self.black_pieces)
            if(flag):
                print("Game drawn through Insufficient material (K vs K + M.P)")
                self.board.result.value = "Game Drawn"
                self.board.reason.value = "through Insufficient material"
                return True

        if (len(self.black_pieces) == 1 and len(self.white_pieces) == 2):
            flag = any(isinstance(piece, WhiteKnight) for piece in self.white_pieces) or any(isinstance(piece, WhiteBishop) for piece in self.white_pieces)
            if (flag):
                print("Game drawn through Insufficient material (K + M.P vs K)")
                self.board.result.value = "Game Drawn"
                self.board.reason.value = "through Insufficient material"
                return

        if(len(self.white_pieces) == 1 and len(self.black_pieces) == 3):
            if(all(isinstance(piece, BlackKnight) for piece in self.black_pieces[1:])):
                print("Game drawn through Insufficient material (K vs K + 2Kn)")
                self.board.result.value = "Game Drawn"
                self.board.reason.value = "through Insufficient material"
                return True

        if(len(self.black_pieces) == 1 and len(self.white_pieces) == 3):
            if(all(isinstance(piece, WhiteKnight) for piece in self.white_pieces[1:])):
                print("Game drawn through Insufficient material (K + 2Kn vs K)")
                self.board.result.value = "Game Drawn"
                self.board.reason.value = "through Insufficient material"
                return True

        if(len(self.white_pieces) == 2 and len(self.black_pieces) == 2):
            flag1 = isinstance(self.white_pieces[1], WhiteKnight) or isinstance(self.white_pieces[1], WhiteBishop)
            flag2 = isinstance(self.black_pieces[1], BlackKnight) or isinstance(self.black_pieces[1], BlackBishop)
            if(flag1 or flag2):
                print("Game drawn through Insufficient material (K + M.P vs K + M.P)")
                self.board.result.value = "Game Drawn"
                self.board.reason.value = "through Insufficient material"
                return True


        if(self.moves == 100):
            self.board.result.value = "Game Drawn"
            self.board.reason.value = "through 50-Move rule"
            return True

        return False

    def updatePosition(self, old: list, new: list, enPassant = False, ePos = [], castling = False, beat = False):
        temp = str()
        if(beat):
            self.positions.clear()
            self.currentPosition[old[0]][old[1]] = "_"
            self.currentPosition[new[0]][new[1]] = self.selected_piece.id

        elif(castling):
            if(new == [7, 6]):
                self.currentPosition[old[0]][old[1]] = "_"
                self.currentPosition[new[0]][new[1]] = self.selected_piece.id
                self.currentPosition[7][7] = "_"
                self.currentPosition[7][5] = "wr"
            elif(new == [7, 2]):
                self.currentPosition[old[0]][old[1]] = "_"
                self.currentPosition[new[0]][new[1]] = self.selected_piece.id
                self.currentPosition[7][0] = "_"
                self.currentPosition[7][3] = "wr"
            elif(new == [0, 6]):
                self.currentPosition[old[0]][old[1]] = "_"
                self.currentPosition[new[0]][new[1]] = self.selected_piece.id
                self.currentPosition[0][7] = "_"
                self.currentPosition[0][5] = "br"
            elif (new == [0, 2]):
                self.currentPosition[old[0]][old[1]] = "_"
                self.currentPosition[new[0]][new[1]] = self.selected_piece.id
                self.currentPosition[0][0] = "_"
                self.currentPosition[0][3] = "br"

        elif(enPassant):
            self.positions.clear()
            self.currentPosition[old[0]][old[1]] = "_"
            self.currentPosition[new[0]][new[1]] = self.selected_piece.id
            self.currentPosition[ePos[0]][ePos[1]] = "_"
        else:
            self.currentPosition[old[0]][old[1]] = "_"
            self.currentPosition[new[0]][new[1]] = self.selected_piece.id


        for i in self.currentPosition:
            temp += "".join(i)

        if(self.white_turn):
            temp += "B"
        else:
            temp += "W"
        temp += "".join(self.threeFoldPawns)

        if(self.wking.pos == [7,4] and [7, 6] in self.wking.moves):
            temp += "wr1"

        if(self.wking.pos == [7,4] and [7, 2] in self.wking.moves):
            temp += "wr2"

        if (self.bking.pos == [0, 4] and [0, 6] in self.bking.moves):
            temp += "br1"

        if (self.bking.pos == [0, 4] and [0, 2] in self.bking.moves):
            temp += "br2"

        if(temp in self.positions):
            self.positions[temp] += 1
        else:
            self.positions.update({temp: 1})

        # Three fold repetition
        if (3 in self.positions.values()):
            self.board.result.value = "Game Drawn"
            self.board.reason.value = "through Threefold Repetition Rule"
            self.gameEnd = True
            self.board.gameEnd = True
            self.board.resultContainer.visible = True
            self.board.resignBtn.disabled = True

    def resigned(self):
        self.gameEnd = True
        self.board.gameEnd = True
        self.board.resultContainer.visible = True
        self.board.reason.value = "through Resignation"
        self.board.resignBtn.disabled = True
        if(self.white_turn):
            self.board.result.value = "Black Won"
        else:
            self.board.result.value = "White Won"
        self.board.page.update()