#====================== Different URLs of the Webpage ===================#

from django.conf.urls import url
from map import views                       # inheritance of map/views.py


app_name = 'map'   # Name of the Application

'''========================== URLs ===================== 
   These URLs will transfer control to the following views.py  - 
   		1 :- @register   --> register function of map/views.py
   		2 :- @index      --> index function of map/views.py  
   		3 :- @user_login --> user_login function of map/views.py
   		4 :- @eav        --> eav function of map/views.py
   		5 :- @parameters --> para_view function of map/views.py
'''
   
urlpatterns = [

    url(r'^register/',views.register,name='register' ),
    url(r'^index/',views.index,name='index' ),
    url(r'^user_login/',views.user_login,name='user_login' ),
    url(r'^eav/',views.eav,name = "eav"),
    url(r'^parameters/',views.para_view,name = "para_view"),

]
