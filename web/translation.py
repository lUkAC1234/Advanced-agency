from modeltranslation.translator import register, TranslationOptions
from .models import PricingModel, PostCategoryModel, PostTagModel, PostModel, \
    FaqModel, JobCategoryModel, FeedbackModel, \
    JobKnowledgesModel, JobModel, ProjectCategory, ProjectModel

@register(PricingModel)
class PricingModelTranslationOptions(TranslationOptions):
    fields = ('type', 'advantages') 

@register(PostCategoryModel)
class PostCategoryModelTranslationOptions(TranslationOptions):
    fields = ('category',) 

@register(PostTagModel)
class PostTagModelTranslationOptions(TranslationOptions):
    fields = ('tag',) 

@register(PostModel)
class PostModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'post_text') 

@register(FaqModel)
class FaqModelTranslationOptions(TranslationOptions):
    fields = ('question', 'answer') 
    
@register(FeedbackModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('text',) 

@register(JobCategoryModel)
class JobCategoryModelTranslationOptions(TranslationOptions):
    fields = ('category',) 

@register(JobKnowledgesModel)
class JobKnowledgesModelTranslationOptions(TranslationOptions):
    fields = ('knowledge',) 

@register(JobModel)
class JobModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'aboutthejob', 'responsibilities', 'requirements', 'location') 

@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('category',) 

@register(ProjectModel)
class ProjectModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description') 

