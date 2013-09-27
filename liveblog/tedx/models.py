from django.db import models
import datetime
# Create your models here.


class Event(models.Model):
	name=models.CharField(max_length=50);
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()
	is_current=models.IntegerField(default=0)
	location=models.CharField(max_length=50);
	picture=models.ImageField(upload_to="ev",blank=True)
	slug=models.CharField(max_length=15);
	def __unicode__(self):
                return str(self.name)

class Author(models.Model):
	name=models.CharField(max_length=50)
	url=models.CharField(max_length=50, blank=True)
	picture=models.ImageField(upload_to="au",blank=True)
	def __unicode__(self):
		return str(self.name)

class Content(models.Model):
	
	TYPE_CHOICES= (
		("TEXT", 'Text'),
		("QUOTE", 'Quote'),
		("PICTURE",'Picture'),
		("TWEET",'Tweet'),
		("FACEBOOK",'Facebook'),
	)	

	content_type=models.CharField(max_length=10,choices=TYPE_CHOICES,default="TEXT")
	author_text=models.CharField(max_length=25, blank=True)
	author=models.ForeignKey(Author,blank=True)	
	text=models.TextField(blank=True)
	picture=models.ImageField(upload_to="content",blank=True)
	picture_url=models.CharField(max_length=150,blank=True)
	event=models.ForeignKey(Event, default=1)
	pub_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return ' - '.join([self.content_type,self.author.name,self.pub_date.strftime("%d %b %H:%M")])
	class Meta:
		ordering=("-pub_date",)
