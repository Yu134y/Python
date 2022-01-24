from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # accountのurls.pyを読み込み
    # path('', include('account.urls')),
    # todoのurls.pyを読み込み
    path('', include('todo.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)