
from main import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('lesson_1/', views.lesson_1, name='lesson_1'),
    path('les/', views.les, name='les'),

]