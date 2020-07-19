from django.contrib import admin
from .models import Applicant, Verifier, User
# from .models import Applicant
# Register your models here.


admin.site.register(Applicant)
admin.site.register(Verifier)
admin.site.register(User)