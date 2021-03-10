import rest_framework.serializers as serializers

from Conversations.models import Conversation, Message, Thought


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('title', 'start_date')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('conversation_id', 'text', 'datetime_sent')


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = ('message_id', 'text', 'datetime_sent')
