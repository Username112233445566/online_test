from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название теста")
    description = models.TextField(verbose_name="Описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст вопроса")

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return self.text


class UserResult(models.Model):
    user = models.CharField(max_length=200, verbose_name="Пользователь")
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField(verbose_name="Результат", default=0.0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.test.title} - {self.score}"

