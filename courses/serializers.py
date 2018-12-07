from django.db.models import Avg

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
    average_rating = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews',
            'average_rating',
        )
        model = models.Course

    '''this is not a good way to do this. should go back and change this to be a 
    value stored in the database that gets updated each time a new reivew is added'''
    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0
        return round(average*2) / 2