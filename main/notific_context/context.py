from main.models import Notification


def latest_notific(request):
    latest_notific = Notification.objects.filter(recipient=request.user, is_read=False)
    return {"latest_notific": latest_notific}
