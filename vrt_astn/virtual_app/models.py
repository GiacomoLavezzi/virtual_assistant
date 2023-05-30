from django.db import models

# Create your models here.
    
class Problem(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Symptom(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Solution(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Prob_to_Sol(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.DO_NOTHING, related_name="solutions")
    solution = models.ForeignKey(Solution, on_delete=models.DO_NOTHING, related_name="problems")
    frequency = models.FloatField()

    def __str__(self):
        return f"{self.problem} è risolto da {self.solution} il {self.frequency*100}% delle volte"

class Sym_to_Prob(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.DO_NOTHING, related_name="related_problems")
    problem = models.ForeignKey(Problem, on_delete=models.DO_NOTHING, related_name="related_symptoms") #
    frequency = models.FloatField()

    def __str__(self):
        return f"{self.symptom} è indice di {self.problem} il {self.frequency*100}% delle volte"

class Prob_to_Sym(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.DO_NOTHING, related_name="shown_symptoms")
    symptom = models.ForeignKey(Symptom, on_delete=models.DO_NOTHING, related_name="related_conditions") #
    frequency = models.FloatField()

    def __str__(self):
        return f"{self.problem} manifesta {self.symptom} il {self.frequency*100}% delle volte"