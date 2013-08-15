from django.db import models
from datetime import datetime
import pytz

class TurnstileDownloadComplete(models.Model):
    name = models.CharField(max_length=100)

class Turnstile(models.Model):
    control_area = models.CharField(max_length=4)
    unit = models.CharField(max_length=4)
    scp = models.CharField(max_length=8)
    datetime = models.DateTimeField()
    entries_counter = models.BigIntegerField()
    exits_counter = models.BigIntegerField()
    entries = models.IntegerField(null=True)
    exits = models.IntegerField(null=True)
    audit = models.CharField(max_length=20, default='REGULAR')

    @classmethod
    def parse(cls, data):
        lines = data.split('\n')
        print len(lines), "lines"
        objects = []
        print "Parsing", len(lines), "lines"
        for line in lines:
            objects.extend(cls.parse_line(line))
        print "Saving", len(objects), "records"
        cls.objects.bulk_create(objects)

    @classmethod
    def parse_line(cls, line):
        line = line.strip()
        if not line: return
        line = line.split(',')
        line.reverse()
        
        control_area = line.pop()
        unit = line.pop()
        scp = line.pop()
        
        while line:
            date = line.pop()
            time = line.pop()
            audit = line.pop()
            entries = line.pop()
            exits = line.pop()
            
            day, month, year = map(int, date.split('-'))
            year += 2000
            
            hour, minute, second = map(int, time.split(':'))
            
            date_time = datetime(day=day, month=month, year=year, hour=hour, minute=minute, second=second, tzinfo=pytz.timezone('US/Eastern'))
            entries = int(entries)
            exits = int(exits)
            
            yield Turnstile(control_area = control_area,
                      unit = unit,
                      scp = scp,
                      datetime = date_time,
                      entries_counter = entries,
                      audit = audit,
                      exits_counter = exits)

    
    

