from django.urls import path, include
from django.views.generic import TemplateView
from .views import (PostList, create_post, PostDetail, PostEdit, PostDelete,
                    CommentsList, create_comment, CommentDetail, CommentDelete, accept_comment)


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('my_posts', PostList.as_view(template_name='my_post_list.html'), name='post_list'),
    path('create/', create_post),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/comment/', create_comment),
    path('comments/', CommentsList.as_view(), name='comments'),
    path('comments/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
    path('comments/<int:pk>/delete', CommentDelete.as_view(), name='comment_delete'),
    path('comments/<int:pk>/accept', accept_comment),
    path('categorys/', TemplateView.as_view(template_name='categorys.html')),
    path('categorys/tanks', PostList.as_view(template_name='category_list/tanks.html'), name='tanks'),
    path('categorys/heals', PostList.as_view(template_name='category_list/heals.html'), name='heals'),
    path('categorys/DD', PostList.as_view(template_name='category_list/DD.html'), name='DD'),
    path('categorys/merchants', PostList.as_view(template_name='category_list/merchants.html'), name='merchants'),
    path('categorys/GuildMasters', PostList.as_view(template_name='category_list/GuildMasters.html'), name='GuildMasters'),
    path('categorys/QuestGivers', PostList.as_view(template_name='category_list/QuestGivers.html'), name='QuestGivers'),
    path('categorys/Blacksmiths', PostList.as_view(template_name='category_list/Blacksmiths.html'), name='Blacksmiths'),
    path('categorys/Tanners', PostList.as_view(template_name='category_list/Tanners.html'), name='Tanners'),
    path('categorys/PotionMakers', PostList.as_view(template_name='category_list/PotionMakers.html'), name='PotionMakers'),
    path('categorys/SpellMasters', PostList.as_view(template_name='category_list/SpellMasters.html'), name='SpellMasters'),

]