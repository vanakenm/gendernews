from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:source_id>/', views.detail, name='detail'),
    path('<int:source_id>/screenshots/<int:analysis_id>', views.screenshot, name='screenshot'),
]