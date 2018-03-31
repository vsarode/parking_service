
import way2sms

username = "9657964535"
password = "G8533A"


def send_sms(receiver, message):
    q = way2sms.sms(username, password)
    q.send(unicode(receiver), message)
    n = q.msgSentToday()
    q.logout()


if __name__ == "__main__":
    send_sms("9657964535", "hi")
