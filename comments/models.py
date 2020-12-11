from djongo import models
from django.utils import timezone
from pytz import timezone as timeLoc


class CommentsModel(models.Model):
    _id = models.ObjectIdField()
    object_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def listData(self):
        return {
            'id': str(self._id),
            'object_id': self.object_id if self.object_id else "",
            'user_id': self.user_id if self.user_id else "",
            'comments': self.comments if self.comments else "",
            'created_at': self.created_at.astimezone(timeLoc("ASIA/JAKARTA")).strftime("%Y-%m-%d %H:%M:%S%z") if self.created_at else "",
            'updated_at': self.updated_at.astimezone(timeLoc("ASIA/JAKARTA")).strftime("%Y-%m-%d %H:%M:%S%z") if self.updated_at else "",
        }
