from django.conf.urls import url
from . import views

urlpatterns = [
   
    url(r'^$', views.home, name='home'),
    url(r'^education/$', views.education, name='education'),
    url(r'^education/school_diploma/$', views.school_diploma, name='school_diploma'),
    url(r'^education/AIT_diploma/$', views.AIT_diploma, name='AIT_diploma'),
    url(r'^education/DonNTU_diploma/$', views.DonNTU_diploma, name='DonNTU_diploma'),
    url(r'^education/license/$', views.license, name='license'),
    url(r'^education/teacher_license/$', views.teacher_license, name='teacher_license'),
    url(r'^experience/$', views.experience, name='experience'),
    url(r'^experience/work1/$', views.book1, name='work1'),
    url(r'^experience/work2/$', views.book2, name='work2'),
    url(r'^experience/work3/$', views.book3, name='work3'),
	url(r'^experience/work4/$', views.book4, name='work4'),
	url(r'^publication/$', views.publication, name='publication'),
	url(r'^characteristic/$', views.characteristic, name='characteristic'),
	url(r'^vlog/$', views.vlog, name='vlog'),
	url(r'^projects/$', views.projects, name='projects'),
]