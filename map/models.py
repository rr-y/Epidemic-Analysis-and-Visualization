
#============================= DataBase Models ==========================
from django.db import models
from django.contrib.auth.models import User


'''========================== User Registration Model =============== 
	It contains the following field -
		1 :- username
		2 :- email
		3 :- password
		4 :- user website url link
		5 :- user profile picture
'''


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True )

	def __str__(self):
		return self.user.username


'''========================== Disease Parameters Model=============== 
	It contains the following field -
		1 :- infection rate of disease , between 0 and 1
		2 :- recovery rate , between 0 nd 1
		3 :- user uploaded file in JSON format containing lattitude and longitude information 
			 of the different locations where disease may spread.
	
'''


class Parameters(models.Model):
	infection_rate = models.FloatField(null = True)
	recovery_rate  = models.FloatField(null = True)
	upload_file    = models.FileField(upload_to = 'profile_pics' , blank = False)


'''========================== SIR Like Model =============== 
	It contains the following field -
		1 :- lattitude information of the location
		2 :- longitude information of the location
		3 :- counter, which can take value 0 and 1. Zero means person is infected
			 , one means person is recovered.
		4 :- Date , to represent one a particular day how many people are infected and recovered.
		     Date information will be used for plotting data from database on the map. 
'''


class SIR(models.Model):
	lat = models.FloatField(null = True)
	lng = models.FloatField(null = True)
	counter = models.IntegerField(null = True)
	date = models.DateField(auto_now = False)

	
