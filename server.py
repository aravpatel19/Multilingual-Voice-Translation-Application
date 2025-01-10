from translator import app, audio_files
import os

if __name__ == "__main__":
    app.launch(server_name="localhost", server_port=8080)
    
    for file in audio_files:
        print(f"Removing {file}")
        os.remove(f'{file}')