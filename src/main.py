import tkinter as tk
import threading
import pyautogui
from pynput import keyboard
from applibs import auto_fish  # import your function

pos = [0, 0]

def auto_fish_thread():
    while running[0]:
        auto_fish(pos)  # call the function from autofisher.py

def toggle_auto_fisher():
    if label_2["text"] == "Off":
        label_2.config(text="On")
        button.config(text="Stop")
        running[0] = True
        threading.Thread(target=auto_fish_thread, daemon=True).start()
    else:
        label_2.config(text="Off")
        button.config(text="Start")
        running[0] = False

def get_mouse_pos():
    global pos 
    pos = pyautogui.position()
    print("Set position:", pos)  # Output: [1322, 764]

# Function to safely toggle from listener thread
def on_press(key):
    try:
        if key.char == 'f':  # replace 'f' with the key you want
            root.after(0, toggle_auto_fisher)  # schedule toggle in main thread
        elif key.char == 'h':  # replace 'f' with the key you want
            root.after(0, get_mouse_pos)  # schedule toggle in main thread
    except AttributeError:
        pass  # special keys like shifgt, ctrl etc. will be ignored

# Start the keyboard listener in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

# ---------------- Tkinter GUI ----------------
root = tk.Tk()
root.geometry("350x150")
root.title("AutoFisher")
root.attributes("-topmost", True)

running = [False]

label = tk.Label(root, text="Activate auto fisher - F", font=('Arial', 14))
label.pack(fill="x", pady=0, padx=10)

label_2 = tk.Label(root, text="Off", font=('Arial', 8))
label_2.pack(fill="x", pady=0, padx=10)

button = tk.Button(root, text="Start", command=toggle_auto_fisher)
button.pack(fill="x", pady=0, padx=10)

label = tk.Label(root, text="Set position - G", font=('Arial', 14))
label.pack(fill="x", pady=0, padx=10)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
cle