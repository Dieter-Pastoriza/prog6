import flet as ft

def main(page):
    page.scroll = True
    page.title = "Karate Store"
    page.window_center()
    page.window_height = 400
    page.window_width = 600
    page.horizontal_alignment = 'CENTER'
    page.bgcolor = "#2C2F33"


    new_task = ft.TextField(hint_text="¿Qué necesitas?", width=300, bgcolor="#3A3D5E", color="#F8F9FA")

    # Función para agregar un producto
    def add_clicked(e):
        if new_task.value:  # Verificar que el campo no esté vacío
            checkbox = ft.Checkbox(label=new_task.value, value=False)
            item_row = ft.Row(controls=[
                checkbox,
                ft.ElevatedButton("Modificar", on_click=lambda e: edit_task(checkbox), bgcolor="#98D8AA", color="#FFFFFF"),
                ft.ElevatedButton("Eliminar", on_click=lambda e: delete_task(item_row),  bgcolor="#EE4E4E",color="#FFFFFF")
            ])
            page.controls.append(item_row)  
            new_task.value = ""
            new_task.focus()
            page.update()

    # Función para modificar un producto seleccionado
    def edit_task(checkbox):
        if not checkbox.value:
            print("Debe seleccionar el producto para modificarlo.")
            return  

        # Crear un campo de texto con el valor actual del checkbox
        edit_field = ft.TextField(value=checkbox.label, expand=True, bgcolor="#23272A", color="#EDEDED")

        # Función para guardar los cambios
        def save_task(e):
            checkbox.label = edit_field.value  # Cambiar el texto del checkbox
            edit_dialog.open = False  
            page.update()

        # Crear el diálogo de edición
        save_button = ft.TextButton("Guardar", on_click=save_task)
        edit_dialog = ft.AlertDialog(
            title=ft.Text("Editar tarea",color="#F0A500"),
            content=edit_field,
            actions=[save_button],
            on_dismiss=lambda e: print("Dialog cerrado")
        )
        page.dialog = edit_dialog
        edit_dialog.open = True 
        page.update()

    # Función para eliminar un producto
    def delete_task(item_row):
        page.controls.remove(item_row) 
        page.update()

    # Función para limpiar todos los productos
    def clear_all(e):
        page.controls = [
            control for control in page.controls
            if not (isinstance(control, ft.Row) and isinstance(control.controls[0], ft.Checkbox))
        ]
        page.update()
    logo = ft.Image(src="./tiendakarate.jpg", height=200)
    header_text = ft.Text("Bienvenidos a Dieter Sensei-Store", size=20, weight=ft.FontWeight.BOLD, color="#F0A500")
    header = ft.Column(controls=[logo, header_text], alignment="center")

    page.add(
        header,
        ft.Divider(height=20),
        ft.Row(controls=[new_task, ft.ElevatedButton("Agregar", on_click=add_clicked, bgcolor="#FABC3F", color="#FFFFFF")]),
        ft.Row([ft.Text(value="Limpiar Productos", color="#F8F9FA"), 
                ft.ElevatedButton("Limpiar", on_click=clear_all,bgcolor="#FF7043", color="#FFFFFF")]) 
    )
    page.update()
ft.app(main)
