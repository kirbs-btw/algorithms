import tkinter as tk
import bars_turtle as tshow

def mainWindow():
    root = tk.Tk()

    root.title("Input Bars")


    canvas = tk.Canvas(root, height=500, width=500)
    canvas.pack()

    #inputs
    topLabel = tk.Label(canvas, text="Inputs:")
    topLabel.grid(row=0, column=1)

    input1 = tk.Entry(canvas)
    input1.grid(row=1, column=1)

    input2 = tk.Entry(canvas)
    input2.grid(row=2, column=1)

    input3 = tk.Entry(canvas)
    input3.grid(row=3, column=1)

    input4 = tk.Entry(canvas)
    input4.grid(row=4, column=1)

    input5 = tk.Entry(canvas)
    input5.grid(row=5, column=1)

    executeButton = tk.Button(canvas, text="show", command = lambda:  tshow.printBars([float(input1.get()), float(input2.get()), float(input3.get()), float(input4.get()), float(input5.get())], 25))
    executeButton.grid(row=6, column=1)

    root.mainloop()





if __name__ == '__main__':
    mainWindow()