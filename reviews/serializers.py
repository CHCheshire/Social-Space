from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)
        
    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Review
        fields = [
            'header', 'text', 'rating', 'author',
            'created_on', 'review_tag', 'is_author'
        ]
