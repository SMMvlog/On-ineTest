from django.contrib import admin
from django.urls import path,include
from testApi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('createtest',views.CreateView,basename='create')
router.register('student/',views.StudentAns,basename='std')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls',namespace='rest_framework')),

]