
from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox
# Colors Part
color0 = "#ffffff"
color1 = "#000000"
color2 = "#4456f0"

# Setting Page Part
window = Tk()
window.geometry("600x450")
window.title("دفترچه تلفن")
window.configure(background=color0)
window.resizable(False, False)


# Frame Part
frame_up = Frame(window, background=color2, width=600, height=50)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, background=color0, width=600, height=150)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, background=color0,
                    width=600, height=100, relief='flat')
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1, sticky=NW)


# Functions Part

def show():
    global tree
    list_header = ['نام', 'جنسیت', 'تلفن', 'ایمیل']
    df_list = view()
    tree = ttk.Treeview(frame_table, selectmode="extended",
                        columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    tree.heading(0, text="نام", anchor=NW)
    tree.heading(1, text="جنسیت", anchor=NW)
    tree.heading(2, text="تلفن", anchor=NW)
    tree.heading(3, text="ایمیل", anchor=NW)

    tree.column(0, width=160, anchor="nw")
    tree.column(1, width=80, anchor="nw")
    tree.column(2, width=180, anchor="nw")
    tree.column(3, width=180, anchor="nw")

    for item in df_list:
        tree.insert("", "end", values=item)


show()


def insert():
    Name = e_name.get()
    Gender = e_gender.get()
    Phone = e_phone.get()
    Email = e_email.get()

    data = [Name, Gender, Phone, Email]
    if Name == "" or Gender == "" or Phone == "" or Email == "":
        messagebox.showerror('data', "لطفا تمام فیلد هارا پر کنید")
    else:
        add(data)
        messagebox.showinfo('data', "با موفقیت اضافه شد")
        e_name.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_email.delete(0, 'end')
        show()


def to_update():
    try:
        tree_data = tree.focus()
        tree_dicshenary = tree.item(tree_data)
        tree_list = tree_dicshenary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Phone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0, Name)
        e_gender.insert(0, Gender)
        e_phone.insert(0, Phone)
        e_email.insert(0, Email)

        def confirm():
            new_name = e_name.get()
            new_gender = e_gender.get()
            new_phone = e_phone.get()
            new_email = e_email.get()

            data = [new_phone, new_name, new_gender, new_phone, new_email]

            update1(data)
            messagebox.showinfo("موفق", "به روز رسانی انجام شد")

            e_name.delete(0, 'end')
            e_gender.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_email.delete(0, 'end')

            for w in frame_table.winfo_children():
                w.destroy()

            b_confirm.destroy()
            show()

        b_confirm = Button(frame_down, text="ثبت", height=1,
                           width=7, bg=color0, fg=color2, font=("ivy 8 bold"), command=confirm)
        b_confirm.place(x=350, y=110)
    except IndexError:
        messagebox.showerror("خطا", "یک مخاطب را از جدول انتخاب کنید")


def to_remove():
    try:
        tree_data = tree.focus()
        tree_dicshenary = tree.item(tree_data)
        tree_list = tree_dicshenary['values']
        tree_phone = str(tree_list[2])
        remove(tree_phone)
        messagebox.showinfo('موفق', 'مخاطب با موفقیت حذف شد')
        for w in frame_table.winfo_children():
            w.destroy()
        show()
    except IndexError:
        messagebox.showerror("خطا", "یک مخاطب را از جدول انتخاب کنید")


def to_search():
    phone = e_search.get()
    data = search(phone)

    def delete_command():
        tree.delete(*tree.get_children())
    delete_command()
    for item in data:
        tree.insert("", 'end', values=item)
    e_search.delete('', 'end')

    # Frame_up widgets
app_welcome = Label(frame_up, text="خوش آمدید ", fg=color0,
                    background=color2, font=("verdana 20 bold"))
app_welcome.place(x=30, y=10)

# Frame_down Widgets
l_name = Label(frame_down, text=": نام کامل", width=10, height=10, font=(
    "ivy 15"), background=color0, foreground=color1, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left',
               highlightthickness=1, relief='solid', background=color0, fg=color1)
e_name.place(x=80, y=20)

l_gender = Label(frame_down, text=": جنسیت", width=10, height=10, font=(
    "ivy 15"), background=color0, foreground=color1, anchor=NW)
l_gender.place(x=10, y=50)
e_gender = ttk.Combobox(frame_down, width=27)
e_gender['value'] = ['نامشخص', 'مرد', 'زن']
e_gender.place(x=80, y=50)


l_phone = Label(frame_down, text=": تلفن", width=10, height=10, font=(
    "ivy 15"), background=color0, foreground=color1, anchor=NW)
l_phone.place(x=10, y=80)
e_phone = Entry(frame_down, width=25, justify='left',
                highlightthickness=1, relief='solid', background=color0, fg=color1)
e_phone.place(x=80, y=80)

l_email = Label(frame_down, text=": ایمیل", width=10, height=10, font=(
    "ivy 15"), background=color0, foreground=color1, anchor=NW)
l_email.place(x=10, y=110)
e_email = Entry(frame_down, width=25, justify='left',
                highlightthickness=1, relief='solid', background=color0, fg=color1)
e_email.place(x=80, y=110)


b_search = Button(frame_down, text="جست و جو", height=1, width=5,
                  bg=color0, fg=color2, font=("ivy 8 bold"), command=to_search)
b_search.place(x=370, y=20)
e_search = Entry(frame_down, width=15, justify='left',
                 relief='solid', fg=color1, background=color0)
e_search.place(x=450, y=20)


b_view = Button(frame_down, text="نمایش", height=1, width=7,
                bg=color0, fg=color2, font=("ivy 8 bold"), command=show)
b_view.place(x=370, y=50)

b_add = Button(frame_down, text="اضافه کردن", height=1, width=7,
               bg=color0, fg=color2, font=("ivy 8 bold"), command=insert)
b_add.place(x=470, y=50)

b_update = Button(frame_down, text="ویرایش", height=1, width=7,
                  bg=color0, fg=color2, font=("ivy 8 bold"), command=to_update)
b_update.place(x=470, y=80)

b_delet = Button(frame_down, text="حذف", height=1, width=7,
                 bg=color0, fg=color2, font=("ivy 8 bold"), command=to_remove)
b_delet.place(x=470, y=110)
# End Part
window.mainloop()
