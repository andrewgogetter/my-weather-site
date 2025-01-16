import secrets
import string


class Password:
    def __init__(self,length,uppercase,symbols)->None:
        self.length=length #is the same as "validator.length=16" in the "call_password" func
        self.use_uppercase=uppercase
        self.use_symbols=symbols
        self.base_chars:str=string.ascii_lowercase+string.digits

        if self.use_uppercase:
            self.base_chars+=string.ascii_uppercase
        if self.use_symbols:
            self.base_chars+=string.punctuation

    def generate_password(self)->str:
        password:list[str]=[]
        for i in range(self.length):
            password.append(secrets.choice(self.base_chars))
        return "".join(password)

    def is_valid_password(self,password:str)->bool: #self refers to "validator" as an instance, and "password:str" refers as its object
        if len(password)<16:
            return False
        has_upper=any(c.isupper() for c in password)
        has_lower=any(c.islower() for c in password)
        return has_upper and has_lower


def call_password()->None:
    validator:Password=Password(length=16,uppercase=False,symbols=True) #our "validator" here is the same as "self" in "__init__".
    for i in range(2):
        generated:str=validator.generate_password()
        print(f"{generated}: {len(generated)} chars")
        print(f"Is valid? {validator.is_valid_password(generated)}")


if __name__=="__main__":
    call_password()