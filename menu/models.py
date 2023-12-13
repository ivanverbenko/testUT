from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.title

    def get_children(self, all_items):
        return [item for item in all_items if item.parent_id == self.id]