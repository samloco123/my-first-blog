from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.search, name='search_results'),
    path('cv/edit/', views.cv_edit, name='cv_edit'),
    path('cv/edit/work', views.cv_add_work, name='cv_add_work'),
    path('cv/edit/education', views.cv_add_educ, name='cv_add_educ'),
    path('cv/view', views.cv_view, name='cv_view'),
]