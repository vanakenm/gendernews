from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:source_id>/analysis/<int:analysis_id>', views.detail, name='detail'),
    path('<int:source_id>/screenshots/<int:analysis_id>', views.screenshot, name='screenshot'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:source_id>', views.site, name='site'),
]