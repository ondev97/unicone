# Main module to handle everything

from tkinter import *
from tkinter import ttk
import tkinter as tk

from backend import Backend
from classes import Model, Manufacturer, Car, Accessory


class FrontEndOne:
    def __init__(self, window):
        self.backend = Backend()
        self.cars_list = []
        self.models = ()
        self.manufacturers = ()
        self.manufacturers_list = []
        self.models_list = []
        self.accessories_list = []
        self.root = window
        self.root.title("FutureARROW Car Sale")
        self.root.geometry("1200x672+50+50")
        self.root.resizable(False, False)

        self.backend.createConnection()
        msg = self.backend.createTables()
        self.title = Label(self.root, text="FutureARROW Car Sale", bd=4, relief=GROOVE,
                      font=("times new roman", 40, "bold"))
        self.title.pack(side=TOP, fill=X)

        self.tabbed_frame = Frame(self.root, bd=4, relief=RIDGE)
        self.tabbed_frame.place(x=0, y=70, width=1198, height=600)

        self.tab_control = ttk.Notebook(self.tabbed_frame)

        tab1 = ttk.Frame(self.tab_control)
        tab2 = ttk.Frame(self.tab_control)
        tab3 = ttk.Frame(self.tab_control)
        tab4 = ttk.Frame(self.tab_control)
        tab5 = ttk.Frame(self.tab_control)

        self.tab_control.add(tab1, text='Manage Cars')
        self.tab_control.add(tab2, text='Manufacturers')
        self.tab_control.add(tab3, text='Car Models')
        self.tab_control.add(tab4, text='Accessories')
        self.tab_control.add(tab5, text='Sales')
        self.tab_control.pack(expand=1, fill="both")

