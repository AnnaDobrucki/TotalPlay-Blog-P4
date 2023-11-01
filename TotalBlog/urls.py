from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('completed/', views.ListBookingView.as_view(), name='completed'),
]