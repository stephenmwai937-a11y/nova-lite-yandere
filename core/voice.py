import os
import sys
from config import VOICE_PROVIDER, VOICE_SPEED, VOICE_PITCH, ELEVENLABS_API_KEY

def speak(text):
    """
    Convert text to speech using Shion's voice characteristics.
    Supports multiple providers: Google, ElevenLabs, pyttsx3
    """
    
    if VOICE_PROVIDER == "google":
        speak_google(text)
    elif VOICE_PROVIDER == "elevenlabs":
        speak_elevenlabs(text)
    elif VOICE_PROVIDER == "pyttsx3":
        speak_pyttsx3(text)
    else:
        print(f"[Voice] Unknown provider: {VOICE_PROVIDER}")

def speak_google(text):
    """
    Use Google Text-to-Speech for natural anime-style voice.
    """
    try:
        from google.cloud import texttospeech
        import subprocess
        
        client = texttospeech.TextToSpeechClient()
        
        synthesis_input = texttospeech.SynthesisInput(text=text)
        
        # Configure voice - female, Japanese-inspired
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-C",  # Female voice
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=VOICE_SPEED,
            pitch=VOICE_PITCH,
        )
        
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config,
        )
        
        # Save and play audio
        with open("temp_audio.mp3", "wb") as out:
            out.write(response.audio_content)
        
        # Play the audio
        play_audio("temp_audio.mp3")
        
    except ImportError:
        print("[Voice] Google Cloud TTS not installed. Install: pip install google-cloud-texttospeech")
    except Exception as e:
        print(f"[Voice Error] Google TTS failed: {str(e)}")

def speak_elevenlabs(text):
    """
    Use ElevenLabs for premium, highly realistic Shion-like voice.
    Requires API key from elevenlabs.io
    """
    try:
        import requests
        
        if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY == "your-elevenlabs-key-here":
            print("[Voice] ElevenLabs API key not set. Using fallback...")
            speak_pyttsx3(text)
            return
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
        
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.85
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            with open("temp_audio.mp3", "wb") as f:
                f.write(response.content)
            play_audio("temp_audio.mp3")
        else:
            print(f"[Voice Error] ElevenLabs failed: {response.status_code}")
    
    except ImportError:
        print("[Voice] requests library not installed. Install: pip install requests")
    except Exception as e:
        print(f"[Voice Error] ElevenLabs TTS failed: {str(e)}")

def speak_pyttsx3(text):
    """
    Fallback to pyttsx3 for offline text-to-speech.
    Less realistic but works offline.
    """
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        engine.setProperty('rate', VOICE_SPEED * 150)  # Speed
        engine.setProperty('pitch', VOICE_PITCH)  # Pitch for feminine voice
        
        # Try to set female voice
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)  # Usually female voice
        
        engine.say(text)
        engine.runAndWait()
        
    except ImportError:
        print("[Voice] pyttsx3 not installed. Install: pip install pyttsx3")
    except Exception as e:
        print(f"[Voice Error] pyttsx3 failed: {str(e)}")

def play_audio(filepath):
    """
    Play audio file using available system player.
    """
    try:
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":  # macOS
            os.system(f"afplay {filepath}")
        else:  # Linux
            os.system(f"aplay {filepath}")
    except Exception as e:
        print(f"[Audio] Could not play: {str(e)}")

def set_voice_provider(provider):
    """
    Dynamically change voice provider.
    """
    global VOICE_PROVIDER
    if provider in ["google", "elevenlabs", "pyttsx3"]:
        VOICE_PROVIDER = provider
        print(f"Voice provider changed to: {provider}")
    else:
        print(f"Unknown provider: {provider}")