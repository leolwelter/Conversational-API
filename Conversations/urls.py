from django.urls import path, include
from rest_framework import routers

from Conversations.views import ConversationViewset, MessageViewset, ThoughtViewset

router = routers.DefaultRouter()

# we specify the basename, just in case we want to override the ModelViewset get_queryset method
#   (and leave out their queryset field)
router.register(r'conversations', ConversationViewset, basename='conversations')
router.register(r'messages', MessageViewset, basename='messages')
router.register(r'thoughts', ThoughtViewset, basename='thoughts')

urlpatterns = [
    path('', include(router.urls)),
]
