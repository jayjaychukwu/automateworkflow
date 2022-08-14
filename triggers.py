def opt_in(list_obj):
    for subscriber in list:
        pass


def time_trigger(list_obj, date, time, timezone):
    pass


def campaign_activity(list_obj, email, activity):
    ACTIVTIES = [
        "sent",
        "opened",
        "not opened",
        "replied",
        "clicked",
        "not clicked",
        "unsubscribed",
        "bounced",
    ]
    if activity not in ACTIVTIES:
        print("Not a valid activity. Check the docs for a valid activity")


def removed_from_list(list_obj):
    pass


def purchase(list_obj, status, product_to_monitor, store_or_payment_platform, products):
    STATUSES = ["purchased", "not purchased", "abadoned cart"]
    if status not in STATUSES:
        print("Invalid status, choose a correct one")


def list_trigger(list_obj):
    pass


def page_visited(list_obj, page, starts_with):
    pass


def registered_or_attended_webinar(list_obj, webinar_or_platform, status):
    pass
