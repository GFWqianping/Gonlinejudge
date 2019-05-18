from datetime import datetime

from django.db import models

from apps.online_judge.models import Problem
# Create your models here.


class ProgrammingProblem(Problem):
    difficulty = models.CharField(max_length=16, default='c', verbose_name='难度',
                                  choices=(('s', '艰巨'), ('a', '困难'), ('b', '中等'), ('c', '简单')))
    heat = models.IntegerField(verbose_name='热度', default=0)
    pass_rate = models.FloatField(verbose_name='通过率', default=0)
    input_format = models.TextField(max_length=256, default='', verbose_name='输入格式')
    output_format = models.TextField(max_length=256, default='', verbose_name='输出格式')
    # status = models.CharField(max_length=16, default='not_answer', verbose_name='状态',
    #                           choices=(('not_pass', '未通过'), ('pass', '已通过'), ('not_answer', '未作答')))

    class Meta:
        verbose_name = '编程题目'
        verbose_name_plural = verbose_name

    def info_update(self, status):
        self.heat = self.heat + 1
        if status == 0:
            self.pass_rate = ((self.heat*self.pass_rate) + 1) / self.heat
        else:
            self.pass_rate = (self.heat * self.pass_rate) / self.heat
        self.save()

    def __str__(self):
        return self.title
