from actstream.models import Action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from tunga_activity.filters import ActionFilter
from tunga_activity.models import NotificationReadLog
from tunga_activity.serializers import ActivitySerializer, NotificationReadLogSerializer


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Activity Resource
    """
    queryset = Action.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]
    filter_class = ActionFilter
    search_fields = (
        'comments__body', 'messages__body', 'uploads__file', 'messages__attachments__file', 'comments__uploads__file'
    )


class NotificationReadLogViewSet(viewsets.ModelViewSet):
    """
    Notification Resource
    """
    queryset = NotificationReadLog.objects.all()
    serializer_class = NotificationReadLogSerializer
    permission_classes = [IsAuthenticated]
