from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

### --- Back_end --- ###
def celsius_picker(event):
    global progres_value
    if entry1.get() == '':
        entry2.configure(placeholder_text = 'Degrees in fahrenheit')
    else:
        final_result = round((float(entry1.get()) * 9/5) + 32,2)
        entry2.configure(placeholder_text = f'{final_result} °F')

        progres_value = (float(entry1.get())+20)/65
        # progressbar.start(10)
        progressbar.set(progres_value)


def fahrenheit_picker(event):
    global progres_value
    if entry2.get() == '':
        entry1.configure(placeholder_text = 'Degrees in celsius')
    else:
        final_result = round(((float(entry2.get()) - 32) * 5/9),2)
        entry1.configure(placeholder_text = f'{final_result} °C')

        # progressbar.start(10)
        progres_value = (final_result+20) / 65
        progressbar.set(progres_value)


def enter_fahrenheit(event):
    global entry1, entry2
    entry1.delete(0, END)
    entry1.configure(placeholder_text = 'Degrees in celsius')

    entry1.grid(row = 1 , column = 0)
    entry1.bind("<Button-1>", enter_celsius)

    entry2.configure(placeholder_text="Enter temperature in °F: ")

    entry2.grid(row = 1, column = 1)
    entry2.bind("<KeyRelease>", fahrenheit_picker)


def enter_celsius(event):
    global entry1, entry2
    entry1.configure(placeholder_text="Enter temperature in °C: ")

    entry1.grid(row = 1 , column = 0)
    entry1.bind("<KeyRelease>", celsius_picker)

    entry2.delete(0, END)
    entry2.configure(placeholder_text = 'Degrees in fahrenheit')

    entry2.grid(row = 1, column = 1)
    entry2.bind("<Button-1>", enter_fahrenheit)





### --- Front_end --- ###
window = customtkinter.CTk()
window.geometry('600x300')

window.title("Temperature Measures Converter APP")

top_frame = Frame(window)
top_frame.pack(padx = 50, pady = 50)


title1 = customtkinter.CTkLabel(top_frame,
                                    text = 'Degrees in Celsius',
                                    text_font = ('arial', 16),
                                    text_color = '#111',
                                    bg_color = None,
                                    fg_color = None)
title1.grid(row = 0, column = 0, padx=10, pady=4)


entry1 = customtkinter.CTkEntry(top_frame,
                                    placeholder_text="Enter temperature in °C: ",
                                    placeholder_text_color = 'black',
                                    width = 190,
                                    height = 30,
                                    border_width = 1,
                                    corner_radius = 5,
                                    fg_color = '#eee',
                                    bg_color = None,
                                    text_color = '#111',
                                    text_font = ('arial',16))
entry1.grid(row = 1 , column = 0, padx=10, pady=10)
entry1.bind("<KeyRelease>", celsius_picker)



title2 = customtkinter.CTkLabel(top_frame,
                                    text = 'Degrees in Fahrenheit',
                                    text_font = ('arial', 16),
                                    text_color = '#111',
                                    bg_color = None,
                                    fg_color = None)
title2.grid(row = 0, column = 1, padx=10, pady=4)

entry2 = customtkinter.CTkEntry(top_frame,
                                    placeholder_text="Degrees in Fahrenheit",
                                    placeholder_text_color = 'black',
                                    width = 190,
                                    height = 30,
                                    border_width = 1,
                                    corner_radius = 5,
                                    fg_color = '#eee',
                                    bg_color = None,
                                    text_color = '#111',
                                    text_font = ('arial',16))
entry2.grid(row = 1, column = 1, padx=10, pady=10)
entry2.bind("<Button-1>", enter_fahrenheit)

progressbar = customtkinter.CTkProgressBar(top_frame,
                                        width = 430,
                                        height = 13,
                                        border_width = 1,
                                        progress_color = ('white','black'))
progressbar.grid(row = 2, column = 0, columnspan = 2, padx=0, pady=(20,0))

lbl1 = customtkinter.CTkLabel(top_frame, text = "It's Freezing", anchor='w', justify="left", text_color = "blue")
lbl1.grid(row = 3, column = 0, padx = (0,100))

lbl2 = customtkinter.CTkLabel(top_frame, text = "It’s Boiling", anchor='e', justify="right", text_color = "red")
lbl2.grid(row = 3, column = 1, padx = (100,0))

window.mainloop()
