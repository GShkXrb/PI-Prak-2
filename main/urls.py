from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rules', views.rules, name='rules'),
    path('ticket_example', views.BiletyView.as_view(), name='ticket_example'),
    path('signs', views.signs, name='signs'),
    path('question/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('test_start', views.test_start, name='test_start'),
    path('test/<ticket>', views.test, name='test'),
    path('test_exam', views.test_exam, name='test_exam'),
    path('exam/<ticket>', views.exam, name='exam'),
]