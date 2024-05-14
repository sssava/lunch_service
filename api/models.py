from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="menu")
    image = models.ImageField(upload_to="menus/")
    menu_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "menu"

    def __str__(self):
        return f"{self.user.username} - {self.menu_date}"


class VotesForMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")
    voting_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="votes")

    class Meta:
        db_table = "votes_for_menu"

    def __str__(self):
        return f"{self.menu.user.role}, {self.voting_date}"
