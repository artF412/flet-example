import flet as ft

def main(page: ft.Page):
    student_names = [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Henry", "Isabel", "Jack"
    ]
    radio_groups = []
    attendance_data = {}

    submit_button = ft.ElevatedButton(text="Submit", disabled=True)
    check_button = ft.ElevatedButton(text="Check", disabled=True)

    def check_all_selected(e=None):
        all_selected = all(rg.value in ["Present", "Absent"] for rg in radio_groups)
        submit_button.disabled = not all_selected
        submit_button.update()

    def handle_submit(e):
        attendance_data.clear()
        for i, name in enumerate(student_names):
            attendance_data[name] = radio_groups[i].value

        check_button.disabled = False
        check_button.update()

        snack = ft.SnackBar(
            content=ft.Text("Submitted successfully!"),
            duration=2000,
        )

        page.overlay.append(snack)
        snack.open = True
        page.update()

    def handle_check(e):
        present = [name for name, status in attendance_data.items() if status == "Present"]
        absent = [name for name, status in attendance_data.items() if status == "Absent"]

        present_text = "\n".join(present) or "ไม่มี"
        absent_text = "\n".join(absent) or "ไม่มี"

        def close_dialog(e):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("ผลการเช็คชื่อ"),
            content=ft.Column([
                ft.Text("🟢 มาเรียน:", weight="bold"),
                ft.Text(present_text),
                ft.Text("🔴 ขาดเรียน:", weight="bold"),
                ft.Text(absent_text),
            ], tight=True),
            actions=[
                ft.TextButton("ปิด", on_click=close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # สร้างตารางแถวละคน
    table_rows = []
    for name in student_names:
        rg = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="Present", label="Present"),
                ft.Radio(value="Absent", label="Absent")
            ], alignment=ft.MainAxisAlignment.CENTER),
            on_change=check_all_selected
        )
        radio_groups.append(rg)

        table_rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Container(content=ft.Text(name), alignment=ft.alignment.center)),
                    ft.DataCell(ft.Container(content=rg, alignment=ft.alignment.center))
                ]
            )
        )

    table_student = ft.DataTable(
        border=ft.border.all(2, ft.Colors.PRIMARY),
        border_radius=8,
        vertical_lines=ft.border.BorderSide(3, ft.Colors.SECONDARY),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.SECONDARY_CONTAINER),
        columns=[
            ft.DataColumn(label=ft.Container(
                content=ft.Text("Student Name"),
                alignment=ft.alignment.center,
                width=150
            )),
            ft.DataColumn(label=ft.Container(
                content=ft.Text("Status"),
                alignment=ft.alignment.center,
                width=150
            ))
        ],
        rows=table_rows,
    )

    submit_button.on_click = handle_submit
    check_button.on_click = handle_check

    button_group = ft.Container(
        content=ft.Row(
            controls=[
                submit_button,
                check_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.title = "Check Status Student"
    page.window.width = 500
    page.window.height = 700

    page.add(
        ft.Container(content=table_student, alignment=ft.alignment.center, padding=20),
        button_group
    )

ft.app(main)
