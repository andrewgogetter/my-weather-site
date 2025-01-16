import json
import requests


#JSON version of the currency converter
# def load_rates(json_file:str)->dict[str,dict]:
#     with open(json_file,"r") as file:
#         return json.load(file)
#
# def show_valid_currencies(currency_storage:dict[str,dict])->None:
#     valid_currencies=list(currency_storage.keys())
#     print("Valid currencies are: ")
#     print(", ".join(valid_currencies)) #", " means just words separated by a comma
#
#
# def convert(currency_amount:float,from_currency:str,to_currency:str,currency_storage:dict[str,dict])->float:
#     from_currency:str=from_currency.upper()
#     to_currency:str=to_currency.upper()
#
#     from_currency_data=currency_storage.get(from_currency)
#     to_currency_data=currency_storage.get(to_currency)
#
#     if from_currency_data is not None and to_currency_data is not None:
#         if from_currency=="eur":
#             return currency_amount*to_currency_data["rate"]
#         else:
#             return currency_amount*(to_currency_data["rate"]/from_currency_data["rate"])
#     else:
#         print("Object that you entered is None!")
#         return
#
#
# def call_rates_convert()->None:
#     currency_rates=load_rates("currency_storage.json") #is the same as "currency_storage"
#
#     while True:
#         try:
#             currency_amount=float(input("Enter the amount to convert: "))
#             from_currency=input("Enter the currency you want to convert from (e.g., EUR): ")
#             to_currency=input("Enter the currency you want to convert to (e.g., USD): ")
#             currency_result=convert(currency_amount,from_currency,to_currency,currency_rates) #we're calling the "convert" func
#
#             if currency_result is not None:
#                 print(f"{currency_amount} {from_currency.upper()} is equal to {currency_result:.2f} {to_currency.upper()}")
#             else:
#                 print("Conversion failed. You might've entered the wrong value. Please try again!")
#                 show_valid_currencies(currency_rates)
#
#             repeat_currency=input("Do you want to perform another conversion (yes/no): ").strip().lower()
#             if repeat_currency!="yes":
#                 break
#
#         except ValueError:
#             print("You have entered the wrong value. Please enter a number for amount!")
#
# if __name__=="__main__":
#     call_rates_convert()


#API version of the currency converter
API_KEY="c4048a1b5646413cacaafd1a0f2c8fe6"
API_URL="http://data.fixer.io/api/latest"


def load_rates()->dict[str,dict]:
    r=requests.get(f"{API_URL}?access_key={API_KEY}")
    data=r.json()

    if r.status_code!=200 or not data.get("success"):
        raise Exception("Fetching data error from the API")

    rates=data["rates"]
    return {currency:{"rate":rate} for currency,rate in rates.items()} #currency and "rate" stand for the keys because we have outer and inner dicts. Rates stand for the name


def show_valid_currencies(currency_storage:dict[str,dict])->None:
    valid_currencies=list(currency_storage.keys())
    print("Valid currencies are: ")
    print(", ".join(valid_currencies)) #", " means just words separated by a comma


def convert(currency_amount:float,from_currency:str,to_currency:str,currency_storage:dict[str,dict])->float:
    from_currency:str=from_currency.upper()
    to_currency:str=to_currency.upper()

    from_currency_data=currency_storage.get(from_currency)
    to_currency_data=currency_storage.get(to_currency)

    if from_currency_data is not None and to_currency_data is not None:
        if from_currency=="eur":
            return currency_amount*to_currency_data["rate"]
        else:
            return currency_amount*(to_currency_data["rate"]/from_currency_data["rate"])
    else:
        print("Object that you entered is None!")
        return


def call_rates_convert()->None:
    currency_rates=load_rates()

    while True:
        try:
            currency_amount=float(input("Enter the amount to convert: "))
            from_currency=input("Enter the currency you want to convert from (e.g., EUR): ")
            to_currency=input("Enter the currency you want to convert to (e.g., USD): ")
            currency_result=convert(currency_amount,from_currency,to_currency,currency_rates) #we're calling the "convert" func

            if currency_result is not None:
                print(f"{currency_amount} {from_currency.upper()} is equal to {currency_result:.2f} {to_currency.upper()}")
            else:
                print("Conversion failed. You might've entered the wrong value. Please try again!")
                show_valid_currencies(currency_rates)

            repeat_currency=input("Do you want to perform another conversion (yes/no): ").strip().lower()
            if repeat_currency!="yes":
                break

        except ValueError:
            print("You have entered the wrong value. Please enter a number for amount!")

if __name__=="__main__":
    call_rates_convert()