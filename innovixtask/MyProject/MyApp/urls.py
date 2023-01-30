from django.urls import path
from .views import CreateCustomUser, ListCustomUser, user_login_view, user_logout_view, update, delete, remove_profile_pic
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', CreateCustomUser.as_view(), name='signup'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('display/', login_required(ListCustomUser.as_view(), login_url='login/'), name='display'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('remove/<int:pk>/', remove_profile_pic, name='remove')

]

