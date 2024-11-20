from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from myprojects.models import Project, Tag, Review
from users.models import Profile



class ReviewSerializers(ModelSerializer):
    class Meta:
        model = Review
        fields = ['owner','value']        


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name']
    

class ProjectSerializers(ModelSerializer):
    owner = ProfileSerializers(many = False)
    tags = TagSerializers(many = True)
    reviews = serializers.SerializerMethodField()    # here which variable we use that variable name is used to retrive data 
    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        print("obj",obj)
        review = obj.review_set.all()
        serializer = ReviewSerializers(review, many = True)
        return serializer.data