import tkinter as tk

def test_function(entry):
    print("this is the entry:", entry)

root = tk.Tk()

background_image = tk.PhotoImage('E:\editan\my.jpg')
background_label = tk.Label(root, image=background_image)
background_label.place (relwidth=1, relheight=1)

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

#background_image = tk.PhotoImage('E:\editan\my.jpg')
#background_label = tk.Label(root, image=background_image)
#background_label.place (relwidth=0.2, relheight=1)

frame = tk.Frame(root, bg='#66ff33', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.2, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relx=0.35, relwidth=0.2, relheight=1)

button = tk.Button(frame, text="Hallo Mbloo", font=40)
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#66ff33', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()