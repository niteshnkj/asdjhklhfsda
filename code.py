from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import cx_Oracle
date = datetime.datetime.now().date()
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
conn = cx_Oracle.connect(user=r'system', password='nimisha123',
dsn=dsn_tns)
my_cursor = conn.cursor()
result =
id_pro =
for r in
id =
my_cursor.execute('select Max(id) from dept')
my_cursor.execute('select id from dept')
result:
r[0]
# temporary lists
products_list = []
product_price = []
product_quantity = []
product_id = []
# list for labels
labels_list = []
class Hospital:
def __init__(self, root):
self.root = root
self.root.title("Department Store Management System")
self.root.geometry("1540x800+0+0")
lbltitle = Label(self.root, bd=20, relief=RIDGE, text='DEPARTMENT
STORE MANAGEMENT SYSTEM', fg="white",
bg="SteelBlue",
font=("times new roman", 45, "bold"))
lbltitle.pack(side=TOP, fill=X)
# var
self.name_var = StringVar()
self.stock_var = StringVar()
self.cp_var = StringVar()
self.sp_var = StringVar()
self.totalcp_var = StringVar()
self.totalsp_var = StringVar()
self.vendor_var = StringVar()
self.vendor_phone_var = StringVar()
self.id_var = StringVar()
# DATA FRAMEDataFrame = Frame(self.root, bd=20, relief=RIDGE, bg="steelblue")
DataFrame.place(x=0, y=130, width=1530, height=400)
dataframeLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
font=("times new roman", 12, "bold"),
text="Add Products")
dataframeLeft.place(x=0, y=5, width=980, height=350)
dataframeRight = LabelFrame(DataFrame, bd=10, relief=RIDGE,
padx=10, font=("times new roman", 12, "bold"),
text="Product Information")
dataframeRight.place(x=990, y=5, width=460, height=350)
# DETAILS FRAME
detailsFrame = Frame(self.root, bd=20, relief=RIDGE)
detailsFrame.place(x=0, y=600, width=1530, height=190)
# labels and entries of window
self.name_l = Label(dataframeLeft, text="Enter Product Name: ",
font='arial 17 bold', padx=2, pady=6)
self.name_l.grid(row=0, column=0, sticky=W)
self.stock_l = Label(dataframeLeft, text="Enter Stocks: ",
font='arial 17 bold', padx=2, pady=6)
self.stock_l.grid(row=1, column=0, sticky=W)
self.cp_l = Label(dataframeLeft, text="Enter Cost Price: ",
font='arial 17 bold', padx=2, pady=6)
self.cp_l.grid(row=2, column=0, sticky=W)
self.sp_l = Label(dataframeLeft, text="Enter Selling Price: ",
font='arial 17 bold', padx=2, pady=6)
self.sp_l.grid(row=3, column=0, sticky=W)
self.vendor_l = Label(dataframeLeft, text="Enter Vendor Name: ",
font='arial 17 bold', padx=2, pady=6)
self.vendor_l.grid(row=4, column=0, sticky=W)
self.vendor_phone_l = Label(dataframeLeft, text="Enter Vendor phone
no: ", font='arial 17 bold', padx=2, pady=6)
self.vendor_phone_l.grid(row=5, column=0, sticky=W)
self.id_l = Label(dataframeLeft, text="Enter Product ID: ",
font='arial 17 bold', padx=2, pady=6)
self.id_l.grid(row=6, column=0, sticky=W)
# entries for the label
self.name_e = Entry(dataframeLeft, width=25, font='arial 16',
textvariable=self.name_var)
self.name_e.grid(row=0, column=1)
self.stock_e = Entry(dataframeLeft, width=25, font='arial 16',
textvariable=self.stock_var)
self.stock_e.grid(row=1, column=1)
self.cp_e = Entry(dataframeLeft, width=25, font='arial 16',
textvariable=self.cp_var)
self.cp_e.grid(row=2, column=1)
self.sp_e = Entry(dataframeLeft, width=25, font='arial 16',textvariable=self.sp_var)
self.sp_e.grid(row=3, column=1)
self.vendor_e = Entry(dataframeLeft, width=25, font='arial 16',
textvariable=self.vendor_var)
self.vendor_e.grid(row=4, column=1)
self.vendor_phone_e = Entry(dataframeLeft, width=25, font='arial
16', textvariable=self.vendor_phone_var)
self.vendor_phone_e.grid(row=5, column=1)
self.id_e = Entry(dataframeLeft, width=25, font='arial 16',
textvariable=self.id_var)
self.id_e.grid(row=6, column=1)
# button frame
ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
ButtonFrame.place(x=0, y=530, width=1530, height=70)
# DETAILS FRAME
detailsFrame = Frame(self.root, bd=20, relief=RIDGE)
detailsFrame.place(x=0, y=600, width=1530, height=190)
# button to add to the database
self.btn_add = Button(ButtonFrame, text="Add to Database",
width=28, bg='steelblue', fg='white',
command=self.get_items, padx=3, pady=6)
self.btn_add.grid(row=0, column=0)
self.btn_clear = Button(ButtonFrame, text="Clear All Fields",
width=28, bg="steelblue", fg='white',
command=self.clear, padx=3, pady=6)
self.btn_clear.grid(row=0, column=1)
self.btn_search = Button(ButtonFrame, command=self.search,
text="Search", width=28, bg="steelblue", fg='white',
padx=3, pady=6)
self.btn_search.grid(row=0, column=2)
self.btn_update = Button(ButtonFrame, command=self.update,
text="Update", width=28, bg="steelblue", fg='white',
padx=3, pady=6)
self.btn_update.grid(row=0, column=3)
self.btn_bill = Button(ButtonFrame, text="Buy Product",
command=self.open, width=28, bg="steelblue",
fg='white', padx=3, pady=6,
)
self.btn_bill.grid(row=0, column=4)
self.btn_delete = Button(ButtonFrame, text="Delete", width=28,
bg="steelblue", fg='white', padx=3, pady=6,
command=self.delete_record)
self.btn_delete.grid(row=0, column=5)self.btn_exit = Button(ButtonFrame, text="Exit", width=28,
bg="steelblue", fg='white', padx=3, pady=6,
command=self.exit)
self.btn_exit.grid(row=0, column=6)
# text box for the logs
self.tBox = Text(dataframeRight, width=60, height=18, font='arial
13')
self.tBox.grid(row=0, column=0)
# self.tBox.insert(END, "ID has reached upto: " + str(id))
# information frame
department_frame = Frame(detailsFrame, bd=6, relief=RIDGE, padx=20,
bg="steelblue")
department_frame.place(x=0, y=2, width=1490, height=160)
# xscroll = ttk.Scrollbar(department_frame, orient=HORIZONTAL)
yscroll = ttk.Scrollbar(department_frame, orient=VERTICAL)
self.dept_table = ttk.Treeview(department_frame, column=(
"Id", "ProductName", "stock", "cp", "sp", "Vendor", "totalSp",
"totalCp", "AssumedProfit", "VendorPhoneno"),yscrollcommand=yscroll.set)
# xscroll.pack(side=BOTTOM, fill=X)
yscroll.pack(side=RIGHT, fill=Y)
# xscroll.config(command=self.dept_table.xview)
yscroll.config(command=self.dept_table.yview)
self.dept_table.heading("Id", text="Product Id")
self.dept_table.heading("ProductName", text="Product Name")
self.dept_table.heading("stock", text="Stock")
self.dept_table.heading("cp", text="Cost Price")
self.dept_table.heading("sp", text="Selling Price")
self.dept_table.heading("Vendor", text="Vendor Name")
self.dept_table.heading("totalSp", text="Total Selling Price")
self.dept_table.heading("totalCp", text="Total Cost Price")
self.dept_table.heading("AssumedProfit", text="Assumed Profit")
self.dept_table.heading("VendorPhoneno", text="Vendor Phone no")
self.dept_table["show"] = "headings"
self.dept_table.pack(fill=BOTH, expand=1)
self.dept_table.column("ProductName", width=100)
self.dept_table.column("stock", width=100)
self.dept_table.column("cp", width=100)
self.dept_table.column("sp", width=100)
self.dept_table.column("Vendor", width=100)
self.dept_table.column("totalSp", width=100)
self.dept_table.column("totalCp", width=100)
self.dept_table.column("AssumedProfit", width=100)
self.dept_table.column("VendorPhoneno", width=100)
self.fetch_data()
self.dept_table.bind("<ButtonRelease-1>", self.get_cursor)
# functionality declarationsdef get_items(self):
self.name = self.name_e.get()
self.stock = self.stock_e.get()
self.cp = self.cp_e.get()
self.sp = self.sp_e.get()
self.vendor = self.vendor_e.get()
self.vendor_phone = self.vendor_phone_e.get()
# dynamic entries
self.totalcp = float(self.cp) * float(self.stock)
self.totalsp = float(self.sp) * float(self.stock)
self.assumed_profit = float(self.totalcp - self.totalsp)
if self.name == '' or self.stock == '' or self.cp == '' or self.sp
== '':
messagebox.showinfo('Error', 'Please Fill all the Entries')
else:
new = [(self.name, self.stock, self.cp, self.sp, self.vendor,
self.totalsp, self.totalcp,
self.assumed_profit, self.vendor_phone)]
my_cursor.executemany(
"insert into dept (name, stock, cp, sp, vendor, totalsp,
totalcp, assumed_profit, vendor_phoneno)
values(:1,:2,:3,:4,:5,:6,:7,:8,:9)",
new)
conn.commit()
self.fetch_data()
self.tBox.insert(END,
"Inserted " + str(self.name) + " into the
database with code " + str(self.id_e.get())+"\n\n")
self.tBox.insert(END,"Product Id:\t\t\t"+self.id_e.get()+"\n")
self.tBox.insert(END, "Product Name:\t\t\t" + self.name_e.get()
+ "\n")
self.tBox.insert(END, "Cost Price:\t\t\t" + self.cp_e.get() +
"\n")
self.tBox.insert(END, "Sell Price:\t\t\t" + self.sp_e.get() +
"\n")
self.tBox.insert(END, "Vendor:\t\t\t" + self.vendor_e.get() +
"\n")
self.tBox.insert(END, "Vendor Phoneno:\t\t\t" +
self.vendor_phone_e.get() + "\n")
messagebox.showinfo('Success', 'Successfully added to the
database')
def clear(self):
self.name_e.delete(0, END)
self.stock_e.delete(0, END)
self.cp_e.delete(0, END)
self.sp_e.delete(0, END)
self.vendor_e.delete(0, END)
self.vendor_phone_e.delete(0, END)
self.id_e.delete(0, END)
def fetch_data(self):
my_cursor.execute("select * from dept")
rows = my_cursor.fetchall()
if len(rows) != 0:self.dept_table.delete(*self.dept_table.get_children())
for i in rows:
self.dept_table.insert("", END, values=i)
conn.commit()
def get_cursor(self, event=""):
cursor_rows = self.dept_table.focus()
content = self.dept_table.item(cursor_rows)
row = content['values']
self.id_var.set(row[0])
self.name_var.set(row[1])
self.stock_var.set(row[2])
self.cp_var.set(row[3])
self.sp_var.set(row[4])
self.vendor_var.set(row[5])
self.vendor_phone_var.set(row[9])
def exit(self):
exit = messagebox.askyesno("Department store management system",
"Are you Sure You want to exit?")
if exit > 0:
self.root.destroy()
return
def search(self):
sql = "select * from dept where id = :1"
res = my_cursor.execute(sql, (self.id_e.get(),))
for r in res:
self.name_var.set(r[1])
self.stock_var.set(r[2])
self.cp_var.set(r[3])
self.sp_var.set(r[4])
self.vendor_var.set(r[5])
self.vendor_phone_var.set(r[9])
# print(self.name_var, self.stock_var,self.cp_var)
def update(self):
self.totalcp = float(self.cp_e.get()) * float(self.stock_e.get())
self.totalsp = float(self.sp_e.get()) * float(self.stock_e.get())
self.assumed_profit = float(self.totalsp - self.totalcp)
my_cursor.execute(
"update dept set
name=:1,stock=:2,cp=:3,sp=:4,vendor=:5,totalsp=:6,totalcp=:7,assumed_profit
=:8,vendor_phoneno=:9 where id=:10",
(
self.name_e.get(),
self.stock_e.get(),
self.cp_e.get(),
self.sp_e.get(),
self.vendor_e.get(),
self.totalsp,
self.totalcp,
self.assumed_profit,
self.vendor_phone_e.get(),
self.id_e.get()
))
conn.commit()
self.fetch_data()
self.clear()
messagebox.showinfo("Success", "Updated Successfully")def delete_record(self):
if self.id_e.get() == "":
messagebox.showerror("Error", "First select the Product")
else:
query = "delete from dept where id=:1"
value = (self.id_e.get(),)
my_cursor.execute(query, value)
conn.commit()
self.clear()
self.fetch_data()
messagebox.showinfo("Delete", "Product has been deleted
successfully")
# MANAGE PRODUCTS
def open(self):
screen = Tk()
screen.title("MY SECOND WINDOW")
screen.geometry("1340x800+0+0")
lbltitle = Label(screen, bd=20, relief=RIDGE, text='MANAGE
PRODUCTS', fg="white",
bg="steelblue",
font=("times new roman", 20, "bold"))
lbltitle.pack(side=TOP, fill=X)
DataFrame = Frame(screen, bd=20, relief=RIDGE)
DataFrame.place(x=0, y=90, width=1340, height=750)
dataframeLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
font=("times new roman", 12, "bold"),
text="Add Products To your Cart")
dataframeLeft.place(x=0, y=5, width=650, height=700)
dataframeRight = LabelFrame(DataFrame, bd=10, relief=RIDGE,
padx=10, font=("times new roman", 12, "bold"),
text="Product Details", bg="steelblue"
,fg="white")
dataframeRight.place(x=660, y=5, width=640, height=700)
self.left = Frame(dataframeLeft, width=650, height=700, bg="white")
self.left.pack(side=LEFT)
self.right = Frame(dataframeRight, width=640, height=700,
bg="steelblue")
self.right.pack(side=RIGHT)
# components
self.heading = Label(dataframeLeft, text="Manage store",
font='arial 40 bold', bg='white')
self.heading.place(x=0, y=0)
self.date_l = Label(self.right, text="Today's Date: " + str(date),
font='arial 15 bold', bg='steelblue',
fg='white')
self.date_l.place(x=0, y=10)
# table invoice
self.tproduct = Label(self.right, text="Products", font='arial 18
bold', fg='white', bg="steelblue")
self.tproduct.place(x=0, y=60)self.tqty = Label(self.right, text="Quantity", font='arial 18
bold', fg='white', bg="steelblue")
self.tqty.place(x=250, y=60)
self.tamt = Label(self.right, text="Amount", font='arial 18 bold',
fg='white', bg="steelblue")
self.tamt.place(x=450, y=60)
# enter stuff
self.enterid = Label(self.left, text="Enter Product's Id",
font='arial 18 bold', bg='white')
self.enterid.place(x=0, y=80)
self.enteride = Entry(self.left, width=25, font='arial 18 bold',
bg='lightblue')
self.enteride.place(x=190, y=80)
self.enterid.focus()
# button
self.search_btn = Button(self.left, text="Search", width=22,
height=2, bg='orange', command=self.getInfo)
self.search_btn.place(x=350, y=120)
self.productname = Label(self.left, text="", font='arial 18 bold',
bg='white', fg='steelblue')
self.productname.place(x=0, y=180)
self.price = Label(self.left, text="", font='arial 18 bold',
bg='white', fg='steelblue')
self.price.place(x=0, y=220)
def getInfo(self):
query = 'select * from dept where id=:1'
res = my_cursor.execute(query, (self.enteride.get()))
for r in res:
self.get_id = r[0]
self.get_name = r[1]
self.get_price = r[4]
self.get_stock = r[2]
self.productname.configure(text="Product's Name: " +
str(self.get_name))
self.price.configure(text='Price: Rs. ' + str(self.get_price))
# create the quantity and discount label
self.quantity_l = Label(self.left, text="Enter Quantity",
font='arial 18 bold', bg='white')
self.quantity_l.place(x=0, y=290)
self.quantity_e = Entry(self.left, width=25, font='arial 18 bold',
bg='lightblue')
self.quantity_e.place(x=190, y=290)
self.quantity_e.focus()
self.disc_l = Label(self.left, text="Enter Discount", font='arial
18 bold', bg='white')
self.disc_l.place(x=0, y=350)
self.disc_e = Entry(self.left, width=25, font='arial 18 bold',bg='lightblue')
self.disc_e.place(x=190, y=350)
self.disc_e.focus()
self.disc_e.insert(END, 0)
self.add_to_cart_btn = Button(self.left, command=self.add_to_cart,
text="Add to cart", width=22, height=2,
bg='orange')
self.add_to_cart_btn.place(x=350, y=400)
# generate bill and change
self.change_l = Label(self.left, text="Given Amount", font='arial
18 bold', bg='white')
self.change_l.place(x=0, y=470)
self.change_e = Entry(self.left, width=25, font='arial 18 bold',
bg='lightblue')
self.change_e.place(x=190, y=470)
self.change_btn = Button(self.left, text="Calculate change",
width=22, height=2, bg='orange',
command=self.change)
self.change_btn.place(x=350, y=530)
self.gen_bill_btn = Button(self.left, text="Generate Bill",
command=self.generate_bill, width=80, height=2,
bg='steelblue', fg='white')
self.gen_bill_btn.place(x=20, y=600)
self.total_l = Label(self.right, text="", font='arial 40 bold',
bg='steelblue', fg='white')
self.total_l.place(x=0, y=570)
def add_to_cart(self):
# get the quantity value from the database
self.qty_val = int(self.quantity_e.get())
if self.qty_val > int(self.get_stock):
messagebox.showinfo("Error", "Not That many products in ous
store.")
else:
self.final_price = (float(self.qty_val) *
float(self.get_price)) - (float(self.disc_e.get()))
products_list.append(self.get_name)
product_price.append(self.final_price)
product_quantity.append(self.qty_val)
product_id.append(self.get_id)
x_index = 0
y_index = 100
counter = 0
for p in products_list:
self.tempname = Label(self.right,
text=str(products_list[counter]), font='arial 18 bold',
bg='steelblue',
fg='white')
self.tempname.place(x=0, y=y_index)
labels_list.append(self.tempname)
self.tempqty = Label(self.right,
text=str(product_quantity[counter]), font='arial 18 bold',
bg='steelblue',fg='white')
self.tempqty.place(x=300, y=y_index)
labels_list.append(self.tempqty)
self.tempprice = Label(self.right,
text=str(product_price[counter]), font='arial 18 bold',
bg='steelblue',
fg='white')
self.tempprice.place(x=500, y=y_index)
labels_list.append(self.tempprice)
y_index += 40
counter += 1
# total configure
self.total_l.configure(text="Total: Rs" +
str(sum(product_price)))
# delete
self.quantity_l.place_forget()
self.quantity_e.place_forget()
self.disc_l.place_forget()
self.disc_e.place_forget()
self.productname.configure(text="")
self.price.configure(text="")
self.add_to_cart_btn.destroy()
# autofocus to the enter id
self.enterid.focus()
self.enteride.delete(0, END)
def change(self):
# get the amount given by customer and the amount generated by the
computer
self.amt_given = float(self.change_e.get())
self.our_total = float(sum(product_price))
self.to_give = abs(self.amt_given - self.our_total)
# label change
self.c_amt = Label(self.left, text="Change: Rs. " +
str(self.to_give), font='arial 18 bold', fg='red',
bg='white')
self.c_amt.place(x=0, y=600)
def generate_bill(self):
# decrease the stock
self.bill_page()
x = 0
initial = "select * from dept where id=:1"
res = my_cursor.execute(initial, (product_id[x]))
for i in products_list:
for r in res:
self.old_stock = r[2]
self.new_stock = int(self.get_stock) - int(product_quantity[x])
sql = "update dept set stock = :1 where id= :2"
my_cursor.execute(sql, (self.new_stock, product_id[x]))
conn.commit()
# insert into transaction
sql2 = "insert into transaction
(product_name,quantity,amount,trans_date)values(:1,:2,:3,:4)"
my_cursor.execute(sql2, (products_list[x], product_quantity[x],product_price[x], date))
conn.commit()
x += 1
messagebox.showinfo("Success", "Done Everything Smoothly")
def welcome_bill(self):
self.textarea.delete('1.0', END)
self.textarea.insert(END, "\t\tBibek Company Pvt. Ltd.\n")
self.textarea.insert(END, f"\n\t\tKathmandu, Nepal")
self.textarea.insert(END, f"\n\t\t9976554347 ")
self.textarea.insert(END, f"\n\t\tInvoice")
self.textarea.insert(END, "\n\t\t" + str(date))
self.textarea.insert(END,
f"\n===============================================")
self.textarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
self.textarea.insert(END,
f"\n===============================================")
def bill_area(self):
self.welcome_bill()
i = 0
for t in products_list:
self.textarea.insert(END, "\n" + str(products_list[i] +
"******")[:7] + "\t\t" + str(
product_quantity[i]) + "\t\t" + str(product_price[i]))
i += 1
self.textarea.insert(END, "\n\n\n\t\t\tTotal: Rs. " +
str(sum(product_price)))
self.textarea.insert(END, "\n\n\t\t\tThanks for visiting.")
def bill_page(self):
screen2 = Tk()
screen2.title("Bill Area")
screen2.geometry("420x400+0+0")
f5 = Frame(screen2, bd=10, relief=GROOVE)
f5.place(x=0, y=10, width=420, height=380)
bill_title = Label(f5, text="Bill Area", font="arial 15 bold",
bd=7, relief=GROOVE).pack(fill=X)
scroll_y = Scrollbar(f5, orient=VERTICAL)
self.textarea = Text(f5, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.configure(command=self.textarea.yview)
self.textarea.pack(fill=BOTH, expand=1)
self.bill_area()
for a in labels_list:
a.destroy()
del (products_list[:])
del (product_price[:])
del (product_quantity[:])
del (product_id[:])
self.total_l.configure(text="")
# self.c_amt.configure(text="")
self.change_e.delete(0, END)
self.enterid.focus()
root = Tk()
ob = Hospital(root)
root.mainloop()