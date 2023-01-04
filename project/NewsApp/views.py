from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class Post_List(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'post_list.html'
    context_object_name = 'Post'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Posts(DetailView):
    model = Post
    context_object_name = 'Post'


class PostCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('NewsApp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class PostCreateArticles(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('NewsApp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit_AR.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class Postedit(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('NewsApp.edit_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class PostDelete(PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('NewsApp.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('fb')


class PosteditArticles(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('NewsApp.edit_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class PostDeleteArticles(PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('NewsApp.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('fb')


class CategoryListView(ListView):
    model = Post
    context_object_name = 'Category'
    template_name = 'category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})