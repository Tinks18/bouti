from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

   ]
