import json
from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from Conversations.models import Conversation, Message, Thought
from Conversations.serializers import ConversationSerializer, MessageSerializer, ThoughtSerializer
from Conversations.test.utils import get_test_data


class ConversationViewTests(TestCase):
    def setUp(self) -> None:
        self.num_thoughts = 4
        self.num_messages = 4
        self.num_conversations = 2
        self.conversations, self.messages, self.thoughts = get_test_data()

        # mock client
        self.client = Client(enforce_csrf_checks=True)

        # misc
        self.decoder = json.JSONDecoder()
        dt = datetime.now()
        self.datetime_sent = dt.isoformat()
        self.start_date = self.datetime_sent.split('T')[0]

    def test_get_all(self):
        # get the url for the list method
        res = self.client.get(reverse('conversations-list'))

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize conversations to be in the same form as actual
        expected = ConversationSerializer(self.conversations, many=True).data
        self.assertEquals(actual, expected)

    def test_get_one(self):
        res = self.client.get(reverse('conversations-detail', args=[self.conversations[0].id]))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data
        expected = ConversationSerializer(self.conversations[0]).data
        self.assertEquals(actual, expected)

    def test_get_one_404(self):
        # does not exist in database
        res = self.client.get(reverse('conversations-detail', args=[404]))
        self.assertEquals(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_many_by_title(self):
        # improperly formed request
        search_term = '1'
        res = self.client.get(reverse('conversations-list') + f'?title={search_term}')
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')
        expected = ConversationSerializer([self.conversations[0]], many=True).data
        self.assertEquals(actual, expected)

        search_term = 'vers'
        res = self.client.get(reverse('conversations-list') + f'?title={search_term}')
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')
        expected = ConversationSerializer(self.conversations, many=True).data
        self.assertEquals(actual, expected)

        search_term = 'Not actually in the title anywhere'
        res = self.client.get(reverse('conversations-list') + f'?title={search_term}')
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')
        expected = ConversationSerializer([], many=True).data
        self.assertEquals(actual, expected)

    def test_post_one(self):
        new_conversation_data = {
            'title': 'Conversation 4',
            'start_date': self.start_date
        }
        res = self.client.post(reverse('conversations-list'), new_conversation_data, content_type='application/json')

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        # should echo added record
        new_conversation_data['id'] = len(self.conversations) + 1
        new_conversation_data['start_date'] = self.start_date
        expected = ConversationSerializer(new_conversation_data).data
        self.assertEquals(res.data, expected)

        # should have added to database
        res = self.client.get(reverse('conversations-detail', args=[new_conversation_data.get('id')]))
        self.assertEquals(res.data, expected)
        self.assertEquals(len(Conversation.objects.all()), len(self.conversations) + 1)


class MessageViewTests(TestCase):
    def setUp(self) -> None:
        self.num_thoughts = 4
        self.num_messages = 4
        self.num_conversations = 2
        self.conversations, self.messages, self.thoughts = get_test_data()

        # mock client
        self.client = Client(enforce_csrf_checks=True)

        # misc
        self.decoder = json.JSONDecoder()
        dt = datetime.now()
        self.datetime_sent = dt.isoformat() + 'Z'  # thanks, python
        self.start_date = self.datetime_sent.split('T')[0]

    def test_get_all(self):
        # get the url for the list method
        res = self.client.get(reverse('messages-list'))

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize to be in the same form as actual
        expected = MessageSerializer(self.messages, many=True).data
        self.assertEquals(actual, expected)

    def test_get_all_by_conversation(self):
        search_cid = 1
        res = self.client.get(reverse('messages-list') + f'?cid={search_cid}')

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize to be in the same form as actual
        expected = MessageSerializer([m for m in self.messages if m.conversation_id == search_cid], many=True).data
        self.assertEquals(actual, expected)

    def test_get_all_by_text(self):
        search_cid = 1
        search_text = 'age'
        res = self.client.get(reverse('messages-list') + f'?cid={search_cid}&text={search_text}')

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize to be in the same form as actual
        expected = MessageSerializer(
            [m for m in self.messages if m.conversation_id == search_cid and search_text in m.text], many=True).data
        self.assertEquals(actual, expected)

    def test_get_one(self):
        res = self.client.get(reverse('messages-detail', args=[self.messages[0].id]))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data
        expected = MessageSerializer(self.messages[0]).data
        self.assertEquals(actual, expected)

    def test_get_one_404(self):
        # does not exist in database
        res = self.client.get(reverse('messages-detail', args=[404]))
        self.assertEquals(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_one(self):
        c = Conversation.objects.get(id=1)
        new_message = {
            'text': 'Message 5',
            'datetime_sent': self.datetime_sent,
            'conversation': c.id
        }
        res = self.client.post(reverse('messages-list'), new_message, content_type='application/json')

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        # should echo added record
        new_message['id'] = len(self.messages) + 1
        new_message['datetime_sent'] = self.datetime_sent
        new_message['conversation'] = c  # we need this to serialize it
        expected = MessageSerializer(new_message).data
        self.assertEquals(res.data, expected)

        # should have added to database
        res = self.client.get(reverse('messages-detail', args=[new_message.get('id')]))
        self.assertEquals(res.data, expected)
        self.assertEquals(len(Message.objects.all()), len(self.messages) + 1)


class ThoughtViewTests(TestCase):
    def setUp(self) -> None:
        self.num_thoughts = 4
        self.num_messages = 4
        self.num_conversations = 2
        self.conversations, self.messages, self.thoughts = get_test_data()

        # mock client
        self.client = Client(enforce_csrf_checks=True)

        # misc
        self.decoder = json.JSONDecoder()
        dt = datetime.now()
        self.datetime_sent = dt.isoformat() + 'Z'  # thanks, python
        self.start_date = self.datetime_sent.split('T')[0]

    def test_get_all(self):
        # get the url for the list method
        res = self.client.get(reverse('thoughts-list'))

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize to be in the same form as actual
        expected = ThoughtSerializer(self.thoughts, many=True).data
        self.assertEquals(actual, expected)

    def test_get_all_by_message(self):
        search_mid = 1
        res = self.client.get(reverse('thoughts-list') + f'?mid={search_mid}')

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data.get('results')

        # serialize to be in the same form as actual
        expected = ThoughtSerializer([t for t in self.thoughts if t.message_id == search_mid], many=True).data
        self.assertEquals(actual, expected)

    def test_get_one(self):
        res = self.client.get(reverse('thoughts-detail', args=[self.thoughts[0].id]))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        actual = res.data
        expected = ThoughtSerializer(self.thoughts[0]).data
        self.assertEquals(actual, expected)

    def test_get_one_404(self):
        # does not exist in database
        res = self.client.get(reverse('thoughts-detail', args=[404]))
        self.assertEquals(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_one(self):
        m = Message.objects.get(id=1)
        new_thought = {
            'text': 'Thought 5',
            'datetime_sent': self.datetime_sent,
            'message': m.id
        }
        res = self.client.post(reverse('thoughts-list'), new_thought, content_type='application/json')

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        # should echo added record
        new_thought['id'] = len(self.thoughts) + 1
        new_thought['datetime_sent'] = self.datetime_sent
        new_thought['message'] = m  # we need this to serialize it
        expected = ThoughtSerializer(new_thought).data
        self.assertEquals(res.data, expected)

        # should have added to database
        res = self.client.get(reverse('thoughts-detail', args=[new_thought.get('id')]))
        self.assertEquals(res.data, expected)
        self.assertEquals(len(Thought.objects.all()), len(self.thoughts) + 1)