#############################################  Car Tab (Frame) #######################################################

        self.car_manage_frame = Frame(tab1, bd=4, relief=RIDGE)
        self.car_manage_frame.place(x=10, y=10, width=300, height=550)

        self.cmf_title = Label(self.car_manage_frame, text="Manage Cars", font=("times new roman", 15, "bold"))
        self.cmf_title.grid(row=0, columnspan=2, pady=20, padx=30)

        self.car_lbl_reg_no = Label(self.car_manage_frame, text="Reg. No", font=("times new roman", 10))
        self.car_lbl_reg_no.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        self.car_reg_no = StringVar()
        self.car_txt_reg_no = Entry(self.car_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                    textvariable=self.car_reg_no)
        self.car_txt_reg_no.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        self.car_lbl_color = Label(self.car_manage_frame, text="Color", font=("times new roman", 10))
        self.car_lbl_color.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        self.car_color = StringVar()
        self.car_txt_color = Entry(self.car_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                   textvariable=self.car_color)
        self.car_txt_color.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        self.car_lbl_no_of_doors = Label(self.car_manage_frame, text="Doors", font=("times new roman", 10))
        self.car_lbl_no_of_doors.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        self.car_no_of_doors = IntVar()
        self.car_txt_no_of_doors = Entry(self.car_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                         textvariable=self.car_no_of_doors)
        self.car_txt_no_of_doors.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        self.car_lbl_model = Label(self.car_manage_frame, text="Model", font=("times new roman", 10))
        self.car_lbl_model.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        self.car_model = StringVar()
        self.car_combo_model = ttk.Combobox(self.car_manage_frame, font=("times new roman", 10), state="readonly",
                                            textvariable=self.car_model)
        self.car_combo_model.grid(row=4, column=1, padx=20, pady=10, sticky='w')

        self.car_lbl_manufacturer = Label(self.car_manage_frame, text="Manufacturer", font=("times new roman", 10))
        self.car_lbl_manufacturer.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        self.car_manufacturer = StringVar()
        self.car_combo_manufacturer = ttk.Combobox(self.car_manage_frame, font=("times new roman", 10),
                                                   state="readonly", textvariable=self.car_manufacturer)
        self.car_combo_manufacturer.grid(row=5, column=1, padx=20, pady=10, sticky='w')

        self.car_button_frame = Frame(self.car_manage_frame, bd=4)
        self.car_button_frame.place(x=10, y=480, width=270)

        self.car_add_btn = Button(self.car_button_frame, text="Add", width=7, command=self.add_car).grid(row=0,
                                    column=0, padx=10, pady=10)
        self.car_delete_btn = Button(self.car_button_frame, text="Delete", width=7, command=self.delete_car).grid(row=0,
                                    column=1, padx=10, pady=10)
        self.car_clear_btn = Button(self.car_button_frame, text="Clear", width=7, command=self.clear_car).grid(row=0, column=2, padx=10, pady=10)

        self.car_details_frame = Frame(tab1, bd=4, relief=RIDGE)
        self.car_details_frame.place(x=320, y=10, width=860, height=550)

        self.car_lbl_search = Label(self.car_details_frame, text="Search By", font=("times new roman", 10))
        self.car_lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        self.car_combobox = StringVar()
        self.car_combo_search = ttk.Combobox(self.car_details_frame, font=("times new roman", 10), state="readonly", textvariable=self.car_combobox)
        self.car_combo_search['values'] = ("Reg.No", "Color", "Model", "Manufacturer")
        self.car_combo_search.grid(row=0, column=1, padx=20, pady=10)
        self.car_combo_search.current(0)

        self.car_search = StringVar()
        self.car_txt_search = Entry(self.car_details_frame, font=("times new roman", 10), bd=4, relief=GROOVE, textvariable=self.car_search)
        self.car_txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        self.car_search_btn = Button(self.car_details_frame, text="Search", width=10, command=self.set_car_data).grid(row=0, column=3, padx=20, pady=10)
        self.car_showall_btn = Button(self.car_details_frame, text="Show All", width=10, command=self.car_showall).grid(row=0, column=4, padx=20, pady=10)

        self.car_table_frame = Frame(self.car_details_frame, bd=4, relief=RIDGE)
        self.car_table_frame.place(x=10, y=40, width=830, height=490)

        self.car_scroll_y = Scrollbar(self.car_table_frame, orient=VERTICAL)
        self.car_table = ttk.Treeview(self.car_table_frame, columns=("reg_no", "color", "no_of_doors", "model", "manufacturer"), yscrollcommand=self.car_scroll_y.set)
        self.car_scroll_y.pack(side=RIGHT, fill=Y)
        self.car_scroll_y.config(command=self.car_table.yview)
        self.car_table.heading("reg_no", text="Reg.No")
        self.car_table.heading("color", text="Color")
        self.car_table.heading("no_of_doors", text="No Of Doors")
        self.car_table.heading("model", text="Model")
        self.car_table.heading("manufacturer", text="Manufacturer")
        self.car_table['show'] = 'headings'
        self.car_table.column("reg_no", width=100)
        self.car_table.column("color", width=100)
        self.car_table.column("no_of_doors", width=100)
        self.car_table.column("model", width=100)
        self.car_table.column("manufacturer", width=100)
        self.car_table.pack(fill=BOTH, expand=1)

        self.car_table.bind("<Double-1>", self.car_doubleclick)

