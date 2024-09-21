#Install pyjokes before execution (!pip install pyjokes)
import pyjokes
joke = pyjokes.get_joke()
response=int(input("want a joke\nPress 1 : "))
if response == 1:
    print(joke)
else:
    print("bloody fool")

