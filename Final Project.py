import tkinter as tk 

#building a window
root = tk.Tk()
root.title ('Final Project Tkinter form.')

#Window size
root.geometry ('700x500+300+300')

#Sizable setting
root.resizable (False, False)

#Building widgets
#title widget
title = tk.Label (root, text = 'World Famous Ice Parlor', font = 'Arial 16 bold', bg = 'Purple', fg = '#FFFFFF')

#building label and text entry

#layout application 
#layout for row 0
title.grid (row = 0, columnspan = 2)