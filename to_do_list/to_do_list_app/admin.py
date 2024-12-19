from django.contrib import admin
from .models import To_do_list, Tags, To_do_listTags



class ArticleThemaInline(admin.TabularInline):
    """
    InLine сущьность связи моделей 
    """
    model = To_do_listTags
    extra = 0


@admin.register(To_do_list)
class To_do_listAdmin(admin.ModelAdmin):

    """
    Админка модели To_do_list
    """
    list_display=['id', 'heading', 'summary', 'term', 'status', 'created_at', 'updated_at']
    inlines = [ArticleThemaInline]


    @admin.display(description="Text summary")
    def summary(self, obj) -> str:
        """
        Метод конвертации столбца 'description' в короткую запись
        """
        if len(obj.description)> 30:
            return f"{obj.description[:20]}..."
        return obj.description
    
    
@admin.register(Tags)
class ThemaAdmin(admin.ModelAdmin):
    """
    Админка для модели Tags
    """
    list_display = ['id', 'title']
    inlines = [ArticleThemaInline]


@admin.register(To_do_listTags)
class ArticleThemaAdmin(admin.ModelAdmin):
    """    
    Админка для модели To_do_listTags
    """
    list_display = ['id', 'to_do', 'tags']
