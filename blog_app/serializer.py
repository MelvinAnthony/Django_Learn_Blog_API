from rest_framework import serializers
from blog_app.models import *



class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Blog
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many = True, read_only = True)



    class Meta:
        model = Category
        fields = '__all__'



# class CategorySerializer(serializers.ModelSerializer):
#     #category_name = serializers.CharField()
#     #category = BlogSerializer(many = True, read_only = True)
#     #category = serializers.StringRelatedField(many = True)
#     #category = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

#     # category = serializers.HyperlinkedRelatedField(
#     #     many = True, 
#     #     read_only = True,
#     #     view_name = 'detial_blog'        
#     # )

#     #category = serializers.SlugRelatedField(many = True, read_only = True, slug_field = 'slug')
    
    # class Meta:
    #     model = Category
    #     exclude = ['id',]











'''
# def blog_title_valid(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Name is too short, it should have at least 5 characters.")
#     return value

class BlogSerializsers(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # blog_title = serializers.CharField(validators=[blog_title_valid])  
    # blog_description = serializers.CharField()
    # post_date = serializers.DateField(required=True)
    # is_public = serializers.BooleanField()
    # slug = serializers.CharField(required=True)



    len_blog_title = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        #fields = ['blog_title','blog_description','data','is_public']          for filter the specific data to gather
        #exclude = ['data','is_public']                              for filter the speific data for skip to gather
    
    def get_len_blog_title(self,object):
        return len(object.blog_title)

    #                 #field level validation
    # def validate_name(self, value):
    #     if len(value) < 4:
    #         return serializers.ValidationError("Title was very short")
        
    #     else:
    #         return value
        
    # def validate_description(self, value):
    #     if len(value) < 10:
    #         return serializers.ValidationError("Description is to short add content")
        
    #     else:
    #         return value



                        #object level validation
    # def validate(self, data):
    #     if data['blog_title'] ==  data['blog_description']:
    #         raise serializers.ValidationError('Name is and description Not a same')
    #     return data

                    # serializers for create manually

# class BlogSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     blog_title = serializers.CharField()
#     #author = serializers.CharField(read_only = True)
#     blog_description = serializers.CharField()
#     post_date = serializers.DateField(required = True)
#     is_public = serializers.BooleanField()
#     slug = serializers.CharField(required = True)


#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get("name",instance.name)
#         #instance.author = validated_data.get("author",instance.author)
#         instance.description = validated_data.get("description",instance.description)
#         instance.post_date = validated_data.get("post_date",instance.post_date)
#         instance.is_public = validated_data.get("is_public",instance.is_public)
#         instance.slug = validated_data.get("slug",instance.slug)
#         instance.save()
#         return instance

'''



