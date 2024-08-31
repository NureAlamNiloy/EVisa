from django.db.models.functions import TruncYear, TruncMonth, TruncWeek
from django.utils import timezone
from rest_framework.views import APIView
from visaprocess.models import VisaApplication, VisaStatus
from rest_framework.response import Response
from django.db.models import Count


# Specific date filtering report.
# class VisaTypeReportView(APIView):
#     def post(self, request):
#         start_date = request.data.get('start_date')
#         end_date = request.data.get('end_date')

#         # Filter VisaApplication by the date range if provided
#         if start_date and end_date:
#             visa_applications = VisaApplication.objects.filter(submission_date__range=[start_date, end_date])
#         else:
#             visa_applications = VisaApplication.objects.all()

#         visatype_weekly = visa_applications.annotate(week=TruncWeek('submission_date')).values('week', 'visa_type').annotate(count=Count('id'))
#         data = {
#             "total" : list(visatype_weekly),
#         }
#         return Response(data)


class VisaTypeReportView(APIView):
    def get(self, request):
        now = timezone.now()
        start_of_last_week = now - timezone.timedelta(days=now.weekday() + 7)
        start_of_last_month = (now.replace(day=1) - timezone.timedelta(days=1)).replace(day=1)
        start_of_last_year = now.replace(month=1, day=1) - timezone.timedelta(days=1)
        start_of_last_year = start_of_last_year.replace(month=1, day=1)

        visatype_weekly = VisaApplication.objects.filter(submission_date__gte=start_of_last_week).annotate(week=TruncWeek('submission_date')).values('week', 'visa_type').annotate(count=Count('id'))
        visatype_monthly = VisaApplication.objects.filter(submission_date__gte=start_of_last_month).annotate(month=TruncMonth('submission_date')).values('month', 'visa_type').annotate(count=Count('id'))
        visatype_yearly = VisaApplication.objects.filter(submission_date__gte=start_of_last_year).annotate(year=TruncYear('submission_date')).values('year', 'visa_type').annotate(count=Count('id'))
        visatype_total = VisaApplication.objects.values('visa_type').annotate(count=Count('id'))

        data = {
            "total" : list(visatype_total),
            "last_week": list(visatype_weekly),
            "last_month": list(visatype_monthly),
            "last_year": list(visatype_yearly),
        }
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


