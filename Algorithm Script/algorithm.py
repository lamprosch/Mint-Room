import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.io import wavfile

def open_file_dialog():
    # Open a file dialog and allow the user to select a WAV file
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        # Load the selected WAV file
        sampling_rate, audio_signal = wavfile.read(file_path)
        # Print a message indicating that the input is complete
        print("Input complete. File loaded successfully.")
        # Return the loaded audio signal
        return sampling_rate, audio_signal
    else:
        print("No file selected.")
        return None, None

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Mint Room Engine")
    root.geometry("450x750")

    # Add a button to open the file dialog
    btn_open = tk.Button(root, text="Select Audio Signal", command=open_file_dialog)
    btn_open.pack(pady=20)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()