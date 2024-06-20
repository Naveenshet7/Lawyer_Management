from datetime import date

from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def lawyer(request):
    lawyer_list = Lawyer.objects.filter(Status="Active")
    paginator = Paginator(lawyer_list, 3)  # Show 3 Lawyer per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request,'lawyer.html', locals())

def lawyerDtls(request,pid):
    lawyer = Lawyer.objects.get(id=pid)
    return render(request, 'lawyerDtls.html', locals())

def search(request):
    sd = None
    lawyer = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        practiceArea = [i.id for i in PracticeArea.objects.filter(Q(PAreaName__icontains=sd))]
        lawyer = Lawyer.objects.filter(Q(practiceArea__in=practiceArea) | Q(LawyerName__icontains=sd) | Q(LawyerEmail__icontains=sd) | Q(LawyerMobileNo__icontains=sd) | Q(State__icontains=sd) | Q(City__icontains=sd))

    return render(request,'search.html', locals())

def view_SearchReports(request,pid):
    lawyer = Lawyer.objects.get(id=pid)
    return render(request, 'view_SearchReports.html', locals())

def contact(request):
    return render(request,'contact.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    practice = PracticeArea.objects.all().count()
    lawyer = Lawyer.objects.all().count()
    activelaw = Lawyer.objects.filter(Status="Active").count()
    blocklaw = Lawyer.objects.filter(Status="Block").count()
    return render(request, 'dashboard.html', locals())

def add_PracticeArea(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        pareaname = request.POST['PAreaName']

        try:
            PracticeArea.objects.create(PAreaName=pareaname)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_PracticeArea.html', locals())


def manage_PracticeArea(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    parea = PracticeArea.objects.all()
    return render(request, 'manage_PracticeArea.html', locals())

def edit_PracticeArea(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    parea = PracticeArea.objects.get(id=pid)
    if request.method == "POST":
        pareaname = request.POST['PAreaName']

        parea.PAreaName = pareaname

        try:
            parea.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_PracticeArea.html', locals())


def delete_PracticeArea(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    parea = PracticeArea.objects.get(id=pid)
    parea.delete()
    return redirect('manage_PracticeArea')


def add_Lawyer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    parea = PracticeArea.objects.all()
    if request.method == "POST":
        pareaid  = request.POST['practiceArea']
        practiceAreaid = PracticeArea.objects.get(id=pareaid)

        lname = request.POST['LawyerName']
        lemail = request.POST['LawyerEmail']
        lmob = request.POST['LawyerMobileNo']
        oadd = request.POST['OfficeAddress']
        city = request.POST['City']
        state = request.POST['State']
        lang = request.POST['LanguageKnown']
        pic = request.FILES['ProfilePic']
        lexp = request.POST['LawyerExp']
        court = request.POST['Courts']
        website = request.POST['Website']
        description = request.POST['Description']
        Status ="Active"

        try:
            Lawyer.objects.create(practiceArea=practiceAreaid, LawyerName=lname, LawyerEmail=lemail,
                                  LawyerMobileNo=lmob, OfficeAddress=oadd, City=city, State=state, LanguageKnown=lang, ProfilePic=pic,
                                  LawyerExp=lexp, Courts=court, Website=website, Description=description, Status=Status, RegDate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Lawyer.html', locals())


def manage_Lawyer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    lawyer = Lawyer.objects.all()
    return render(request, 'manage_Lawyer.html', locals())

def edit_Lawyer(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    parea = PracticeArea.objects.all()
    lawyer = Lawyer.objects.get(id=pid)
    if request.method == "POST":
        pareaid = request.POST['practiceArea']
        practiceAreaid = PracticeArea.objects.get(id=pareaid)

        lname = request.POST['LawyerName']
        lemail = request.POST['LawyerEmail']
        lmob = request.POST['LawyerMobileNo']
        oadd = request.POST['OfficeAddress']
        city = request.POST['City']
        state = request.POST['State']
        lang = request.POST['LanguageKnown']
        lexp = request.POST['LawyerExp']
        court = request.POST['Courts']
        website = request.POST['Website']
        description = request.POST['Description']
        status = request.POST['Status']

        lawyer.practiceArea = practiceAreaid
        lawyer.LawyerName = lname
        lawyer.LawyerEmail = lemail
        lawyer.LawyerMobileNo = lmob
        lawyer.OfficeAddress = oadd
        lawyer.City = city
        lawyer.State = state
        lawyer.LanguageKnown = lang
        lawyer.LawyerExp = lexp
        lawyer.Courts = court
        lawyer.Website = website
        lawyer.Description = description
        lawyer.Status = status
        try:
            lawyer.save()
            error = "no"
        except:
            error = "yes"

        try:
            pic = request.FILES['ProfilePic']
            lawyer.ProfilePic = pic
            lawyer.save()
        except:
            pass
    return render(request, 'edit_Lawyer.html', locals())


def delete_Lawyer(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    lawyer = Lawyer.objects.get(id=pid)
    lawyer.delete()
    return redirect('manage_Lawyer')

def bwdateReports(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']
        lawyer = Lawyer.objects.filter(Q(RegDate__gte=fd) & Q(RegDate__lte=td))
        return render(request, 'btwdatesReports.html', locals())
    return render(request,'bwdateReports.html')

def view_Reports(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    lawyer = Lawyer.objects.get(id=pid)
    return render(request, 'view_Reports.html', locals())


def searchReport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    lawyer = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        practiceArea = [i.id for i in PracticeArea.objects.filter(Q(PAreaName__icontains=sd))]
        lawyer = Lawyer.objects.filter(Q(practiceArea__in=practiceArea) | Q(LawyerName__icontains=sd) | Q(LawyerEmail__icontains=sd) | Q(LawyerMobileNo__icontains=sd) | Q(State__icontains=sd) | Q(City__icontains=sd))

    return render(request,'searchReport.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')