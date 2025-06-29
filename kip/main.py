import flet as ft

def main(page: ft.Page):
    # Structure GUI Title and Scale
    page.title = "My Expenses"
    page.window.width = 700
    page.window.height = 500
    
    list_expenses = []
    
    def on_click_add(e):
        pass
    
    def on_click_summary(e):
        def close_dialog(e):
            dialog.open = False
            page.update
        
        dialog = ft.AlertDialog(
            model=True,
            title=ft.Text("Summary")
        )
    
    header_title = ft.Row([
        ft.Container(
            content=ft.Text("Expense Tracker",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            selectable=True,
                            ),
            margin=10,
            alignment=ft.alignment.center,
            expand=1
        )
    ])
    
    field_item = ft.Row([
        ft.Container(
            content=ft.TextField(label="Item",
                                border_color="#ffffff",
                                width=500),
            margin=5,
            alignment=ft.alignment.center,
            expand=1
        )
    ])
    
    field_price = ft.Row([
        ft.Container(
            content=ft.TextField(label="Price",
                                border_color="#ffffff",
                                width=500),
            margin=5,
            alignment=ft.alignment.center,
            expand=1
        )
    ])
    
    button_add = ft.ElevatedButton(text="Add")
    button_summary = ft.ElevatedButton(text="View Summary")
    
    button_add.on_click = on_click_add
    button_summary.on_click = on_click_summary
    
    group_button = ft.Container(
        padding=ft.Padding(10 , 20 ,10 , 10),
        content=ft.Row(
            [
                ft.Container(content=button_add),
                ft.Container(content=button_summary),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
    
    page.add(header_title,
            field_item,
            field_price,
            group_button)
    
ft.app(main)