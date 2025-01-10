from translator import app, audio_files
import os

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=8080)
    
    for file in audio_files:
        print(f"Removing {file}")
        os.remove(f'{file}')