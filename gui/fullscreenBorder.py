# This code creates a red border around the screen using Tkinter.

import tkinter as tk

root = tk.Tk()
# Make main window full-screen
root.attributes('-fullscreen', True) 
# Make main window always on top
root.attributes('-topmost',True)
# Make the background transparent
root.wm_attributes("-transparentcolor", root['bg'])

# Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create the canvas upon which we draw
canvas = tk.Canvas(root, highlightthickness=0)

# Draw a 5px red border around the edges of the screen
canvas.create_line(0, 0, screen_width, 0, fill='red', width=5)
canvas.create_line(0, 0, 0, screen_height, fill='red', width=5)
canvas.create_line(0, screen_height, screen_width, screen_height, fill='red', width=5)
canvas.create_line(screen_width, 0, screen_width, screen_height, fill='red', width=5)   
canvas.pack(fill=tk.BOTH, expand=True) # configure canvas to occupy the whole main window

root.configure(bg="red")

root.mainloop()