from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from memories import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_memory/<int:memory_id>/', views.delete_memory, name='delete_memory'),
    # Add other URL patterns here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
