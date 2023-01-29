from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from ads.models import Ad, Comment


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'title',
            'price',
            'description',
            'pk',
            'image'
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(source='author.phone')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_id = serializers.IntegerField(source='author.id')

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        ]


class AdCreateSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(source='author.phone', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.IntegerField()

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        ]


class AdUpdateSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(source='author.phone', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        ]


# ------------------COMMENTS SERIALIZERS------------------

class CommentsListSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image')

    class Meta:
        model = Comment
        fields = [
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image')

    class Meta:
        model = Comment
        fields = [
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    author_id = serializers.IntegerField()
    ad_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = [
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image'
        ]


class CommentUpdateSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    author_id = serializers.IntegerField(read_only=True)
    ad_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image'
        ]
