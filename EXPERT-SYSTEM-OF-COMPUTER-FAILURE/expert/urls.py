from django.urls import include, path
from django.contrib import admin
from . import views
from expert.views import professions

app_name = 'expert'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_view, name='login'),
    path('professions/', views.login_view, name='professions'),
	path('logout/', views.logout_view, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('evaluation/', views.evaluation, name='evaluation'),
	path('results/', views.results, name='results'),
	
]


admin.site.site_header = 'Administration CONFEXPERT'                    # default: "Django Administration"
admin.site.index_title = 'Page Administration'                       # default: "Site administration"
admin.site.site_title = 'Administration de CONFEXPERT'           # default: "Django site admin"
