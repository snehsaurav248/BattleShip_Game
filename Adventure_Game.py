import tkinter as tk
from tkinter import messagebox

# Room class
class Room:
    def __init__(self, description, connections, items):
        self.description = description
        self.connections = connections
        self.items = items

# Initialize rooms
def initialize_rooms():
    rooms = {}
    rooms["entrance"] = Room("You are at the entrance of a dark cave.",
                             {"north": "hallway"},
                             [])
    rooms["hallway"] = Room("You are in a hallway with doors to the east and west.",
                            {"south": "entrance", "east": "kitchen", "west": "library"},
                            [])
    rooms["kitchen"] = Room("You are in a kitchen. There's a strange smell here.",
                            {"west": "hallway"},
                            ["key"])
    rooms["library"] = Room("You are in a library. There are many dusty books.",
                            {"east": "hallway", "north": "secret room"},
                            [])
    rooms["secret room"] = Room("You found a secret room! There is a treasure chest here.",
                                {"south": "library"},
                                ["treasure"])
    return rooms

# Global variables
current_room = "entrance"
inventory = []

# Function to center the Tkinter window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

# Display current room description
def display_room():
    room = rooms[current_room]

    description_label.config(text=room.description)
    items_label.config(text="Items in the room: " + ", ".join(room.items))

# Move to another room
def move(direction):
    global current_room
    if direction in rooms[current_room].connections:
        current_room = rooms[current_room].connections[direction]
        display_room()
    else:
        messagebox.showinfo("Invalid Move", "You can't go that way.")

# Take an item from the room
def take_item():
    global current_room, inventory
    item = entry.get()
    if item in rooms[current_room].items:
        inventory.append(item)
        rooms[current_room].items.remove(item)
        display_room()
        messagebox.showinfo("Item Taken", "You took the " + item + ".")
    else:
        messagebox.showinfo("Item Not Found", "There is no " + item + " here.")

# Display inventory
def display_inventory():
    messagebox.showinfo("Inventory", "Your inventory: " + ", ".join(inventory))

# Main Tkinter GUI setup
root = tk.Tk()
root.title("Text Adventure Game")

# Initialize rooms
rooms = initialize_rooms()

# Center the window
window_width = 400
window_height = 300
center_window(root, window_width, window_height)

# Create widgets
frame = tk.Frame(root)
frame.pack(pady=10)

description_label = tk.Label(frame, text="", wraplength=380, justify="center", font=("Arial", 12))
description_label.pack(pady=10)

items_label = tk.Label(frame, text="", wraplength=380, justify="center", font=("Arial", 10))
items_label.pack()

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry_label = tk.Label(entry_frame, text="Command: ")
entry_label.pack(side=tk.LEFT)

entry = tk.Entry(entry_frame, width=30, font=("Arial", 10))
entry.pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

go_button = tk.Button(button_frame, text="Go", width=10, command=lambda: move(entry.get()))
go_button.pack(side=tk.LEFT, padx=10)

take_button = tk.Button(button_frame, text="Take", width=10, command=take_item)
take_button.pack(side=tk.LEFT, padx=10)

inventory_button = tk.Button(button_frame, text="Inventory", width=10, command=display_inventory)
inventory_button.pack(side=tk.LEFT, padx=10)

# Display initial room
display_room()

# Run the Tkinter event loop
root.mainloop()
