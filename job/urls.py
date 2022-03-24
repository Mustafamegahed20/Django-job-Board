from django.urls import include, path
from graphviz import view

from . import  views



urlpatterns = [

    path('',views.job_list),#get all jobs
    path('<int:id>',views.job_detail), #get deatial about the job what i need

]