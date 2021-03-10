from django.contrib import admin

# Register your models here.
from Conversations.models import Conversation, Message, Thought

admin.site.register([Conversation, Message, Thought])
