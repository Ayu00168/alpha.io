from django.urls import path
from User.views import CreateUserView, LoginUserView, LogoutUserView


urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name="create_user"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('logout/', LogoutUserView.as_view(), name="logout"),
]