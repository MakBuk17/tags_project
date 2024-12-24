from django.urls import path
from .views import home, tag_detail

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('<str:tag>/', tag_detail, name='tag_detail'),  # Детальная страница для тега
]
