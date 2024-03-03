"""
Vistas para el blog
"""
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

from .forms import PostForm
from .models.post_model import Post
from apps.blog.tasks import upload_cover_image


class HomeView(ListView):
    """
    Vista basada en clase para la página de inicio del blog
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.published.all()
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = self.queryset.order_by('-published_at')[:3]
        return context


class PostDetailView(DetailView):
    """
    Vista basada en clase para la página de detalle de un post
    """
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostList(ListView):
    """
    Vista basada en clase para la página de listado de posts
    """
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    queryset = Post.published.all()
    paginate_by = 10


class PostCreateView(FormView):
    """
    Vista basada en clase para la creación de un post
    """
    template_name = 'blog/create.html'
    form_class = PostForm
    success_url = '/create/'

    def form_valid(self, form):
        cd = form.cleaned_data
        image_file: InMemoryUploadedFile | None = cd.get('cover_image')
        # print(cd)

        post: Post = form.save(author=User.objects.first())
        # print(post.id)

        if image_file and post.id:
            image_bytes: bytes = image_file.read()
            upload_cover_image.delay(image_bytes, post.id)

        return super().form_valid(form)
