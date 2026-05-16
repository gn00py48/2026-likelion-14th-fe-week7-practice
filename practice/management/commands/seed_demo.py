from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from practice.models import Review


class Command(BaseCommand):
    help = "Create demo admin account and sample review data"

    def handle(self, *args, **options):
        admin_username = "admin"
        admin_password = "admin"

        user, created = User.objects.get_or_create(username=admin_username)

        user.set_password(admin_password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("admin 계정을 생성했습니다."))
        else:
            self.stdout.write(self.style.WARNING("기존 admin 계정의 비밀번호를 admin으로 초기화했습니다."))

        if not Review.objects.exists():
            Review.objects.create(
                reviewer_name="아기사자",
                star=5,
                content="Form 태그 실습을 위한 예시 후기입니다! 이름, 별점, 후기 내용이 DB에 저장되고 화면에 출력되는 흐름을 확인해보세요.",
            )
            self.stdout.write(self.style.SUCCESS("예시 후기 1개를 생성했습니다."))
        else:
            self.stdout.write(self.style.WARNING("이미 후기가 존재하여 예시 후기는 추가하지 않았습니다."))

        self.stdout.write(self.style.SUCCESS("seed_demo 작업이 완료되었습니다."))
        self.stdout.write("관리자 계정: admin / admin")