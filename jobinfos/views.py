from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator

from jobinfos.models import JobInfo
from jobinfos.models import ExpInfo

def index(request, page = 1):
  per_page = 50
  page = int(page)
  jobs_list = JobInfo.objects.order_by('-pub_date', '-id')[(page - 1)*per_page:page*per_page]
  p = Paginator(JobInfo.objects.all(), per_page)
  return render(request, 'jobinfos/index.html', { 'jobs_list': jobs_list, 'paginator': p.page(page) })

def joblist(request):
  jobs_list = JobInfo.objects.order_by('-pub_date', '-id')
  return render(request, 'jobinfos/all.html', { 'jobs_list': jobs_list })

def detail(request, job_id):
  try:
    job = JobInfo.objects.get(id=job_id)
  except JobInfo.DoesNotExist:
    raise Http404
  return render(request, 'jobinfos/detail.html', {'job': job})

def explist(request):
  exps_list = ExpInfo.objects.order_by('-pub_date', '-id')
  return render(request, 'jobinfos/explist.html', { 'exps_list': exps_list })

def expdetail(request, exp_id):
  try:
    exp = ExpInfo.objects.get(id=exp_id)
  except ExpInfo.DoesNotExist:
    raise Http404
  return render(request, 'jobinfos/expdetail.html', {'exp': exp})

def youdaonote(request):
  return render(request, 'jobinfos/youdaonote.html')