from tkinter import *
from tkinter import messagebox


def center_window(win, width=400, height=300):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


def login():
    username = e1.get()
    password = e2.get()
    if username == "amir" and password == "123456":
        messagebox.showinfo("ورود موفق", "خوش آمدید!")
        window.destroy()  # بستن برنامه بعد از ورود موفق
    else:
        global attempts
        attempts += 1
        messagebox.showerror("خطا", f"نام کاربری یا رمز عبور اشتباه است!\nتعداد تلاش‌های ناموفق: {attempts}")
        if attempts >= 3:
            messagebox.showwarning("هشدار", "تعداد تلاش‌های مجاز تمام شد! برنامه بسته می‌شود.")
            window.destroy()


def reset_fields():
    e1.delete(0, END)
    e2.delete(0, END)

def toggle_password():
    if show_password_var.get():
        e2.config(show="")
    else:
        e2.config(show="*")

# ایجاد پنجره اصلی
window = Tk()
window.title("login")
window.config(bg="#f0f0f5")
center_window(window, 350, 300)

attempts = 0  

# طراحی لیبل‌ها و ورودی‌ها
lblUser = Label(window, text="نام کاربری :", font=("Vazirmatn", 14), bg="#f0f0f5")
lblUser.grid(row=0, column=0, padx=10, pady=10, sticky=E)

e1 = Entry(window, font=("Vazirmatn", 14))
e1.grid(row=0, column=1, padx=10, pady=10)

lblPass = Label(window, text="رمز عبور :", font=("Vazirmatn", 14), bg="#f0f0f5")
lblPass.grid(row=1, column=0, padx=10, pady=10, sticky=E)

e2 = Entry(window, font=("Vazirmatn", 14), show="*")
e2.grid(row=1, column=1, padx=10, pady=10)

# چک باکس نمایش رمز عبور
show_password_var = BooleanVar()
chkShowPass = Checkbutton(window, text="نمایش رمز عبور", variable=show_password_var, command=toggle_password, bg="#f0f0f5", font=("Vazirmatn", 10))
chkShowPass.grid(row=2, column=1, sticky=W, padx=10)

# دکمه‌های ورود و ریست
btnLogin = Button(window, text="ورود", font=("Vazirmatn", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5, command=login)
btnLogin.grid(row=3, column=0, pady=20)

btnReset = Button(window, text="پاک کردن", font=("Vazirmatn", 12, "bold"), bg="#f44336", fg="white", padx=20, pady=5, command=reset_fields)
btnReset.grid(row=3, column=1, pady=20)

window.mainloop()