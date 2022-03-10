from django.urls import path

from users import views

urlpatterns = [
    path('register/callback', views.handle_callback)
]
