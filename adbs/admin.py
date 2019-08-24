from django.contrib import admin
from adbs.models import HeroInfo, BookInfo

# Register your models here.

# 子类TabularInline：以表格的形式嵌入。
class HeroInfoTabular(admin.TabularInline):
    #关联模型的名字
    model = HeroInfo

    #编辑的个数
    extra = 1

# 子类StackedInline：以块的形式嵌入。
class HeroInfoStacked(admin.StackedInline):
    #关联模型的名字
    model = HeroInfo

    #编辑的个数
    extra = 1
#自定义 Admin管理器对象 Manager
class BookInfoAdmin(admin.ModelAdmin):
    # 列操作
    # 1.显示哪些字段
    list_display = ['id','btitle','bpub_date','date_time']
    # 2.每页显示的个数
    list_per_page = 2
    # 3.操作选项的位置
    actions_on_top = True
    actions_on_bottom = True
    # 4. 右侧过滤器
    # list_filter = ['hgender']
    # 5. 搜索框
    search_fields = ['btitle']
    # 6. 自定义列的名字 方法列
    # 7. 关联对象
    # 编辑页面操作---详情页
    #1. 显示字段
    # fields = ['btitle','bpub_date']
    #2. 分组显示
    fieldsets = (
        ('必传', {'fields': ('btitle', 'bpub_date','image')}),
        ('选填', {'fields': ('bread', 'bcomment'),
                'classes':('collapse',),
                }),
    )
    #3. 关联对象 块 和表  填写书本信息 填写对应的英雄
    # inlines = [HeroInfoTabular]
    inlines = [HeroInfoStacked]



#多继承
admin.site.register(BookInfo,BookInfoAdmin)

#装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hbook','read']
    # 4. 右侧过滤器
    list_filter = ['hgender']


#站点 首页 设置
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用'