#############################################  Manufacturer Tab (Frames) #######################################################

        self.manufacturer_manage_frame = Frame(tab2, bd=4, relief=RIDGE)
        self.manufacturer_manage_frame.place(x=10, y=10, width=350, height=550)

        self.mamf_title = Label(self.manufacturer_manage_frame, text="Manage Manufacturers", font=("times new roman", 15, "bold"))
        self.mamf_title.grid(row=0, columnspan=2, pady=20, padx=30)

        self.manufacturer_lbl_id = Label(self.manufacturer_manage_frame, text="Manufacturer Id", font=("times new roman", 10))
        self.manufacturer_lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        self.manufacturer_id = StringVar()
        self.manufacturer_txt_id = Entry(self.manufacturer_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                        textvariable=self.manufacturer_id)
        self.manufacturer_txt_id.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        self.manufacturer_lbl_name = Label(self.manufacturer_manage_frame, text="Name", font=("times new roman", 10))
        self.manufacturer_lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        self.manufacturer_name = StringVar()
        self.manufacturer_txt_name = Entry(self.manufacturer_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                    textvariable=self.manufacturer_name)
        self.manufacturer_txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        self.manufacturer_button_frame = Frame(self.manufacturer_manage_frame, bd=4)
        self.manufacturer_button_frame.place(x=10, y=480, width=320)

        self.manufacturer_add_btn = Button(self.manufacturer_button_frame, text="Add", width=7, command=self.add_manufacturer).grid(row=0, column=0, padx=10, pady=10)
        self.manufacturer_update_btn = Button(self.manufacturer_button_frame, text="Update", width=7, command=self.update_manufacturer).grid(row=0, column=1, padx=10, pady=10)
        self.manufacturer_delete_btn = Button(self.manufacturer_button_frame, text="Delete", width=7, command=self.delete_manufacturer).grid(row=0, column=2, padx=10, pady=10)
        self.manufacturer_clear_btn = Button(self.manufacturer_button_frame, text="Clear", width=7, command=self.clear_manufacturer).grid(row=0, column=3, padx=10, pady=10)

        self.manufacturer_details_frame = Frame(tab2, bd=4, relief=RIDGE)
        self.manufacturer_details_frame.place(x=370, y=10, width=810, height=550)

        self.manufacturer_lbl_search = Label(self.manufacturer_details_frame, text="Search By", font=("times new roman", 10))
        self.manufacturer_lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        self.manufacturer_combobox = StringVar()
        self.manufacturer_combo_search = ttk.Combobox(self.manufacturer_details_frame, font=("times new roman", 10), state="readonly", textvariable=self.manufacturer_combobox)
        self.manufacturer_combo_search['values'] = ("Manufacturer Id", "Name")
        self.manufacturer_combo_search.grid(row=0, column=1, padx=20, pady=10)
        self.manufacturer_combo_search.current(0)

        self.manufacturer_search = StringVar()
        self.manufacturer_txt_search = Entry(self.manufacturer_details_frame, font=("times new roman", 10), bd=4, relief=GROOVE, textvariable=self.manufacturer_search)
        self.manufacturer_txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        self.manufacturer_search_btn = Button(self.manufacturer_details_frame, text="Search", width=10, command=self.set_manufacturer_data).grid(row=0, column=3, padx=20, pady=10)
        self.manufacturer_showall_btn = Button(self.manufacturer_details_frame, text="Show All", width=10, command=self.manufacturer_showall).grid(row=0, column=4, padx=20, pady=10)

        self.manufacturer_table_frame = Frame(self.manufacturer_details_frame, bd=4, relief=RIDGE)
        self.manufacturer_table_frame.place(x=10, y=40, width=780, height=490)

        self.manufacturer_scroll_y = Scrollbar(self.manufacturer_table_frame, orient=VERTICAL)
        self.manufacturer_table = ttk.Treeview(self.manufacturer_table_frame, columns=("manufacturer_id", "name"), yscrollcommand=self.manufacturer_scroll_y.set)
        self.manufacturer_scroll_y.pack(side=RIGHT, fill=Y)
        self.manufacturer_scroll_y.config(command=self.manufacturer_table.yview)
        self.manufacturer_table.heading("manufacturer_id", text="Manufacturer Id")
        self.manufacturer_table.heading("name", text="Name")
        self.manufacturer_table['show'] = 'headings'
        self.manufacturer_table.pack(fill=BOTH, expand=1)

        self.manufacturer_table.bind("<Double-1>", self.manufacturer_doubleclick)

