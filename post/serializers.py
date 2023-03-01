from rest_framework import serializers
from post.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def validate_featured_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)
       
    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'title', 'author', 'is_author', 'updated_on', 'content',
            'featured_image', 'created_on',
            'profile_id', 'profile_image', 'like_id', 'likes_count',
            'post_tag']
