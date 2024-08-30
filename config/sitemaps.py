from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from web.models import (
    PostModel, PricingModel, ProjectModel, JobModel, FaqModel,
    ContactusModel, FeedbackModel, UserModel, JobApplyModel, AdminReply
)

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return ['main:index', 'main:about', 'main:faqlist', 'main:contact', 'main:pricing', 'main:blog', 'main:job', 'main:projects']

    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return PostModel.objects.filter(is_private=False)

    def lastmod(self, obj):
        return obj.posted_on

    def location(self, obj):
        return reverse('main:blogdetail', args=[obj.slug])

class PricingSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return PricingModel.objects.all()

    def lastmod(self, obj):
        pass

    def location(self, obj):
        return reverse('main:pricingdetail', args=[obj.slug])

class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ProjectModel.objects.all()

    def lastmod(self, obj):
        return obj.posted_on

    def location(self, obj):
        return reverse('main:projectdetail', args=[obj.pk])

class JobSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return JobModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:jobdetail', args=[obj.pk])

class FaqSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.4

    def items(self):
        return FaqModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:faqlist')

class ContactSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return ContactusModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:contact')

class FeedbackSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return FeedbackModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:contact')

class UserSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return UserModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('main:profile')

class JobApplySitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return JobApplyModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:job')

class AdminReplySitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return AdminReply.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('main:adminReplyForm', args=[obj.pk])