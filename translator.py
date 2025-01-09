import gradio as gr
import openai
from openai import OpenAI
import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings
import uuid
from pathlib import Path

languages = ["Spanish", "Hindi", "Japanese", "French", "German", "Italian"]
voice = "9QpnP6IzFuprlUmbvbaP"
voice_model = "eleven_multilingual_v2"
openai_model = 'gpt-4o-mini'

def voice_to_voice(audio_file):
    
    # transcribe the audio file
    audio_file = Path(audio_file)
    transcription_response = audio_transcription(audio_file)
    text = transcription_response
    
    audio_files = []
    for language in languages:
        translation = text_translation(text, language)
        audio_path = Path(text_to_speech(translation))
        audio_files.append(audio_path)
    
    print(tuple(audio_files))
    return tuple(audio_files)
        

def audio_transcription(audio_file):
    
    client = OpenAI()
    
    try:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="text"
        )
    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        raise gr.Error(f"OpenAI API returned an API Error: {e}")
    
    except openai.APIConnectionError as e:
        #Handle connection error here
        raise gr.Error(f"Failed to connect to OpenAI API: {e}")
        
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        raise gr.Error(f"OpenAI API request exceeded rate limit: {e}")
    
    return transcription
    
def text_translation(text, language):
    
    client = OpenAI()
    
    try:
        completion = client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role": "system", "content": f"You are a translator. Translate the following text into {language}. Maintain the general mood and tone of the text."},
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        raise gr.Error(f"OpenAI API returned an API Error: {e}")
    except openai.APIConnectionError as e:
        #Handle connection error here
        raise gr.Error(f"Failed to connect to OpenAI API: {e}")
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        raise gr.Error(f"OpenAI API request exceeded rate limit: {e}")
    
    return completion.choices[0].message.content
    
def text_to_speech(text):
    client = ElevenLabs()
    
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=voice, # Arav voice
        output_format="mp3_22050_32",
        text=text,
        model_id=voice_model, # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )
    
    # Generating a unique file name for the output MP3 file
    save_file_path = f"./audio-files/{uuid.uuid4()}.mp3"
    
    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
                
    print(f"{save_file_path}: A new audio file was saved successfully!")
    
    # Return the path of the saved audio file
    return save_file_path

audio_input = gr.Audio(
    sources=["microphone"],
    type='filepath'
)

languages = ["Spanish", "Japanese", "French", "German", "Italian", "Hindi"]
language_dropdown = gr.Dropdown(languages, label="Select a language to translate to:")

language_boxes = []
for language in languages:
    language_boxes.append(gr.Audio(label=language))

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=language_boxes
)

if __name__ == "__main__":
    demo.launch()
    