from django.shortcuts import render, render_to_response
from django.views import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import ProgrammingProblem
# Create your views here.


class QuestionHomeView(View):

    def get(self, request):
        all_problems = ProgrammingProblem.objects.all()

        # # 模拟是数据变多
        # for i in range(5):
        #     all_problems.append(all_problems)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_problems, per_page=1, request=request)
        # per_page 每页条数

        problems = p.page(page)

        return render_to_response('question_home.html', {
            'problems': problems,
        })


class AnswerView(View):

    def get(self, request, pk):
        problem = ProgrammingProblem.objects.get(id=pk)
        return render(request, 'answer.html', {'problem': problem})
