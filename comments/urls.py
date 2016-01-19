from django.conf.urls import url

from comments import views

urlpatterns = [
    url(r'^$', views.CommentsView.as_view(), name='comments'),
    url(r'^comments/$', views.comment_list),
]