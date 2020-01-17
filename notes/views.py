from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from .forms import NotesCreateForm, NotesUpdateForm
from .models import Notes

class NotesCreateView(LoginRequiredMixin, CreateView):
	model = Notes
	form_class = NotesCreateForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		super().get_context_data(**kwargs)
		kwargs['createnew'] = 'active'
		return super().get_context_data(**kwargs)

class NotesListView(LoginRequiredMixin, ListView):
	model = Notes
	paginate_by = 2
	def get_queryset(self):	
		user = self.request.user
		return Notes.objects.filter(user=user).order_by('-created_on')

	def get_context_data(self, **kwargs):
		super().get_context_data(**kwargs)
		kwargs['mynotes'] = 'active'
		return super().get_context_data(**kwargs)

class NotesDetailView(LoginRequiredMixin, DetailView):
	model = Notes

class NotesUpdateView(LoginRequiredMixin, UpdateView):
	model = Notes
	form_class = NotesUpdateForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.last_modified = timezone.now()
		return super().form_valid(form)

class NotesDeleteView(LoginRequiredMixin, DeleteView):
	model = Notes
	success_url = '/'