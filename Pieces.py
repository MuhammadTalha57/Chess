class Piece:
    def __init__(self, pos: list, img:str, id:str):
        self.pos = pos
        self.moves = []
        self.beat_moves = []
        self.img = img
        self.id = id

class WhitePawn(Piece):
    def __init__(self, pos: list, img:str, id:str, no: int):
        super().__init__(pos, img, id)
        self.en_passant = False         # Could be captured
        self.firstMove = True
        self.no = no

class BlackPawn(Piece):
    def __init__(self, pos: list, img:str, id:str, no:int):
        super().__init__(pos, img, id)
        self.firstMove = True
        self.en_passant = False         # Could be captured
        self.no = no

class WhiteKnight(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)

class BlackKnight(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)

class WhiteBishop(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)

class BlackBishop(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)

class WhiteRook(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)
        self.moved = False

class BlackRook(Piece):
    def __init__(self, pos:list, img, id:str):
        super().__init__(pos, img, id)
        self.moved = False

class WhiteQueen(Piece):
    def __init__(self, pos:list, img:str, id:str):
        super().__init__(pos, img, id)

class BlackQueen(Piece):
    def __init__(self, pos:list, img, id:str):
        super().__init__(pos, img, id)

class WhiteKing(Piece):
    def __init__(self, pos: list, img, id:str):
        super().__init__(pos, img, id)
        self.check = False
        self.moved = False

class BlackKing(Piece):
    def __init__(self, pos: list, img, id:str):
        super().__init__(pos, img, id)
        self.check = False
        self.moved = False