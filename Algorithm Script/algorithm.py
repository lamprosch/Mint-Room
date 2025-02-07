import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.io import wavfile
import sounddevice as sd

# Global variables to store the audio signal and sampling rate
audio_signal = None
sampling_rate = None

def open_file_dialog():
    global sampling_rate, audio_signal 
    # Open a file dialog and allow the user to select a WAV file
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        # Load the selected WAV file
        sampling_rate, audio_signal = wavfile.read(file_path)
        if audio_signal.dtype == np.int16:
            audio_signal = audio_signal / 32768.0
        elif audio_signal.dtype == np.int32:
            audio_signal = audio_signal / 2147483648.0
        # Print a message indicating that the input is complete
        print("Input complete. File loaded successfully.")
        print(f"Sampling rate: {sampling_rate}")
        print(f"Audio signal: {audio_signal}")
    else:
        print("No file selected.")

def play_audio():
    global sampling_rate, audio_signal
    # Play the audio signal using the sounddevice library
    if audio_signal is not None:
        sd.play(audio_signal, sampling_rate)
        sd.wait()
    else:
        print("No audio loaded.")

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Mint Room Engine")
    root.geometry("450x700")

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    # Define button styles
    button_style = {
        "font": ("Segoe UI Variable", 10),
        "bg": "#F3F3F3",
        "fg": "#000000",
        "activebackground": "#E5E5E5",
        "activeforeground": "#000000",
        "width": 15,
        "height": 2,
        "relief": "flat",
        "borderwidth": 0,
        "highlightthickness": 0
    }

    # Add a button to open the file dialog
    btn_open = tk.Button(button_frame, text="Input New Signal", command=open_file_dialog, **button_style)
    btn_open.pack(side=tk.LEFT, padx=5)
    btn_open = tk.Button(button_frame, text="Apply Algorithm", **button_style)
    btn_open.pack(side=tk.LEFT, padx=5)
    btn_open = tk.Button(button_frame, text="Play Audio", command=play_audio, **button_style)
    btn_open.pack(side=tk.LEFT, padx=5)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()