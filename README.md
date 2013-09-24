FelixLive
=========

Django powered live blogging system, built in 10 hours :)

### The Premise:

Felix needed a live blogging system for our coverage of the TEDxAlbertopolis event held in the Royal Albert Hall (23rd Sept. '13). At the time we couldn't use our usual live blogging system because the author had graduated and took his knowledge with him. Additionally theis system was built overnight (and morning) before the event took place at 1400h. I decided to create the blog because I decided the popular alternative (Storify) lacked the flexibility required.

### The Live Site:

The blog is available at http://felixlive.co.uk. I hosted the website on a LAMP stack on a cloud server. The admin page can be found at /admin. The live site is built very simply with only one front-facing url (the main url) and a JSON endpoint (available at /api/content). The django admin interface was used to provide a very basic method for adding content to the live page. The "live" nature of the blog is facilitated by jQuery which allows the page to reload a list of the content every 30 seconds to refresh the blog feed items on the page.
		
#### Django Models:
		
The site uses three models to organise data, Author, Content and Event. 
				
##### Event:
This model holds information about the live blogging event. This is used to separate the content objects by event (useful for future events). The default event is TEDxAlbertopolis.

##### Author:
This model contains an author object that holds information about the "author" of the content. This contains an optional image of the author as well as their name and a link to a relevent internet resource.
				
##### Content:
The content model contains the data being published on the live blog (attributed to a related author object). It can be used to display a text snippet, a quotation, an embedded tweet, a picture or an embedded Facebook post.
	
#### Front End Design:

Since the website had to be made quickly I used elements of Twitter's Bootsrap library to give the website a simple, hopefully elegent layout, using "wells" to contain each conent item. I also embedded the live feed of the event at the top of the page and changed the page so that the live content feed slotted into the area below, allowing consumers to take in both sources of media.
		
### To Do:
- Create a separate interface to add content to the blog
- Tidy up the front page design
- Add social media links (tweet button, fb like, etc.)
- Make a more efficient way to refresh the live-updating content (ideas, long-polling, comet, store publish time of last received content and send a post/get to endpoint to receive filtered content only)
- Use Moustace templating system for content via JSON instead of messy JS conditional problems.

### Required Packages (Installed on Ubuntu 12.04 using aptitude)

- apache2
- mysql-server
- php5 php5-common
- libapache2-mod-auth-mysql php5-mysql
- python-dev python-mysqldb python-django

### Other Required Libraries/Plugins

- Jquery (hosted by Google)
- Bootstrap v. 2.3.2
- Twitter Live Feed Widget

### Required Changes:
To host a version of this website, you will need-
 1. A server capable of containing a LAMP stack
 2. To change the relevent settings in settings.sample.py (email address, database credentials and project parent folder) and save these changes to settings.py
