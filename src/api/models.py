import uuid
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models


class AlertMessage(models.Model):
    ALERT_TYPE_CHOICES = (
        ('alert', 'Alert'),
        ('news', 'News'),
        ('information', 'Information'),
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField(
        null=False, blank=False,
        help_text="Detailed down description of message - markdown and html langauge supported"
    )
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPE_CHOICES, null=False, blank=False, default='alert')

    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @classmethod
    def latest_alert(cls):
        messages = cls.objects.filter(is_active=True).order_by('-created_on')
        if messages:
            return messages[0]
        return None
