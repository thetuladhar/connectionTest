# CREATED URLS PATH

from django.urls import path

from . import views

urlpatterns = [
    #Login and Authenticate

    path('', views.login_view, name='login'),
    path('authenticate/', views.authenticate, name='authenticate'),

    path('logout/', views.logout, name='logout'),

    #Add User
    path('add_user/', views.add_user, name='add_user'),
    path('create/', views.validate, name='create'),

    #homepage
    path('homepage/', views.homepage_view,name='homepage'),

    # Other URL patterns
    #path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

    #comments
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:post_id>/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    #IMAGE RELATED URLS
    path('images/', views.images, name='images'),

    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('image_detail/<int:pk>/', views.image_detail, name='image_detail'),

    path('add_image_comment/<int:image_id>/', views.add_image_comment, name='add_image_comment'),
    path('delete_image_comment/<int:image_id>/<int:comment_id>/', views.delete_image_comment, name='delete_image_comment'),

    path('<str:username>/', views.user_profile, name='user_profile'),
]
#DEBUG IMAGE MISSING FEATURE
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
