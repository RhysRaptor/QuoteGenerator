def userInputs():
    #defining some variables
    failedInputs = 0
    noOfCharacters = 0

    #input verification
    while noOfCharacters < 1 or noOfCharacters > 6:
        try:
            noOfCharacters = int(input("Enter the number of characters, from 1-6."))
        except ValueError:
            print("This isn't a number.")
            failedInputs += 1

        failedInputs += 1
        
        failingToInput(failedInputs)
        
        #funny computer dialogue

    failingToInput(failedInputs)
    
    print(noOfCharacters)

def failingToInput(failedInputs2):
    match failedInputs2:
            case 3:
                print("This is not a difficult step.")
            case 4:
                print("This is getting ridiculous.")
            case 5:
                print("Okay I'm tired.")
            case 6:
                print("Meme stop it.")

userInputs()

