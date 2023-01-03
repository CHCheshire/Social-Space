from django.shortcuts import render
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from social_space.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import permissions, status, filters
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ReviewList(APIView):

    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Review.objects.all()
    search_fields = ['author_username', 'header']
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(
            review, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ReviewDetail(APIView):
    permission_classes = {IsOwnerOrReadOnly}
    serializer_class = ReviewSerializer

    def get_object(self, pk):
        try:
            review = Review.objects.get(pk=pk)
            self.check_object_permissions(self.request, review)
            return review
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(
            review, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(
            review, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
