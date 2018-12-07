from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only':True}
        }
        fields = (
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review

    def validate_rating(self, value):
        if value in range(1,6):
            return value
        raise serializers.ValidationError(
            'Rating must be an integer between 1 and 5'
        )


class CourseSerializer(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="apiv2:review-detail"
    )

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews'
        )
        model = models.Course