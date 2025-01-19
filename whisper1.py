import whisper
import os
# Load the Whisper model
model = whisper.load_model("base")
# Transcribe the audio file
# result = model.transcribe("1.mp3")
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "1.mp3"
file_path = os.path.join(current_dir, file_name)
print(file_path)
result = model.transcribe(file_path, fp32=True)

# Output the transcription
print(result["text"])

