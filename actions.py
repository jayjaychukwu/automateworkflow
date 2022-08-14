class Actions:
    def send_mail(previous_campaign, campaign, email_list: list):
        for x in email_list:
            print(
                "email_subject: ",
                campaign,
                ", email_body: ",
                previous_campaign,
                ", sent_to: ",
                x,
            )

    def add_delay():
        pass

    def add_to_list():
        pass

    def remove_from_list():
        pass

    def apply_tags():
        pass

    def remove_tags():
        pass

    def auto_register_for_webinar():
        pass
