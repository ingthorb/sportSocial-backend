"""sportSocialBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from API import views

schema_view = get_swagger_view(title='Sport Social API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('sports/', views.SportList.as_view()),
    path('events/', views.EventList.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('groups/', views.GroupList.as_view()),
    path('cities/', views.CityList.as_view()),
    path('countries/', views.CountryList.as_view()),
    path('events/<int:id>', views.EventDetail.as_view()),
    path('comments/<int:id>', views.CommentDetail.as_view()),
    path('sports/<int:id>', views.SportDetail.as_view()),
    path('groups/<int:id>', views.GroupsDetails.as_view()),
    path('cities/<int:id>', views.CityDetails.as_view()),
    path('countries/<int:id>', views.CountryDetail.as_view())
]
