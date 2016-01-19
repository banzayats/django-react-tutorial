from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text')

        def create(self, validated_data):
            return Comment.objects.create(**validated_data)
