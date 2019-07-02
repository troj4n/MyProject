from django.conf.urls import url
from django.conf.urls import include
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

urlpatterns=[
		path('',views.get,name='get'),
		#path('users/<str:slug>/',views.get_user_details),

		path('blogs/',views.blog_list_view,name='blogs_list_view'),
		path('write-blog/',views.blog_create_view,name='create_blog'),
		path('<str:slug>/edit',views.blog_update_view,name='update_blog'),
		path('<str:slug>/delete',views.blog_delete_view,name='delete_blog'),
		path('<str:slug>/',views.blog_detail_view,name='detail_view'),	
		
]