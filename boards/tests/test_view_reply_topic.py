from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from ..models import Board, Post, Topic
from ..views import reply_topic

class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all reply_topic view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='DJango', description='DJango board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello World', board=self.board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet.')
        self.url = reverse('reply_topic', kwargs={'pk':self.board.pk, 'topic_pk': self.topic.pk})