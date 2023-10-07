from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from .models import TypingTest, User,Contest,Questions,Submissions
from .forms import testPageForm
from django.http import JsonResponse, request
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "quizapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.save()
        except IntegrityError:
            return render(request, "quizapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "quizapp/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "quizapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "quizapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def index(request):
    if request.user.is_authenticated:
        cont = Contest.objects.all()
        return render(request , "quizapp/index.html", {
            "contests":cont
        })
    else:
        return HttpResponseRedirect(reverse("login"))

@login_required
def test(request,contestid):
    if(request.method == "POST"):
        ct=Contest.objects.get(id=contestid)
        if ct.contestType == "typing":
            accuracy = float(request.POST.get("accuracy", 0))
            time_taken = int(request.POST.get("time_taken", 0))
            backspace_count = int(request.POST.get("backspace_count", 0))
            import pdb;pdb.set_trace()
            typed_text = request.POST.get("user_typing", "")
            words_per_minute = int(len(typed_text.split()) / (time_taken / 60))
            maxScore = int(request.POST.get("max_score", 0))
            sub = Submissions(
                user=request.user,
                contestid=ct,
                score=accuracy*maxScore,
                userSubmision=typed_text,
                timeTaken=time_taken,
                wordsPerMin=words_per_minute,
                backspaceCount=backspace_count
            )
            sub.save()
            ct.subs.add(request.user)
            return HttpResponseRedirect(reverse("scores", args=[contestid]))
        else:
            score = 0
            qset = Questions.objects.filter(contestid=contestid)
            for i in qset:
                try:
                    res = request.POST[f"q{i.id}"]
                except:
                    res=0
                if(res == i.correctoption):
                    score = score + i.points
            print(f"score = {score}")
            sub = Submissions(user=request.user,contestid=ct,score=score)
            sub.save()
            ct.subs.add(request.user)
            return HttpResponseRedirect(reverse("scores",args=[contestid]))
    else:
        cnt = Contest.objects.filter(id=contestid).get()
        if cnt.contestType == "typing":
            para = TypingTest.objects.get(contestid=cnt)
            return render(request , "quizapp/typingtest.html", {
                "cnt":cnt,
                "original_paragraph": para.paragraph
            })
        else:
            obj = Questions.objects.filter(contestid=contestid)
            return render(request , "quizapp/test.html", {
                "obj":obj,
                "cnt":cnt
            })

@login_required
def Scores(request,contestid):
    subs = Submissions.objects.filter(user=request.user,contestid=contestid).order_by("-subTime")
    return render(request , "quizapp/profile.html", {
        "subs":subs
    })

@login_required
def Profile(request):
    subs = Submissions.objects.filter(user=request.user)
    return render(request , "quizapp/profile.html", {
        "subs":subs
    })

@csrf_exempt
@login_required
def enroll(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)
        contestid = data.get("id")
        contest = Contest.objects.get(id=contestid)
        contest.enrolments.add(request.user)
        return JsonResponse({"message":"enrolled!!"}, status=201)

    else:
        return JsonResponse({"error":"PUT method required"}, status=400)


def leaderboard(request,contestid):
    if(contestid == 0):
        obj = Submissions.objects.order_by("-score")
        return render(request,"quizapp/leaderboard.html", {
            "obj":obj,
        })
    else:
        obj = Submissions.objects.filter(contestid__id=contestid).order_by("-score")
        contestname = Contest.objects.values('contestName').get(id=contestid)['contestName']
        return render(request,"quizapp/leaderboard.html", {
            "obj":obj,
            "flag":contestname,
        })
