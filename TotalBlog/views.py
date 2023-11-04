from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib import messages
from .models import *
from .forms import *


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 12


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
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

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class BookingView(FormView):

    template_name = 'bookings.html'
    form_class = OnlineForm

    def booking_view(self, request):
        return render(request, 'bookings.html')

    def post(self, request):

        form = OnlineForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect(reverse('completed'))
        else:
            messages.error(request, 'Seems like you need to fill'
                                    'out all the required fields')

        return render(request, 'bookings.html', {
                'form': form
                }
                )


class ListBookingView(generic.DetailView):

    def get(self, request, *args, **kwargs):

        bookings = Booking.objects.filter(user__id=request.user.id)
        return render(request, 'completed.html', {
            'bookings': bookings
            }
        )


def edit_booking_view(request, booking_id):

    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            if request.method == 'POST':
                form = OnlineForm(data=request.POST, instance=booking)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Booking has been updated')
                    return redirect('/')
        else:
            messages.error(request, 'You do not have the authority'
                                    'to access this page!')
            return redirect('/')

    form = OnlineForm(instance=booking)

    return render(request, 'edit_bookings.html', {
        'form': form
        })


def delete_booking(request, booking_id):

    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            booking.delete()
            # Pops up a message to the user when a bookings is cancelled
            messages.success(request, 'Your booking has been cancelled')
            return redirect('/')
        else:
            messages.error(request, 'You cannot access this'
                                    'page without a log in!')
            return redirect('/')
