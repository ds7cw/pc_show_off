from django.db.models.signals import post_save
from django.dispatch import receiver
from pc_show_off.accounts.models import AppUser, Profile


@receiver(post_save, sender=AppUser)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
