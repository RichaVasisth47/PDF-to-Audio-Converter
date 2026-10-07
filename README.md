# PDF to Speech Audiobook Converter 🎧

A simple and powerful Python desktop application that converts multi-page PDF documents into high-quality audio files using a clean dark-themed graphical user interface (GUI).

## ✨ Features
- **Modern Dark Theme GUI:** Built with `tkinter` featuring an intuitive and clean user interface.
- **Full Document Support:** Automatically splits long text into manageable chunks and merges them using `pydub` to convert entire multi-page books without length restrictions.
- **100% Free & Open-Source:** Uses `gTTS` (Google Text-to-Speech) and `PyPDF2`—no paid API keys, subscriptions, or credit cards required.
- **Easy Audio Export:** Saves the final output directly as an `output_audio.mp3` file in the project directory.

## 🛠️ Tech Stack
- **Python** (Programming Language)
- **Tkinter** (GUI Framework)
- **PyPDF2** (PDF Text Extraction)
- **gTTS** (Text-to-Speech Engine)
- **Pydub** (Audio Chunk Merging)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/pdf-to-speech-converter.git](https://github.com/your-username/pdf-to-speech-converter.git)
   cd pdf-to-speech-converter

Install the required dependencies:

Bash
pip install gTTS PyPDF2 pydub

Run the application:

Bash
python main.py

🚀 How to Use
Launch the application.

Click on the "Browse PDF & Convert" button.

Select any text-based .pdf file from your computer.

Wait for the status to show "Done! Full audio saved."

Find your output_audio.mp3 file in the project folder and play it!

📄 License
This project is open-source and available for educational and personal use.
