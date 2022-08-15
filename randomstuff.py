#Testing out different implementation routes

from actions import Actions
from conditionals import Conditionals

send_mail = Actions.send_mail
is_on_a_list = Conditionals.is_on_a_list

send_mail(
    previous_campaign="Hello",
    campaign="I am here",
    email_list=["hearth@her.com"],
    conditionals=is_on_a_list("heart@her.com", ["heart@her.com"]), #This is a problem, Make conditionals entities on their own 
    next_action=Actions.add_to_list,
)
