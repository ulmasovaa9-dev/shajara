from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_family_tree_data, name='family_tree_url'),
    path('add/', views.add_person_view, name='add_person_url'),
    path('person/<int:pk>/', views.person_detail_view, name='person_detail_url'),
    path(
        'person/<int:pk>/delete/',
        views.delete_person_view,
        name='delete_person_url',
    ),
]