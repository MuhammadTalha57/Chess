import flet as ft

class Block(ft.UserControl):
    audio = ft.Audio(src="move-self.mp3")
    @classmethod
    def makeSound(cls):
        cls.audio.play()

    def __init__(self, b_size, col, page, pos, board, func, img='C:\\Users\Talha\PycharmProjects\PythonPractice\Images\\Transparent.png'):
        super().__init__()
        self.b_size = b_size
        self.col = col
        self.img = img
        self.page = page
        self.pos = pos
        self.cont = ft.Container(on_click = lambda _: func(self.pos), bgcolor=self.col, width=self.b_size, height=self.b_size, image_src=self.img,image_fit=ft.ImageFit.CONTAIN, border=ft.border.all(0.2, self.col), border_radius=0)

    def build(self):
        return self.cont

    def img_set(self, img:str):
        self.img = img
        self.cont.image_src = img
        self.update()
        self.page.update()

    def img_get(self):
        return self.img

    def col_change(self, col:str):
        self.cont.bgcolor = col
        self.cont.border = ft.border.all(0.2, self.col)
        # Was raising exception when trying to Update board (updateBoard func in Board)
        try:
            self.update()
        except:
            pass