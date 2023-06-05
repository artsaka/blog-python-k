from django.urls import path
from .views import panel,displayForm, insertData, deleteData

urlpatterns = [
    path('', panel, name="panel"),
    # path for creating article by a writer
    path('displayForm', displayForm, name="displayForm"),
    # path for article's content
    path('insertData', insertData, name="insertData"),
    path('deleteData/<int:id>', deleteData, name="deleteData")
]