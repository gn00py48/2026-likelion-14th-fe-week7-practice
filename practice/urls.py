from django.urls import path
from . import views

app_name = "practice"

urlpatterns = [
    path("", views.home, name="home"),
    path("auth/", views.auth_page, name="auth"),
    path("review/", views.review_page, name="review"),

    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("create-review/", views.create_review, name="create_review"),
]