from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import ContactForm


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
            "blog/post_detail.html",
            {
                "post": post,
             },
        )


def contact(request):
    """
    Submits contact  form 
    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('blog/contact?submitted = True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'blog/contact.html',
                  {'form': form, 'submitted': submitted})