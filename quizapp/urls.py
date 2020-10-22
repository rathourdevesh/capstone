from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("test/<int:contestid>", views.test, name="test"),
    path("scores/<int:contestid>",views.Scores,name="scores"),
    path("profile",views.Profile,name="profile"),
    path("leaderboard/<int:contestid>",views.leaderboard,name="leaderboard"),

    #API Routes
    path("enroll/",views.enroll,name="enroll"),
]