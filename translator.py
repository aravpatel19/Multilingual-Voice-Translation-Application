import gradio as gr
import openai
import elevenlabs
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
import uuid
from pathlib import Path
import os

# List of languages to translate to
languages = ["Spanish", "Hindi", "Arabic", "Japanese", "French", "German", "Italian"]
# Voice ID and model ID for the Eleven Labs API
voice = "9QpnP6IzFuprlUmbvbaP"
voice_model = "eleven_multilingual_v2"
# OpenAI model to use for translation
openai_model = 'gpt-4o-mini'
audio_files = []

# Function to translate the voice input to multiple languages
def voice_to_voice(audio_file):
    # transcribe the audio file
    audio_file = Path(audio_file)
    transcription_response = audio_transcription(audio_file)
    text = transcription_response
    
    for language in languages:
        translation = text_translation(text, language)
        audio_path = Path(text_to_speech(translation, language))
        audio_files.append(audio_path)
    
    print(tuple(audio_files))
    return tuple(audio_files)
        

# Function to transcribe the audio file
def audio_transcription(audio_file):
    
    client = openai.OpenAI()
    
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
    
# Function to translate the text to the target language
def text_translation(text, language):
    
    client = openai.OpenAI()
    
    try:
        # Create a completion using the OpenAI API
        completion = client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role": "system",
                            "content": f"""You are a highly precise English-to-{language} translator. Your sole output must be the {language} translation of the given English text in strict JSON format. 
                            {{"translation": "...", "language": "..."}} 
                            Do not add explanations, commentary, or context. In the translation, you may change some language to ensure the translation is culturally appropriate. Maintain the mood and tone of the original text.

                        Example 1:
                        Input: Hello
                        Output: {{"translation": "Hola", "language": "Spanish"}}
                                {{"translation": "नमस्ते", "language": "Hindi"}}
                                {{"translation": "مرحبا", "language": "Arabic"}}
                                {{"translation": "こんにちは", "language": "Japanese"}}
                                {{"translation": "Bonjour", "language": "French"}}
                                {{"translation": "Hallo", "language": "German"}}
                                {{"translation": "Ciao", "language": "Italian"}}

                        Example 2:
                        Input: How are you?
                        Output: {{"translation": "¿Cómo estás?", "language": "Spanish"}}
                                {{"translation": "आप कैसे हैं?", "language": "Hindi"}}
                                {{"translation": "كيف حالك؟", "language": "Arabic"}}
                                {{"translation": "お元気ですか？", "language": "Japanese"}}
                                {{"translation": "Comment ça va?", "language": "French"}}
                                {{"translation": "Wie geht es dir?", "language": "German"}}
                                {{"translation": "Come stai?", "language": "Italian"}}

                        Example 3:
                        Input: I love programming.
                        Output: {{"translation": "Me encanta programar.", "language": "Spanish"}}
                                {{"translation": "मुझे प्रोग्रामिंग पसंद है।", "language": "Hindi"}}
                                {{"translation": "أنا أحب البرمجة.", "language": "Arabic"}}
                                {{"translation": "私はプログラミングが大好きです。", "language": "Japanese"}}
                                {{"translation": "J'aime programmer.", "language": "French"}}
                                {{"translation": "Ich liebe Programmieren.", "language": "German"}}
                                {{"translation": "Adoro programmare.", "language": "Italian"}}

                        Now translate the provided English text."""
                },
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
    
    import json

    # Assuming `output` contains the string response from the OpenAI API
    translation = completion.choices[0].message.content

    try:
        # Convert the string to a JSON object
        json_object = json.loads(translation)
        print(json_object)
        
        # Access specific fields, if needed
        translation = json_object.get('translation', '')
        language = json_object.get('language', '')
        print(f"Translation: {translation}, Language: {language}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    return translation
    
# Function to convert the translated text to speech
def text_to_speech(text, language):
    
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
    save_file_path = f"./audio-files/{language}-{uuid.uuid4()}.mp3"
    
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

language_dropdown = gr.Dropdown(languages, label="Select a language to translate to:")

language_boxes = []
for language in languages:
    language_boxes.append(gr.Audio(label=language))

app = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=language_boxes
)