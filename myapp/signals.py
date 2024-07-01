from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Contact,Hakkimizda,BaslikGorsel

@receiver(post_migrate)
def create_initial_contact(sender, **kwargs):
    if sender.name == 'myapp':
        if not Contact.objects.exists():
            Contact.objects.create()


@receiver(post_migrate)
def create_initial_hakkimizda(sender, **kwargs):
    if sender.name == 'myapp':
        if not Hakkimizda.objects.exists():
            Hakkimizda.objects.create()



@receiver(post_migrate)
def create_initial_baslikgorsel(sender, **kwargs):
    if sender.name == 'myapp':  # 'myapp' yerine kendi uygulama adınızı koyun
        if not BaslikGorsel.objects.exists():
            initial_data = [
                {"name": "Referanslar", "slug": "referanslar"},
                {"name": "Hakkımızda", "slug": "hakkimizda"},
                {"name": "İletişim", "slug": "iletisim"},
            ]

            for data in initial_data:
                BaslikGorsel.objects.create(name=data['name'], slug=data['slug'])
