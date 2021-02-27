from django.db import models


class Profession(models.Model):
    name = models.TextField(verbose_name="Профессия", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class Test(models.Model):
    VAR = (('A', 'A'),
           ('B', 'B'),
           ('C', 'C'))
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, default=1)
    question = models.CharField(verbose_name="Вопрос", max_length=2000)
    varA = models.CharField(verbose_name='Вариант А', max_length=1000, default='')
    varB = models.CharField(verbose_name='Вариант B', max_length=1000, default='')
    varC = models.CharField(verbose_name='Вариант C', max_length=1000, default='')
    correct_answer = models.CharField(verbose_name='Правильный ответ', max_length=1, choices=VAR)

    def __str__(self):
        return f"{self.profession.name}[{self.id}]"

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Answer(models.Model):
    name = models.CharField(verbose_name="Фамилия сотрудника", max_length=100)
    profession = models.ForeignKey(Profession, verbose_name='Должность', on_delete=models.CASCADE, default=1)
    test = models.TextField(verbose_name='Тесты', default='')
    answer = models.TextField(verbose_name='Ответы на тесты', default='')
    result = models.CharField(verbose_name='Результат тестирование', max_length=10, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пройденный тест"
        verbose_name_plural = "Пройденные тесты"


class SendEmail(models.Model):
    mail = models.EmailField()
    message = models.CharField(max_length=100, default="")
