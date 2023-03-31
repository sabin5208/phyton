import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.title("bmi 꼐산")

window.geometry("640x400+100+100")

window.resizable(False, False)

he = tkinter.StringVar()

we = tkinter.StringVar()

def btn_click() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = w_value / (h_value * h_value)
    tkinter.messagebox.showinfo("결과",result)

title_label = tkinter.Label(window, text = "bmi 계산기")

title_label.config(font = ("Arial", 25))

title_label.config(fg = "red")

title_label.pack()

height_label = tkinter.Label(window, text = "신장")
                
height_label.config(font = ("Arial", 24))

height_label.place(x = 30, y = 70)
                   
height_entry = tkinter.Entry(window,textvariable = he)
height_entry.place(x = 120, y = 81)

btn = tkinter.Button(window, text = "확인", command = btn_click)
btn.place(x = 30, y = 250)

weight_label = tkinter.Label(window, text = "체중")
                
weight_label.config(font = ("Arial", 24))

weight_label.place(x = 30, y = 150)
                   
weight_entry = tkinter.Entry(window,textvariable = we)
weight_entry.place(x = 120, y = 160)



window.mainloop()
