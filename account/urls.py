from django.urls import path
from .views import user_login, Home, user_logout

app_name = 'account'
urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('home/', Home.as_view(), name='home'),
]

