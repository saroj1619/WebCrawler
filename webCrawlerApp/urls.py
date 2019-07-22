from django.urls import path
from.views import WebCrawlerView
urlpatterns = [
    path('', WebCrawlerView.as_view()),
]
