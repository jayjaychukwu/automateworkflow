from autoresponder import AutoResponder
from ecom_marketing import Ecommerce_and_Marketing
import blank

print("Hello! Welcome to Automation. Please choose a number from the options below")
print("1. Autoresponder")
print("2. Ecommerce and Marketing")
print("3. Blank")
print("Hint: Type in '1', '2' or '3' to make a choice.")
automationchoice = int(input())

match automationchoice:
    case 1:
        print("You have chosen Autoresponder")
        print("What would you like to do? Choose Below")
        print("1. Welcome New Subcribers")
        print("2. Respond to Subscriber changes")
        print("Type in either '1' or '2'")
        autoresponder_choice = int(input())
        match autoresponder_choice:
            case 1:
                AutoResponder.Welcome_new_subscribers()
            case 2:
                AutoResponder.Respond_to_subscriber_changes()
            case others:
                print("Invalid choice! Choose 1 or 2, start again!")
                exit(0)
    case 2:
        print("You have chosen Ecommerce and Marketing")
        print("What would you like to do? Choose Below")
        print("1. Thank first-time customers")
        print("2. Enable order notifications")
        print("3. Turn on an abadoned cart email")
        print("4. Retarget site visitors")
        print("Type in either '1', '2', '3' or '4'")
        autoresponder_choice = int(input())
        match autoresponder_choice:
            case 1:
                Ecommerce_and_Marketing.Thank_first_time_customers()
            case 2:
                Ecommerce_and_Marketing.Enable_order_notifications()
            case 3:
                Ecommerce_and_Marketing.Turn_on_an_abadoned_cart_email()
            case 4:
                Ecommerce_and_Marketing.Retarget_site_visitors()
            case others:
                print("Invalid choice! Choose 1 or 2, start again!")
                exit(0)
    case 3:
        print("You have chosen Blank")
        #collect the name of the automation
        # name = Blank()
        #define the rest with name.trigger, name.action, name.conditional
        print("Choose a Trigger element")
        print("1. opt-in 2. Time trigger 3. Campaign Activity 4. Remove from list")
        print("5. Purchase 6. List Trigger 7. Page Visited 8. Registered or attended webinar")
        trigger_choice = int(input())
        match trigger_choice:
            case 1:
                Ecommerce_and_Marketing.Thank_first_time_customers()
            case 2:
                Ecommerce_and_Marketing.Enable_order_notifications()
            case 3:
                Ecommerce_and_Marketing.Turn_on_an_abadoned_cart_email()
            case 4:
                Ecommerce_and_Marketing.Retarget_site_visitors()
            case 5:
                Ecommerce_and_Marketing.Thank_first_time_customers()
            case 6:
                Ecommerce_and_Marketing.Enable_order_notifications()
            case 7:
                Ecommerce_and_Marketing.Turn_on_an_abadoned_cart_email()
            case 8:
                Ecommerce_and_Marketing.Retarget_site_visitors()
            case others:
                print("Invalid choice! Choose 1 or 2, start again!")
                exit(0)
    case others:
        print("Invalid choice, start the program again and make a valid choice")
        exit(0)
