from rest_framework import serializers
from system_app.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    # 新增這一行(*)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = "__all__"
    