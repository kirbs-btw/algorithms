import tkinter as tk
import getData as gd

def mainWindow():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    canvas.create_text(250, 100, text="Display Table", anchor="n")

    displayTableButton = tk.Button(canvas, text="Display", command = lambda: displayTable(dbInput.get()))
    displayTableButton.place(relx=0.5, rely=0.4, anchor="n")

    dbInput = tk.Entry(canvas)
    dbInput.place(relx=0.5, rely=0.3, anchor="n")

    root.mainloop()

def insertData(canvas, data):
    row = 0
    for i in data:
        row += 1
        column = 0
        for j in i:
            column += 1
            tk.Label(canvas,text=j).grid(row=row, column=column)


def displayTable(dbName):
    root = tk.Tk()
    print("hello")
    canvas = tk.Canvas(root)
    canvas.pack()

    data = gd.getData(dbName)
    insertData(canvas, data)

    root.mainloop()

    pass


if __name__ == '__main__':
    mainWindow()