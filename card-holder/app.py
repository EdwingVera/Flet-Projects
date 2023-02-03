from flet import *
from settings import ColorList as cl
import clipboard


class App(UserControl):

    def WalletContainer(self):
        
        # Some variables set as compoments
        self.CardList = Column(
            alignment='start',
            spacing=25,
        )
        
        self.ImportButton = IconButton(
            icon=icons.DOWNLOAD,
            icon_size=16,
            on_click=lambda e: self.OpenEntryForm(),
            disabled=True,
        )
        
        self.InsertButton = IconButton(
            icon=icons.ADD,
            icon_size=16,
            on_click=lambda e: self.OpenEntryForm(),
            disabled=True,
        )
        
        self.WalletContainer = Container(
            # alignment=alignment.center_right,
            # padding=padding.only(right=200),
            # Use CARD to get elevation feature
            content=Card(
                elevation=15,
                content=Container(
                    content=Column(
                        scroll="auto",
                        alignment="start",
                        spacing=25,
                        controls=[
                            self.snack,
                            Row(
                                alignment="spaceBetween",
                                controls=[
                                    # Title of the app
                                    Text(
                                        "Wallite", color="white", size=20, weight="bold"
                                    ),
                                    # Container with the icon buttons
                                    Container(
                                        content=Row(
                                            spacing=0,
                                            tight=True,
                                            alignment="end",
                                            controls=[
                                                self.InsertButton,
                                                self.ImportButton,
                                            ],
                                        )
                                    ),
                                ],
                            ),
                            Container(
                                content=Column(
                                    controls=[self.CardList],
                                ),
                            ),
                        ],
                    ),
                    width=360,
                    height=580,
                    padding=padding.all(20),
                    alignment=alignment.top_center,
                    border_radius=border_radius.all(15),
                    gradient=self.GradientGenerator(
                        cl.WALLITE["from"], cl.WALLITE["to"]
                    ),
                ),
            ),
        )

        return self.WalletContainer

    # Method that generates the gradients for backgrounds
    def GradientGenerator(self, start, end):
        self.ColorGradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end
            ]
        )
    
    def build(self):
        self.CardColumn = Column()
        self.snack = SnackBar(Text('NumberCopied!'))

        return Container(
            content=(
                Column(
                    alignment='center',
                    controls=[
                        #self.EntryForm(),
                        self.WalletContainer()
                    ]
                )
            ),
            width=900,
            height=800,
            margin=margin.all(-10),
            gradient=self.GradientGenerator(cl.BACKGROUND['from'], cl.BACKGROUND['to']),
            alignment=alignment.center,
        )
