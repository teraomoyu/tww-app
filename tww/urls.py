from django.urls import path

from . import views

app_name = "tww"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:random_index>/upload/", views.upload, name="upload"),
    path("all/", views.view_all_writings, name="view_all_writings"),
    path("<int:writing_id>/view/", views.view, name="view"),
]
