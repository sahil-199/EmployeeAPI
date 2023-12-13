from django.urls import path
from .views import EmpList,EditEmp
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',EmpList.as_view(),name='Emp'),
    path('edit/<int:pk>/',EditEmp.as_view(),name='EditEmp'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]