from django.urls import path

from . import views


urlpatterns = [
    #path("index", views.index, name="index"),#EMPTY OPENS The FILEPATH BEFORE
    # path("first_view", views.first_view, name="firstview"),
    # path("date_time", views.date_time, name="date_time"),
    # path("random_quote", views.random_quote, name="quotes"),

    # ex: /first_project/index/
    path("index", views.index, name="index"),
    # ex: /first_project/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /first_project/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /first_project/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path('login/', views.login_view, name='login'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('check/', views.check_logged_in, name='check'),

    path('logout/', views.logout, name='logout'),

    #Add User
    path('add_user/', views.add_user, name='add_user'),
    path('create/', views.validate, name='create'),

    #Welcome page and restricted page restricted by login
    path('welcome/', views.welcome_view,name='welcome'),
    path('restricted/',views.restricted_view ,name='restricted'),

]



