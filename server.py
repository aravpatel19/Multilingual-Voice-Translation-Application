from translator import app, audio_files
import os

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 8080))
    app.launch(server_name="0.0.0.0", server_port=port)