import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


def check_status(url:str) -> None:
    try:
        r: Response=requests.get(url)
        status_code:int=r.status_code
        headers:CaseInsensitiveDict[str]=r.headers #[str] stands for the dict keys. The "headers" are the keys, and we get in the console their values
        content_type:str=headers.get("Content-Type","Unknown") #the second param is by default. The "Content-Type" is the key, so we'll get the value in the console
        server:str=headers.get("Server","Unknown")
        r_time:float=r.elapsed.total_seconds()

        print(f"URL: {url}")
        print(f"Status code: {status_code}")
        print(f"Content type: {content_type}")
        print(f"Server: {server}")
        print(f"Response time: {r_time:.2f} seconds")
    except RequestException as e:
        print(f"Error: {e}")


def call_check_status() -> None:
    url:str="https://www.nationalgeographic.com/"
    check_status(url=url)


if __name__=="__main__":
    call_check_status()