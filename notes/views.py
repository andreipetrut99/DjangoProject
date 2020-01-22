from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from notes.forms import NotesForm
from notes.models import Notes


class NotesIndex(ListView):
    model = Notes
    context_object_name = 'all_notes'
    template_name = 'notes/notes_index.html'


class CreateNotesView(CreateView):
    model = Notes
    template_name = 'notes/notes_form.html'
    form_class = NotesForm

    def get_success_url(self):
        return reverse('notes:index')


class UpdateNotesView(UpdateView):
    model = Notes
    template_name = 'notes/notes_form.html'
    form_class = NotesForm

    def get_success_url(self):
        return reverse('notes:index')


class DeleteNotesView(DeleteView):
    model = Notes
    template_name = 'notes/notes_form.html'
    form_class = NotesForm

    def get_success_url(self):
        return reverse('notes:index')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('notes:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
