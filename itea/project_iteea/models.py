from django.db import models
 
class Vacansy(models.Model):
    title_ru = models.CharField(max_length=255, verbose_name='Название вакансии')
    title_en = models.CharField(max_length=255, verbose_name='Название вакансии')
    title_tm = models.CharField(max_length=255, verbose_name='Название вакансии')
    image = models.ImageField(upload_to='static/images', null=False, blank=False)
    description_en = models.CharField(max_length=200, null=False, blank=False)
    description_ru = models.CharField(max_length=200, null=False, blank=False)
    description_tm = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        ) 
    phone_number = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        )
    email = models.EmailField(
        null=False,
        blank=False,
        )
class Course(models.Model):
    name_en = models.CharField(max_length=200, null=False, blank=False)
    name_ru = models.CharField(max_length=200, null=False, blank=False)
    name_tm = models.CharField(max_length=200, null=False, blank=False)
    description_en = models.CharField(max_length=200, null=False, blank=False)
    description_ru = models.CharField(max_length=200, null=False, blank=False)
    description_tm = models.CharField(max_length=200, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    duration = models.PositiveBigIntegerField(blank=False, null=False)
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f"name or course:{self.name_en}"
    
class Course_Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='static/images', null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    course = models.ManyToManyField(Course,related_name='course')
    def __str__(self):
        return self.name

    
class Team(models.Model):
    name_en = models.CharField(max_length=200, null=False, blank=False)
    name_ru = models.CharField(max_length=200, null=False, blank=False)
    name_tm = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='static/images', null=False, blank=False)
    role = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return f"{self.role}"
    colour = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

class News_email(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )

class News(models.Model):
    title_tm = models.CharField(max_length=255, blank=False, null=False)
    title_ru = models.CharField(max_length=255, blank=False, null=False)
    title_en = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='static/images/', blank=False, null=False)
    content_tm = models.TextField(blank=False, null= False)
    content_ru = models.TextField(blank=False, null=False)
    content_en = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    places = models.PositiveBigIntegerField(
        null=False,
        blank=False,
        default=0,
    )
    ordered_places = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        default=0,
    )
    new_email = models.ManyToManyField(News_email,related_name='new_email')
