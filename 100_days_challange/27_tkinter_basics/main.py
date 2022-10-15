# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=640, height=320)
#
# # Label
# my_label = tkinter.Label(text="I am a label",
#                          font=("Arial", 24))
# my_label.pack()
#
# window.mainloop()
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))