#############################################  Model Tab (Frame) #######################################################

        self.model_manage_frame = Frame(tab3, bd=4, relief=RIDGE)
        self.model_manage_frame.place(x=10, y=10, width=350, height=550)

        self.mmf_title = Label(self.model_manage_frame, text="Manage Models",
                        font=("times new roman", 15, "bold"))
        self.mmf_title.grid(row=0, columnspan=2, pady=20, padx=30)

        self.model_lbl_model_no = Label(self.model_manage_frame, text="Model No.", font=("times new roman", 10))
        self.model_lbl_model_no.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        self.model_model_no = StringVar()
        self.model_txt_model_no = Entry(self.model_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE, textvariable=self.model_model_no)
        self.model_txt_model_no.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        self.model_lbl_name = Label(self.model_manage_frame, text="Name", font=("times new roman", 10))
        self.model_lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        self.model_name = StringVar()
        self.model_txt_name = Entry(self.model_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE, textvariable=self.model_name)
        self.model_txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        self.model_price = DoubleVar()
        self.model_lbl_price = Label(self.model_manage_frame, text="Price", font=("times new roman", 10))
        self.model_lbl_price.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        self.model_txt_price = Entry(self.model_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE, textvariable=self.model_price)
        self.model_txt_price.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        self.model_button_frame = Frame(self.model_manage_frame, bd=4)
        self.model_button_frame.place(x=10, y=480, width=320)

        self.model_add_btn = Button(self.model_button_frame, text="Add", width=7, command=self.add_model).grid(row=0, column=0, padx=10, pady=10)
        self.model_update_btn = Button(self.model_button_frame, text="Update", width=7, command=self.update_model).grid(row=0, column=1, padx=10, pady=10)
        self.model_delete_btn = Button(self.model_button_frame, text="Delete", width=7, command=self.delete_model).grid(row=0, column=2, padx=10, pady=10)
        self.model_clear_btn = Button(self.model_button_frame, text="Clear", width=7, command=self.clear_model).grid(row=0, column=3, padx=10, pady=10)

        self.model_details_frame = Frame(tab3, bd=4, relief=RIDGE)
        self.model_details_frame.place(x=370, y=10, width=810, height=550)

        self.lbl_search = Label(self.model_details_frame, text="Search By", font=("times new roman", 10))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        self.model_combobox = StringVar()
        self.combo_search = ttk.Combobox(self.model_details_frame, font=("times new roman", 10), state="readonly", textvariable=self.model_combobox)
        self.combo_search['values'] = ("Model No", "Name")
        self.combo_search.grid(row=0, column=1, padx=20, pady=10)
        self.combo_search.current(0)

        self.model_search = StringVar()
        self.txt_search = Entry(self.model_details_frame, font=("times new roman", 10), bd=4, relief=GROOVE, textvariable=self.model_search)
        self.txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        self.search_btn = Button(self.model_details_frame, text="Search", width=10, command=self.set_model_data).grid(row=0, column=3, padx=20, pady=10)
        self.showall_btn = Button(self.model_details_frame, text="Show All", width=10, command=self.model_showall).grid(row=0, column=4, padx=20, pady=10)

        self.model_table_frame = Frame(self.model_details_frame, bd=4, relief=RIDGE)
        self.model_table_frame.place(x=10, y=40, width=780, height=490)

        self.model_scroll_y = Scrollbar(self.model_table_frame, orient=VERTICAL)
        self.model_table = ttk.Treeview(self.model_table_frame, columns=("model_no", "name", "price"), yscrollcommand=self.model_scroll_y.set)
        self.model_scroll_y.pack(side=RIGHT, fill=Y)
        self.model_scroll_y.config(command=self.model_table.yview)
        self.model_table.heading("model_no", text="Model No")
        self.model_table.heading("name", text="Name")
        self.model_table.heading("price", text="Price")
        self.model_table['show'] = 'headings'
        self.model_table.pack(fill=BOTH, expand=1)

        self.model_table.bind("<Double-1>", self.model_doubleclick)

