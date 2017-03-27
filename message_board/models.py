from django.db import models

class Topic(models.Model):
	topic_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.topic_name

class Message(models.Model):
	message_text = models.CharField(max_length=2500)
	pub_date = models.DateTimeField('date writen')
	topic = models.ForeignKey(Topic)
	def __str__(self):
		return self.message_text
	
