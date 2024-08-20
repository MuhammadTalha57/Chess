import flet as ft
from configparser import ConfigParser

config = ConfigParser()
config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")
board = int(config.get('SETTINGS','board'))

def config_write():
    config['SETTINGS'] = {'board':str(board), 'timed':config.get('SETTINGS', 'timed'), 'time limit':config.get('SETTINGS', 'time limit')}
    with open('C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini', 'w') as f:
        config.write(f)

class Options(ft.UserControl):
    def board_click(self, clicked_board, board_no):
        global board
        board = board_no
        self.green_board.image_opacity, self.brown_board.image_opacity , self.black_board.image_opacity = 0.3, 0.3, 0.3
        clicked_board.image_opacity = 1
        self.green_board.update(), self.brown_board.update(), self.black_board.update()

    def back_clicked(self,e):
        config_write()
        self.page.go('/')

    def __init__(self, page):
        super().__init__()
        self.page = page

        green_opacity, brown_opacity, black_opacity = 0.3, 0.3, 0.3
        # Selecting board acc to user's config
        if (board == 0):
            green_opacity = 1
        elif (board == 1):
            brown_opacity = 1
        else:
            black_opacity = 1

        self.green_board = ft.Container(width=200,height=200,image_src="C:\\Users\Talha\PycharmProjects\PythonPractice\Images\Green_Board.PNG",
        image_fit=ft.ImageFit.CONTAIN, image_opacity=green_opacity, on_click=lambda e :self.board_click(self.green_board,0)
                                        )
        self.brown_board = ft.Container(width=200, height=200,
        image_src="C:\\Users\Talha\PycharmProjects\PythonPractice\Images\Brown_Board.PNG",
        image_fit=ft.ImageFit.CONTAIN, image_opacity=brown_opacity,
        on_click=lambda e: self.board_click(self.brown_board,1)
                                        )
        self.black_board = ft.Container(width=200, height=200,
        image_src="C:\\Users\Talha\PycharmProjects\PythonPractice\Images\Black_White_Board.PNG",
        image_fit=ft.ImageFit.CONTAIN, image_opacity=black_opacity,
        on_click=lambda e: self.board_click(self.black_board,2)
                                        )

    def build(self):
        r1 = ft.Row(controls=[ft.Text(value="OPTIONS", color="white", expand=True, theme_style=ft.TextThemeStyle.DISPLAY_LARGE, weight=ft.FontWeight.BOLD)])
        r2 = ft.Row(controls= [ft.Text(value="Board", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.BOLD)])
        r3 = ft.Row(controls=[self.green_board, self.brown_board, self.black_board])
        r4 = ft.Row(controls=[ft.ElevatedButton(text='Back', on_click=self.back_clicked)])

        return ft.View(route='/options', controls=[r1, r2, r3, r4])