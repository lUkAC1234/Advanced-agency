from modeltranslation.translator import register, TranslationOptions
from .models import UserModel,PricingModel, PostCategoryModel, PostTagModel, PostModel, \
    PostView, FeedbackModel, ContactusModel, FaqModel, JobCategoryModel, \
    JobKnowledgesModel, JobModel, JobApplyModel, ProjectCategory, ProjectModel, \
    PartnersModel, CheckOut

@register(UserModel)
class UserModelTranslationOptions(TranslationOptions):
    fields = ('company', 'location', 'position')  # Add fields you want to translate

@register(PricingModel)
class PricingModelTranslationOptions(TranslationOptions):
    fields = ('type', 'advantages')  # Add fields you want to translate

@register(PostCategoryModel)
class PostCategoryModelTranslationOptions(TranslationOptions):
    fields = ('category',)  # Add fields you want to translate

@register(PostTagModel)
class PostTagModelTranslationOptions(TranslationOptions):
    fields = ('tag',)  # Add fields you want to translate

@register(PostModel)
class PostModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'post_text')  # Add fields you want to translate

@register(FeedbackModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('text',)  # Add fields you want to translate

@register(ContactusModel)
class ContactusModelTranslationOptions(TranslationOptions):
    fields = ('fullname', 'company', 'text')  # Add fields you want to translate

@register(FaqModel)
class FaqModelTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')  # Add fields you want to translate

@register(JobCategoryModel)
class JobCategoryModelTranslationOptions(TranslationOptions):
    fields = ('category',)  # Add fields you want to translate

@register(JobKnowledgesModel)
class JobKnowledgesModelTranslationOptions(TranslationOptions):
    fields = ('knowledge',)  # Add fields you want to translate

@register(JobModel)
class JobModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'aboutthejob', 'responsibilities', 'requirements', 'location')  # Add fields you want to translate

@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('category',)  # Add fields you want to translate

@register(ProjectModel)
class ProjectModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # Add fields you want to translate

@register(PartnersModel)
class PartnersModelTranslationOptions(TranslationOptions):
    fields = ('title',)  # Add fields you want to translate

@register(CheckOut)
class CheckOutTranslationOptions(TranslationOptions):
    fields = ('first_name', 'address', 'city', 'position')  # Add fields you want to translate
