from django.db import models

# Create your models here.
class Domain(models.Model):
    url = models.URLField(verbose_name="URL to Ping")
    interval = models.PositiveIntegerField(verbose_name="Interval in Seconds", help_text="Time between pings in seconds")
    description = models.TextField(blank=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Active Status")

    def __str__(self):
        return self.url