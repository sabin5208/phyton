from tkinter import *

def insertData() :
    pass

def selectData() :
    pass

root = Tk()
root.title("컴과 3학년 1반 10번 박용빈")
editFrame = Frame(root)
editFrame.pack()
listFrame = Frame(root)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

edit1 = Entry(editFrame, width = 10)
edit2 = Entry(editFrame, width = 10)
edit3 = Entry(editFrame, width = 10)
edit4 = Entry(editFrame, width = 10)
edit1.pack(side = LEFT, padx = 10, pady = 10)
edit2.pack(side = LEFT, padx = 10, pady = 10)
edit3.pack(side = LEFT, padx = 10, pady = 10)
edit4.pack(side = LEFT, padx = 10, pady = 10)


btnInsert = Button(editFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)

btnSelect = Button(editFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = "yellowgreen")
listData1.pack(side = LEFT, fill = X, expand = 1)

listData2 = Listbox(listFrame, bg = "yellowgreen")
listData2.pack(side = LEFT, fill = X, expand = 1)

listData3 = Listbox(listFrame, bg = "yellowgreen")
listData3.pack(side = LEFT, fill = X, expand = 1)

listData4 = Listbox(listFrame, bg = "yellowgreen")
listData4.pack(side = LEFT, fill = X, expand = 1)

root.mainloop()
