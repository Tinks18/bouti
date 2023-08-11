from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, Review
from .forms import ContactForm, ResponseForm, ReviewForm
from django.views.generic import (
    ListView, CreateView, )


from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        response = post.response.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "response": response,
                "response": False,
                "liked": liked,
                "response_form": ResponseForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        response = post.response.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        response_form = ResponseForm(data=request.POST)
        if response_form.is_valid():
            response_form.instance.email = request.user.email
            response_form.instance.name = request.user.username
            response = response_form.save(commit=False)
            response.post = post
            response.save()
        else:
            response_form = ResponseForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "response": response,
                "response": True,
                "response_form": response_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog/post_detail', args=[slug]))


class Reviews(ListView):
    model = Review
    template_name = "reviews.html"
    context_object_name = 'reviews'


class CreateReview(LoginRequiredMixin, CreateView):
    """ View to create a review """
    template_name = 'add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReview, self).form_valid(form)
