from django.db import models



class Bilety(models.Model):
    question_number = models.IntegerField(blank=True, null=True)
    ticket_number = models.IntegerField(blank=True, null=True)
    ticket_category = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    question = models.CharField(blank=True, null=True, max_length=255)
    answer_text1 = models.CharField(blank=True, null=True, max_length=255)
    is_correct1 = models.BooleanField(blank=True, null=True)
    answer_text2 = models.CharField(blank=True, null=True, max_length=255)
    is_correct2 = models.BooleanField(blank=True, null=True)
    answer_text3 = models.CharField(blank=True, null=True, max_length=255)
    is_correct3 = models.BooleanField(blank=True, null=True)
    answer_text4 = models.CharField(blank=True, null=True, max_length=255)
    is_correct4 = models.BooleanField(blank=True, null=True)
    correct_answer = models.CharField(blank=True, null=True, max_length=255)
    answer_tip = models.TextField(blank=True, null=True)
    id_chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bilety'
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы билетов'

    def __str__(self):
        return "Билет "+ str(self.ticket_number)+". Вопрос "+str(self.question_number)




class Chapter(models.Model):
    topic = models.CharField(blank=True, null=True, max_length=255)
    id_chapter = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'chapter'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.topic
