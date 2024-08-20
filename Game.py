import flet as ft
import MainMenu
import Options
import Board

def main(page: ft.Page):
    mmView = MainMenu.Main_menu(page.window_width, page.window_height, page).build()
    optView = Options.Options(page).build()
    game = Board.Board(page)
    gameView = game.build()


    def route_change(e:ft.RouteChangeEvent):
        page.views.clear()
        if(page.route=='/'):
            page.views.append(mmView)
        elif(page.route=='/options'):
            page.views.append(optView)
        elif(page.route == '/game'):
            game.c.initialize()
            page.views.append(gameView)
            game.initialize()

        page.update()

    page.on_route_change=route_change
    page.go('/')

ft.app(target=main)