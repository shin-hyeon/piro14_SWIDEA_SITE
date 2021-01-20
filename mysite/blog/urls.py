from django.urls import path, re_path, register_converter
from .import views

app_name = 'blog'

urlpatterns = [
    path('idea/create/', views.idea_new, name='idea_new'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('', views.idea_list, name='idea_list'),
    path('idea/update/<int:pk>', views.idea_update, name='idea_update'),
    path('idea/delete/<int:pk>', views.idea_delete, name='idea_delete'),

    path('devtool/', views.devtool_list, name='devtool_list'),
    path('devtool/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtool/create/', views.devtool_new, name='devtool_new'),
    path('devtool/update/<int:pk>', views.devtool_update, name='devtool_update'),
    path('devtool/delete/<int:pk>', views.devtool_delete, name='devtool_delete'),
]
    