from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, about, create, good, POSTLoginView, profile, POSTLogoutView, ChangeUserInfoView, \
    POSTChangeView, RegisterUserView, RegisterDoneView, user_activate, DeleteUserView, editpost, deletepost, detail

app_name = 'news'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail, name='detail'),
    path('accounts/profile/add/', create, name='add'),
    path('good/', good, name='good'),
    path('about/', about, name='about'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', POSTLoginView.as_view(), name='login'),
    path('accounts/logout/', POSTLogoutView.as_view(), name='logout'),
    path('accounts/profile/delete', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/editpost/<int:pk>/', editpost, name='edit_post'),
    path('accounts/profile/deletepost/<int:pk>/', deletepost, name='delete_post'),
    path('accounts/password/change', POSTChangeView.as_view(), name='password_change'),

]
