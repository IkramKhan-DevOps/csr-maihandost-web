from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


"""
At the start please be careful to start migrations
--------------------------------------------------

STEP: 1 comment current_subscription [FIELD] in model [USER]
STEP: 1 py manage.py makemigrations accounts
STEP: 2 py manage.py migrate
Then do next ...

"""


class User(AbstractUser):
    profile_image = ResizedImageField(
        upload_to='accounts/images/profiles/', null=True, blank=True, size=[100, 100], quality=75, force_format='PNG',
        help_text='size of logo must be 100*100 and format must be png image file', crop=['middle', 'center']
    )
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_statistics(self):
        stats = UserStatistics.objects.filter(user__pk=self.pk)
        if not stats:
            return UserStatistics.objects.create(user=self)
        return stats[0]

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        self.profile_image.delete(save=True)
        super(User, self).delete(*args, **kwargs)


class UserStatistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Statistics'
        verbose_name_plural = 'Users Statistics'

    def __str__(self):
        return f"{self.user} Statistics"


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_statics")
def create_user_stats(sender, instance, created, **kwargs):
    """
    :TOPIC if user creates at any point the statistics model will be initialized
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        user = User.objects.get(pk=instance.pk)
        UserStatistics.objects.create(
            user=user
        )


