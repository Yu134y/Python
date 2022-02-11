from apscheduler.schedulers.background import BackgroundScheduler
from .methods import send_tweets


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_tweets,
        'interval',
        seconds=30,
    )
    scheduler.start()
