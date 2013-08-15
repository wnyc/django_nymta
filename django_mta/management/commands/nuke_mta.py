from django.core.management.base import BaseCommand, CommandError
from django_mta.models import Turnstile, TurnstileDownloadComplete

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Turnstile.objects.all().delete()
        TurnstileDownloadComplete.objects.all().delete()
