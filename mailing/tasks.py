from django_journal.celery import app


@app.task
def send_notification(user_email):
    """
    Тестова функція заглушка.
    Потрібна для відправки повідомлень email\sms\message по контактним даним користувача.
    Розсилку створює вчитель або адміністрація.
    """
    return user_email
