def send_mail(previous_campaign, campaign, email_list):
    for x in email_list:
        print(
            "email_subject: ",
            campaign,
            ", email_body: ",
            previous_campaign,
            ", sent_to: ",
            x,
        )
