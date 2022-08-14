from autoresponder import AutoResponder

print("Hello! Welcome to Automation. Please choose a number from the options below")
print("1. Autoresponder")
print("2. Ecommerce and Marketing")
print("3. Blank")
print("Hint: Type in '1', '2' or '3' to make a choice.")
automationchoice = int(input())

match automationchoice:
    case 1:
        AutoResponder.Welcome_new_subscribers()
    case 2:
        print("Ecom")
    case 3:
        print("Blank")
    case others:
        print("Invalid choice, start the program again and make a valid choice")
        exit(0)
