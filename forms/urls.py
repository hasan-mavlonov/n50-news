from django.urls import path

from forms.views import create_user_info_view, get_user_info_list, get_user_info_detail, delete_user_info, update_user_info

app_name = 'form'

urlpatterns = [
    path('list/', get_user_info_list, name="list"),
    path('form/', create_user_info_view, name="form"),
    path('<int:pk>/', get_user_info_detail, name="detail"),
    path('delete/<int:pk>/', delete_user_info, name="delete"),
    path('update/<int:pk>/', update_user_info, name="update"),
]
