# Framework imports
from django.core import exceptions
from rest_framework import serializers

# App imports
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price') # noqa

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        # Check, title must be a string!
        if not isinstance(title, str):
            raise exceptions.ValidationError(
                {
                    "Status": False,
                    "Message": "Please provide a valid title string",
                }
            )

        # Check, title and author must be exists in database
        if Book.objects.filter(title=title, author=author).exists():
            raise exceptions.ValidationError(
                {
                    "Status": False,
                    "Message": "You can not upload that the same book title and author!" # noqa
                }
            )
        return data