#############################################  Accessories Tab (Frame)  #############################################

        self.accessory_manage_frame = Frame(tab4, bd=4, relief=RIDGE)
        self.accessory_manage_frame.place(x=10, y=10, width=350, height=550)

        self.amf_title = Label(self.accessory_manage_frame, text="Manage Accessories",
                               font=("times new roman", 15, "bold"))
        self.amf_title.grid(row=0, columnspan=2, pady=20, padx=30)

        self.accessory_lbl_id = Label(self.accessory_manage_frame, text="Id", font=("times new roman", 10))
        self.accessory_lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        self.accessory_id = StringVar()
        self.accessory_txt_id = Entry(self.accessory_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                        textvariable=self.accessory_id)
        self.accessory_txt_id.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        self.accessory_lbl_name = Label(self.accessory_manage_frame, text="Name", font=("times new roman", 10))
        self.accessory_lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        self.accessory_name = StringVar()
        self.accessory_txt_name = Entry(self.accessory_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                    textvariable=self.accessory_name)
        self.accessory_txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        self.accessory_price = DoubleVar()
        self.accessory_lbl_price = Label(self.accessory_manage_frame, text="Price", font=("times new roman", 10))
        self.accessory_lbl_price.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        self.accessory_txt_price = Entry(self.accessory_manage_frame, font=("times new roman", 10), bd=5, relief=GROOVE,
                                     textvariable=self.accessory_price)
        self.accessory_txt_price.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        self.accessory_button_frame = Frame(self.accessory_manage_frame, bd=4)
        self.accessory_button_frame.place(x=10, y=480, width=320)

        self.accessory_add_btn = Button(self.accessory_button_frame, text="Add", width=7, command=self.add_accessory).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10)
        self.accessory_update_btn = Button(self.accessory_button_frame, text="Update", width=7, command=self.update_accessory).grid(
            row=0, column=1, padx=10, pady=10)
        self.accessory_delete_btn = Button(self.accessory_button_frame, text="Delete", width=7, command=self.delete_accessory).grid(
            row=0, column=2, padx=10, pady=10)
        self.accessory_clear_btn = Button(self.accessory_button_frame, text="Clear", width=7, command=self.clear_accessory).grid(
            row=0, column=3, padx=10, pady=10)

        self.accessory_details_frame = Frame(tab4, bd=4, relief=RIDGE)
        self.accessory_details_frame.place(x=370, y=10, width=810, height=550)

        self.accessory_lbl_search = Label(self.accessory_details_frame, text="Search By", font=("times new roman", 10))
        self.accessory_lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        self.accessory_combobox = StringVar()
        self.accessory_combo_search = ttk.Combobox(self.accessory_details_frame, font=("times new roman", 10), state="readonly",
                                         textvariable=self.accessory_combobox)
        self.accessory_combo_search['values'] = ("Id", "Name")
        self.accessory_combo_search.grid(row=0, column=1, padx=20, pady=10)
        self.accessory_combo_search.current(0)

        self.accessory_search = StringVar()
        self.accessory_txt_search = Entry(self.accessory_details_frame, font=("times new roman", 10), bd=4, relief=GROOVE,
                                textvariable=self.accessory_search)
        self.accessory_txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        self.accessory_search_btn = Button(self.accessory_details_frame, text="Search", width=10, command=self.set_accessory_data).grid(
            row=0, column=3, padx=20, pady=10)
        self.accessory_showall_btn = Button(self.accessory_details_frame, text="Show All", width=10, command=self.accessory_showall).grid(
            row=0, column=4, padx=20, pady=10)

        self.accessory_table_frame = Frame(self.accessory_details_frame, bd=4, relief=RIDGE)
        self.accessory_table_frame.place(x=10, y=40, width=780, height=490)

        self.accessory_scroll_y = Scrollbar(self.accessory_table_frame, orient=VERTICAL)
        self.accessory_table = ttk.Treeview(self.accessory_table_frame, columns=("id", "name", "price"),
                                        yscrollcommand=self.accessory_scroll_y.set)
        self.accessory_scroll_y.pack(side=RIGHT, fill=Y)
        self.accessory_scroll_y.config(command=self.accessory_table.yview)
        self.accessory_table.heading("id", text="Id")
        self.accessory_table.heading("name", text="Name")
        self.accessory_table.heading("price", text="Price")
        self.accessory_table['show'] = 'headings'
        self.accessory_table.pack(fill=BOTH, expand=1)

        self.accessory_table.bind("<Double-1>", self.accessory_doubleclick)

##############################################  Sales Tab (Frame) #####################################################

        self.sale_details_frame = Frame(tab5, bd=4, relief=RIDGE)
        self.sale_details_frame.place(x=10, y=10, width=1165, height=350)

##############################################  Method Calls #####################################################
        self.set_manufacturer_data()
        self.set_car_data()
        self.set_model_data()
        self.set_accessory_data()
        self.set_car_models()
        self.set_car_manufacturers()
        if msg=="tables were successfully created":
            self.popupmsg("Welcome To FutureARROW Car Sale System")

#############################################  Car Methods #######################################################

    def car_showall(self):
        self.car_search.set("")
        self.set_car_data()

    def add_car(self):
        model = None
        manufacturer = None
        for m in self.models_list:
            if m.getModelNo()==self.car_model.get():
                model = m
        for m in  self.manufacturers_list:
            if m.getId()==self.car_manufacturer.get():
                manufacturer = m
        car = Car(self.car_reg_no.get().strip(), self.car_color.get().strip(), self.car_no_of_doors.get(), model, manufacturer)
        msg = self.backend.addCar(car)
        self.set_car_data()
        self.popupmsg(msg)

    def delete_car(self):
        model = None
        manufacturer = None
        for m in self.models_list:
            if m.getModelNo() == self.car_model.get():
                model = m
        for m in self.manufacturers_list:
            if m.getId() == self.car_manufacturer.get():
                manufacturer = m
        car = Car(self.car_reg_no.get().strip(), self.car_color.get().strip(), self.car_no_of_doors.get(), model, manufacturer)
        msg = self.backend.removeCar(car)
        self.set_car_data()
        self.popupmsg(msg)

    def clear_car(self):
        self.car_reg_no.set("")
        self.car_color.set("")
        self.car_no_of_doors.set(0)
        self.car_model.set("")
        self.car_manufacturer.set("")

    def set_car_models(self):
        models = []
        for model in self.models_list:
            models.append(model.getModelNo())
        self.models = tuple(models)
        self.car_combo_model['values'] = self.models

    def set_car_manufacturers(self):
        manufacturers = []
        for manufacturer in self.manufacturers_list:
            manufacturers.append(manufacturer.getId())
        self.manufacturers = tuple(manufacturers)
        self.car_combo_manufacturer['values'] = self.manufacturers

    def car_doubleclick(self,event):
        item = self.car_table.selection()
        for i in item:
            for c in self.cars_list:
                if c.getRegNo() == self.car_table.item(i, "values")[0]:
                    self.car_reg_no.set(c.getRegNo())
                    self.car_color.set(c.getColor())
                    self.car_no_of_doors.set(c.getNoOfDoors())
                    self.car_combo_model.current(self.models.index(c.getModel().getModelNo()))
                    self.car_combo_manufacturer.current(self.manufacturers.index(c.getManufacturer().getId()))

    def set_car_data(self):
        search_by = self.car_combobox.get()
        condition = self.car_search.get().strip()
        self.cars_list = self.backend.viewCars("")
        self.car_table.delete(*self.car_table.get_children())
        for car in self.cars_list:
            if search_by=="Reg.No":
                if condition=="":
                    self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
                else:
                    if car.getRegNo().find(condition)!=-1:
                        self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
            elif search_by=="Color":
                if condition=="":
                    self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
                else:
                    if car.getColor().find(condition)!=-1:
                        self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
            elif search_by=="Model":
                if condition=="":
                    self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
                else:
                    if car.getModel().getModelNo().find(condition)!=-1:
                        self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
            elif search_by=="Manufacturer":
                if condition=="":
                    self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
                else:
                    if car.getManufacturer().getId().find(condition)!=-1:
                        self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))
            else:
                self.car_table.insert("", tk.END, values=(car.getRegNo(), car.getColor(), car.getNoOfDoors(), car.getModel().getModelNo(), car.getManufacturer().getId()))


#############################################  Manufacturer Methods #######################################################

    def set_manufacturer_data(self):
        search_by = self.manufacturer_combobox.get()
        condition = self.manufacturer_search.get().strip()
        self.manufacturers_list = self.backend.viewManufacturers("")
        self.manufacturer_table.delete(*self.manufacturer_table.get_children())
        for manufacturer in self.manufacturers_list:
            if search_by=="Manufacturer Id":
                if condition=="":
                    self.manufacturer_table.insert("", tk.END, values=(manufacturer.getId(), manufacturer.getName()))
                else:
                    if manufacturer.getId().find(condition)!=-1:
                        self.manufacturer_table.insert("", tk.END, values=(manufacturer.getId(), manufacturer.getName()))
            elif search_by=="Name":
                if condition=="":
                    self.manufacturer_table.insert("", tk.END, values=(manufacturer.getId(), manufacturer.getName()))
                else:
                    if manufacturer.getName().find(condition)!=-1:
                        self.manufacturer_table.insert("", tk.END, values=(manufacturer.getId(), manufacturer.getName()))
            else:
                self.manufacturer_table.insert("", tk.END, values=(manufacturer.getId(), manufacturer.getName()))

    def add_manufacturer(self):
        manufacturer = Manufacturer(self.manufacturer_id.get().strip(), self.manufacturer_name.get().strip())
        msg = self.backend.addManufacturer(manufacturer)
        self.set_manufacturer_data()
        self.set_car_manufacturers()
        self.popupmsg(msg)

    def update_manufacturer(self):
        manufacturer = Manufacturer(self.manufacturer_id.get().strip(), self.manufacturer_name.get().strip())
        msg = self.backend.updateManufacturer(manufacturer)
        self.set_manufacturer_data()
        self.set_car_manufacturers()
        self.popupmsg(msg)

    def delete_manufacturer(self):
        manufacturer = Manufacturer(self.manufacturer_id.get().strip(), self.manufacturer_name.get().strip())
        msg = self.backend.removeManufacturer(manufacturer)
        self.set_manufacturer_data()
        self.clear_manufacturer()
        self.set_car_manufacturers()
        self.popupmsg(msg)

    def clear_manufacturer(self):
        self.manufacturer_id.set("")
        self.manufacturer_name.set("")

    def manufacturer_showall(self):
        self.manufacturer_search.set("")
        self.set_manufacturer_data()

    def manufacturer_doubleclick(self,event):
        item = self.manufacturer_table.selection()
        for i in item:
            for m in self.manufacturers_list:
                if m.getId() == self.manufacturer_table.item(i, "values")[0]:
                    self.manufacturer_id.set(m.getId())
                    self.manufacturer_name.set(m.getName())

#############################################  Model Methods #######################################################

    def model_doubleclick(self,event):
        item = self.model_table.selection()
        for i in item:
            for m in self.models_list:
                if m.getModelNo() == self.model_table.item(i, "values")[0]:
                    self.model_model_no.set(m.getModelNo())
                    self.model_name.set(m.getName())
                    self.model_price.set(m.getPrice())

    def set_model_data(self):
        search_by = self.model_combobox.get()
        condition = self.model_search.get().strip()
        self.models_list = self.backend.viewModels("")
        self.model_table.delete(*self.model_table.get_children())
        for model in self.models_list:
            if search_by=="Name":
                if condition=="":
                    self.model_table.insert("", tk.END, values=(model.getModelNo(), model.getName(), model.getPrice()))
                else:
                    if model.getName().find(condition)!=-1:
                        self.model_table.insert("", tk.END, values=(model.getModelNo(), model.getName(), model.getPrice()))
            elif search_by=="Model No":
                if condition=="":
                    self.model_table.insert("", tk.END, values=(model.getModelNo(), model.getName(), model.getPrice()))
                else:
                    if model.getModelNo().find(condition)!=-1:
                        self.model_table.insert("", tk.END, values=(model.getModelNo(), model.getName(), model.getPrice()))
            else:
                self.model_table.insert("", tk.END, values=(model.getModelNo(), model.getName(), model.getPrice()))

    def add_model(self):
        model = Model(self.model_model_no.get().strip(), self.model_name.get().strip(), round(self.model_price.get(),2))
        msg = self.backend.addModel(model)
        self.set_model_data()
        self.set_car_models()
        self.popupmsg(msg)

    def update_model(self):
        model = Model(self.model_model_no.get().strip(), self.model_name.get().strip(), round(self.model_price.get(),2))
        msg = self.backend.updateModel(model)
        self.set_model_data()
        self.set_car_models()
        self.popupmsg(msg)

    def delete_model(self):
        model = Model(self.model_model_no.get().strip(), self.model_name.get().strip(), round(self.model_price.get(),2))
        msg = self.backend.removeModel(model)
        self.set_model_data()
        self.set_car_models()
        self.clear_model()
        self.popupmsg(msg)

    def clear_model(self):
        self.model_model_no.set("")
        self.model_name.set("")
        self.model_price.set(0)

    def model_showall(self):
        self.model_search.set("")
        self.set_model_data()

