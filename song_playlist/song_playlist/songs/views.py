from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Song
from .populate_db_data import insert_data_into_db
from .serializers import SongSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view, renderer_classes
from .models import Song
from .serializers import SongSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    """

    :param request:
    :return: List of all available API's
    """
    result_obj = {
        "Songs list": "http://127.0.0.1:8000/songs/",
        "Get details of given song": "http://127.0.0.1:8000/songs/?title=all",
        "Rate song": "http://127.0.0.1:8000/rate_song/1"
    }
    return Response(result_obj)


def insert_data(request):
    """
    :param request:
    :return: Success message after data insertion
    """
    if request.method == 'GET':
        msg = insert_data_into_db()
        data = {'msg': msg}
        return JsonResponse(data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def song_list(request):
    """
    :param request:
    :return: List of all song playlist with details & given with title shows the details of the song respectively.
    """
    title = request.GET.get('title', '')
    if title:
        songs = Song.objects.filter(title__icontains=title).order_by('index')
    else:
        songs = Song.objects.all().order_by('index')

    page = request.GET.get('page', 1)
    page_size = 10
    paginator = Paginator(songs, page_size)
    try:
        song_page = paginator.page(page)
    except PageNotAnInteger:
        song_page = paginator.page(1)
    except EmptyPage:
        song_page = paginator.page(1)
    serializer = SongSerializer(song_page, many=True)
    previous = song_page.previous_page_number() if song_page.has_previous() else None
    next = song_page.next_page_number() if song_page.has_next() else None
    result_obj = {
        "count": paginator.count,
        "next": next,
        "previous": previous,
        "num_pages": paginator.num_pages,
        "data": serializer.data
    }
    return Response(result_obj)


@api_view(['GET', 'PUT'])
def rate_song(request, pk):
    """
    :param request:
    :return: Select the song & give the ratings
    """
    data = request.data
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


