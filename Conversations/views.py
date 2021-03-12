from rest_framework import viewsets

from Conversations.models import Conversation, Message, Thought
from Conversations.serializers import ConversationSerializer, MessageSerializer, ThoughtSerializer


# be sure to set serializer_class and queryset on all views!
# for our purposes (i.e. not worrying about authentication, permissions, or users)
# the default DRF ViewSets function just fine

# Conversation views
class ConversationViewset(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all().order_by('id').order_by('id')

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title:
            return Conversation.objects.filter(title__contains=title)
        else:
            return Conversation.objects.all().order_by('id')


# Message views
class MessageViewset(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('id')

    def get_queryset(self):
        c_id = self.request.query_params.get('cid', None)
        text = self.request.query_params.get('text', None)
        if text and c_id:
            return Message.objects.filter(conversation=c_id, text__contains=text)
        elif c_id:
            return Message.objects.filter(conversation=c_id)
        elif not text:
            return Message.objects.all().order_by('id')


# Thought views
class ThoughtViewset(viewsets.ModelViewSet):
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all().order_by('id')

    def get_queryset(self):
        m_id = self.request.query_params.get('mid', None)
        c_id = self.request.query_params.get('cid', None)
        if not (m_id or c_id):
            return Thought.objects.all().order_by('id')
        elif m_id:
            return Thought.objects.filter(message=m_id)
        elif c_id:
            return Thought.objects.filter(message__conversation__id=c_id)
