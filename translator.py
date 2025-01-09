import gradio as gr
import assemblyai as aai
import os

assembly_api_key = os.environ.get('ASSEMBLY_API_KEY')

def voice_to_voice(audio_file):
    
    # transcribe the audio file
    transcription_response = audio_transcription(audio_file)
    
    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text
        

def audio_transcription(audio_file):
    aai.settings.api_key = assembly_api_key
    
    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)
    
    return transcription
    
def text_translation():
    return True
    
def text_to_speech():
    return True

audio_input = gr.Audio(
    sources=["microphone"],
    type='filepath'
)


demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="Japanese"), gr.Audio(label="French"), gr.Audio(label="German"), gr.Audio(label="Italian")]
)

if __name__ == "__main__":
    demo.launch()
    