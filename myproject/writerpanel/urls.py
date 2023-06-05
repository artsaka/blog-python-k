from django.urls import path
from .views import panel,displayForm, insertData, deleteData, editData, updateData

urlpatterns = [
    path('', panel, name="panel"),
    # path for creating article by a writer
    path('displayForm', displayForm, name="displayForm"),
    # path for article's content
    path('insertData', insertData, name="insertData"),
    path('deleteData/<int:id>', deleteData, name="deleteData"),
    path('editData/<int:id>', editData, name="editData"),
    path('updateData/<int:id>', updateData, name="updateData")
]