from django.urls import path
from . import views

urlpatterns = [

    path('', views.images, name='homepage'),
    path('image/<int:pk>/delete/', views.delete_image, name='delete_image'),
    #image detail
    path('image/<int:pk>/', views.image_detail, name='image_detail'),

    #NEW URL PATTERNS
    path('add_Imagecomment/<int:image_id>/', views.add_Imagecomment, name='add_Imagecomment'),
    path('delete_Imagecomment/<int:image_id>/<int:comment_id>/', views.delete_Imagecomment, name='delete_Imagecomment'),

]

from django.conf import settings 
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)