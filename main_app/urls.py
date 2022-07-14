from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('people/', views.person_index, name='index'),
  path('person/<int:person_id>/', views.person_detail, name='detail'),
  path('person/create/', views.PersonCreate.as_view(), name='person_create'),
  path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
  path('interests/', views.InterestList.as_view(), name='interests_index'),
  path('person/<int:person_id>/add_photo/', views.add_photo, name='add_photo'),
]