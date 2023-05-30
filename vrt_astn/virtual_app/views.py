from django.shortcuts import render, redirect
from virtual_app.models import Problem, Symptom, Solution, Prob_to_Sol, Prob_to_Sym, Sym_to_Prob

# Create your views here.
def index(request):
    return render(request, "virtual_app/index.html", {
        "symptoms":Symptom.objects.all().order_by("name"),
    })

def symptom_analysis(request):
    #redirect malevolous
    if request.method != "POST":            
        return redirect("/")
    
    #get data from user
    symptoms_1 = []                        
    for symptom in Symptom.objects.all():
        if request.POST.get(symptom.name):
            symptoms_1.append(symptom.name)

    #organise data in objects from database
    symptoms = Symptom.objects.all().filter(name__in=symptoms_1)
    rel_problems = Sym_to_Prob.objects.all().filter(symptom__in=symptoms)
    
    #first evaluation of the problem frequency (already normalised)
    problems_frequencies = {}
    for rel_problem in rel_problems:
        if rel_problem.problem.name not in problems_frequencies:
            problems_frequencies[rel_problem.problem.name]=(rel_problem.frequency/len(symptoms))
        else:
            problems_frequencies[rel_problem.problem.name]+=(rel_problem.frequency/len(symptoms))

    #second evaluation of the problem frequency with Bernoullian (not normalised)
    for prob_to_sym in Prob_to_Sym.objects.all().filter(problem__name__in=problems_frequencies):
        if prob_to_sym.symptom.name in symptoms_1:
            problems_frequencies[prob_to_sym.problem.name]*=prob_to_sym.frequency
        else:
            problems_frequencies[prob_to_sym.problem.name]*=(1-prob_to_sym.frequency)

    #calculation of normalisation factor
    total_frequency_norm = 0
    for problem in problems_frequencies:
        total_frequency_norm += problems_frequencies[problem]
    
    #normalisation
    for problem in problems_frequencies:
        problems_frequencies[problem]/=total_frequency_norm

    #solution evaluation
    solutions = {}
    for problem in problems_frequencies:
        solutions[problem] = Prob_to_Sol.objects.all().filter(problem__name=problem)

    return render(request, "virtual_app/probs_and_sols.html", {
        "problems":dict(sorted(problems_frequencies.items(), key=lambda x:-x[1])),
        "solutions":solutions
    })

def problem(request, problem_name):
    sym_to_probs = Sym_to_Prob.objects.all().filter(problem__name=problem_name)
    prob_to_syms = Prob_to_Sym.objects.all().filter(problem__name=problem_name)
    return render(request, "virtual_app/problem.html", {
        "sym_to_probs":sym_to_probs,
        "prob_to_syms":prob_to_syms
    })

def symptom(request, symptom_name):
    sym_to_probs = Sym_to_Prob.objects.all().filter(symptom__name=symptom_name)
    prob_to_syms = Prob_to_Sym.objects.all().filter(symptom__name=symptom_name)
    return render(request, "virtual_app/symptom.html", {
        "sym_to_probs":sym_to_probs,
        "prob_to_syms":prob_to_syms
    })

