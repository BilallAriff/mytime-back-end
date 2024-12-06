
from django.contrib import admin
from django.urls import path, include
from .views import welcome_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_page, name="welcome"),
    path('api/users/', include('users.urls'))
]
