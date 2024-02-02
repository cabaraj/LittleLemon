from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
    # visit the following end with a POST method passing username and password
    # to generate a token
    path('api-token-auth/', obtain_auth_token),
    
]