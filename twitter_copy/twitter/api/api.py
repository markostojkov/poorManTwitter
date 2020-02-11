from rest_framework import viewsets
from twitter.models import Post
from twitter.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing twitter post instances.
	"""
	serializer_class = PostSerializer
	queryset = Post.objects.all()