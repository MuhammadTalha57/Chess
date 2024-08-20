import flet as ft
from configparser import ConfigParser
from time import sleep

config = ConfigParser()
config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")

if(config.get('SETTINGS','timed')=='True'):
    timed=True
else:
    timed=False

time_limit = int(config.get('SETTINGS','time limit'))

def config_write():
    config.read("C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini")
    config['SETTINGS'] = {'board':config.get('SETTINGS','board'), 'timed':str(timed), 'time limit':str(time_limit)}
    with open('C:\\Users\Talha\PycharmProjects\PythonPractice\Settings.ini', 'w') as f:
        config.write(f)

class Main_menu(ft.UserControl):
    # When user starts the game
    def start_clicked(self,e):
        self.btn_column.visible = False
        self.start_clicked_column.visible = True
        self.cont.image_opacity = 0.2
        self.cont.update()
        self.btn_column.update()
        self.start_clicked_column.update()

    # When User click Back in the start menu
    def back_clicked(self,e):
        config_write()
        self.start_clicked_column.visible = False
        self.btn_column.visible=True
        self.cont.image_opacity = 0.7
        self.cont.update()
        self.btn_column.update()
        self.start_clicked_column.update()

    def time_toggled(self,e):
        global timed
        timed = not timed
        self.time_drp_down.disabled = not timed
        self.time_drp_down.update()
        config_write()

    def time_drp_down_changed(self,e):
        global time_limit
        val = self.time_drp_down.value
        if(val=='2 minutes'):
            time_limit = 2
        elif(val=='5 minutes'):
            time_limit = 5
        elif (val == '10 minutes'):
            time_limit = 10
        elif (val == '15 minutes'):
            time_limit = 15
        elif (val == '30 minutes'):
            time_limit = 30
        elif (val == '60 minutes'):
            time_limit = 60
        config_write()

    def play_clicked(self, e):
        self.btn_column.visible = True
        self.start_clicked_column.visible = False
        self.cont.image_opacity = 0.7
        self.cont.update()
        self.btn_column.update()
        self.start_clicked_column.update()

        self.page.go('/game')
        sleep(0.01) # For avoiding the error that BLOCKS aren't added to the page

    def __init__(self, sc_width, sc_height, page):
        super().__init__()
        self.sc_width, self.sc_height, self.page = sc_width, sc_height, page
        self.bg_img_opacity = 0.7

        # Contains START, OPTIONS and QUIT buttons
        start_btn = ft.ElevatedButton(text="START",on_click=self.start_clicked)
        opt_btn = ft.ElevatedButton(text="OPTIONS",on_click=lambda e : self.page.go('/options'))
        quit_btn = ft.ElevatedButton(text="QUIT", on_click=lambda e : self.page.window_destroy())

        self.btn_column = ft.Column( horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
            start_btn,opt_btn,quit_btn] )

        # Dropdown for selecting time
        self.time_drp_down = ft.Dropdown(
            value=f'{time_limit} minutes',disabled=not timed,width=100,label='Time',on_change=self.time_drp_down_changed,options=[
                ft.dropdown.Option('2 minutes'),
                ft.dropdown.Option('5 minutes'),
                ft.dropdown.Option('10 minutes'),
                ft.dropdown.Option('15 minutes'),
                ft.dropdown.Option('30 minutes'),
                ft.dropdown.Option('60 minutes'),
                                                                ]
                                        )

        # Column for Start menu
        time_text = ft.Text(value="Timed", theme_style=ft.TextThemeStyle.DISPLAY_SMALL,weight=ft.FontWeight.BOLD)
        r1 = ft.Row(spacing=100,controls=[time_text,ft.Switch(value=timed, on_change=self.time_toggled)])

        play_btn = ft.ElevatedButton(text='PLAY',width=100,bgcolor='green',color='white',on_click=self.play_clicked)
        back_btn = ft.ElevatedButton(text='BACK', width=100, color='white', on_click=self.back_clicked)
        r3 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[play_btn,back_btn])

        self.start_clicked_column = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False,width=self.sc_width//4,height=self.sc_height//4,
                                    controls=[r1,self.time_drp_down,r3]
                                            )

        self.start_clicked_cont = ft.Container(content=self.start_clicked_column)

    def build(self):
        # Chess Heading
        r1 = ft.Row(
            controls=[ft.Text(value="CHESS", theme_style=ft.TextThemeStyle.DISPLAY_LARGE, weight=ft.FontWeight.BOLD)],
            height=(self.sc_height) // 2, alignment=ft.MainAxisAlignment.CENTER
        )

        # For Buttons
        r2 = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.btn_column, self.start_clicked_cont,
            ]
        )

        self.cont = ft.Container(
            image_src='C:\\Users\Talha\PycharmProjects\PythonPractice\\Images\\Main_menu_image.png',
            image_fit=ft.ImageFit.FILL,
            alignment=ft.alignment.top_center,
            expand=True,
            image_opacity=self.bg_img_opacity,
            blend_mode=ft.BlendMode.COLOR,
            content=ft.Column(controls=[r1, r2])
        )
        return ft.View(route='/', controls=[self.cont], padding=0)