"""
URL configuration for exam_portal project.
"""

from django.contrib import admin
from django.urls import path, include

# ✅ ADD THESE (for images)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Admin Panel
    path('admin/', admin.site.urls),

    # Exams App URLs
    path('', include('exams.urls')),

]

# Custom 404 Page
handler404 = "exams.views.custom_404_view"

# ✅ IMPORTANT (Image/media fix)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)