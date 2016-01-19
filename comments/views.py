from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsView(TemplateView):
    template_name = "comments/index.html"


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def comment_list(request):
    """
    List all comments, or create a new comment.
    """
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JSONResponse(serializer.data)

    if request.method == 'POST':
        data = FormParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
