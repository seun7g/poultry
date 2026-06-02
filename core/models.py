from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Information"

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    whatsapp_link = models.URLField(blank=True, null=True)
    footer_text = models.TextField()

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Settings"

class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default='#')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
