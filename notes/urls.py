from rest_framework import routers
from django.urls import path, include
from notes import views

router = routers.DefaultRouter()
router.register('notes', views.NotesView, 'notes')

urlpatterns = [
    path('api/note/', include(router.urls)),
]