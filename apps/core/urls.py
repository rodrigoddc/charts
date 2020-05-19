from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import IndexView, DataJsonViewSet

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('json/', DataJsonViewSet.as_view()),
    path('json/<int:pk>/', DataJsonViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)