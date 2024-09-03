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
        self.wordDict = insertDict2("./dictionaries/rudict.txt",self.trie)
        self.defArea = ft.Column()
            
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
            self.tasks_view,
            self.defArea,          
        ]

    def add_clicked(self, e):
        if self.text_field.value:
            worddef =  "Слово не найдено"
            if self.text_field.value in self.wordDict:
                worddef = self.wordDict[self.text_field.value]
            definition = ft.Container(
                    content=ft.Text(worddef),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=600,
                    bgcolor=ft.colors.CYAN_200,
                    # height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            self.defArea.controls = definition
            # self.page.add(ft.Column(definition))
            self.text_field.value = ""
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
        self.defArea.controls = []
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
    page.window.height = 480
    page.window.width = 640
    page.window.center()
    
    
    with open("./dictionaries/russian.txt", "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
    

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)



ft.app(target=main)
