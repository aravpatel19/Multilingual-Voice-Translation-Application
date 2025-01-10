
# Multilingual Voice Translation Application

This application allows users to speak into the app, and their speech is translated into multiple languages, providing meaningful and context-aware translations. The application leverages advanced AI tools, including **ElevenLabs** for voice cloning and **OpenAI's GPT-4o-mini** for natural and nuanced translations.

You can try it out here: [Multilingual Voice Translation Application](https://multilingual-voice-translator-aravpatel.azurewebsites.net/)

---

## Features

- **Natural Translations:** Uses OpenAI's GPT-4o-mini for translations that accurately convey the meaning, including idioms and expressions.
- **Voice Cloning:** Utilizes ElevenLabs to clone "Arav's Voice," ensuring translations sound natural and authentic.
- **Supported Languages:** 
  - Spanish
  - Hindi
  - Arabic
  - Japanese
  - French
  - German
  - Italian
- **User-Friendly Interface:** Built with **Gradio** for a seamless user experience.

---

## Requirements

- **OpenAI API key**
- **ElevenLabs API key**
- Python 3.8 or above
- Dependencies listed in `requirements.txt`

---

## Setup Instructions

1. Clone the repository:
   ```bash
   gh repo clone aravpatel19/Multilingual-Voice-Translation-Application
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Export your API keys:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   export ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
   ```

4. Run the application:
   ```bash
   gradio translator.py
   ```

---

That's it! You're ready to use the Multilingual Voice Translation Application.
