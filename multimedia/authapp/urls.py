from django.urls import path
from multimedia.authapp import views as vw
urlpatterns = [
    path("my_profile/<int:userid>/", vw.my_profile, name="myProfile" ),
]
