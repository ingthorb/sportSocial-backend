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
from django.urls import path
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('swagger-ui/', permanent=False)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('sports/', views.SportList.as_view()),
    path('events/', views.EventList.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('groups/', views.GroupList.as_view()),
    path('cities/', views.CityList.as_view()),
    path('countries/', views.CountryList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('sports/<int:id>', views.SportDetail.as_view()),
    path('cities/<int:pk>', views.CityDetails.as_view()),
    path('countries/<int:pk>', views.CountryDetail.as_view()),
    path('users/', views.UserList.as_view())
]
