import date
from django.db import models

class Topic(models.Model):						#Create Topic Table
	TopicID = models.CharField(max_length = 20,primaryKey =true)	#Set TopicID VarChar(20) as PrimaryKey	
	topic_name = models.CharField(max_length = 200)			#
	def __str__(self):						#
		return self.topic_name					#

#class Message(models.Model):
#	message_text = models.CharField(max_length=2500)
#	pub_date = models.DateTimeField('date written')
#	topic = models.ForeignKey(Topic)
	
	
class Posts(models.Model):						#Create Post table
	post_id = models.Field(primary_key = true)			#Set TopicID VarChar(20) as PrimaryKey
	Text = models.CharField(max_length = 1000)			#Allow for 1000 characters for Text part of Posts
	UserID = models.ForeginKey(Users)				#Link to Foreign Key of Users
	TopicID = models.ForeginKey(Topic)				#Link to Foreign Key of Topic
	def __str__(self):						#Allows for text prompt for User Input
			return self.message_text			
	
class Users(models.Model):						#Create Users table
	user_id	= models.Field(primary_key = true)			#Set TopicID VarChar(20) as PrimaryKey
	password = models.CharField(max_length = 100)			#
	JoinDate = models.DateTimeField('date joined')			#
	Post_ID = models.ForeignKey(Posts)				#
	badge_name = models.ForeignKey(Badge)				#Unsure if need or not

class Badges(models.Model):						#Create Badges table
	badge_name = models.CharField(max_length=20,primary_key=true)	#Set badge_name VarChar(20) as PrimaryKey
	UserID = models.ManyToManyField(Users)				#Set ForeginKey UserId as ManyToMany with Badges
		
class Private_Messages(models.Model):					#create PM table
	message_id = models.IntegerField(default = 0)			#Set TopicID VarChar(20) as PrimaryKey
	send_date = models.DateTimeField('date sent')			#
	text = models.CharField(max_length = 2500)			#
	user_id = models.ForeignKey(Users)				#
	def __str__(self):						#
			return self.message_text			#
		
class Board(models.Model):						#Create Board Table
	BoardName = models.CharField(max_length = 50)			#
	
class FileAttatchments(models.Model):					#Create File Attatchments Table
	FileURL = models.FileField(upload_to = 'uploads/%y/%m/%d')	#
	PostID = models.ForeignKey(Posts)				#
	
class HaveBadge(models.Model):						#
	
