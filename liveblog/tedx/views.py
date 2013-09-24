# Create your views here.
from liveblog.tedx.models import *
from django.shortcuts import render_to_response, redirect
from django.utils import simplejson
#from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse

def home(request):
	posts=Content.objects.all()
	return render_to_response('home.html',{ 'content':posts })


#       sfd @method_decorator(csrf_exempt)
def get_content(request):
 	content_json=[]
 	posts=Content.objects.all()
	for post in posts:
		post_data={'id':post.id, 'content_type':post.content_type, 'pub_date':post.pub_date.strftime("%d %b %H:%M")};
		if (post.author):
			post_data["author_name"]=post.author.name
			if (post.author.url):
				post_data["author_url"]=post.author.url
			else:
				post_data["author_url"]="http://tedxalbertopolis.com/speakers"
			
			if (post.author.picture):
				post_data["author_img"]=post.author.picture.url
		if (post.author_text):
			post_data["author_name"]=post.author_text
		if (post.picture):
			post_data["img"]=post.picture.url
		if (post.picture_url):
			post_data["img"]=post.picture_url
		if (post.text):
			post_data["text"]=post.text
		content_json.append(post_data)
	return HttpResponse(simplejson.dumps(content_json), mimetype='application/json')	
 
