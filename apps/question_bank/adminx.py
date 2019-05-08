import xadmin
from xadmin import views

from .models import ProgrammingProblem


class ProgrammingProblemSettings(object):
    list_display = ('id', 'title', 'content', 'pass_rate', 'input_format', 'output_format',
                    'input_sample', 'output_sample', 'difficulty', 'heat', )
    search_fields = ('id', 'title', 'content', 'input_sample', 'output_sample', 'difficulty', 'heat', 'pass_rate')
    list_filter = ('id', 'title', 'content', 'pass_rate', 'input_format', 'output_format',
                   'input_sample', 'output_sample', 'difficulty', 'heat', )


xadmin.site.register(ProgrammingProblem, ProgrammingProblemSettings)

