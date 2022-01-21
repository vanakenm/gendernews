from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('notes', views.notes, name='notes'),
    path('send-message', views.send_message, name='send-message'),
    path('posts/un-mois-de-check', views.one_month, name='one-month'),
]