from django.shortcuts import render
from rest_framework.views import APIView
from visaprocess.models import VisaApplication, VisaStatus
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.

class VisaTypeReportView(APIView):
    def get(self,request):
        visatype_count = VisaApplication.objects.values('visa_type').annotate(count=Count('id'))
        all_types = ['Tourist', 'Business', 'Student','Work', 'Medical', 'Medical', 'Family']
        type_count_dict = {item['visa_type']:item['count'] for item in visatype_count}
        data = {types:type_count_dict.get(types,0) for types in all_types}
        return Response(data)


class VisaStatusReportView(APIView):
    def get(self, request):
        visaStatus_count = VisaStatus.objects.values('visa_status').annotate(count=Count('id'))
        all_statuses = ['AdminApprove', 'Pending','PoliceVerification','Approved']
        status_count_dict = {item['visa_status']: item['count'] for item in visaStatus_count}
        data = {status: status_count_dict.get(status, 0) for status in all_statuses}
        return Response(data )
 
class ApproveRejectReportView(APIView):
    def get(self, request):
        approve_count = VisaApplication.objects.filter(is_approved=True).count()
        reject_count = VisaApplication.objects.filter(rejected=True).count()
        total_application = VisaApplication.objects.count()
        under_modified = VisaApplication.objects.filter(is_modified=True).count()

        data = {
            'total_approve' : approve_count,
            'total_reject' : reject_count,
            'total_application' : total_application,
            'under_modified' : under_modified
        }

        return Response(data)


