from django.db.models.signals import pre_save, post_save
from django.core.signals import request_started, request_finished
from django.contrib.auth.models import User
from django.dispatch import receiver

def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email !='':
        user.username = user.email
    print('Signal Triggerre')

@receiver(pre_save, sender=User)
def afterFinishedUpdateWithDecorator(sender, **kwargs):
    print(sender.username)
    print('Signla connect by decorator : After')

@receiver(post_save, sender=User)
def beforeRequestUpdateWithDecorator(sender, **kwargs):
    print('Signla connect by decorator : Before')

pre_save.connect(updateUser, sender=User)
