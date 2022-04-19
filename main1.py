# name: str = ""
import datetime

truefalse: bool = True


def hello_xy(name: str = "default") -> str:
    if truefalse:
        print("True")
    if not truefalse:
        print("False")
        if name == "default":
            name = input("What is your name? ")
    else:
        print(f"I know you! Your name is {name}")
    return f"{datetime.datetime.now()} - Hello {name}!"


print(hello_xy())
# print(hello_xy("kecskeeee"+"3"))
# print(hello_xy(name="ez egy név"))
