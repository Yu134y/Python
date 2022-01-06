from django.contrib import admin  # admin モジュールのインポート
from text_app.models import Customer  # model モジュールからモデルクラスのインポート


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')  # 一覧で表示させるフィールド
    list_display_links = ('id', )  # 更新用リンクを指定するフィールド

# 管理サイトへの登録関数
admin.site.register(Customer, CustomerAdmin)
