import flet
from flet import *
from app import App

def main(page:Page):
    
    page.title = "Finance Tracker"
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.update()
    
    app = App()
    page.add(app)
    
flet.app(target=main)