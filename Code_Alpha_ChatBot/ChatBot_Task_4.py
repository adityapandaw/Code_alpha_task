
print("\n Welcome! To AI Chat Bot ")
print(" Chat With AI! \n")

def Chat_Bot(user):

    if (user == "HELLO"):
        return "Hi!\n"
    elif (user == "HOW ARE YOU"):
        return "I'm Fine ,Thanks!\n"
    elif (user == "BYE"):
        return "Good Bye!\n"
    else:
        return "Sorry, I don't understand\n"

while(True):
    user = str(input("You : ")).strip().upper()
    
    response = Chat_Bot(user)
    print(f"Chat Bot : {response}")

    if user == "BYE":
        break