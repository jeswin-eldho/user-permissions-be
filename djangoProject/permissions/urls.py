from django.urls import path

from djangoProject.permissions.views import UserView, RoleView, UsersView

app_name = "djangoProject.permissions"

urlpatterns = [
    path(
        "",
        UserView.as_view(),
        name="user",
    ),
    path(
        "users",
        UsersView.as_view(),
        name="users",
    ),
    path(
        "roles",
        RoleView.as_view(),
        name="role",
    ),
]
