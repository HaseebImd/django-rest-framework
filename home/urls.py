from django.urls import path,include
from .views import *

urlpatterns = [
    # path("", views.home, name="home"),
    # path("student", views.save_student,),
    # path("update_student/<id>/", views.update_student,),
    # path("delete_student/<id>/", views.delete_student,),
    path("student", StudentApiView.as_view(),),

    ]
