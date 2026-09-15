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

# Learning Settings
ENABLE_LEARNING = True
MAX_MEMORIES = 1000
CONTEXT_WINDOW = 10  # Number of previous messages to remember
