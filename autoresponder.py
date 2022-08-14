from actions import send_mail


class AutoResponder:
    def Welcome_new_subscribers():
        user = input("What is your name? ")
        email_add = input("What is your email address? ")
        template = "Welcome New Subscriber!"
        campaign = "You,re welcome " + user
        send_mail(previous_campaign=template, campaign=campaign, email_list=[email_add])
        return print(template, campaign)

    def Respond_to_subscriber_changes():
        email_add = input("What is your email address? ")
        changes = input("What do you want to change? ")
        template = "You have made some changes"
        campaign = "Changes made successfully!"
        send_mail(previous_campaign=template, campaign=campaign, email_list=[email_add])
        return print(template, campaign)
