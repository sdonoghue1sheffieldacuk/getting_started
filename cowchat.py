import cowsay
cowsay.cow("hello! mooo")

while True:
    input_text = input("Chat, or type 'quit': ")
    if input_text.lower() == "quit":
        cowsay.cow("Goodbye! Moo! Moo! Moo!")
        break

    cowsay.cow(input_text + " Moo!")