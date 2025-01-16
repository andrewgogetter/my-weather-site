#Simplified version of the program

# from collections import Counter
# import re
#
#
# def word_frequency(text: str) -> list[tuple[str,int]]:
#     lowered_text: str = text.lower()
#     words: list[str] = re.findall(r"\b\w+\b",lowered_text)
#     words_count: Counter = Counter(words)
#     return words_count.most_common() #it returns the most common word at the top
#
#
# def call_word() -> None:
#     text: str = input("Enter a text: ")
#     get_word: list[tuple[str,int]] = word_frequency(text)
#
#     for word,count in get_word:
#         print(f"{word}: {count}")
#
# if __name__=="__main__":
#     call_word()


#Advanced version of the program

import os

def word_frequency(file_name):
    word_count={}
    if not os.path.isfile(file_name):
        print(f"The file {file_name} was not found")
        return {}

    try:
        with open(file_name,"r") as file:
            text=file.read()
            words=text.split()

            for word in words:
                word=word.lower()
                word=word.strip('.,:;!?()[]{}@#$%^&*-_+=|/')
                if word: #it means that the word is not empty
                    word_count[word]=word_count.get(word,0)+1 #0 means we start from the "0" word, and 1 means we count it as the first

        sorted_words=dict(sorted(word_count.items()))
        return sorted_words

    except Exception as e:
        print(f"An unknown error has occurred: {e}")
        return {}


def user_input():
    file_name=input("Enter the file name: ")
    frequencies=word_frequency(file_name)
    if not frequencies:
        print("No word frequencies was found")
    else:
        for word,count in frequencies.items():
            print(f"{word}: {count}")


if __name__=="__main__":
    user_input()