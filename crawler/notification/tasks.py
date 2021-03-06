from django.db.models import Sum
from django.utils import timezone
from celery.utils.log import get_task_logger

from . import models, utils
from crawler.celery import crawler
from agency import models as age_models

logger = get_task_logger(__name__)


@crawler.task(name="count_daily_news")
def count_daily_news():
    logger.info(f"count_daily_news started at {timezone.localtime()}")
    yesterday = timezone.localtime() - timezone.timedelta(days=1)
    new_links = (
        age_models.Report.objects.filter(created_at__gt=yesterday).aggregate(
            Sum("new_links")
        )["new_links__sum"]
        or 0
    )
    message = f"Today we saw {new_links} new links"
    bot = models.TelegramBot.objects.first()
    account = models.TelegramAccount.objects.first()
    utils.telegram_bot_sendtext(bot.telegram_token, account.chat_id, message)
