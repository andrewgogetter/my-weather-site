import re
from collections import Counter


def open_file(path:str) -> str:
    with open(path,"r") as file:
        text:str=file.read()
        return text


def analyzer(text:str) -> dict[str,int]:
    result: dict[str,int] = {
        "The text contains: \n"
        "1. Characters with spaces": len(text),
        "2. Characters without spaces": len(text.replace(" ","")),
        "3. Number of space characters": text.count(" "),
        "4. Number of words": len(text.split())
    }
    return result


def common_words_analyzer(text:str):
    text=text.lower()
    words=re.findall(r"\b\w+\b",text)
    total_words=len(words)
    print(f"Total words in the text: {total_words}\n")
    word_counts=Counter(words)
    common_words=word_counts.most_common(5)
    return common_words


def call_openFile_analyzer() -> None:
    text:str=open_file("my_notes.txt")
    analysis:dict[str,int]=analyzer(text)
    common_words = common_words_analyzer(text)

    for key, value in analysis.items():
        print(f"{key}: {value}")

    print("\nMost common words: ")
    for word,count in common_words:
        print(f"{word}: {count}")


if __name__=="__main__":
    call_openFile_analyzer()