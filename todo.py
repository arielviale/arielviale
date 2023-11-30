import flet as ft

def main(page: ft.Page):
    
    page.title = "Todo App"
    
    input_text = ft.TextField(hint_text="What needs to be done?", autofocus=True, width=350)
    
    
    def button_clicked(e):
        page.add(ft.Checkbox(label=input_text.value))
        
        
    page.add(
        ft.Row(
            [       
                input_text,
                ft.ElevatedButton(text="Add", on_click=button_clicked)
                
            ]
        )
    )          

ft.app(target=main)