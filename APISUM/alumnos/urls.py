from django.conf.urls import url
from alumnos import views

urlpatterns= [
	url(r'^alumnos/$', views.AlumnoList.as_view()),
	url(r'^alumnos/(?P<pk>[0-9]+)/$', views.AlumnosDetail.as_view()),
]