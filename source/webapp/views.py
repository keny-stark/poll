from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from webapp.forms import PollForm, ChoiceForm, ChoiceForPollForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChoiceForm()
        return context


class PollCreateView(CreateView):
    template_name = 'poll/add_poll.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})


class PollUpdate(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/edit.html'
    redirect_url = 'poll'

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})


class DeletePoll(DeleteView):
    template_name = 'poll/delete_poll.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')


class ChoiceForPollCreateView(CreateView):
    template_name = 'choice/add_choice.html'
    form_class = ChoiceForPollForm

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choice.create(**form.cleaned_data)
        return redirect('article_view', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)


class ChoiceUpdate(UpdateView):
    model = Choice
    form_class = PollForm
    template_name = 'choice/edit_choice.html'
    redirect_url = 'choice'

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})


class DeleteChoice(DeleteView):
    template_name = 'choice/delete_choice.html'
    model = Choice
    context_object_name = 'choice'
    success_url = reverse_lazy('index')

