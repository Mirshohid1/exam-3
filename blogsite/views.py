from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Author, Comment
from .forms import CommentForm, ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView, DetailView, FormView
from django.views.generic.edit import CreateView, FormMixin
from django.contrib import messages


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.all() \
            .select_related('author') \
            .prefetch_related('images', 'categories', 'tags')

        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['author'] = Author.objects.get(flag_about=True)
        except Exception as e:
            print(f"Error: {e}")
            context['author'] = None

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            form.save()
        return redirect('post_detail', self.kwargs['pk'])

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = "New Contact Form Submission"
        email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, email_message, from_email, recipient_list)

        return super().form_valid(form)

class TermsConditionsTemplateView(TemplateView):
    template_name = 'terms-conditions.html'

class PrivacyPolicyTemplateView(TemplateView):
    template_name = 'privacy-policy.html'