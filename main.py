import flet
from flet import *
from app import App

def start(page:Page):
    
    # App Title
    page.title = "Wallite"
    
    # App Dimensions
    page.window_width = 450
    page.window_height = 790
    
    # Update
    page.update()
    
    # Call the App() class from app.py file
    app = App()
    # Add the isntance of App() ==> app to the root page
    page.add(app)
    
flet.app(target=start)