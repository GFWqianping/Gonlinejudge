import xadmin
from xadmin import views

from .models import ProgrammingProblem


class ProgrammingProblemSettings(object):
    list_display = ('id', 'title', 'content', 'input_sample', 'output_sample', 'difficulty', 'heat', 'pass_rate')
    search_fields = ('id', 'title', 'content', 'input_sample', 'output_sample', 'difficulty', 'heat', 'pass_rate')
    list_filter = ('id', 'title', 'content', 'input_sample', 'output_sample', 'difficulty', 'heat', 'pass_rate')


xadmin.site.register(ProgrammingProblem, ProgrammingProblemSettings)

