from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CommentForms
from django.views.generic.list import ListView
from .models import BlogPostModel, TagsModel


class PostListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        posts = BlogPostModel.objects.filter(active=True).order_by('-publish_date')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = BlogPostModel.objects.all().filter(active=True).order_by('-publish_date')[:5]
        context['popular_tags'] = TagsModel.objects.all()[:8]
        return context


class PostDetailView(View):
    def get(self, request, slug):
        post = BlogPostModel.objects.get(slug=slug)
        context = {}
        context['post'] = post
        context['last_post'] = BlogPostModel.objects.all().filter(active=True).order_by('-publish_date')[:5]
        context['popular_tags'] = TagsModel.objects.all()[:8]
        context['form'] = CommentForms()
        return render(request, 'blog/detail.html', context)

    def post(self, request, slug):
        form = CommentForms(request.POST)
        post = BlogPostModel.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:detail', kwargs={'slug': slug}))
        else:
            messages.add_message(request, messages.WARNING, 'Вы ввели не правильный проверочный код')
            return redirect(reverse('blog:detail', kwargs={'slug': slug}))


class PostListTagsView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return BlogPostModel.objects.filter(active=True).filter(tags__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = BlogPostModel.objects.all().filter(active=True).order_by('-publish_date')[:5]
        context['popular_tags'] = TagsModel.objects.all()[:8]
        return context
