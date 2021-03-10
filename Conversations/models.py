from django.db import models


class Conversation(models.Model):
    title = models.CharField(default=None, max_length=64)
    start_date = models.DateField(default=None)


class Message(models.Model):
    conversation_id = models.ForeignKey('Conversation', on_delete=models.CASCADE)
    text = models.CharField(default=None, max_length=256)
    datetime_sent = models.DateTimeField(default=None)


class Thought(models.Model):
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE)
    text = models.CharField(default=None, max_length=256)
    datetime_sent = models.DateTimeField(default=None)
