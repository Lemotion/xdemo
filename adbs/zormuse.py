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

