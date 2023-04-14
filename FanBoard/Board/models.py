from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.get_username()}'


tanks = 'TK'
heals = 'HL'
DD = 'DD'
merchants = 'MC'
GuildMasters = 'GM'
QuestGivers = 'QG'
Blacksmiths = 'BM'
Tanners = 'TR'
PotionMakers = 'PM'
SpellMasters = 'SM'

Category = [
    (tanks, 'Танки'),
    (heals, 'Хилы'),
    (DD, 'ДД'),
    (merchants, 'Торговцы'),
    (GuildMasters, 'Гилдмастеры'),
    (QuestGivers, 'Квестгиверы'),
    (Blacksmiths, 'Кузнецы'),
    (Tanners, 'Кожевники'),
    (PotionMakers, 'Зельевары'),
    (SpellMasters, 'Мастера заклинаний'),
]


class Post(models.Model):
    post_name = models.CharField(max_length=255)
    post_text = models.TextField()
    post_cat = models.CharField(max_length=2, choices=Category, default=tanks)
    time_in = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.post_name.title()}'


class Comments(models.Model):
    com_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE)
    com_text = models.TextField()
    com_accept = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now_add=True)

