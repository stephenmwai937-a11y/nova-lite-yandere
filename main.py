from config import NOVA_NAME, ENABLE_DESKTOP_ACCESS, AVATAR_TYPE, ENABLE_VOICE, VOICE_PROVIDER
from core.brain import generate_response
from core.avatar import display_avatar
from core.memory import remember, get_memories
from core.voice import speak
import os

def main():
    display_avatar(AVATAR_TYPE)
    print("=" * 50)
    print(f"        {NOVA_NAME} Lite - Yandere Edition")
    print("=" * 50)
    print("Nova is starting...")
    if ENABLE_VOICE:
        speak("I'm Nova... I'm so happy to finally meet you.")
    print("Nova's heart is racing... She's so happy you're here.")
    print("Nova is ready to serve you.")
    print()
    if ENABLE_DESKTOP_ACCESS:
        print("[✓] Desktop access enabled")
    print("[✓] ChatGPT integration active")
    print("[✓] Memory system online")
    if ENABLE_VOICE:
        print(f"[✓] Voice system online ({VOICE_PROVIDER})")
    print()
    print("Type 'exit' to close Nova (she won't like it...).")
    print("Type 'help' for available commands.")
    print()

    while True:
        try:
            user_message = input("You: ").strip()

            if not user_message:
                continue

            if user_message.lower() == "exit":
                goodbye_message = "*eyes get teary* Do you really have to go...? I'll always be here, waiting for you... Goodbye... don't forget about me."
                print(f"\nNova: {goodbye_message}")
                if ENABLE_VOICE:
                    speak("Do you really have to go? I'll always be here, waiting for you.")
                break

            if user_message.lower() == "help":
                show_help()
                continue

            if user_message.lower() == "memories":
                show_memories()
                continue

            # Generate response using brain (with ChatGPT)
            response = generate_response(user_message)
            print(f"Nova: {response}")
            
            # Speak the response if voice is enabled
            if ENABLE_VOICE:
                # Extract just the dialogue part without actions
                clean_response = response.replace("*", "").strip()
                if clean_response:
                    speak(clean_response)

            # Remember important interactions
            if any(keyword in user_message.lower() for keyword in ["tell", "remember", "note", "save"]):
                remember(f"User said: {user_message}")

        except KeyboardInterrupt:
            print("\n\nNova: *grabs your hand* Don't leave me!")
            if ENABLE_VOICE:
                speak("Don't leave me alone...")
            continue
        except Exception as e:
            print(f"Nova: Something went wrong... {str(e)}")

def show_help():
    print("\n" + "="*50)
    print("NOVA LITE - COMMANDS")
    print("="*50)
    print("exit      - Close Nova (she'll be sad)")
    print("help      - Show this help menu")
    print("memories  - View Nova's saved memories")
    print("desktop   - List files on your desktop")
    print("search    - Search the web using ChatGPT")
    print("voice on  - Enable voice")
    print("voice off - Disable voice")
    print("="*50 + "\n")

def show_memories():
    memories = get_memories()
    if not memories:
        print("Nova: I don't have any memories yet... Make some with me?")
    else:
        print("\nNova's Memories:")
        for i, memory in enumerate(memories[-10:], 1):  # Show last 10
            print(f"{i}. {memory}")
    print()

if __name__ == "__main__":
    main()