#===================== Different Forms Corresponding to Models ==================#

from django import forms
from django.contrib.auth.models import User
from map.models import UserProfileInfo , Parameters        #Injection of parameter and user profile information model

'''========================== UserForm=====================
   This is the form corresponding to the UserProfileInfo Model.
   It contains the following field for inputting data from the user - 
   		1 :- username
   		2 :- email
   		3 :- password
   		4 :- user blog url
   		5 :- user profile picture
'''

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

	class Meta():
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	portfolio_site = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'website url'}))

	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')

'''========================== ParameterForm =====================
   This is the form corresponding to the Parameters Model.
   It contains all the field for inputting data from the user.
   		
'''

class ParameterForm(forms.ModelForm):

	class Meta():
		model = Parameters
		fields = '__all__'
		 

