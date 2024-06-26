from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogapp.forms import ArticleForm
from blogapp.models import Article
from blogapp.services import get_cached_article_list
from pytils.translit import slugify


# Create your views here.
class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["object_list"] = get_cached_article_list()
        return context_data


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object

    # и как быть с кешированием если объект меняется при прсомотре? Никак.


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    permission_required = "blogapp.add_article"
    success_url = reverse_lazy("blogapp:article_list")

    login_url = "users:login"
    redirect_field_name = "login"

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_article = form.save()
    #         new_article.slug = slugify(new_article.name)
    #         new_article.save()
    #     return super().form_valid(form)
    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        get_cached_article_list(recached=True)
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    permission_required = "blogapp.change_article"

    # success_url = reverse_lazy('article:blog')

    login_url = "users:login"
    redirect_field_name = "login"

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_article = form.save()
    #         new_article.slug = slugify(new_article.name)
    #         new_article.save()
    #     return super().form_valid(form)
    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        get_cached_article_list(recached=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blogapp:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("blogapp:article_list")
    permission_required = "blogapp.delete_article"

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        get_cached_article_list(recached=True)
        return super().form_valid(form)
