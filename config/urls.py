from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from web import views
from .sitemaps import StaticViewSitemap, PostSitemap, PricingSitemap, ProjectSitemap, JobSitemap, FaqSitemap, ContactSitemap, FeedbackSitemap, UserSitemap, JobApplySitemap, AdminReplySitemap

sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'pricing': PricingSitemap,
    'projects': ProjectSitemap,
    'jobs': JobSitemap,
    'faqs': FaqSitemap,
    'contacts': ContactSitemap,
    'feedback': FeedbackSitemap,
    'users': UserSitemap,
    'job_applies': JobApplySitemap,
    'admin_replies': AdminReplySitemap,
}

handler404 = views.PageNotFound
handler403 = views.ForbiddenPage

urlpatterns = [
    path('cybercode/admin/panel', admin.site.urls),
    path('', include('web.urls')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="bunin/robots.txt", content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(
    # Add your i18n patterns here
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
