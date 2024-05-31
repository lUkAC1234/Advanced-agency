from django.utils import timezone
from datetime import timedelta
from .models import VisitHistory

class TrackUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = timezone.now()
        three_hours_ago = now - timedelta(hours=3)

        if request.user.is_authenticated:
            last_visit = VisitHistory.objects.filter(user=request.user).last()
            if not last_visit or last_visit.timestamp < three_hours_ago:
                VisitHistory.objects.create(user=request.user)
        else:
            ip_address = self.get_client_ip(request)
            last_visit = VisitHistory.objects.filter(ip_address=ip_address).last()
            if not last_visit or last_visit.timestamp < three_hours_ago:
                VisitHistory.objects.create(ip_address=ip_address)
        
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip