from django.core.management.base import BaseCommand
from apps.telegram_bot.views import bot  # Замените на правильный путь к вашему боту

class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('START TELEGRAM BOT'))
        bot.polling(none_stop=True, interval=0)
