from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
             },
        )


# Create your views here.
# class PostList(generic.View):
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             'blog.html',
#             # {
#             #     'blog_form': BLOGForm()
#             # }
#         )
# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "blog.html"
#     paginate_by = 6








# def post_list(request):
#     return render(request, 'blog/post_list.html')
