from tts.engine import speak
from utils.input_handler import get_user_input

def main():
    text = get_user_input()
    speak(text)

if __name__ == "__main__":
    main()
