from actions import send_mail


class Ecommerce_and_Marketing:
    def Thank_first_time_customers(product: str, email_list: list):
        product = input("What did the user buy? ")
        email_add = input("What is the user's address? ")
        template = "Thank you for purchasing from us!"
        campaign = "Keep buying from us! We appreciate you " + email_add.split("@")[0]
        send_mail(previous_campaign=template, campaign=campaign, email_list=[email_add])
        return print(template, campaign)

    def Enable_order_notifications():
        pass

    def Turn_on_an_abadoned_cart_email():
        pass

    def Retarget_site_visitors():
        pass
