from django.urls import path
from .views import MeetingListCreateView, MeetingDetailView, MeView

urlpatterns = [
    path('meetings/', MeetingListCreateView.as_view(), name='meeting-list'),
    path('meetings/<int:pk>/', MeetingDetailView.as_view(), name='meeting-detail'),
     path('api/users/me/', MeView.as_view(), name='user-detail'),
]
