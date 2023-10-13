from django.urls import path
from . import views

urlpatterns =[
    path('',views.main, name ='main'),
    path('blog/',views.index, name = 'index'),
    path('register/',views.registration, name = 'regi_form'),
    path('signin/',views.sign_in, name= 'sign_in'),
    path('test/', views.test, name = 'test'),
    path('about/', views.about_us, name = 'aboutus'),
    path('blog/details/<int:id>', views.details, name = 'details'),
    
]
