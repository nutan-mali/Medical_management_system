from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    # path("", views.expense_list, name="expense_list"),

]