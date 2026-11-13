import tkinter as tk
import random

# Function to draw the dice faces based on the rolled number
def draw_dice(number):
    # Clear the canvas before drawing a new face
    canvas.delete("all")
    
    # Draw white backgrounded dice with a black border
    canvas.create_rectangle(10, 10, 190, 190, fill="white", outline="black", width=4)
    
    dots = []
    
    if number == 1:
        dots = [(100, 100)]
    elif number == 2:
        dots = [(50, 50), (150, 150)]
    elif number == 3:
        dots = [(50, 50), (100, 100), (150, 150)]
    elif number == 4:
        dots = [(50, 50), (150, 50), (50, 150), (150, 150)]
    elif number == 5:
        dots = [(50, 50), (150, 50), (100, 100), (50, 150), (150, 150)]
    elif number == 6:
        dots = [(50, 50), (150, 50), (50, 100), (150, 100), (50, 150), (150, 150)]
    
    # Draw black circles (dots) for each coordinate in the list
    for x, y in dots:
        canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="black")

# Function to simulate rolling animation
def roll_dice():
    # Roll animation effect
    for i in range(8):
        temp_val = random.randint(1, 6)
        draw_dice(temp_val)
        root.update()
        root.after(50)  # 50 milliseconds delay for smooth animation
        
    # Final dice value after animation stops
    final_val = random.randint(1, 6)
    draw_dice(final_val)

# Main window setup
root = tk.Tk()
root.title("Animated Dice Simulator")
root.geometry("250x300")
root.config(bg="#f0f0f0")

# White Canvas area for the dice
canvas = tk.Canvas(root, width=200, height=200, bg="#f0f0f0", highlightthickness=0)
canvas.pack(pady=15)

# Roll button styling and placement
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12, "bold"), command=roll_dice, bg="#4CAF50", fg="white", padx=10, pady=5)
roll_button.pack()

# Initial state of the dice when the program starts
draw_dice(1)

# Run the application main loop
root.mainloop()
