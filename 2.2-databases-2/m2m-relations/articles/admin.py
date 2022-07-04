from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleScope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_category = 0
        categories = []
        for form in self.forms:
            if form.cleaned_data.get('tag'):
                if form.cleaned_data.get('tag').name in categories:
                    raise ValidationError('Categories are duplicated')
                else:
                    categories.append(form.cleaned_data.get('tag').name)
            if form.cleaned_data.get('is_main'):
                main_category += 1

        if main_category > 1:
            raise ValidationError('Select only 1 the main category')
        elif main_category == 0:
            raise ValidationError('Select the main category')

        return super().clean()

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

