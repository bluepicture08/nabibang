from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER_CHOICES=(
    ('female', '여자'),
    ('male', '남자')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    age = models.PositiveIntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, blank=True)
    self_introduce = models.TextField(max_length=500, blank=True)
    profile_img = models.ImageField(null=True, blank=True)

    def __str__(self) :
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
