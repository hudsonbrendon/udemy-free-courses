from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from courses.models import Course

from telegram import Bot, ParseMode
from twython import Twython
from twython.exceptions import TwythonError


@receiver(post_save, sender=Course) 
def send_message_telegram(sender, instance, **kwargs):
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    bot.send_message(
        chat_id="@udemy_free_courses",
        text=instance.message,
        parse_mode=ParseMode.HTML
    )

@receiver(post_save, sender=Course) 
def send_message_twitter(sender, instance, **kwargs):
    twitter = Twython(settings.TWITTER_API_KEY, 
                      settings.TWITTER_API_SECRET,
                      settings.TWITTER_OAUTH_TOKEN,
                      settings.TWITTER_OAUTH_TOKEN_SECRET)
    try:
        twitter.update_status(status=instance.message)
    except TwythonError as error:
        if error.error_code == 403:
            pass