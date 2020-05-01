from django.urls import path
from .views import base, base1,base2,base3,base4
urlpatterns = [
path('', base.as_view(), name='home'),
path('post/<int:pk>/', base1.as_view(), name='post_detail'), 
path('post/new/', base2.as_view(), name='post_new'), 
path('post/<int:pk>/edit/',base3.as_view(), name='post_edit'),
path('post/<int:pk>/delete/',base4.as_view(), name='post_delete'),
 
]