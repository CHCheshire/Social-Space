from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_featured_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.featured_image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.featured_image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'title', 'author', 'updated_on', 'content',
            'featured_image', 'excerpt', 'created_on', 'status', 'likes',
            'profile_id', 'profile_image', 'featured_image_filter']
