import flet as ft
from trie import Trie,TrieNode
from trieInsert import insertDict2, insertDict


class TodoApp(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.trie = Trie()
        insertDict2("./dictionaries/rudict.txt",self.trie)
        
        self.list_view = ft.ListView(
            expand=1,
            spacing=10,
            controls=[],
        )
        self.list_cont = ft.Container(
            content = self.list_view,
            bgcolor= ft.colors.WHITE,
        )
        self.text_field = ft.TextField(label="Введите слово")
        self.text_field.on_change = self._filter_list
        
        self.stack = ft.Stack(
            controls=[
                self.col,  # Base layer
                self.list_cont,                    
            ],
        )

        
        self.controls = [
            ft.Row(
                controls=[
                    self.text_field,
                    ft.ElevatedButton(expand=True,
                        content=ft.Row(
                        [
                            ft.Icon(name=ft.icons.MENU_BOOK_OUTLINED, color="blue"),
                            ft.Text(value="Посмотреть определение", weight=ft.FontWeight.BOLD, size=16, italic=True,color=ft.colors.BLUE)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        # content=ft.Text(value="Определение", size=16, font_family="Segoe Print Bold",),
                        style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                            ft.MaterialState.FOCUSED: ft.colors.BLACK,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={ft.MaterialState.PRESSED: ft.colors.LIGHT_BLUE_ACCENT_200, "": ft.colors.BLUE_100,},
                        padding={ft.MaterialState.DEFAULT: 20},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={"pressed": 0, "": 1},
                        animation_duration=500,
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.WHITE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                        },
                        shape={
                            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                        },
                        ),              
                        on_click=self.add_clicked,
                        ),                   
                ],
            ),
            self.list_cont,
            
        ]

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()

    def _filter_list(self, e):
        query = e.control.value.lower()
        if query:
            # self.filtered_items = [item for item in self.items if query in item.lower()]
            self.filtered_items = self.trie.autocomplete(query.title())
            print(len(self.filtered_items))
        else:
            self.filtered_items = []
        self.list_view.controls = [
            ft.ListTile(
                title=ft.Text(item),
                on_click=lambda e, item=item: self._on_list_item_click(item)
            ) for item in self.filtered_items
        ]
        self.page.update()

    def _on_list_item_click(self, item):
        self.text_field.value = item
        self.filtered_items = []
        self.list_view.controls = [] 
        self.page.update()
        print(f"Selected item: {item}") 



class CustomAutoComplete_Widget():
    def __init__(self, items,col):
        # self.page = page
        self.items = items
        self.col = col
        self.filtered_items = []
        self._build()

    def _build(self):
        self._assets()
        self.stack = ft.Stack(
            controls=[
                self.col,  # Base layer
                self.list_cont,                    
            ],
        )
        # self.page.add(self.text_field, self.stack)  # Add the stack

    def _assets(self):
        self.list_view = ft.ListView(
            expand=1,
            spacing=10,
            controls=[],
        )
        self.list_cont = ft.Container(
            content = self.list_view,
            bgcolor= ft.colors.WHITE,
        )
        self.text_field = ft.TextField(label="Filter list")
        self.text_field.on_change = self._filter_list

    def _filter_list(self, e):
        query = e.control.value.lower()
        if query:
            # self.filtered_items = [item for item in self.items if query in item.lower()]
            self.filtered_items = self.items.autocomplete(query.title())
            print(len(self.filtered_items))
        else:
            self.filtered_items = []
        self.list_view.controls = [
            ft.ListTile(
                title=ft.Text(item),
                on_click=lambda e, item=item: self._on_list_item_click(item)
            ) for item in self.filtered_items
        ]
        self.page.update()

    def _on_list_item_click(self, item):
        self.text_field.value = item
        self.filtered_items = []
        self.list_view.controls = [] 
        self.page.update()
        print(f"Selected item: {item}") 


def main(page: ft.Page):
    page.title = "Dictionary with definitions"
    
    with open("./dictionaries/russian.txt", "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
    
    trie = Trie()
    # insertDict("./dictionaries/russian.txt",trie)
    insertDict2("./dictionaries/rudict.txt",trie)
    # all_items = ["fruit" + str(i) for i in range(1, 1001)]

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)


    # column = ft.Column(
    # )

    # CustomAutoComplete_Widget( trie,column)


ft.app(target=main)
