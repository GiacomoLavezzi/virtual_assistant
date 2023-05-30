from django.contrib import admin
from virtual_app.models import Problem, Symptom, Solution, Prob_to_Sol, Prob_to_Sym, Sym_to_Prob

# Register your models here.
admin.site.register(Problem)
admin.site.register(Symptom)
admin.site.register(Solution)
admin.site.register(Prob_to_Sol)
admin.site.register(Prob_to_Sym)
admin.site.register(Sym_to_Prob)