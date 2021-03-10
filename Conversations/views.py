from rest_framework import viewsets

from Conversations.models import Conversation, Message, Thought
from Conversations.serializers import ConversationSerializer, MessageSerializer, ThoughtSerializer


# import logging
# logger = logging.getLogger('django.server')


# be sure to set serializer_class and queryset on all views!

class ConversationViewset(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    # filter_backends = (filters.backends.DjangoFilterBackend,)
    # filterset_class = LookupFilterset


class MessageViewset(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    # filter_backends = (filters.backends.DjangoFilterBackend,)
    # filterset_class = LookupFilterset


class ThoughtViewset(viewsets.ModelViewSet):
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()
    # filter_backends = (filters.backends.DjangoFilterBackend,)
    # filterset_class = LookupFilterset
