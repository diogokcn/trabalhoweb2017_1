from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.http import Http404

class UserFormView(View):
	form_class = UserForm
	template_name = 'registration/registration_form.html'

	# Display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# Process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#Cleaned (nomalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credential are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home:index')

		return render(request, self.template_name, {'form': form})