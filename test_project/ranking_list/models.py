from django.db import models

# Create your models here.


class TBRanking_list(models.Model):
    """排行榜"""
    grade = models.IntegerField(db_index=True)  # 分数

    client_num = models.CharField(unique=True, max_length=32)  #  客户端号

    class Meta: 
        db_table = 'tb_ranking_list'
