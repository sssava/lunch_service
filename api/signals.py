from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Menu, VotesForMenu


@receiver(post_save, sender=Menu)
def create_votes_for_menu(sender, instance, created, **kwargs):
    if created:
        VotesForMenu.objects.create(menu=instance)
