from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('work/<int:pk>/', views.work, name='work'),
    path('work/<int:pk>/leave_comment', views.leave_comment, name='leave_comment'),
    path('registration', views.Sign_View, name='sign'),
    path('account/logout', views.Sign_Out, name='logout'),
    path('account/login', views.Login_View, name='login'),
]
