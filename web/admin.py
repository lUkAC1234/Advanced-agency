from django.contrib import admin
from .models import (
    UserModel, 
    PricingModel, 
    PostModel, 
    FeedbackModel, 
    ContactusModel, 
    FaqModel, 
    JobModel, 
    JobCategoryModel, 
    ProjectModel, 
    ProjectCategory, 
    PostTagModel, 
    PostCategoryModel, 
    PartnersModel, 
    JobApplyModel, 
    CheckOut, 
    JobKnowledgesModel, 
    VisitHistory, 
    AdminReply
)
from django.utils.translation import gettext_lazy as _
# For saving html code
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(VisitHistory)
class VisitHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'get_visit_duration', 'is_online_status', 'timestamp')
    list_filter = ('user', 'timestamp', 'ip_address')
    search_fields = ('user__username', 'ip_address')
    readonly_fields = ('user', 'ip_address', 'timestamp', 'start_time', 'end_time', 'is_online_status')

    def get_visit_duration(self, obj):
        return obj.visit_duration

    def is_online_status(self, obj):
        if obj.is_online:
            return format_html('<span class="user_online_status" style="color: white; background: green; padding: 0.25rem 1rem;">Online</span>')
        else:
            return format_html('<span class="user_offline_status" style="color: white; background: red; padding: 0.25rem 1rem;">Offline</span>')
    is_online_status.short_description = 'Online Status'

@admin.register(PricingModel)
class PricingAdmin(TranslationAdmin):
    list_display = ['id', 'type', 'price']
    list_display_links = ['id', 'type', 'price']
    search_fields = ['type', 'price']
    prepopulated_fields = {'slug': ('type', )}

@admin.register(PostModel)
class PostAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'user']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    readonly_fields = ('user', 'posted_on')
    prepopulated_fields = {'slug': ('title', )}

    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.user = request.user
        super().save_model(request, obj, form, change)
        
@admin.register(PostTagModel)
class PostTagAdmin(TranslationAdmin):
    list_display = ['id', 'tag']
    list_display_links = ['id', 'tag']
    search_fields = ['tag']

@admin.register(PostCategoryModel)
class PostCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']
    
@admin.register(FeedbackModel)
class FeedbackAdmin(TranslationAdmin):
    list_display = ['id', 'text']
    list_display_links = ['id', 'text']
    search_fields = ['text']

@admin.register(ContactusModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'company']
    list_display_links = ['id', 'company']
    search_fields = ['company']
    readonly_fields = ['created_at']
    
@admin.register(AdminReply)
class AdminReply(admin.ModelAdmin):
    list_display = ['id', 'subject']
    list_display_links = ['id', 'subject']
    search_fields = ['subject']
    readonly_fields = ['created_at']

@admin.register(FaqModel)
class FAQAdmin(TranslationAdmin):
    list_display = ['id', 'question']
    list_display_links = ['id', 'question']
    search_fields = ['question']

@admin.register(JobModel)
class JobAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(JobCategoryModel)
class JobCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']

@admin.register(JobKnowledgesModel)
class JobKnowledgesAdmin(TranslationAdmin):
    list_display = ['id', 'knowledge']
    list_display_links = ['id', 'knowledge']
    search_fields = ['knowledge']

@admin.register(JobApplyModel)
class JobApplyyAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName']
    list_display_links = ['id', 'firstName']
    search_fields = ['firstName']
    readonly_fields = ['created_at']

@admin.register(ProjectCategory)
class ProjectsCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']

@admin.register(ProjectModel)
class ProjectsAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    readonly_fields = ['posted_on']

@admin.register(PartnersModel)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'total_price']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name']
    readonly_fields = ['created_at', 'item', 'total_price', 'success_checkout']


admin.site.site_header = 'Cyber Code'
admin.site.site_title = 'Cyber Code'