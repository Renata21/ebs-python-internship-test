from unicodedata import category
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer

from drf_util.decorators import serialize_decorator


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    '''
    7 Endpoint that returns the Blog post object and list of comments.
    '''
    serializer_class = BlogSerializer, CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        # added comments form this blog 
        comments = Comment.objects.all().filter(blog_id=pk)
        # added param dict for a return with 2 types of objects
        param = {
            "blog": BlogSerializer(blog).data,
            "comments": CommentSerializer(comments, many=True).data
        }
        return Response(param)


class CreateBlogPostView(GenericAPIView):
    ''' 
    3 Endpoint for creating a blog post that will add a new record in blog table
    '''
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            category=validated_data['category'],
            enabled=True
        )
        blog.save()

        return Response(BlogSerializer(blog).data)


class CreateCommentView(GenericAPIView):
    ''' 
    6 Endpoint for creating a comment to a blog post and created blog_comment table with these fields
    '''
    serializer_class = CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comment.objects.create(
            text = validated_data['text'],
            blog = validated_data['blog']
        )
        comment.save()

        return Response(CommentSerializer(comment).data)
