from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookViewset
from .views import BookListApiView
from .views import BookControlView
from .views import BookCreateApiView
from .views import BookDeleteApiView
from .views import BookDetailApiView
from .views import BookUpdateApiView
from .views import BookListCreateApiView

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('booklistcreate/', BookListCreateApiView.as_view()),
    path('bookcontrol/<int:pk>/', BookControlView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls
