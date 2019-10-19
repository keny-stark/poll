"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll'),
    path('poll/add/', PollCreateView.as_view(), name='poll_add'),
    path('poll/<int:pk>/edit/', PollUpdate.as_view(), name='update_poll'),
    path('poll/<int:pk>/delete/', DeletePoll.as_view(), name='delete_poll'),
    path('poll/<int:pk>/add_choice/', ChoiceForPollCreateView.as_view(), name='create_new_choice'),
    path('poll/choice/delete/<int:pk>/', DeleteChoice.as_view(), name='delete_choice'),
    path('poll/answer/', AnswerView.as_view(), name='answer'),
    path('poll/choice/update/<int:pk>/', ChoiceUpdate.as_view(), name='update_choice'),
    path('poll/add_answer/<int:pk>/', AnswerForPollCreateView.as_view(), name='answer_add'),
]
