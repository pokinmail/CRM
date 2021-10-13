from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithDepartmentView, CustomUserCreate
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = DefaultRouter()
router.register('customuser', CustomUserViewSet, basename='customuser')
# generate patients/id/

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithDepartmentView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('', include(router.urls)),
]