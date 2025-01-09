# Multilingual Voice Translation Application

This application allows users to speak into the app, and it translates their spoken words into multiple languages with enhanced understanding and meaning. The translations are outputted in high-quality, natural-sounding audio using a cloned voice for a seamless and personalized experience.

## Features

1. **Languages Supported**: The app supports translations into the following languages:
   - Spanish
   - Hindi
   - Japanese
   - French
   - German
   - Italian

2. **Enhanced Translations**:
   - Utilizes OpenAI's `gpt-4o-mini` for contextual and meaningful translations.
   - Goes beyond literal translations by conveying the intended meaning and explaining idioms.

3. **Professional Voice Cloning**:
   - Leverages ElevenLabs’ professional voice cloning to replicate "Arav’s Voice."
   - Translated audio uses the `eleven-multilingual-v2` model for high-quality multilingual output.

4. **User-Friendly Interface**:
   - Built with Gradio for an intuitive and interactive user interface.

---

## Prerequisites

Before running the application, ensure you have the following:

1. **API Keys**:
   - OpenAI API key
   - ElevenLabs API key

2. **Export the API Keys**:
   Set the environment variables by running these commands in your terminal:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   export ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
   ```

3. **Dependencies**:
   Install the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

---

## Installation and Usage

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/multilingual-voice-translator.git
cd multilingual-voice-translator
```

### Step 2: Install Dependencies
Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Set API Keys
Export your API keys:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
export ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
```

### Step 4: Run the Application
Start the application using Gradio:

```bash
python translator.py
```

### Step 5: Use the Application
- Speak into the microphone.
- The app translates your spoken words into the selected language.
- Translations are outputted as audio in "Arav’s Voice."

---

## How It Works

1. **Input Speech**:
   - The user speaks into the microphone.

2. **Translation with Context**:
   - The app uses OpenAI’s `gpt-4o-mini` to provide contextually meaningful translations, ensuring idioms and nuances are preserved.

3. **Voice Cloning**:
   - ElevenLabs’ professional voice cloning generates natural-sounding translations in "Arav’s Voice."

4. **Output**:
   - The translated text is displayed, and the audio translation is played.

---

## Example Workflow
1. Speak: "It’s raining cats and dogs."
2. Translation (to Spanish): "Está lloviendo a cántaros."
3. Audio Output: Plays the Spanish translation in "Arav’s Voice."

---

## Acknowledgments
This project leverages the following technologies:

- [OpenAI API](https://platform.openai.com/)
- [ElevenLabs](https://elevenlabs.io/)
- [Gradio](https://gradio.app/)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Feedback
If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.

Enjoy using the Multilingual Voice Translation Application!