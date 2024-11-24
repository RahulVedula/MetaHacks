from django.urls import path, include
from django.shortcuts import redirect
from .views import VideoFeedAPIView, hand_keypoints_view, home_view


urlpatterns = [
    path('api/video-feed/', VideoFeedAPIView.as_view(), name='video-feed'),
    path('api/hand-keypoints/', hand_keypoints_view, name='hand-keypoints'),
    path('api/home/', home_view, name='home'),
    path('', lambda request: redirect('api/video-feed/')),  # Redirect root to /api/home/
]
