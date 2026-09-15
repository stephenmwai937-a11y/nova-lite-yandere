# Nova Lite configuration

NOVA_NAME = "Nova"

MODEL_PATH = "models/nova-model.gguf"

MEMORY_FILE = "data/memory.json"

# ChatGPT/OpenAI Integration
OPENAI_API_KEY = "your-api-key-here"  # Replace with your actual API key
USE_CHATGPT = True  # Enable ChatGPT integration

# Desktop Access
DESKTOP_PATH = "~/Desktop"
ENABLE_DESKTOP_ACCESS = True
ENABLE_FILE_OPERATIONS = True
ENABLE_SCREEN_CAPTURE = False  # Set to True if you want screenshot capability

# Avatar Settings
AVATAR_TYPE = "ascii"  # Options: "ascii", "image"
AVATAR_PATH = "assets/nova_avatar.png"

# Voice Settings (Shion from "That Time I Got Reincarnated as a Slime")
ENABLE_VOICE = True  # Enable/disable voice synthesis
VOICE_PROVIDER = "google"  # Options: "google", "elevenlabs", "pyttsx3"
VOICE_SPEED = 1.0  # 0.5 to 2.0 (0.5 = slow, 1.0 = normal, 2.0 = fast)
VOICE_PITCH = 1.2  # 0.5 to 2.0 (higher = more feminine/Shion-like)

# ElevenLabs Settings (for premium Shion voice)
ELEVENLABS_API_KEY = "your-elevenlabs-key-here"
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Shion-like voice ID

# Learning Settings
ENABLE_LEARNING = True
MAX_MEMORIES = 1000
CONTEXT_WINDOW = 10  # Number of previous messages to remember
