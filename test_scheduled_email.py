from datetime import datetime, timedelta
from scheduled_email import scheduled_email

def test_should_return_message_when_email_scheduled_for():
    message = 'This email is scheduled for today at 10:50.'
    date = datetime.now()
    assert scheduled_email(date) == message

def test_should_return_message_for_tomorrow():
    message_tomorrow = 'This email is scheduled for tomorrow at 10:50.'
    date = datetime.now()
    tomorrow = date+timedelta(days=1)
    assert scheduled_email(tomorrow) == message_tomorrow