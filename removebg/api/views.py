from django.shortcuts import render
from api.models import Removebg
from api.serializers import RemovebgSerializer,RemovebgUpdateSerializer,RemovebgPostSerializer
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from django.views import View
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
def removebg(request):
	return render(request,'removebg/index.html')

class RemovebgView(generics.ListAPIView):

    queryset = Removebg.objects.all()
    serializer_class = RemovebgSerializer


class RemovebgEdit(generics.RetrieveUpdateAPIView):

    queryset = Removebg.objects.all()
    serializer_class =RemovebgUpdateSerializer

class RemovebgDetails(generics.RetrieveAPIView):

    queryset = Removebg.objects.all()
    serializer_class = RemovebgSerializer

class RemovebgPost(generics.ListCreateAPIView):
    serializer_class = RemovebgPostSerializer
  

class RemovebgpostView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = RemovebgPostSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# post = Post.objects.create(title='First post', text='This is a first post')
# print(PostSerializer(post).data)
# class RemovebgAdd(View):

#     def post(self, request):

#         print(request.FILES)
#         Removebg.objects.create(
#             images=request.FILES.get('images'),
       
#         )
#         return HttpResponse('success')

