import flet
from flet import *


class App(UserControl):

    def movement_card(self, title : str, action : bool, value : int):
        
        self.title = title
        self.action = action
        self.value = value
        
        self.card_title = Container(
            width=298,
            height=42,
            content=Row(
                spacing=12,
                controls=[
                    Icon(
                        name=icons.ARROW_UPWARD,
                        color="#38A169"
                    ),
                    Text(value=self.title, color='black', size=18)
                ]
            )
        )
        
        self.card_value = Container(
            width=120,
            height=42,
            alignment=alignment.center,
            content=(
                Text(value=f'$ {self.value}', color='black', size=18, weight='bold')
            )
        )
        
        return Container(
            width=418,
            height=42,
            padding=8,
            border_radius=12,
            bgcolor='white',
            content=Row(
                alignment='start',
                vertical_alignment='center',
                controls=[
                    self.card_title,
                    self.card_value,
                ]
            )
        )
    
    def build(self):

        self.balance_value = Text('00.000$', size=24)

        self.balance_bar = Container(
            width=320,
            height=40,
            bgcolor="#3182CE",
            alignment=alignment.center,
            border_radius=32,
            content=self.balance_value
        )

        self.money_movements = ListView(
            expand=True,
            spacing=16,
            controls=[
                self.movement_card('Walmart', True, 12000),
            ]
        )

        self.new_movement = FilledButton(
            text='New',
            icon=icons.ARROW_RIGHT,
        )

        return Container(
            width=450,
            height=790,
            border_radius=32,
            padding=16,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=[
                    "#060C12",
                    "#000000"
                ]
            ),
            content=Column(
                horizontal_alignment='center',
                expand=True,
                controls=[
                    self.balance_bar,
                    self.money_movements,
                    self.new_movement,
                ]
            )
        )
