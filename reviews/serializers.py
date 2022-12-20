from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Review
        fields = [
            'header', 'text', 'rating'
        ]
