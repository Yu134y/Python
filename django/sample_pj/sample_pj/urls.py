from django.urls import path, include  # URL指定およびアプリケーション別URL定義指定用関数のインポート
from django.contrib import admin  # 管理サイト設定用インポート

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理サイトのURL設定
    path('text/',  # アプリケーション別URL
         include('text_app.urls')),  # アプリケーション別URL定義モジュールの指定
    path('myapp/', include('my_app.urls')),
]
