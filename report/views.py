from collections import defaultdict
from django.utils import timezone
from rest_framework.views import APIView
from visaprocess.models import VisaApplication, VisaStatus
from rest_framework.response import Response
from django.db.models import Count
from datetime import datetime

class VisaTypeReportView(APIView):
    def get(self, request):
        now = timezone.now()
        start_of_last_week = now - timezone.timedelta(days=now.weekday() + 7)
        start_of_last_month = (now.replace(day=1) - timezone.timedelta(days=1)).replace(day=1)
        start_of_last_year = now.replace(month=1, day=1) - timezone.timedelta(days=1)
        start_of_last_year = start_of_last_year.replace(month=1, day=1)

        visa_apps = VisaApplication.objects.filter(submission_date__gte=start_of_last_year)
        weekly_grouping = defaultdict(lambda: defaultdict(int))
        monthly_grouping = defaultdict(lambda: defaultdict(int))
        yearly_grouping = defaultdict(lambda: defaultdict(int))
        
        for app in visa_apps:
            if app.submission_date >= start_of_last_week:
                week = app.submission_date.strftime('%Y-%W')
                weekly_grouping[app.visa_type][week] += 1


            if app.submission_date >= start_of_last_month:
                month = app.submission_date.strftime('%Y-%m')
                monthly_grouping[app.visa_type][month] += 1

            year = app.submission_date.strftime('%Y')
            yearly_grouping[app.visa_type][year] += 1
            
        visatype_total = VisaApplication.objects.values('visa_type').annotate(count=Count('id'))

        data = {
            "total": list(visatype_total),
            "last_week": weekly_grouping,
            "last_month": monthly_grouping,
            "last_year": yearly_grouping,
        }
        return Response(data)

class VisaStatusReportView(APIView):
    def get(self, request):
        visaStatus_count = VisaStatus.objects.values('visa_status').annotate(count=Count('id'))
        all_statuses = ['AdminApprove', 'Pending', 'PoliceVerification', 'Approved']
        status_count_dict = {item['visa_status']: item['count'] for item in visaStatus_count}
        data = {status: status_count_dict.get(status, 0) for status in all_statuses}
        return Response(data)

class ApproveRejectReportView(APIView):
    def get(self, request):
        approve_count = VisaApplication.objects.filter(is_approved=True).count()
        reject_count = VisaApplication.objects.filter(rejected=True).count()
        total_application = VisaApplication.objects.count()
        under_modified = VisaApplication.objects.filter(is_modified=True).count()

        data = {
            'total_approve': approve_count,
            'total_reject': reject_count,
            'total_application': total_application,
            'under_modified': under_modified
        }

        return Response(data)
