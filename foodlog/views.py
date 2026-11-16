from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from foodlog.models import FoodLog
from foodlog.serializers import FoodLogSerializer


class FoodLogListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        qs = FoodLog.objects.filter(owner=auth_user)

        serializer_instance = FoodLogSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        auth_user = request.user

        serializer_instance = FoodLogSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=auth_user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)



from foodlog.permissions import IsOwner

class FoodLogRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        # qs = FoodLog.objects.get(id=pk)

        qs = get_object_or_404(FoodLog,id=pk) #this is for checking if the object exists or not, if not it will return 404 error

        self.check_object_permissions(request,qs) #this is for checking the permission of the user to access the object

        serializer_instance = FoodLogSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        #instance = FoodLog.objects.get(id=pk)

        instance = get_object_or_404(FoodLog,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instance=FoodLogSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        # qs = FoodLog.objects.get(id=pk).delete()

        qs = get_object_or_404(FoodLog,id=pk)

        self.check_object_permissions(request,qs)

        qs.delete()

        return Response({"message":"deleted"})


from datetime import datetime
from django.db.models import Sum

# class FoodLogSummaryView(APIView):

#     authentication_classes = [authentication.BasicAuthentication]

#     permission_classes = [permissions.IsAuthenticated]

#     def get(self,request):

#         auth_user = request.user

#         auth_user_expenses = FoodLog.objects.filter(owner=auth_user)

#         response_data = {
#             "todays_total":0,
#             "monthly_total":0
#         }

#         cur_date = datetime.today().date()

#         todays_total = auth_user_expenses.filter(created_at__date = cur_date).values("amount").aggregate(total=Sum("amount")).get("total")

#         response_data = {"todays_total"}=todays_total