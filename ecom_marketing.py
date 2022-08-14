from actions import Actions

send_mail = Actions.send_mail


class Ecommerce_and_Marketing:
    def Thank_first_time_customers(product: str, email_list: list):
        product = input("What did the user buy? ")
        email_add = input("What is the user's address? ")
        template = "Thank you for purchasing from us!"
        campaign = "Keep buying from us! We appreciate you " + email_add.split("@")[0]
        send_mail(previous_campaign=template, campaign=campaign, email_list=[email_add])
        return print(template, campaign)

    def Enable_order_notifications(product, other_products):
        product = input("What did the user add to his/her cart? ")
        other_products = input("What other things did the user see? ")
        email_add = input("What is the email address of this user? ")
        template = (
            "Here is your receipt! Remember those other things you saw like "
            + other_products
            + " they are still available."
        )
        campaign = "Be free to come back anytime!"
        return send_mail(
            previous_campaign=template, campaign=campaign, email_list=[email_add]
        )

    def Turn_on_an_abadoned_cart_email(product: str, email_list: list):
        product = input("What did the user add to his/her cart? ")
        email_add = input("What is the email address of this user? ")
        template = "We noticed you haven't checked out your cart"
        campaign = "Look at all the nice things in your cart!"
        return send_mail(
            previous_campaign=template, campaign=campaign, email_list=[email_add]
        )

    def Retarget_site_visitors():
        product = input("What did the user see on your page? ")
        email_add = input("Email address of the user? ")
        template = (
            "Hey! Remember that " + product + " you saw on our site? It's available"
        )
        campaign = "Don't forget the cool stuff you saw!"
        return send_mail(template, campaign, [email_add])
