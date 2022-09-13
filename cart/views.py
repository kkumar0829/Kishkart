from django.db.models.signals import post_save
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CartData, ProductPrice, PostSave
from .serializers import CartSerializer


# Create your views here.
class CartViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            item = CartData.objects.get(id=id).lol.price_id
            item_name = CartData.objects.get(id=id).product_name
            # print("inside get")
            return Response(str(item) + item_name)
            # serializer = CartSerializer(item)  # 1 hi item ko serialize kar sakta hai
            # return Response({"status": "success hai get", "data": serializer.data}, status=status.HTTP_200_OK)

        item = CartData.objects.all()
        serializer = CartSerializer(item, many=True)
        return Response({"status": "success hai get", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print("inside post")
            return Response({"status": "success hai post", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "Error hai post", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = CartData.objects.get(id=id)
        serializer = CartSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success hai patch", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(CartData, id=id)
        item.delete()
        return Response({"status": "deleted a entry", "data": "Entry deleted"})


# def demo_post_save(sender, **kwargs):
#     entry = "HIi"
#     print("postallll.....")
#     return Response({"status": "post signa a entry", "data": "postal entry"})
#
#
# post_save.connect(demo_post_save, sender=CartViews)

# class PriceViews(APIView):
#     def get(self, request, product_id):
#         if product_id:
#             item = ProductPrice.objects.get(product_id=product_id)
#             serializer = PriceSerializer(item)
#             return Response({"status": "success hai Price get", "data": serializer.data}, status=status.HTTP_200_OK)
#

# class One2one(APIView):
#     def get(self,request,id):
#         if id:
#             item = CartData.objects.get(id=id)
#             serializer = PriceSerializer(item)
#             return Response({"status": "success hai Price get", "data": serializer.data}, status=status.HTTP_200_OK)
#
