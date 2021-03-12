from django.test import TestCase
from Conversations.models import Conversation, Message, Thought
from Conversations.test.utils import get_test_data


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.num_thoughts = 4
        self.num_messages = 4
        self.num_conversations = 2

        # mock Conversation, Message, Thought
        self.conversations, self.messages, self.thoughts = get_test_data()

    def test_models_created(self):
        conversations = Conversation.objects.all()
        messages = Message.objects.all()
        thoughts = Thought.objects.all()

        self.assertEquals(len(conversations), self.num_conversations)
        self.assertEquals(len(messages), self.num_messages)
        self.assertEquals(len(thoughts), self.num_thoughts)

        for expected in self.conversations:
            self.assertIn(expected, conversations)
        for expected in self.messages:
            self.assertIn(expected, messages)
        for expected in self.thoughts:
            self.assertIn(expected, thoughts)