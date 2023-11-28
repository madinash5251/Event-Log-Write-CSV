# functions.py

# Import necessary libraries and modules
import pandas as pd  # For data manipulation and analysis
from tkinter import filedialog, Toplevel, Text, END  # Import END from tkinter

# Define a function to extract and sort events from a CSV file
def extract_and_sort_events(root):
    # Open a file dialog to select a CSV file and get its path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    # Check if a file was selected
    if file_path:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)

        # Convert the 'Timestamp' column to datetime format for proper sorting
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Sort the events based on the 'Timestamp' column
        sorted_events = df.sort_values('Timestamp')

        # Create a new window (Toplevel) for displaying sorted events
        display_window = Toplevel(root)
        display_window.title("Sorted Events")

        # Create a Text widget to display the sorted events
        text_area = Text(display_window, width=80, height=20)
        text_area.pack()

        # Insert the sorted events into the Text widget
        text_area.insert(END, sorted_events.to_string(index=False))

        # Save the sorted events to a text file named 'sorted_events.txt'
        sorted_events.to_csv('sorted_events.txt', index=False, header=True, sep='\t')