#############################################  Accessory Methods #######################################################

    def add_accessory(self):
        accessory = Accessory(self.accessory_id.get().strip(), self.accessory_name.get().strip(), round(self.accessory_price.get(), 2))
        msg = self.backend.addAccessory(accessory)
        self.set_accessory_data()
        self.popupmsg(msg)

    def delete_accessory(self):
        accessory = Accessory(self.accessory_id.get().strip(), self.accessory_name.get().strip(), round(self.accessory_price.get(), 2))
        msg = self.backend.removeAccessory(accessory)
        self.set_accessory_data()
        self.popupmsg(msg)

    def update_accessory(self):
        accessory = Accessory(self.accessory_id.get().strip(), self.accessory_name.get().strip(), round(self.accessory_price.get(), 2))
        msg = self.backend.updateAccessory(accessory)
        self.set_accessory_data()
        self.popupmsg(msg)

    def clear_accessory(self):
        self.accessory_id.set("")
        self.accessory_name.set("")
        self.accessory_price.set(0)

    def accessory_showall(self):
        self.accessory_search.set("")
        self.set_accessory_data()

    def set_accessory_data(self):
        search_by = self.accessory_combobox.get()
        condition = self.accessory_search.get().strip()
        self.accessories_list = self.backend.viewAccessories("")
        self.accessory_table.delete(*self.accessory_table.get_children())
        for accessory in self.accessories_list:
            if search_by == "Name":
                if condition == "":
                    self.accessory_table.insert("", tk.END, values=(accessory.getId(), accessory.getName(), accessory.getPrice()))
                else:
                    if accessory.getName().find(condition) != -1:
                        self.accessory_table.insert("", tk.END, values=(accessory.getId(), accessory.getName(), accessory.getPrice()))
            elif search_by == "Id":
                if condition == "":
                    self.accessory_table.insert("", tk.END, values=(accessory.getId(), accessory.getName(), accessory.getPrice()))
                else:
                    if accessory.getId().find(condition) != -1:
                        self.accessory_table.insert("", tk.END, values=(accessory.getId(), accessory.getName(), accessory.getPrice()))
            else:
                self.accessory_table.insert("", tk.END, values=(accessory.getId(), accessory.getName(),
                                                                accessory.getPrice()))

    def accessory_doubleclick(self, event):
        item = self.accessory_table.selection()
        for i in item:
            for a in self.accessories_list:
                if a.getId() == self.accessory_table.item(i, "values")[0]:
                    self.accessory_id.set(a.getId())
                    self.accessory_name.set(a.getName())
                    self.accessory_price.set(a.getPrice())

#############################################  Sale Methods #########################################################

    def clear_sale(self):
        pass

    def accessory_sale(self):
        pass

    def set_accessory_sale(self):
        pass

    def sale_doubleclick(self):
        pass

#############################################  Common Methods #######################################################

    @staticmethod
    def popupmsg(msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=("times new roman", 10))
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        b1.pack()
        popup.resizable(False, False)

        windowwidth = popup.winfo_reqwidth()
        windowheight = popup.winfo_reqheight()
        print("Width", windowwidth, "Height", windowheight)
        positionright = int(popup.winfo_screenwidth() / 2 - windowwidth / 2)
        positiondown = int(popup.winfo_screenheight() / 2 - windowheight / 2)
        popup.geometry("+{}+{}".format(positionright, positiondown))

        popup.mainloop()


root = Tk()
ob = FrontEndOne(root)
root.mainloop()
