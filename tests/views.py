from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, UserResult, Question
from .forms import TestForm

# Create your views here.

def test_list(request):
    tests = Test.objects.all()
    return render(request, "test_list.html", {"tests": tests})


def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()

    if request.method == "POST":
        form = TestForm(request.POST, questions=questions)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            
            score = 0
            total = questions.count()
            for question in questions:
                selected_answer = form.cleaned_data.get(f"question_{question.id}")
                if selected_answer and selected_answer.is_correct:
                    score += 1
            
            percentage = (score / total) * 100
            
            UserResult.objects.create(
                user=name,
                test=test,
                score=percentage
            )
            
            return redirect("test_result", pk=pk, username=name)
    else:
        form = TestForm(questions=questions)

    return render(request, "test_detail.html", {"test": test, "form": form})


def test_result(request, pk, username):
    test = get_object_or_404(Test, pk=pk)
    
    result = UserResult.objects.get(test=test, user=username)

    if not result:
        return render(request, "test_result.html", {"test": test, "error": "Результаты не найдены."})
    
    result = round(result.score, 2)

    return render(request, "test_result.html", {"test": test, "result": result})

