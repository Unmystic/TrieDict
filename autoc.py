# import flet as ft

# def main(page: ft.Page):
#     page.add(
#         ft.AutoComplete(
#             suggestions=[
#                 ft.AutoCompleteSuggestion(key="one 1", value="One"),
#                 ft.AutoCompleteSuggestion(key="two 2", value="Two"),
#                 ft.AutoCompleteSuggestion(key="three 3", value="Three"),
#             ],
#             on_select=lambda e: print(e.control.selected_index, e.selection),
#         )
#     )

# ft.app(target=main)

import flet as ft
from trie import Trie,TrieNode
from trieInsert import insertDict2

class CustomAutoComplete_Widget():
    def __init__(self, page, items,col):
        self.page = page
        self.items = items
        self.col = col
        self.filtered_items = items.copy()
        self._build()

    def _build(self):
        self._assets()
        self.stack = ft.Stack(
            controls=[
                self.col,  # Base layer
                self.list_cont,     
            ],
        )
        self.page.add(self.text_field, self.stack)  # Add the stack

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
            self.filtered_items = [item for item in self.items if query in item.lower()]
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
    page.title = "Filtered List Example"


    with open("./dictionaries/russian.txt", "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
    all_items = ["fruit" + str(i) for i in range(1, 1001)]

    column = ft.Column(
    )

    CustomAutoComplete_Widget(page, words,column)


ft.app(target=main)

# import flet as ft


# def main(page: ft.Page):
#     list_example = ["one 1", "two 2", "three 3"]
#     auto_complete = ft.AutoComplete(
#         suggestions=[ft.AutoCompleteSuggestion(value=i) for i in list_example],
#         on_select=lambda e: print(e.selection),
#     )
#     text_file = ft.TextField(width=400)
#     page.add(ft.Row([ft.Column([text_file, ft.Stack(controls=[auto_complete],width=400)]),
#                                 ft.Column([text_file, ft.Stack(controls=[auto_complete],width=400)])]))


# ft.app(target=main)