import tkinter

window = tkinter.Tk()
window.title("GUI Program by yb5208")

window.geometry("640x400+100+100")
window.resizable(False, False)

def btn_click():
    label.config(font=("Arial", 40))
    label.config(text = "안산공업고등학교 컴퓨터과")
    label.config(fg = "red")
label = tkinter.Label(window, text = "안산공업고등학교")
label.pack()

button = tkinter.Button(window, text = "커져라", command = btn_click)
button.pack()
window.mainloop()
