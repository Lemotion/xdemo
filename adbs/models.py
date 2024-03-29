from django.db import models
# 自定义管理器对象
# class BookInfoManager(models.manager):
#     #1.系统自带的方法
#     def all(self):
#
#         return super.filter(id__lt=3)
#     #2.添加自己的方法
#     def add_book(self,title,date_time):
#         book = self.model()
#         book.btitle = title
#         book.bpub_date = date_time
#         book.save()
#
#         return book

# Create your models here.
# 创建模型对象
#定义图书模型类BookInfo
class BookInfo(models.Model):
    #2.绑定管理器对象
    # books = BookInfoManager
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    image = models.ImageField(upload_to="abs",null=True,verbose_name="上传头像")


    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    # 自定义方法 列
    def date_time(self):

        return self.bpub_date.strftime('%Y-%m-%d')
    date_time.short_description ='自定义日期'
    date_time.admin_order_field = 'bpub_date'


#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    #关联 书本的 阅读量
    def read(self):

        return self.hbook.bread
    read.short_description = "书的阅读量"
    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname