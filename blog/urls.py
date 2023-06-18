from django.urls import path
from . import views

urlpatterns = [
    #   path('', views.post_list, name='blog'),
    # path("", views.PostList.as_view(), name="home"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("contact/", views.contact, name="contact"),
   ]
