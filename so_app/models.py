from django.db import models


class StackOverflowTagsInfo(models.Model):
    """
    Stores SO's tag details: tag name, total posts and unanswered posts
    """
    tag = models.CharField(max_length=20)
    post_count = models.IntegerField()
    unanswered_count = models.IntegerField()

    def __unicode__(self):
        return self.tag