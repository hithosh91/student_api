from django.urls  import path
from .views import (studentCreatview,studentdelete,studentgetall,studentgetbyid,studentupdate)


urlpatterns=[
    path("create/", studentCreatview.as_view() ,name="studentCreatView"),
    path("all/",studentgetall.as_view(),name="studentgetall"),
    path("<int:pk>/",studentgetbyid.as_view(),name="studentgetbyid"),
    path("<int:pk>/update",studentupdate.as_view(),name="update"),
    path("<int:pk>/delete",studentdelete.as_view(),name="deletestudent"),
]