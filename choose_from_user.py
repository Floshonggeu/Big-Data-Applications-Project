def choosemodel():
    # Asking the user what model he wants to use
    userchoice = input("What model do you want to use?\n Write '1' for Random Forest,\n Write '2' for Gradient Boosting,\n Write '3' for XGBoost")
    return userchoice

def verifychoice(userchoice):
    # Verifying that the user has entered a correct value
    if ((userchoice != '1') and (userchoice != '2') and (userchoice != '3')):
        # Printing error message
        print("You have to write 1, 2, or 3! Try again")
        # Indicating that the entry isn't right
        return 0
    else:
        # Indicating that everything is alright
        return 1

def choiceloop():
    # Defining variable to verify the entry
    verifiedmodel = 0
    # If the user input isn't good, try again and again until it is good
    while (verifiedmodel != 1):
        # Asking the user what model he wants to use
        userchoice = choosemodel()
        # Verifying that the user's choice is good
        verifiedmodel = verifychoice(userchoice)
        # Transforming the user's input to int
        if (verifiedmodel == 1):
            chosenmodel = int(userchoice)
    return chosenmodel

def chooseestimators():
    # Asking user how many estimators he wants to use
    estimators = int(input("How many estimators do you want?"))
    return estimators

def anothermodel():
	# Asking user if he wants build another model
	anotherone = int(input("Write '1' if you want to build another model, '0' if you want to stop"))
	return anotherone