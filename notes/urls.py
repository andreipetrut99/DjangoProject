from django.conf.urls import url
from django.urls import path, include

from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.NotesIndex.as_view(), name='index'),
    path('delete/<int:pk>/', views.DeleteNotesView.as_view(), name='remove_note'),
    path('update/<int:pk>/', views.UpdateNotesView.as_view(), name='update_note'),
    path('add/', views.CreateNotesView.as_view(), name='create_note'),
    ]