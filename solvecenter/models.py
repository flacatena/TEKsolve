from django.db import models

class Hardware(models.Model):
    
    hardware_device = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering=['hardware_device']
        verbose_name_plural = "Hardware"

    def __str__(self):
        return self.hardware_device

class Software(models.Model):

    software_product = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering=['software_product']
        verbose_name_plural = "Software"

    def __str__(self):
        return self.software_product
    
class Issue(models.Model):
    hardware = models.ForeignKey(Hardware, null=True, blank=True, on_delete=models.CASCADE)
    software = models.ForeignKey(Software, null=True, blank=True, on_delete=models.CASCADE)
    reported_issue = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reported_issue
    
class Resolution(models.Model):
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE, related_name='resolutions')
    reported_resolution = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reported_resolution


    
