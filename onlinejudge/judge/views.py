from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views import generic
import os, filecmp
# from judge.functions.functions import handle_uploaded_file

from .forms import ProblemForm
from .models import Problem
import subprocess
import os


def handle_uploaded_file(f):
    with open('solutions/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def intro(request):
    return render(request, 'base.html')


def view_problems(request):
    problems_list = Problem.objects.order_by('-problem_name')[:5]
    context = {'problems_list': problems_list}
    return render(request, 'prob.html', context)


def problem_detail(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'detail.html', {'problem': prob})


def add_problem(request):
    context = {}
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST, request.FILES)
        if problem_form.is_valid():
            # save a new problem
            handle_uploaded_file(request.FILES["file"])
 #           subprocess.call(["g++", "/Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/123.cpp", "-o", "temp.exe"], shell=True)
#            out_container = open('mohit.txt', 'w')
           # testout = 'media/' + test.test_output.url
            subprocess.call(["g++", "temp.cpp", "-o", "temp.exe"], shell=True)
            k = subprocess.call(['temp.exe'], stdin=test.test_input, stdout=out_container, shell=True)
            out_container.close()


        # test = Test.objects.get(problem__problem_name=problem.problem_name)

         #   os.system('g++ /Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/123.cpp'),
          #  os.system(  'a.exe < /Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/input.txt >/Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/output.txt')
            #data, temp = os.pipe()

            # write to STDIN as a byte object(convert string
            # to bytes with encoding utf8)
          #  os.write(temp, bytes("5 10\n", "utf-8"));
           # os.close(temp)

            # store output of the program as a byte string in s
            #s = subprocess.check_output("g++ /Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/123.cpp -o out2;./out2", input=data, shell=True)

            # decode s to a normal string
            #print(s.decode("utf-8"))
            problem = problem_form.save()
            problem.save()
            # subprocess.call(["g++", "C:/Users/rasto/Downloads/OJ_MVP/OJ_MVP/onlinejudge/solutions/123.cpp"])
            # subprocess.call("a.exe")
            # print('got EXE')
            # link the to the problem and save the test case to db
            return HttpResponseRedirect("/judge/problem")
    else:
        # instantiate a new ProblemForm and then render the addproblem page
        problem_form = ProblemForm()
        context['problem_form'] = problem_form
        return render(request, "addprob.html", context)
    # if user is not logged in, throw him to a sign-in page
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect("http://127.0.0.1:8000/login")
    # else:
#C:\Users\rasto\Downloads\OJ_MVP\OJ_MVP\onlinejudge\123.cpp
# def submit(request, problem_id):
#     if request.method == 'POST':
#         sub_form = SubmissionForm(request.POST, request.FILES)
#         if sub_form.is_valid():
#             # handle_uploaded_file(request.POST, request.FILES)
#             sub = sub_form.save()
#             sub.problem = Problem.objects.get(code=problem_id)
#             print(sub.problem.code)
#             # sub.submitter = Coder.objects.get(user=request.user)
#             # print(sub.submitter)
#             sub.save()
#             # evaluate_submission.delay(sub.id)
#             return HttpResponse("Code Submitted!")
#     else:
#         sub_form = SubmissionForm()
#         payload = {"sub_form": sub_form, "pid": problem_id}
#         return render(request, "detail.html", payload)
#


# Create your views here.
