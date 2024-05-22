import tkinter as tk
from config import *
from tkinter import messagebox
from tkinter import ttk

class HomeView:

    def __init__(self, window, service, user) -> None:
        window.destroy()
        self.__window = tk.Tk()
        self.__service = service
        self.__user = user
        self.__configure_window()
        self.__setup_menu_bar()
        self.__frame_home_view = tk.Frame(master = self.__window, background = background_color_home)
        self.__frame_add_product = tk.Frame(master = self.__window, background = background_color_add_product)
        self.__show_home_view()

    def __configure_window(self):
        self.__window.geometry(window_size)
        self.__window.title("App Sqlite3 | Home")
        self.__window.resizable(width = False, height = False)

    def __setup_menu_bar(self):
        menu_bar = tk.Menu(master = self.__window)
        menu_bar.add_command(label = "Home", command = self.__show_home_view)
        menu_bar.add_command(label = "Add Product", command = self.__show_add_product)
        menu_bar.add_command(label = "Exit", command = self.__exit_window)
        self.__window.config(menu = menu_bar)
        
    def __exit_window(self):
        self.__service.close_conection()
        self.__window.quit()

    def __show_home_view(self):
        self.__frame_home_view.pack(fill = "both", expand = True)
        # Configurar peso de columnas
        self.__frame_home_view.columnconfigure(index = 0, weight = 1)
        self.__frame_home_view.columnconfigure(index = 1, weight = 1)
        self.__frame_home_view.columnconfigure(index = 2, weight = 1)
        self.__frame_home_view.columnconfigure(index = 3, weight = 1)
        self.__frame_home_view.columnconfigure(index = 4, weight = 1)
        self.__frame_home_view.columnconfigure(index = 5, weight = 1)
        # Obtenemos todos los productos de la BD
        all_products = self.__service.get_all_products()
        # Widget Label Titulo
        tk.Label(
            master = self.__frame_home_view,
            text = "Home",
            font = ("Comic Sans", 30, "bold"),
            bg = background_color_home,
            fg = "black",
            pady = 20
        ).grid(row = 0, column = 0, columnspan = 6)
        # Widget Label Correo usuario
        tk.Label(
            master = self.__frame_home_view,
            text = f"Usuario: {self.__user[1]}",
            font = ("Comic Sans", 15, "bold"),
            bg = background_color_home,
            fg = "gray",
            pady = 10
        ).grid(row = 1, column = 0, sticky = "w", padx = 50)
        tk.Label(
            master = self.__frame_home_view,
            text = f"Tabla de Productos:",
            font = ("Comic Sans", 15, "bold"),
            bg = background_color_home,
            fg = "gray",
            pady = 10
        ).grid(row = 2, column = 0, sticky = "w", padx = 50)
        # Treeview -> widget para ver tablas
        if len(all_products) >= 1:
            products_table = ttk.Treeview(
                master = self.__frame_home_view,
                height = 10,
                columns = (1, 2, 3, 4, 5)
            )
            products_table.grid(row = 3, column = 0, pady = 10, columnspan = 6, padx = 20)
            # configurar columns del table
            products_table.column("#0", width=50) 
            products_table.column("#1", width=100)
            products_table.column("#2", width=150)
            products_table.column("#3", width=100)
            products_table.column("#4", width=50)
            products_table.column("#5", width=100)
            # configurar cabeceras de la tabla
            products_table.heading("#0", text = "ID", anchor = "center"),
            products_table.heading("#1", text = "Producto", anchor = "w"),
            products_table.heading("#2", text = "Descripcion", anchor = "w"),
            products_table.heading("#3", text = "Precio", anchor = "w"),
            products_table.heading("#4", text = "Stock", anchor = "w")
            products_table.heading("#5", text = "Fecha Agregado", anchor = "w")
            # agregar data a la talba
            for product in all_products:
                products_table.insert(
                    "",
                    "end",
                    text = product[0],
                    values=(product[1], product[2], product[3], product[4], product[5])
                )
        else:
            # Cuando se cargue la app y no se tenga ni un elemento creado en la tabla productos
            tk.Label(
                master = self.__frame_home_view,
                text = "No tiene productos registrados",
                font = ("Comic Sans", 15, "bold"),
                bg = background_color_home,
                fg = "gray",
            ).grid(row = 3, column = 0, columnspan = 6, pady = 100)
        self.__remove_view(current_view = self.__frame_home_view)

    def __show_add_product(self):
        self.__frame_add_product.pack(fill = "both", expand = True)

        # configurar anchor de columnas
        self.__frame_add_product.columnconfigure(index = 0, weight = 1)
        self.__frame_add_product.columnconfigure(index = 1, weight = 1)
        # Variables de control
        product_name = tk.StringVar()
        product_price = tk.StringVar()
        product_stock = tk.StringVar()
        # Titulo
        tk.Label(
            master = self.__frame_add_product,
            text = "Agregar Producto: ",
            font = title_font,
            bg = background_color_add_product,
            fg = "Black",
            pady = 20
        ).grid(row = 0, column = 0, columnspan = 2, sticky = "w", padx = 30)
        # Nombre
        tk.Label(
            master = self.__frame_add_product,
            text = "Nombre del producto: ",
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
        ).grid(row = 1, column = 0, sticky = "e", pady = 5)
        tk.Entry(
            master = self.__frame_add_product,
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
            background = "white",
            textvariable = product_name
        ).grid(row = 1, column = 1, sticky = "w", pady = 5, padx = 10)
        # Descripcion
        tk.Label(
            master = self.__frame_add_product,
            text = "Descripcion: ",
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
        ).grid(row = 2, column = 0, sticky = "e", pady = 5)
        add_decription_text = tk.Text(
            master = self.__frame_add_product,
            width = 20,
            height = 10,
            font = label_font,
            fg = "black",
            padx = 5,
            pady = 5
        )
        # Precio
        tk.Label(
            master = self.__frame_add_product,
            text = "Precio: ",
            font = label_font,
            bg = background_color_add_product,
            fg = "Black"
        ).grid(row = 3, column = 0, sticky = "e", pady = 5)
        tk.Entry(
            master = self.__frame_add_product,
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
            background = "white",
            textvariable = product_price
        ).grid(row = 3, column = 1, sticky = "w", pady = 5, padx = 10)
        add_decription_text.grid(row = 2, column = 1, sticky = "w", pady = 5, padx = 10)
        # Stock
        tk.Label(
            master = self.__frame_add_product,
            text = "Stock: ",
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
        ).grid(row = 4, column = 0, sticky = "e", pady = 5)
        tk.Entry(
            master = self.__frame_add_product,
            font = label_font,
            bg = background_color_add_product,
            fg = "Black",
            background = "white",
            textvariable = product_stock
        ).grid(row = 4, column = 1, sticky = "w", pady = 5, padx = 10)
        add_decription_text.grid(row = 2, column = 1, sticky = "w", pady = 5, padx = 10)
        # botones
        tk.Button(
            master = self.__frame_add_product,
            text = "Cancelar",
            font = ("Comic Sans", 12, "bold"),
            bg = background_color_button_cancel,
            fg = "white",
            activeforeground = "gray",
            activebackground = "black",
            padx = 10,
            pady = 5,
            command = lambda: self.__remove_text_entry(
                name_variable = product_name,
                description_text = add_decription_text,
                price_variable = product_price,
                stock_variable = product_stock
            )
        ).grid(row = 5, column = 0, sticky = "e", pady = 10, padx =5)
        tk.Button(
            master = self.__frame_add_product,
            text = "Agregar",
            font = ("Comic Sans", 12, "bold"),
            bg = background_color_button_action,
            fg = "white",
            activeforeground = "gray",
            activebackground = "black",
            padx = 10,
            pady = 5,
            command = lambda: self.__save_product(
                name_variable = product_name,
                description_text = add_decription_text,
                price_variable = product_price,
                stock_variable = product_stock
            )
        ).grid(row = 5, column = 1, sticky = "w", pady = 10, padx = 5)

        self.__remove_view(current_view = self.__frame_add_product)

    def __remove_text_entry(self, name_variable, description_text, price_variable, stock_variable):
        name_variable.set("")
        description_text.delete("1.0", "end-1c")
        price_variable.set("")
        stock_variable.set("")

    def __save_product(self, name_variable, description_text, price_variable, stock_variable):
        reuslt = self.__service.add_product(
            name_variable.get(),
            description_text.get("1.0", "end-1c"),
            price_variable.get(),
            stock_variable.get()
        )
        if reuslt == True:
            self.__remove_text_entry(name_variable, description_text, price_variable, stock_variable)
            messagebox.showinfo(
                title = "Registro realizado correctamente!",
                message = "Se realizo correctamente el registro del producto"
            )
            self.__show_home_view()
        else: 
            messagebox.showerror(
                title = "Registro realizado incorrectamente!",
                message = "Verifique correctamente los campos a digitar"
            )

    def __remove_view(self, current_view):
        if current_view == self.__frame_home_view:
            self.__frame_add_product.pack_forget()
        else:
            self.__frame_home_view.pack_forget()