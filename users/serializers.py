from rest_framework import serializers
from .models import (
    Profile,
    FavoriteMovieGenre,
    FavoriteMusicGenre,
    FavoriteSport,
)
from pathlib import Path


class BaseFavoriteGenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'genre']
        extra_kwargs = {'genre': {'required': False, 'allow_null': True}}


class FavoriteMovieGenreSerializer(BaseFavoriteGenreSerializer):
    class Meta(BaseFavoriteGenreSerializer.Meta):
        model = FavoriteMovieGenre


class FavoriteMusicGenreSerializer(BaseFavoriteGenreSerializer):
    class Meta(BaseFavoriteGenreSerializer.Meta):
        model = FavoriteMusicGenre


class FavoriteSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSport
        fields = ['id', 'sport']
        extra_kwargs = {'sport': {'required': False, 'allow_null': True}}


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    favorite_movie_genre = FavoriteMovieGenreSerializer(allow_null=True)
    favorite_music_genre = FavoriteMusicGenreSerializer(allow_null=True)
    favorite_sport = FavoriteSportSerializer(allow_null=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def update_nested_instance(self, related_instance, data, model_class):
        if data is not None:
            if related_instance:
                for attr, value in data.items():
                    setattr(related_instance, attr, value)
                related_instance.save()
            else:
                related_instance = model_class.objects.create(**data)
        return related_instance

    def update(self, instance, validated_data):
        nested_data = {
            'favorite_movie_genre': validated_data.pop(
                'favorite_movie_genre', None
            ),
            'favorite_music_genre': validated_data.pop(
                'favorite_music_genre', None
            ),
            'favorite_sport': validated_data.pop('favorite_sport', None),
        }

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        for field, data in nested_data.items():
            model_class = self.fields[field].Meta.model
            setattr(
                instance,
                field,
                self.update_nested_instance(
                    getattr(instance, field), data, model_class
                ),
            )

        instance.save()
        return instance

    def validate_image(self, value):
        path = Path(value.name)
        file_extension = path.suffix.lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if file_extension not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg, or png!'
            )
        return value

    class Meta:
        model = Profile
        fields = [
            'owner',
            'first_name',
            'last_name',
            'bio',
            'favorite_movie_genre',
            'favorite_music_genre',
            'favorite_sport',
            'image',
            'location',
            'url_link',
            'contact_email',
            'is_active',
            'created_at',
            'updated_at',
            'is_owner',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
