from django.urls import path
from . import views
urlpatterns = [
    path('test',views.test),
    
    path('test1',views.test1),
    
    path('test2',views.test2),
    
    path('test3',views.test3),
    
    path('home',views.home),
    
    path('home2',views.home2),
    
    path('index',views.index),
    
    path('add',views.add),
 
    path('addcode',views.addcode),
    
    path('check',views.check),
    
    path('checkcode',views.checkcode),
    
    path('login',views.login),
    
    path('log', views.log),
    
    path('show',views.show),
    
    path('del/<int:id>',views.dele),

    path('newhome',views.newhome),
]
