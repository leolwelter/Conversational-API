import rest_framework.serializers as serializers

from Conversations.models import Conversation, Message, Thought


# the url field is created for us by HyperlinkedModelSerializer

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'start_date')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('conversation', 'id', 'text', 'datetime_sent')


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = ('message', 'id', 'text', 'datetime_sent')
