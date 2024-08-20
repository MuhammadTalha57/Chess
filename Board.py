import flet as ft
from configparser import ConfigParser

from Block import Block
from Chess import Chess
from Pieces import WhiteQueen, BlackQueen, WhiteBishop, BlackBishop, WhiteKnight, BlackKnight, WhiteRook, BlackRook

config = ConfigParser()

block_colors = (('white','#769656'),('#85501c','#301800'),('white','black'))
border_colors = ('#18240b','#211305','white')

config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")
board = int(config.get('SETTINGS', 'board'))

selectionColor = "#545351"
moveColor = "#73726f"
checkColor = "#750707"

# Images
wking = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wking.png"
wqueen = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wqueen.png"
wbishop = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wbishop.png"
wknight = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wknight.png"
wrook = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wrook.png"
wpawn = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\wpawn.png"

bking = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bking.png"
bqueen = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bqueen.png"
bbishop = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bbishop.png"
bknight = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bknight.png"
brook = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\brook.png"
bpawn = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\bpawn.png"

transparent_img = "C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\Transparent.png"


class Board(ft.UserControl):
    def initialize(self):
        self.wBeatenPieces = 0
        self.bBeatenPieces = 0
        self.pawnPromotion = False
        self.tempImages = []
        self.j = 0  # Used for giving ID to promoted Bishop
        self.gameEnd = False
        self.updateBoard()

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.c = Chess(self)
        # Clocks
        self.w_clock_cont, self.b_clock_cont = ft.Container(width=100, content=ft.Text(value='{:02d}:{:02d}'.format(self.c.clock.wTime // 60, self.c.clock.wTime % 60), size=20,
                                             weight=ft.FontWeight.BOLD), alignment=ft.alignment.center), ft.Container(width=100,content=ft.Text(
            value='{:02d}:{:02d}'.format(self.c.clock.bTime // 60, self.c.clock.bTime % 60), size=20, weight=ft.FontWeight.BOLD),alignment=ft.alignment.center)

    def updateClocks(self):
        if(self.c.white_turn):
            self.w_clock_cont.content = ft.Text(value='{:02d}:{:02d}'.format(self.c.clock.wTime // 60, self.c.clock.wTime % 60),
                                                size=20,
                                                weight=ft.FontWeight.BOLD)
        else:
            self.b_clock_cont.content = ft.Text(
                value='{:02d}:{:02d}'.format(self.c.clock.bTime // 60, self.c.clock.bTime % 60), size=20, weight=ft.FontWeight.BOLD)

        if(self.c.clock.wTime == 0):
            self.c.gameEnd = True
            self.gameEnd = True
            self.resultContainer.visible = True
            self.resignBtn.disabled = True
            if(len(self.c.black_pieces) == 1):
                self.result.value = "Game Drawn"
                self.reason.value = "through timeout vs insufficient material"
            else:
                self.result.value = "Black Won"
                self.reason.value = "through timeout"
        elif(self.c.clock.bTime == 0):
            self.c.gameEnd = True
            self.gameEnd = True
            self.resultContainer.visible = True
            self.resignBtn.disabled = True
            if (len(self.c.white_pieces) == 1):
                self.result.value = "Game Drawn"
                self.reason.value = "through timeout vs insufficient material"
            else:
                self.result.value = "White Won"
                self.reason.value = "through timeout"

        self.page.update()

    def selectBlocks(self, positions: list):
        firstBlock = True
        for i,j in positions:
            if(firstBlock):
                self.blocks[i][j].col_change(selectionColor)
                firstBlock = False
            else:
                self.blocks[i][j].col_change(moveColor)

    def deselectBlocks(self, positions: list, gameEnd = False):
        for i,j in positions:
            if((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                self.blocks[i][j].col_change(block_colors[board][0])
            else:
                self.blocks[i][j].col_change(block_colors[board][1])

        if(not gameEnd): # Flag used for ending the game to deselect blocks
            self.showCheck()


    def showCheck(self):
        if(self.c.wking.check):
            self.blocks[self.c.wking.pos[0]][self.c.wking.pos[1]].col_change(checkColor)
        else:
            i, j = self.c.wking.pos
            if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                self.blocks[i][j].col_change(block_colors[board][0])
            else:
                self.blocks[i][j].col_change(block_colors[board][1])

        if(self.c.bking.check):
            self.blocks[self.c.bking.pos[0]][self.c.bking.pos[1]].col_change(checkColor)
        else:
            i, j = self.c.bking.pos
            if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                self.blocks[i][j].col_change(block_colors[board][0])
            else:
                self.blocks[i][j].col_change(block_colors[board][1])

    def promotePawn(self):
        self.pawnPromotion = True
        tempBlocks = [self.blocks[3][3], self.blocks[3][4], self.blocks[4][3],  self.blocks[4][4]]
        self.tempImages = [self.blocks[3][3].img_get(), self.blocks[3][4].img_get(), self.blocks[4][3].img_get(), self.blocks[4][4].img_get()]


        if(self.c.white_turn):  # White Promotion
            for b in tempBlocks:
                b.col_change("black")
            tempBlocks[0].img_set(wqueen)
            tempBlocks[1].img_set(wbishop)
            tempBlocks[2].img_set(wrook)
            tempBlocks[3].img_set(wknight)
        else:   # Black Promotion
            for b in tempBlocks:
                b.col_change("white")
            tempBlocks[0].img_set(bqueen)
            tempBlocks[1].img_set(bbishop)
            tempBlocks[2].img_set(brook)
            tempBlocks[3].img_set(bknight)
    def move(self, pos:list, move:list, moves:list, beatMoves:list, castling: bool, pawnPromotion: bool, callFromBeat = False):
        if(pawnPromotion):
            self.j = move[1]
            self.promotePawn()
            while(self.pawnPromotion):
                pass
            self.c.selected_piece.pos = move
            if(self.c.white_turn):
                self.c.updateWhitePositions(pos, move)
                self.c.checkWhiteenPassant(self.c.selected_piece, move)
                self.c.updateBlackenPassant()
                self.c.updateRookMoved("White")
                self.c.updateKingMoved('White')
                self.c.moveCalculator()
                self.c.updatePosition(old = pos, new = move, beat = callFromBeat)
                self.c.white_turn = False
            else:
                self.c.updateBlackPositions(pos, move)
                self.c.checkBlackenPassant(self.c.selected_piece, move)
                self.c.updateWhiteenPassant()
                self.c.updateRookMoved("Black")
                self.c.updateKingMoved("Black")
                self.c.moveCalculator()
                self.c.updatePosition(old=pos, new=move, beat=callFromBeat)

                self.c.white_turn = True

            self.showCheck()
            self.blocks[move[0]][move[1]].img_set(self.c.selected_piece.img)
            self.blocks[pos[0]][pos[1]].img_set(transparent_img)
            temp = [pos] + moves + beatMoves
            self.deselectBlocks(temp)
            self.c.selected_piece = None
        else:
            self.showCheck()
            self.blocks[move[0]][move[1]].img_set(self.blocks[pos[0]][pos[1]].img_get())
            self.blocks[pos[0]][pos[1]].img_set(transparent_img)
            temp = [pos] + moves + beatMoves
            self.deselectBlocks(temp)
            if(castling):
                if(move == [7,6]):
                    self.blocks[7][5].img_set(self.blocks[7][7].img_get())
                    self.blocks[7][7].img_set(transparent_img)
                elif(move == [7, 2]):
                    self.blocks[7][3].img_set(self.blocks[7][0].img_get())
                    self.blocks[7][0].img_set(transparent_img)
                elif(move == [0, 6]):
                    self.blocks[0][5].img_set(self.blocks[0][7].img_get())
                    self.blocks[0][7].img_set(transparent_img)
                elif(move == [0, 2]):
                    self.blocks[0][3].img_set(self.blocks[0][0].img_get())
                    self.blocks[0][0].img_set(transparent_img)
        Block.makeSound()

    def beat(self, pos:list, move:list, moves:list, beatMoves:list, enPassant, pawnPromotion: bool):
        if(pawnPromotion):
            if(self.c.white_turn):  # WHite Beated
                self.b_beaten_blocks[self.bBeatenPieces].img_set(self.blocks[move[0]][move[1]].img_get())
                self.bBeatenPieces += 1
            else:
                self.w_beaten_blocks[self.wBeatenPieces].img_set(self.blocks[move[0]][move[1]].img_get())
                self.wBeatenPieces += 1
        elif(enPassant):
            if (not self.c.white_turn):  # White beated black
                self.b_beaten_blocks[self.bBeatenPieces].img_set(self.blocks[move[0]+1][move[1]].img_get())
                self.bBeatenPieces += 1
            else:
                self.w_beaten_blocks[self.wBeatenPieces].img_set(self.blocks[move[0]-1][move[1]].img_get())
                self.wBeatenPieces += 1
        else:
            if (not self.c.white_turn):  # White beated black
                self.b_beaten_blocks[self.bBeatenPieces].img_set(self.blocks[move[0]][move[1]].img_get())
                self.bBeatenPieces += 1
            else:
                self.w_beaten_blocks[self.wBeatenPieces].img_set(self.blocks[move[0]][move[1]].img_get())
                self.wBeatenPieces += 1

        self.move(pos, move, moves, beatMoves, False, pawnPromotion)
        if(enPassant and not self.c.white_turn):    # White En passes
            self.blocks[move[0] + 1][move[1]].img_set(transparent_img)

        if(enPassant and self.c.white_turn):        # Black En passes
            self.blocks[move[0] - 1][move[1]].img_set(transparent_img)

        self.blocks[pos[0]][pos[1]].img_set(transparent_img)

    def blockClicked(self, pos: list):
        if(not self.gameEnd):
            if(self.pawnPromotion):
                if(self.c.white_turn):
                    if(pos == [3,3]):
                        self.c.white_pawns.remove(self.c.selected_piece)
                        self.c.white_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = WhiteQueen(self.c.selected_piece.pos, wqueen, "wq")
                        self.pawnPromotion = False
                        self.c.white_pieces.append(self.c.selected_piece)
                    elif(pos == [3, 4]):
                        self.c.white_pawns.remove(self.c.selected_piece)
                        self.c.white_pieces.remove(self.c.selected_piece)
                        if(self.j % 2 == 0):
                            self.c.selected_piece = WhiteBishop(self.c.selected_piece.pos, wbishop, "wb")
                        else:
                            self.c.selected_piece = WhiteBishop(self.c.selected_piece.pos, wbishop, "wB")
                        self.pawnPromotion = False
                        self.c.white_pieces.append(self.c.selected_piece)
                    elif(pos == [4, 3]):
                        self.c.white_pawns.remove(self.c.selected_piece)
                        self.c.white_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = WhiteRook(self.c.selected_piece.pos, wrook, "wr")
                        self.pawnPromotion = False
                        self.c.white_pieces.append(self.c.selected_piece)
                    elif(pos == [4, 4]):
                        self.c.white_pawns.remove(self.c.selected_piece)
                        self.c.white_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = WhiteKnight(self.c.selected_piece.pos, wknight, "wK")
                        self.pawnPromotion = False
                        self.c.white_pieces.append(self.c.selected_piece)

                else:
                    if (pos == [3, 3]):
                        self.c.black_pawns.remove(self.c.selected_piece)
                        self.c.black_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = BlackQueen(self.c.selected_piece.pos, bqueen, "bq")
                        self.pawnPromotion = False
                        self.c.black_pieces.append(self.c.selected_piece)
                    elif (pos == [3, 4]):
                        self.c.black_pawns.remove(self.c.selected_piece)
                        self.c.black_pieces.remove(self.c.selected_piece)
                        if(self.j % 2 == 0):
                            self.c.selected_piece = BlackBishop(self.c.selected_piece.pos, bbishop, "bB")
                        else:
                            self.c.selected_piece = BlackBishop(self.c.selected_piece.pos, bbishop, "bb")
                        self.pawnPromotion = False
                        self.c.black_pieces.append(self.c.selected_piece)
                    elif (pos == [4, 3]):
                        self.c.black_pawns.remove(self.c.selected_piece)
                        self.c.black_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = BlackRook(self.c.selected_piece.pos, brook, "br")
                        self.pawnPromotion = False
                        self.c.black_pieces.append(self.c.selected_piece)
                    elif (pos == [4, 4]):
                        self.c.black_pawns.remove(self.c.selected_piece)
                        self.c.black_pieces.remove(self.c.selected_piece)
                        self.c.selected_piece = BlackKnight(self.c.selected_piece.pos, bknight, "bK")
                        self.pawnPromotion = False
                        self.c.black_pieces.append(self.c.selected_piece)

                self.deselectBlocks([[3,3], [3,4], [4, 3], [4, 4]])
                self.blocks[3][3].img_set(self.tempImages[0])
                self.blocks[3][4].img_set(self.tempImages[1])
                self.blocks[4][3].img_set(self.tempImages[2])
                self.blocks[4][4].img_set(self.tempImages[3])
            else:
                self.c.blockClicked(pos, self)

    def beatenBlockClicked(self, pos: list):
        pass

    def reset(self, playAgain = True):
        self.result.value = ""
        self.reason.value = ""
        self.resultContainer.visible = False
        if (playAgain):
            self.c.initialize()
            self.initialize()
        self.placePieces()
        for i in range(2, 6):
            for j in range(8):
                self.blocks[i][j].img_set(transparent_img)
        for b in self.w_beaten_blocks:
            b.img_set(transparent_img)
        for b in self.b_beaten_blocks:
            b.img_set(transparent_img)

    def mainMenu(self):
        self.reset(False)
        self.page.go("/")

    def placePieces(self):
        self.blocks[7][0].img_set(wrook)
        self.blocks[7][1].img_set(wknight)
        self.blocks[7][2].img_set(wbishop)
        self.blocks[7][3].img_set(wqueen)
        self.blocks[7][4].img_set(wking)
        self.blocks[7][5].img_set(wbishop)
        self.blocks[7][6].img_set(wknight)
        self.blocks[7][7].img_set(wrook)
        self.blocks[6][0].img_set(wpawn)
        self.blocks[6][1].img_set(wpawn)
        self.blocks[6][2].img_set(wpawn)
        self.blocks[6][3].img_set(wpawn)
        self.blocks[6][4].img_set(wpawn)
        self.blocks[6][5].img_set(wpawn)
        self.blocks[6][6].img_set(wpawn)
        self.blocks[6][7].img_set(wpawn)

        self.blocks[0][0].img_set(brook)
        self.blocks[0][1].img_set(bknight)
        self.blocks[0][2].img_set(bbishop)
        self.blocks[0][3].img_set(bqueen)
        self.blocks[0][4].img_set(bking)
        self.blocks[0][5].img_set(bbishop)
        self.blocks[0][6].img_set(bknight)
        self.blocks[0][7].img_set(brook)
        self.blocks[1][0].img_set(bpawn)
        self.blocks[1][1].img_set(bpawn)
        self.blocks[1][2].img_set(bpawn)
        self.blocks[1][3].img_set(bpawn)
        self.blocks[1][4].img_set(bpawn)
        self.blocks[1][5].img_set(bpawn)
        self.blocks[1][6].img_set(bpawn)
        self.blocks[1][7].img_set(bpawn)

    def updateBoard(self):
        global board
        config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")
        board = int(config.get('SETTINGS', 'board'))

        for cont in self.r2_c_r1.controls:
            cont.bgcolor = border_colors[board]
            content = cont.content
            if(not isinstance(content, ft.Text)):
                for c in content.controls:
                    c.bgcolor = border_colors[board]
                    if(board == 2):
                        c.color = "black"
                    else:
                        c.color = "white"

        for cont in self.r2_c_r2_c2.controls:
            cont.bgcolor = border_colors[board]
            content = cont.content
            if(not isinstance(content, ft.Text)):
                for c in content.controls:
                    c.bgcolor = border_colors[board]
                    if(board == 2):
                        c.color = "black"
                    else:
                        c.color = "white"

        for i in range(8):
            for j in range(8):
                if((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    self.blocks[i][j].col_change(block_colors[board][0])
                else:
                    self.blocks[i][j].col_change(block_colors[board][1])

        self.resignBtn.disabled = False
        self.page.update()

    def build(self):
        # Dimensions
        sc_width, sc_height = self.page.window_width, self.page.window_height
        board_size = sc_height - 200
        block_size = board_size // 8

        # Black Clock
        r1 = ft.Row(controls=[self.b_clock_cont], alignment=ft.MainAxisAlignment.CENTER)

        # Top Border
        if (board == 2):
            self.r2_c_r1 = ft.Row(spacing=0,
                             controls=[ft.Container(width=20, bgcolor=border_colors[board], content=ft.Text()),
                                       ft.Container(width=board_size, bgcolor=border_colors[board],
                                                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                   controls=[
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='a'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='b'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='c'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='d'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='e'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='f'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='g'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='black', value='h')])),
                                       ft.Container(width=20, bgcolor=border_colors[board], content=ft.Text())])
        else:
            self.r2_c_r1 = ft.Row(spacing=0,
                             controls=[ft.Container(width=20, bgcolor=border_colors[board], content=ft.Text()),
                                       ft.Container(width=board_size, bgcolor=border_colors[board],
                                                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                   controls=[
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='a'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='b'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='c'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='d'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='e'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='f'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='g'),
                                                                       ft.Text(bgcolor=border_colors[board],
                                                                               color='white', value='h')])),
                                       ft.Container(width=20, bgcolor=border_colors[board], content=ft.Text())])

        # Beaten Column, Left Border, Board, Right Border, Beaten Column
        r2_c_r2 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=0)

        self.w_beaten_blocks = list()
        r2_c_r2_c1 = ft.Column(spacing=0)
        for i in range(8):
            r = ft.Row(spacing=0)
            for j in range(2):
                b = Block(b_size=block_size, col='#1f1101', pos=[i,j], page = self.page, board=self, func=self.beatenBlockClicked)
                r.controls.append(b)
                self.w_beaten_blocks.append(b)
            r2_c_r2_c1.controls.append(r)
        r2_c_r2.controls.append(r2_c_r2_c1)

        # Left Border
        if (board == 2):
            self.r2_c_r2_c2 = ft.Column(controls=[ft.Container(width=20, height=board_size, bgcolor=border_colors[board],
                                                          content=ft.Column(spacing=0,
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            height=board_size, width=20, controls=[
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 8'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 7'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 6'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 5'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 4'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 3'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 2'),
                                                                  ft.Text(bgcolor=border_colors[board], color='black',
                                                                          value=' 1')]))])
        else:
            self.r2_c_r2_c2 = ft.Column(controls=[ft.Container(width=20, height=board_size, bgcolor=border_colors[board]
                                                          , content=ft.Column(spacing=0,
                                                                              alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                              height=board_size, width=20, controls=[
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 8'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 7'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 6'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 5'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 4'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 3'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 2'),
                        ft.Text(bgcolor=border_colors[board], color='white',
                                value=' 1')]))])
        r2_c_r2.controls.append(self.r2_c_r2_c2)

        # Board
        self.blocks = list()
        r2_c_r2_c3 = ft.Column(spacing=0)
        for i in range(8):
            self.blocks.append(list())
            r = ft.Row(spacing=0)
            for j in range(8):
                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    b = Block(block_size, block_colors[board][0], page = self.page, board=self, func=self.blockClicked, pos=[i,j])
                else:
                    b = Block(block_size, block_colors[board][1], page = self.page, board=self, pos = [i,j], func=self.blockClicked)
                # b.pos = [i,j]
                r.controls.append(b)
                self.blocks[i].append(b)
            r2_c_r2_c3.controls.append(r)
        r2_c_r2.controls.append(r2_c_r2_c3)

        # Right Border
        r2_c_r2.controls.append(self.r2_c_r2_c2)

        # Black Beaten Pieces Slots
        self.b_beaten_blocks = list()
        r2_c_r2_c4 = ft.Column(spacing=0)
        for i in range(8):
            r = ft.Row(spacing=0)
            for j in range(2):
                b = Block(b_size=block_size, col='#1f1101', page = self.page, board=self, pos=[i,j], func=self.beatenBlockClicked)
                r.controls.append(b)
                self.b_beaten_blocks.append(b)
            r2_c_r2_c4.controls.append(r)
        r2_c_r2.controls.append(r2_c_r2_c4)

        # Bottom Border is same as the top border

        r2 = ft.Row(controls=[ft.Column(controls=[self.r2_c_r1, r2_c_r2, self.r2_c_r1], spacing=0,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER)], spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER)

        r3 = ft.Row(controls=[self.w_clock_cont], alignment=ft.MainAxisAlignment.CENTER)

        self.resignBtn = ft.ElevatedButton(text="Resign", on_click=lambda e: self.c.resigned())
        r4 = ft.Row(controls=[self.resignBtn], alignment=ft.MainAxisAlignment.CENTER)

        c = ft.Column(controls=[r1, r2, r3, r4])

        self.result = ft.Text(value="", size= 17, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER, width = block_size*4)
        self.reason = ft.Text(value = "", size = 13, italic=True, color = "white", text_align=ft.TextAlign.CENTER, width = block_size*4)

        playAgainBtn = ft.ElevatedButton(text="Play Again",on_click= lambda e: self.reset())
        mainMenuBtn = ft.ElevatedButton(text="Main Menu",on_click= lambda e: self.mainMenu())

        self.resultContainer = ft.Container(visible = False, bgcolor="black", width=block_size*4, height = block_size*2, top=self.page.window_height//2 - 106, left = self.page.window_width //2 -(block_size*2) - 8,
                                       content= ft.Column(controls=[self.result, self.reason, ft.Row([playAgainBtn, mainMenuBtn], alignment=ft.MainAxisAlignment.SPACE_EVENLY)], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
                                       )

        stack = ft.Stack(controls=[c, self.resultContainer, Block.audio])

        # Setting up the images
        self.placePieces()

        return ft.View(route='/game',padding=0, controls=[stack])