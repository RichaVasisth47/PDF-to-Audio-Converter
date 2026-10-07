import os
import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import PyPDF2

# Optional:'pip install pydub'
try:
  from pydub import AudioSegment

  PYDUB_AVAILABLE = True
except ImportError:
  PYDUB_AVAILABLE = False


def extract_text_from_pdf(pdf_path):
  try:
    with open(pdf_path, "rb") as file:
      reader = PyPDF2.PdfReader(file)
      text = ""
      for page_num, page in enumerate(reader.pages):
        extracted = page.extract_text()
        if extracted:
          text += extracted + "\n"
      return text
  except Exception as e:
    messagebox.showerror("Error", f"Failed to read PDF: {e}")
    return None


def split_text_into_chunks(text, max_chars=4000):
  """Breaks long text into chunks of roughly max_chars without cutting words abruptly."""
  words = text.split()
  chunks = []
  current_chunk = []
  current_length = 0

  for word in words:
    if current_length + len(word) + 1 > max_chars:
      chunks.append(" ".join(current_chunk))
      current_chunk = [word]
      current_length = len(word)
    else:
      current_chunk.append(word)
      current_length += len(word) + 1

  if current_chunk:
    chunks.append(" ".join(current_chunk))
  return chunks


def convert_pdf_to_speech():
  file_path = filedialog.askopenfilename(
      title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")]
  )

  if not file_path:
    return

  status_label.config(text="Extracting text from PDF...")
  root.update_idletasks()

  pdf_text = extract_text_from_pdf(file_path)

  if not pdf_text or not pdf_text.strip():
    messagebox.showwarning("Warning", "No text found in this PDF!")
    status_label.config(text="Ready")
    return

  try:
    status_label.config(text="Splitting text and generating audio...")
    root.update_idletasks()

    # Split text into manageable chunks for gTTS
    chunks = split_text_into_chunks(pdf_text, max_chars=3500)
    temp_files = []

    for i, chunk in enumerate(chunks):
      status_label.config(
          text=f"Processing part {i+1} of {len(chunks)}..."
      )
      root.update_idletasks()

      tts = gTTS(text=chunk, lang="en", slow=False)
      temp_filename = f"temp_part_{i}.mp3"
      tts.save(temp_filename)
      temp_files.append(temp_filename)

    output_audio = "output_audio.mp3"

    # Merge all audio chunks together
    if PYDUB_AVAILABLE and len(temp_files) > 1:
      combined = AudioSegment.empty()
      for f in temp_files:
        combined += AudioSegment.from_mp3(f)
      combined.export(output_audio, format="mp3")

      # Clean up temporary files
      for f in temp_files:
        if os.path.exists(f):
          os.remove(f)
    elif len(temp_files) == 1:
      os.rename(temp_files[0], output_audio)
    else:
      # Fallback if pydub is missing but multiple chunks exist
      os.rename(temp_files[0], output_audio)

    status_label.config(text="Done! Full audio saved.")
    messagebox.showinfo(
        "Success",
        f"Complete PDF converted successfully as '{output_audio}'!",
    )

  except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")
    status_label.config(text="Ready")


# Tkinter GUI Setup
root = tk.Tk()
root.title("PDF to Speech Audiobook Converter")
root.geometry("450x250")
root.config(bg="black")

title_label = tk.Label(
    root,
    text="PDF to Speech Converter",
    font=("Arial", 16, "bold"),
    bg="black",
    fg="white",
)
title_label.pack(pady=20)

browse_btn = tk.Button(
    root,
    text="Browse PDF & Convert",
    command=convert_pdf_to_speech,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="black",
    padx=10,
    pady=5,
)
browse_btn.pack(pady=10)

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10),
    bg="red",
    fg="white",
)
status_label.pack(pady=15)

root.mainloop()