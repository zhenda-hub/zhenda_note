from django.db import models
from utils.base_model import BaseModel


class Note(BaseModel):
    title = models.CharField(max_length=20, verbose_name='题目')
    content = models.TextField(verbose_name='内容')
    note_group = models.ForeignKey('NoteGroup', on_delete=models.SET_NULL, verbose_name='属组', null=True, blank=True)
    # 默认反向关联为 小写类名_set 可以自定义
    # note_group = models.ForeignKey('NoteGroup', on_delete=models.SET_NULL, verbose_name='属组', null=True, blank=True, related_name='notes')
    is_fast = models.BooleanField(verbose_name='快速访问', default=False)
    # owner = models.

    def __str__(self):
        return f'{self.note_group}-{self.title}'


class NoteGroup(BaseModel):
    name = models.CharField(max_length=20, verbose_name='组名')

    def __str__(self):
        return f'{self.name}'
    # owner = models.

# models.Manager
# models.Model

