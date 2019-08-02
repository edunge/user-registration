from django.conf.urls import url
from new_website import views
from django.urls import path

##TEMPLATE TAGGING
app_name = 'new_website'

urlpatterns=[
    path('',views.index,name='index'),
    path('base/', views.base, name='base'),
    path('register/',views.register, name='register'),
    path('logout/',views.user_logout, name='logout'),
    path('user_login/',views.user_login,name="user_login"),
    # path('login/',views.login,name='login')
]