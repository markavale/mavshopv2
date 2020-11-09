from django.db import models


class PageVisit(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return "Total Page Visit: {0}".format(self.count)

