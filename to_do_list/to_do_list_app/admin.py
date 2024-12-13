from django.contrib import admin
from .models import To_do_list

@admin.register(To_do_list)
class To_do_listAdmin(admin.ModelAdmin):

    """
    Админка модели To_do_list
    """
    list_display=['id', 'heading', 'summary', 'term', 'status', 'created_at', 'updated_at']

    @admin.display(description="Text summary")
    def summary(self, obj) -> str:
        """
        Метод конвертации столбца 'description' в короткую запись
        """
        if len(obj.description)> 30:
            return f"{obj.description[:20]}..."
        return obj.description
