from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='home'),
    url(r'^sayhello/', views.hello, name='hello'),
    #url(r'^id/(?P<pk>\d+)/$', views.board_topics, name='board_topics'), # we could just use (\d+) for implicity
    url(r'^id/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^id/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    #url(r'^id/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)$', views.topic_posts, name='topic_posts'),
    url(r'^id/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^id/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^id/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='edit_post'),
    #url(r'^new_post/$', views.NewPostView.as_view(), name='new_post'),
]