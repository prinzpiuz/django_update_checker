"""Module for generating and sending message to Microsoft Teams
"""
import pymsteams


def send_teams_msg(teams_url: str, card_title: str, card_link: str, summmary: str):
    """To generate and send message in teans

    Args:
        teams_url (str): teams url
        title (str): tittle for the card
        link (str): link in the card
        summary (str): message summary
    """
    try:
        avatar_url = "https://avatars.githubusercontent.com/u/27804?s=200&v=4"
        teams_message = pymsteams.connectorcard(teams_url)
        teams_message.text(" ")  # this is needed
        teams_message.title(card_title)
        teams_message.color("#0C4B33")
        teams_message_card = pymsteams.cardsection()
        teams_message_card.activityImage(avatar_url)
        teams_message_card.activityTitle(summmary)
        teams_message_card.activitySubtitle(f'<a href="{card_link}">Read More Here</a>')
        teams_message.addSection(teams_message_card)
        teams_message.send()
    except pymsteams.TeamsWebhookException as error:
        print(error)
    print(f"message send status is {teams_message.last_http_response.status_code}")
