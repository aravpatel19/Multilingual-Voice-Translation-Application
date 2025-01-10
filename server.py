from translator import app, audio_files
import os

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 8080))
    app.launch(server_name="localhost", server_port=port)
    
    for file in audio_files:
        print(f"Removing {file}")
        os.remove(f'{file}')