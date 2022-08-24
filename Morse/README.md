# Morse Encrypt/Decrypter With Python

**You Can Simply Use This Project To Convert Any Text To Morse Code And Do Anything That You Want !**

## Installation

```
git clone https://github.com/Arshiatmi/Morse
cd Morse
python example.py # Run your Code Here
```

## Usage

```
import morse

instance = morse.Morse()
instance("Hello World") # Encrypt To Morse
instace(".... . .-.. .-.. ---",mode=Mode.decrypt) # Decrypt To Text

# Or Like This
instance.encrypt("Hello World")
instance.decrypt(".... . .-.. .-.. ---")

# Or Like This
instance.morse("Hello World")
instance.text(".... . .-.. .-.. ---")


# You Can Use This Class Like This
print(instance) # Prints The Last Morse Code
print(len(instance)) # Prints The Length Of The Last Morse Code ( In English Characters Not Morse Characters )
print(instance.raw_morse) # Prints The Last Morse Code In Raw Format
print(instance.last_morse) # Prints The Last Morse Code With Escaped Characters
```

# Built With

- [Python](https://www.python.org) - Scripting Language

## Authors

- **Arshia Tamimi** - [MegaExpert](https://github.com/Arshiatmi)
