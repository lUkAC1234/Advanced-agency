from modeltranslation.translator import register, TranslationOptions
from .models import PricingModel, PostCategoryModel, PostTagModel, PostModel, \
    FaqModel, JobCategoryModel, \
    JobKnowledgesModel, JobModel, ProjectCategory, ProjectModel

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

