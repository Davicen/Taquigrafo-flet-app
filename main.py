import math
import flet as ft
from sympy import false
from page_record import RecordPage
from components import styles

def main(page: ft.Page):

    page.title = "Taquigrafo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = styles.theme_clear
    page.bgcolor = styles.APP_WHITE
    #page.window_bgcolor = styles.APP_WHITE
    page.update()
    
    def copy_to_clipboard(self,e):
        page.set_clipboard(page, self.transcription.value) # type: ignore
        self.update()

    # create application instance
    todo = RecordPage(page=page)

    # add application's root control to the page
    page.add(todo)

ft.app(target=main, view=ft.AppView.FLET_APP)