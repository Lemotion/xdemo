from datetime import date

#1.增加 save

from adbs.models import BookInfo, HeroInfo

book = BookInfo(
    btitle='西游记',
    bput_date=date(1988,1,1),
    bread=10,
    bcomment=10
)
book.save()
#2. create
HeroInfo.objects.create(
    hname='沙悟净',
    hgender=0,
    hbook=book
)

#2. 删除 .objects.get().delete
hero = HeroInfo.objects.get(id=13)
hero.delete()
# .objects.filter().delete()
HeroInfo.objects.filter(id=14).delete()

#3.修改 save
hero = HeroInfo.objects.get(hname='猪八戒')
hero.hname = '猪悟能'
hero.save()
 # .objects.filter().update()
HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')

#1. 查询 基本查询 get all count
BookInfo.objects.get(id=3)
BookInfo.objects.all()
BookInfo.objects.count()

# 2. 过滤查询 filter exclude
BookInfo.objects.filter(id=3)
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(id__=3)

# 大于 小于 gt lt e
BookInfo.objects.filter(id__lt=2)

# 包含 contains startswith endswith
BookInfo.objects.filter(btitle__contains='八')
BookInfo.objects.filter(btitle__startswith='笑')
BookInfo.objects.filter(btitle__endswith='狐')

# 判断是否为空 isnull
BookInfo.objects.filter(btitle__isnull=True)

# 范围 in
BookInfo.objects.filter(id__in=[2,4])
# 日期
BookInfo.objects.filter(bpub_date__year=1995)
BookInfo.objects.filter(bpub_date__gte=date(1995,1,1))

#1. 两个 字段 对比 过滤 breaad__get = bcomment F对象
# 例：查询阅读量大于等于评论量的图书
from django.db.models import F, Q, Sum,Avg,Count,Max,Min

BookInfo.objects.filter(bread__gte=F('bcomment'))
BookInfo.objects.filter(bcomment__gte=F('bread')*2)
#2. 两个条件 对比 过滤 Q对象 & | ~
# 查询2阅读量大于20，并且编号小于3的图书。&
BookInfo.objects.filter(bread__gt=20,id__lt=3)
BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
BookInfo.objects.filter(~Q(id=3))

#聚合查询 aggregate()
#Avg 平均，Count 数量，Max 最大，Min 最小，Sum 求和
BookInfo.objects.aggregate(Sum('id'))
BookInfo.objects.aggregate(Avg('id'))
BookInfo.objects.aggregate(Max('id'))
BookInfo.objects.aggregate(Min('id'))

# 排序 order_by 降序 -
BookInfo.objects.all().order_by('id')
BookInfo.objects.all().order_by('-id')

# 1.关联查询
# 1: n
# 根据  书 找书本 对应 所有英雄
book = BookInfo.objects.get(id=1)
book.heroinfo_set.all()
# n: 1
# 英雄 对应 的 书
hero = HeroInfo.objects.get(id=11)
hero.hbook

# 2.关联过滤查询  关联模型类名小写__属性名__条件运算符=值
# 由多模型类条件查询一模型类数据: n:1
# 查询图书，要求图书英雄为"东方不败 "
BookInfo.objects.filter(heroinfo__hname__exact="东方不败")

# 由一模型类条件查询多模型类数据:
# 查询书名为“天龙八部”的所有英雄。
HeroInfo.objects.filter(hbook__btitle__exact="天龙八部")

# querySet 类型
# 1.惰性加载 懒加载
qs = BookInfo.objects.filter(id__lt=3)
# 2.缓存
[q for q in qs]
[q for q in qs]

# objects -- 自定义 管理器 对象 Manager

