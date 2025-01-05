import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello World GUI")

    # Create a label widget with "Hello, World!" text
    label = tk.Label(root, text="I'm SHRAVAN", font=("Arial", 29))

    # Pack the label widget to make it visible in the window
    label.pack(padx=20, pady=20)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
