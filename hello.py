#Importo la libreria
import flet as ft 




#Defino la funcion main

def main(page: ft.Page):
    page.title = "Hello World"
    #Controles para textos
    text = ft.Text(value="Mi primer texto")
    
    page.controls.append(text)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    
    
   

#Iniciamos la app
ft.app(target=main)