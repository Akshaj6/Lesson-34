from tkinter import *
root = Tk()
root.title('Number Pad')
root.geometry('250x300')
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
for i in range(4):
    for j in range(3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1,
            bg = "#d0efff"            
        )
        frame.grid(row=i, column=j, sticky='nsew')
        label = Label(master=frame, text=nums[i][j], bg = "#d0efff", font=('Arial', 18))
        label.pack(expand=True, fill='both', padx=5, pady=5)
root.mainloop()