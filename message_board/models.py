import date								#import the date
from django.db import models

class Users(models.Model):						#Create Users table
	user_id	= models.CharField(max_length=20,primary_key = true)	#Set TopicID VarChar(20) as PrimaryKey
	password = models.CharField(max_length = 20)			#Set password as VarChar(20)
	JoinDate = models.DateTimeField('date joined')			#Set date joined
	Post_ID = models.ForeignKey(Posts)				#Unsure if Needed
	badge_name = models.ForeignKey(Badge)				#Unsure if Needed 
	
class Badges(models.Model):						#Create Badges table
	badge_name = models.CharField(max_length=20,primary_key=true)	#Set badge_name VarChar(20) as PrimaryKey
	UserID = models.ManyToManyField(Users)				#Set ForeginKey UserId as ManyToMany with Badges	
	
class Private_Messages(models.Model):					#create PM table
	message_id = models.CharField(max_length=20,primary_key=true)	#Set TopicID VarChar(20) as PrimaryKey
	SendDate = models.DateTimeField('date sent')			#add Date Sent
	text = models.CharField(max_length = 1000)			#Include text field for message
	UserID = models.ForeignKey(Users)				#Link to Users; Django auto stores Char as not null 
	def __str__(self):						#Allows for User Input
			return self.message_text			
	
class Posts(models.Model):						#Create Post table
	post_id = models.CharField(max_length=20,primary_key = true)	#Set TopicID VarChar(20) as PrimaryKey
	Text = models.CharField(max_length = 1000)			#Allow for 1000 characters for Text part of Posts
	UserID = models.ForeginKey(Users)				#Link to Foreign Key of Users
	TopicID = models.ForeginKey(Topic)				#Link to Foreign Key of Topic
	def __str__(self):						#Allows for text prompt for User Input
			return self.message_text		
	
class FileAttatchments(models.Model):					#Create File Attatchments Table
	FileURL = models.FileField(upload_to = 'uploads/%y/%m/%d')	#Upload file to MEDIA_ROOT/uploads/'year'/'month'/'date'
	PostID = models.ForeignKey(Posts)				#Link to Posts	
	
class Topic(models.Model):						#Create Topic Table
	TopicID = models.CharField(max_length = 20,primaryKey =true)	#Set TopicID VarChar(20) as PrimaryKey	
	topic_name = models.CharField(max_length = 50)			#set topic name.
	BoardName = models.ForeignKey(Board)				#Link to Board
	def __str__(self):						#Allow for user input
		return self.topic_name					#

		
class Board(models.Model):						#Create Board Table
	BoardName = models.CharField(max_length=50,primary_key=true)	#set Borad Name as PrimaryKey
	
#class Message(models.Model):
#	message_text = models.CharField(max_length=2500)
#	pub_date = models.DateTimeField('date written')
#	topic = models.ForeignKey(Topic)
	
	
class HaveBadge(models.Model):						#unsure if needed due to manytomanyfield in Django
	
