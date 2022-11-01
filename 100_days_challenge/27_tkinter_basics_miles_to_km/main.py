import tkinter

windows = tkinter.Tk()
windows.title("Mile to Km Converter")
windows.config(padx=15, pady=15)
windows.minsize(width=250, height=100)

# input
input_miles = tkinter.Entry()
input_miles.grid(column=1, row=0)

# label
miles = tkinter.Label(text='Miles')
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result = tkinter.Label(text=0, font=("Arial", 12, 'bold'))
result.grid(column=1, row=1)

km = tkinter.Label(text='Km')
km.grid(column=2, row=1)

# button
calculate = tkinter.Button(text="Calculate",
                           command=lambda: result.
                           config(text=str(round(float(input_miles.get()) * 1.609, 2))))
calculate.grid(column=1, row=2)

windows.mainloop()
