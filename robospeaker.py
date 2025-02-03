
import os
def speak(text):
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
              f'$speak.Speak(\'{text}\')"'
    os.system(command)

# The initial message
def main():
  speak("Welcome to Robo Speaker 1.1 created by Ankita")

# Asking for user input
  while True:
   a = input("Enter how I can help: ")
   if a=="q":
      break
   speak(f" {a}")

if __name__ == "__main__":
    main()
