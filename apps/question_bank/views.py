import time
from django.shortcuts import render, render_to_response
from django.views import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from question_bank.models import ProgrammingProblem
from apps.online_judge.models import SubmitRecord, User
from apps.utils.judger_to import code_to_judger, get_results
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
            'request': request
        })


class AnswerView(View):

    def get(self, request, pk):
        problem = ProgrammingProblem.objects.get(id=pk)
        return render(request, 'question_mirror_answer.html', {'problem': problem, 'pk': pk})

    def post(self, request, pk):
        lang = request.POST.get('lang', '')
        user_codes = request.POST.get('code', '')
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        problem = ProgrammingProblem.objects.get(id=pk)

        resp = code_to_judger(problem_id=pk, language=lang, code=user_codes)
        submission_id = resp.json().get('data').get('submission_id')
        time.sleep(2)
        result = get_results(submission_id)

        sub_record = SubmitRecord()
        sub_record.status = result.get('result')
        sub_record.language = lang
        sub_record.problem_id = problem
        sub_record.user_id = user
        sub_record.record = user_codes
        sub_record.memory_cost = result.get('statistic_info').get('memory_cost')
        sub_record.time_cost = result.get('statistic_info').get('time_cost')
        sub_record.save()
        return render(request, 'question_mirror_answer.html')


class SubmitRecordView(View):
    def get(self, request):
        all_records = SubmitRecord.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_records, per_page=5, request=request)
        # per_page 每页条数

        records = p.page(page)

        return render_to_response('submit.html', {
            'records': records,
            'request': request
        })


class TestView(View):
    def get(self, request):
        return render(request, 'question_mirror_answer.html')
