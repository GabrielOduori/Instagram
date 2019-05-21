from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.index, name = 'index'),
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^upload_image/', views.upload_image, name='upload_image'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^stream/', views.stream, name='stream'),
    url(r'^login/', views.login_user, name = 'login'),
    url(r'^logout/', views.logout_user, name = 'logout'),
    url(r'^register/', views.register_user, name = 'register'),
    url(r'^images/(?P<id>\d+)/$', views.image_detail, name = 'image_detail'),
    url(r'^images/(?P<id>\d+)/comment', views.add_comment, name = 'add_comment'),
    
    
    
    # url(r'^logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),

   
    
    
    # url(r'^$', views.news_of_day, name = 'newsToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news, name = 'pastNews'),
    # url(r'^search/', views.search_results, name = 'search_results'),
    # url(r'^article/(\d+)',views.article,name ='article'),
    # url(r'^news/articles$', views.new_article, name = 'new-article'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
