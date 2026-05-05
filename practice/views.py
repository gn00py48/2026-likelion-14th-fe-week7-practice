from django.shortcuts import render, redirect
from .models import PracticeUser, Review


def home(request):
    return redirect("practice:auth")


def auth_page(request):
    return render(request, "practice/auth.html")


def review_page(request):
    reviews = Review.objects.all().order_by("-created_at")

    return render(request, "practice/review.html", {
        "reviews": reviews
    })


# 회원가입
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        PracticeUser.objects.create(
            username=username,
            password=password
        )

    return redirect("practice:auth")


# 로그인 (간단 비교용)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = PracticeUser.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            return redirect("practice:review")

    return redirect("practice:auth")


# 후기 작성
def create_review(request):
    if request.method == "POST":
        reviewer_name = request.POST.get("reviewer_name")
        star = request.POST.get("star")
        content = request.POST.get("content")
        photo = request.FILES.get("photo")

        Review.objects.create(
            reviewer_name=reviewer_name,
            star=star,
            content=content,
            photo=photo
        )

    return redirect("practice:review")