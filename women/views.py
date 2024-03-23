from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from rest_framework import generics, viewsets

from .permissions import IsAdmin
from .serializers import WomenSerial


class CreateSetWomen(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerial
    permission_classes = (IsAuthenticatedOrReadOnly, )

class UpdateSetWomen(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerial

class DeleteSetWomen(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerial
    permission_classes = (IsAdmin, )

# class ViewsetWomen(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerial

# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerial

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerial
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerial
#
# class WomenCheckAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerial

# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all().values()
#         return Response({'womens': WomenSerial(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerial(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"GG"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error":"GG"})
#
#         serializer = WomenSerial(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "GG"})
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"ERROR": "Object Not Found !"})
#
#         return Response({"post": f"Object {str(pk)} is deleted"})
