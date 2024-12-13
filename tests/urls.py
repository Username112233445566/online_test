from django.urls import path
from .views import test_detail, test_list, test_result 

urlpatterns = [
    path("", test_list, name="test_list"),
    path("<int:pk>/", test_detail, name="test_detail"),
    path("<int:pk>/result/<str:username>/", test_result, name="test_result"),
]
