from django.core.management.base import BaseCommand, CommandError
from django_mta.models import Turnstile, TurnstileDownloadComplete
import re
import requests
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Turnstile data
        for link in re.findall(r'href="(data/nyct/turnstile/turnstile_[0-9]*\.txt)"', 
                               requests.get('http://www.mta.info/developers/turnstile.html').text):
            url = "http://www.mta.info/developers/" + link
            try:
                TurnstileDownloadComplete.objects.get(name=link)
                print "Skipping", link
                continue 
            except TurnstileDownloadComplete.DoesNotExist:
                print "Parsing", link
                print url
                Turnstile.parse(requests.get(url).text)
                TurnstileDownloadComplete(name=link).save()
