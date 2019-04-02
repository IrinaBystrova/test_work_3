from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('notes/', views.NotesList.as_view(), name='Noteslist'),
    path('notes/<str:pk>', views.NoteDetail.as_view(), name='Notedetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
