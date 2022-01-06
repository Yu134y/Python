from django.contrib import admin  # admin モジュールのインポート
from my_app.models import Product  # model モジュールからモデルクラスのインポート


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'release_date')  # 一覧で表示させるフィールド
    list_display_links = ('id', )  # 更新用リンクを指定するフィールド

# 管理サイトへの登録関数
admin.site.register(Product, ProductAdmin)
