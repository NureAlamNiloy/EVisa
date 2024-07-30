from django.shortcuts import render
from rest_framework.views import APIView
from visaprocess.models import VisaApplication, VisaStatus
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.

class VisaTypeReportView(APIView):
    def get(self,request):
        visatype_count = VisaApplication.objects.values('visa_type').annotate(count=Count('id'))
        data = {
            'visa_types':{item['visa_type']:item['count'] for item in visatype_count}
        }
        return Response(data )


class VisaStatusReportView(APIView):
    def get(self, request):
        visaStatus_count = VisaStatus.objects.values('visa_status').annotate(count=Count('id'))
        data = {
            'visa_statuses' : {item['visa_status']:item['count'] for item in visaStatus_count}
        }
        return Response(data )


class ApproveRejectReportView(APIView):
    def get(self, request):
        approve_count = VisaApplication.objects.filter(is_approved=True).count()
        reject_count = VisaApplication.objects.filter(rejected=True).count()

        data = {
            'total_approve' : approve_count,
            'total_reject' : reject_count
        }

        return Response(data)

