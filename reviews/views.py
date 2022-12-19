from django.shortcuts import render
from rest_framework.views import APIView
from .models import Review
# Create your views here.


class reviewList(APIView):

    def index(request: HttpRequest) -> HttpResponse:
        review = Review.objects.all()
        for post in posts:
            rating = Rating.objects.filter(post=post, user=request.user).first()
            post.user_rating = rating.rating if rating else 0
        return render(request, "index.html", {"posts": posts})

    def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
        post = Post.objects.get(id=post_id)
        Rating.objects.filter(post=post, user=request.user).delete()
        post.rating_set.create(user=request.user, rating=rating)
        return index(request)

