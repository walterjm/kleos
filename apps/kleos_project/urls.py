from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^jobs$', views.get_job),
	url(r'^resume/submit$', views.submit_resume),
	url(r'^employers$', views.employerportal),
	url(r'^signin$', views.signin),
	#(?P<user_id>\d+)
  ]