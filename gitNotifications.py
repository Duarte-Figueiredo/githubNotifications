import sys
from github import Github
from RssBuilder import RssBuilderObj


def login(api_token):
    return Github(api_token)


def convert_to_rss(notification_list):
    rss = RssBuilderObj.RssBuilder("Github notifications")

    for notification in notification_list:
        rss.add_item(get_notification_item(notification))

    return rss.to_xml()


def get_notification_item(notification):
    return RssBuilderObj.RssItem(
        notification.subject.title,
        notification.reason,
        remove_api_link(notification.subject.url)
    )


def remove_api_link(git_link):
    return git_link.replace("api.", "").replace("repos/", "")


def get_notification_thread(g_user, notification_id):
    return g_user.get_notification(notification_id)


def get_unread_notifications(g_user):
    return g_user.get_notifications()


def get_notification_title(notification):
    return notification.subject.title


def main():
    g_user = login(sys.argv[1]).get_user()

    print(convert_to_rss(get_unread_notifications(g_user)))


if len(sys.argv) < 2:
    print("usage: python gitNotification.py <API_TOKEN>")
main()
