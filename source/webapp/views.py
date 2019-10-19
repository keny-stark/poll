from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice


class IndexView(ListView):
    context_object_name = 'poll'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    model = Poll
    template_name = 'poll/poll.html'


class PollCreateView(CreateView):
    template_name = 'poll/add_poll.html'
    model = Poll
    form_class = PollForm
    redirect_url = 'poll'


class PollUpdate(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/edit.html'
    redirect_url = 'poll'
    success_url = reverse_lazy('index')


class DeletePoll(DeleteView):
    template_name = 'poll/delete_poll.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')



