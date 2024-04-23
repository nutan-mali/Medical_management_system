from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path("user_profile/", views.user_profile, name="user_profile"),
    path('medicine/<int:medicine_id>/', views.medicine, name='medicine'),
    # path('medicine/', views.medicine, name='medicine'),
   path('medicine_report/<int:medicine_id>/', views.medicine_report, name='medicine_report')

    
]