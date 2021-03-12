from typing import List, Tuple
from Conversations.models import Conversation, Message, Thought
from typing import List, Tuple

from Conversations.models import Conversation, Message, Thought


def get_test_data() -> Tuple[List[Conversation], List[Message], List[Thought]]:
    # mock Conversation, Message, Thought
    c1 = Conversation.objects.create(id=1, title='Conversation 1', start_date='2021-03-11')
    c2 = Conversation.objects.create(id=2, title='Conversation 2', start_date='2021-03-10')
    m1 = Message.objects.create(id=1, conversation=c1, text='Message 1', datetime_sent='2021-03-11T15:14:13Z')
    m2 = Message.objects.create(id=2, conversation=c1, text='Message 2', datetime_sent='2021-03-11T12:59:05Z')
    m3 = Message.objects.create(id=3, conversation=c2, text='Message 3', datetime_sent='2021-03-11T17:01:43Z')
    m4 = Message.objects.create(id=4, conversation=c2, text='Message 4', datetime_sent='2021-03-11T11:14:13Z')
    t1 = Thought.objects.create(id=1, message=m1, text='Thought "one"', datetime_sent='2021-03-11T15:14:13Z')
    t2 = Thought.objects.create(id=2, message=m2, text='Thought 2', datetime_sent='2021-03-11T12:59:05Z')
    t3 = Thought.objects.create(id=3, message=m3, text='Thought three', datetime_sent='2021-03-11T17:01:43Z')
    t4 = Thought.objects.create(id=4, message=m4, text='Thought 04', datetime_sent='2021-03-11T11:14:13Z')
    return [c1, c2], [m1, m2, m3, m4], [t1, t2, t3, t4]