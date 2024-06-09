from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)


custom_urls = [
    # path('messages/<int:pk>/censored/', MessageViewSet.as_view({'post':'censor_message'}), name='censor-message'),
    path('messages/bot/ask/', MessageViewSet.as_view({'post':'ask_bot'}), name='ask-bot')
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include(custom_urls))
]
