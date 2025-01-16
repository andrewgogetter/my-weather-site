morse_code: dict[str,str]={
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    "+": ".-.-.", "-": "-....-", "x": "-...-", "/": "-..-.", "=": "-...-",
    "?": "..--..", "!": "-.-.--", ".": ".-.-.-", ",": "--..--", ";": "-.-.-.", ":": "---...",
    "@": ".--.-.", "_": "..--.-", "(": "-.--.", ")": "-.--.-", "'": ".----."," ": "/"
}

reverse_morse={value:key for key, value in morse_code.items()} #this swapping the keys and values in our dict

def convert_to_morse(user_input:str) -> str:
    return " ".join(morse_code.get(char.upper(), "") for char in user_input) #we use "" to prevent the program from crashing when entering the value that doesn't exist in morse code

def convert_to_text(user_input1:str) -> str:
    morse_words=user_input1.split("/")
    decoded_message=[]

    try:
        for morse_word in morse_words:
            letters=morse_word.split()
            decoded_word="".join(reverse_morse[letter] for letter in letters)
            decoded_message.append(decoded_word)
        return " ".join(decoded_message) #the "join" method auto convert out list into a single string
    except KeyError:
        print("You have to enter Morse code not text!")
        call_morse()


def call_morse() -> None:
    try:
        user_choice:int=int(input("Choose (1) for converting to Morse or (0) for converting to text: "))
        if user_choice==1:
            user_input:str=input("Enter text: ")
            output:str=convert_to_morse(user_input)
            print(output)
        elif user_choice==0:
            user_input1:str=input("Enter Morse code: ")
            output:str=convert_to_text(user_input1)
            print(output)
        else:
            print("You have to enter 1 or 0")
            call_morse()
    except ValueError:
        print("You have to enter a number (1 or 0)")
        call_morse()


if __name__=="__main__":
    call_morse()