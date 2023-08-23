import time
import pyautogui as pyag
import  tkinter as tk

def screenshot():
    name = int(round(time.time()* 1000))
    name = 'C:/Files/Gheve/Projects/test/python lesson/Project_1/screenshots/{}.png'.format(name) 
    # C:/Files/Gheve/Projects/test/python lesson/ is the local file path where Project_1 is located
    img = pyag.screenshot(name)
    img.show()

root = tk.Tk()
root.geometry("300x300")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)

close.pack(side=tk.LEFT)

root.mainloop()