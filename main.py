# main.py

# Import the tkinter library, which provides the graphical user interface
import tkinter as tk

# Import the function 'extract_and_sort_events' from the 'functions' module in the 'app' package
from app.functions import extract_and_sort_events

# Define the main function responsible for creating the GUI and initiating the program
def main():
    # Create a Tkinter root window, the main window of the application
    root = tk.Tk()

    # Set the title of the root window to 'CSV File Upload'
    root.title("CSV File Upload")

    # Set the initial size of the root window to 600x600 pixels
    root.geometry("600x600")

    # Create a button widget in the root window for uploading a CSV file
    # The 'command' parameter associates the button with the 'extract_and_sort_events' function
    # 'lambda' is used to pass the 'root' window as an argument to 'extract_and_sort_events'
    upload_button = tk.Button(root, text="Upload CSV", command=lambda: extract_and_sort_events(root))

    # Place the 'Upload CSV' button in the root window using the 'pack' geometry manager
    upload_button.pack()

    # Start the Tkinter event loop, which listens for user interactions and updates the GUI
    root.mainloop()

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Call the main function to start the application
    main()
