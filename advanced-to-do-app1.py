from flet import *
from custom_checkbox import CustomCheckBox


def main(page: Page):
    BG = '#041955'
    FWG = 'yellow'
    FG = '#3450a1'
    PINK = '#eb06ff'

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='purple'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5,0.5],
                    colors=['#00000000', PINK],

                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(alignment='center',
                    controls=[

                    ]        )

            )
        ]
    )

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8,alignment=alignment.center_right)
        # page_2.controls[0].border_radius=border_radius.only(
        #     topLeft=35,
        #     topRight=20,
        #     bottomLeft=35,
        #     bottomRight=0,
        # )
        page_2.update()


    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(1,alignment=alignment.center_right)
        page_2.update()


    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(
    #         pages[page.route]
    #         # View(
    #         #     "/",
    #         #     [
    #         #         container
    #         #     ],
    #         # ),
    #     )

    create_task_view = Container(
        content=Container(on_click=lambda _: page.go('/'),
            height=40,width=40,
            content=Text('x')
            )
    )  

    # pages = {
    #     '/':View(
    #         "/",
    #         [
    #             container
    #         ],
    #     ),
    #     '/create_task': View(
    #         "/create_task",
    #         [
    #             create_task_view
    #         ],
    #     )
    # }


    tasks = Column(
        height=400,
        scroll='auto',
        # controls=[
        #     Container(height=50,width=300,bgcolor='blue'),
        #     Container(height=50,width=300,bgcolor='green'),
        #     Container(height=50,width=300,bgcolor='purple'),
        #     Container(height=50,width=300,bgcolor='yellow'),
        #     ]

    )

    for i in range(15):

        tasks.controls.append(
            Container(height=50,width=400,bgcolor='blue',border_radius=25,padding=padding.only(
                left=20,top=13,
            ),
            content=CustomCheckBox(
                color='Yellow',
                size=25,font_size=20,
                label='Create interesting content!'
            )),
        )

    categories_Card = Row(
        scroll='auto'

    )
    categories = ['Business','Family','Friends']
    for i, category in enumerate(categories):
        categories_Card.controls.append(
            Container(
                bgcolor=FWG,
                height=150,
                width=180,
                border_radius=20,
                padding=25,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='Blue',
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor='pink',
                            )
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                          content=Icon(
                              icons.MENU)),
                        Row(
                            controls=[
                              Icon(icons.SEARCH),
                              Icon(icons.NOTIFICATIONS_OUTLINED)
                            ],
                        ),   
                    ],
                ),
                Container(height=13,padding=20,bgcolor='yellow',),
                Text(
                    value='What\'s up, Olivia!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10,bottom=25,),
                    content=categories_Card
                ),
                Container(height=15),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                       tasks,
                       FloatingActionButton(bottom=2,right=20,
                           icon = icons.ADD,on_click=lambda _: page.go('/create_task')
                       ) 
                    ]
                )
            ],
        ),
    )


    page_1 = Container(
        width=400,
        height=850,
        bgcolor='yellow',
        border_radius=35,
        padding=padding.only(left=50,top=60,right=200),


        content=Column(
            controls=[
                Row(alignment='end',
                    controls=[
                        Container(border_radius=25,
                        padding=padding.only(
                            top=13,left=13,
                        ),
                        height=50,
                        width=50,
                        border=border.all(color='white',width=1),
                        on_click=lambda e: restore(e),
                        content=Text('<'))
                    ]
                ),
                Container(height=20),
                circle,
                Text('Olivia\nMitchel',size=32,weight='bold'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP,color='red'),
                    Text('Templetes',size=15,weight=FontWeight.W_300,color='pink',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL,color='red'),
                    Text('Templetes',size=15,weight=FontWeight.W_300,color='pink',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED,color='red'),
                    Text('Templetes',size=15,weight=FontWeight.W_300,color='pink',font_family='poppins')
                ]),

                # images
                # Image(src=f"/images/1.png",
                # width=300,
                # height=200,)
                # Container(border_radius=25,padding=padding.only(top=13,left=13),
                          
                #     height=50,width=50,border=border.all(color='blue',width=2),
                #     on_click=lambda e: restore(e),
                #     content=Text('<')
                # )
            ]
        )
    )
    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor='Pink',
                border_radius=38,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                    top=50,
                    left=20,
                    right=40,
                    bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=500, 
        height=650, 
        bgcolor='Blue60',
        border_radius=38,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )

    )
    # this page is used in the next page open and first page open
    pages = {
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main)
