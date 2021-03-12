from django.db import models


class Conversation(models.Model):
    title = models.CharField(default=None, max_length=64)
    start_date = models.DateField(default=None)

    def __str__(self):
        return 'id {}: {} ({})'.format(self.id, self.title, self.start_date)


class Message(models.Model):
    # conversation_id in db
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE)
    text = models.CharField(default=None, max_length=256)
    datetime_sent = models.DateTimeField(default=None)

    def __str__(self):
        return 'c_id {}: {} ({})'.format(self.conversation.id, self.text, self.datetime_sent)


class Thought(models.Model):
    # message_id in db
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    text = models.CharField(default=None, max_length=256)
    datetime_sent = models.DateTimeField(default=None)

    def __str__(self):
        return 'm_id {}: {} ({})'.format(self.message.id, self.text, self.datetime_sent)
