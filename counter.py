import flet as ft 
from time import sleep

def main(page: ft.Page):
    page.title = "Counter App"
    
    text = ft.Text(value="Count", font_family="Arial", size=50, color="blue")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(text)
    
    for i in range(1,11):
        text.value = "Count" + str(i)
        page.update()
        sleep(1)
    
   



ft.app(target=main)