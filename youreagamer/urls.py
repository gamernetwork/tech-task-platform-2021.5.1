from django.contrib import admin
from django.urls import include, path

from cms import views

urlpatterns = [
    path('v1/', include([
        path('posts', views.GetPosts.as_view()),
    ])),
    path('admin/', admin.site.urls),
]
