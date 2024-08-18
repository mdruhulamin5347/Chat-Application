# In context_processors.py
from .models import NotificationModel

def unread_notifications(request):
    if request.user.is_authenticated:
        return {'unread_notifications_count': NotificationModel.objects.filter(user=request.user, is_read=False).count()}
    return {}
