from difflib import SequenceMatcher
from datetime import datetime
import requests


class ChatBot:
    def __init__(self,name:str, api_key:str, responses:dict[str,str])->None: #first str means a user input, the second is a bot response
        self.name=name
        self.responses=responses
        self.api_key=api_key
        self.default_response="The similarity rate is too low"

    @staticmethod
    def calc_similarity(input_sentence:str,response_sentence:str)->float:
        sequence:SequenceMatcher=SequenceMatcher(a=input_sentence,b=response_sentence) #it's gonna compare a and b
        return sequence.ratio() #simple as it sounds (ratio between a and b)

    def get_best_response(self,user_input:str)->tuple[str,float]: #str stands for a response and float for how similar it to a user input
        highest_similarity:float=0.0
        best_match:str="No similarities were detected"

        for response in self.responses:
            similarity:float=self.calc_similarity(user_input,response)
            if similarity>highest_similarity:
                highest_similarity=similarity
                best_match:str=self.responses[response]

        return best_match,highest_similarity

    def fetch_weather(self,city:str)->str:
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=imperial"
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            temp=data["main"]["temp"]
            weather_descr=data["weather"][0]["description"]
            return f"The weather in {city} is {temp} F with {weather_descr}"
        else:
            print("Sorry, the weather data is unavailable")


    def run_bot(self)->None:
        print(f"Hello, my name's {self.name}, what can I do for you?")

        while True:
            user_input:str=input("Ask the bot: ")
            if user_input.lower() in ["bye","exit","no","quit","stop"]:
                print("Goodbye! Have a great day!")
                break

            response,similarity=self.get_best_response(user_input) #response here stands for "best_match"

            if similarity<0.5:
                response=self.default_response

            if "weather" in user_input.lower() or "forecast" in user_input.lower():
                city=user_input.lower().replace("weather","").replace("forecast","").replace("in","").strip() #we'll get just the "city" string
                if city:
                    response=self.fetch_weather(city)
                else:
                    response="Please specify a city"

            if response=="GET_TIME":
                response=f"Current time is: {datetime.now():%H:%M}"

            print(f"{self.name}: {response}, have similarity: {similarity:.2f}")


def call_bot()->None:
    api_key="bd1154802d37b66c9b145e27f90f356c"
    responses:dict[str,str]={
        "hello": "Hellow! How are you today?",
        "how are you": "Great, thanks! What about you?",
        "what time is it": "GET_TIME",
        "what can you tell me about yourself": "I'm a bot, you can ask me your questions",
        "what programming language you're written on": "I was written on Python",
        "do you know something about your responses, how it works": "All my functioning is pre-made, and answers depend on the similarity of user questions. More precisely on their ratio",
        "in what languages can you respond": "I can respond only in English as it is the international language and the most common in the world",
        "bye": "Goodbye! Have a great day!"
    }

    chatbot:ChatBot=ChatBot(name="Johny", api_key=api_key, responses=responses)
    chatbot.run_bot()


if __name__=="__main__":
    call_bot()