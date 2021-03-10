from django.urls import path, include
from rest_framework import routers

from Conversations.views import ConversationViewset
from Conversations.views import MessageViewset
from Conversations.views import ThoughtViewset

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewset, basename='Conversation')
router.register(r'messages', MessageViewset, basename='Message')
router.register(r'thoughts', ThoughtViewset, basename='Thought')

urlpatterns = [
    path('', include(router.urls))
]
