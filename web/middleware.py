import logging
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import VisitHistory

logger = logging.getLogger(__name__)

class TrackUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)

        if request.user.is_authenticated:
            user = request.user
            if user.is_superuser:
                is_admin = True
            else:
                is_admin = False
        else:
            user = None
            is_admin = False

        now = timezone.now().replace(microsecond=0)

        # Check if there's a recent visit history for this user/IP
        last_visit = None
        if not is_admin:
            last_visit = VisitHistory.objects.filter(user=user, ip_address=ip_address).last()

        # Check if the user is considered online
        is_online = False
        if last_visit:
            is_online = last_visit.is_online

        # Update or create visit history
        if not is_admin:
            if last_visit:
                # If the user is no longer authenticated, end the visit
                if not user:
                    last_visit.end_time = now
                    last_visit.save()
                    logger.info(f"End time updated for user {user}")
                # If the user is authenticated, update the end time if it's been more than 3 hours
                elif last_visit.start_time < now - timedelta(minutes=30):
                    last_visit.end_time = now
                    last_visit.save()
                    logger.info(f"End time updated for user {user}")
            # If there's no visit history or the user started a new session, create a new visit history
            else:
                logger.info(f"No previous visit history found for user {user}")
                username = user.username if user else "Anonymous user"
                visit = VisitHistory.objects.create(user=user, ip_address=ip_address, start_time=now)
                logger.info(f"New visit history created for user {username}")

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    