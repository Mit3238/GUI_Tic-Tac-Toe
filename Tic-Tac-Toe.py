from tkinter import *

root = Tk()
root.title('Tic-Tac-Toe')

my_label = Label(root, text=" It's 'O' Turn ", font=('Helvetica', 26))
turn = 1
run = True
list1 = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']


def check(sym):
    if list1[1] == list1[2] == list1[3] == sym or list1[7] == list1[8] == list1[9] == sym or list1[4] == list1[5] == \
            list1[6] == sym:
        for item in root.winfo_children():
            item.destroy()
        label = Label(root, text=sym + ' You won', font=('Helvetica', 34))
        label.pack(pady=20, padx=20)
    elif list1[1] == list1[4] == list1[7] == sym or list1[3] == list1[6] == list1[9] == sym or list1[2] == list1[5] == \
            list1[8] == sym:
        for item in root.winfo_children():
            item.destroy()
        label = Label(root, text=sym + ' You won', font=('Helvetica', 34))
        label.pack(pady=20, padx=20)
    elif list1[1] == list1[5] == list1[9] == sym or list1[7] == list1[5] == list1[3] == sym:
        for item in root.winfo_children():
            item.destroy()
        label = Label(root, text=sym + ' You won', font=('Helvetica', 34))
        label.pack(pady=20, padx=20)
    elif button_1['state'] == button_2['state'] == button_3['state'] == button_4['state'] == button_5['state'] == \
            button_6['state'] == button_7['state'] == button_8['state'] == button_9['state'] == DISABLED:
        for item in root.winfo_children():
            item.destroy()
        label = Label(root, text='Game Tie', font=('Helvetica', 34))
        label.pack(pady=20, padx=20)


def symbol(button, num):
    global turn
    if turn % 2 == 0:
        button.config(text=' X ', border=3)
        button['state'] = DISABLED
        list1[num] = 'X'
        my_label.config(text=" It's 'O' Turn ")
        check('X')
    else:
        button.config(text=' O ', border=3)
        button['state'] = DISABLED
        list1[num] = 'O'
        my_label.config(text=" It's 'X' Turn ")
        check('O')

    turn += 1


button_1 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_1, 1))
button_2 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_2, 2))
button_3 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_3, 3))
button_4 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_4, 4))
button_5 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_5, 5))
button_6 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_6, 6))
button_7 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_7, 7))
button_8 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_8, 8))
button_9 = Button(root, text='   ', font=('Helvetica', 36), command=lambda: symbol(button_9, 9))

button_1.grid(row=1, column=0, pady=10, padx=10)
button_2.grid(row=1, column=1, pady=10, padx=10)
button_3.grid(row=1, column=2, pady=10, padx=10)
button_4.grid(row=2, column=0, pady=10, padx=10)
button_5.grid(row=2, column=1, pady=10, padx=10)
button_6.grid(row=2, column=2, pady=10, padx=10)
button_7.grid(row=3, column=0, pady=10, padx=10)
button_8.grid(row=3, column=1, pady=10, padx=10)
button_9.grid(row=3, column=2, pady=10, padx=10)
my_label.grid(row=0, column=0, columnspan=3)

root.mainloop()
