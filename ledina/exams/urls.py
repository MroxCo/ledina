from django.conf.urls import url
from ledina.exams import views


urlpatterns = [
    url(r'^(?P<letnik_id>[1-4])/$', views.letnik, name="letnik_id"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)$', views.subject, name="subject_id"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)/dodaj$', views.create_exam, name="create_exam"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)/comment$', views.comment, name="comment"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)/remove_comment$', views.remove_comment, name="remove_comment"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)/remove_exam$', views.remove_exam, name="remove_exam"),
    url(r'^(?P<letnik_id>[1-4])/(?P<classes_id>[A-G])/(?P<subject_id>[\w\-]+)/mark_exam$', views.mark_exam, name="mark_exam"),

]














































