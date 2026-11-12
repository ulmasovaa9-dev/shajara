from django.db import models


class Person(models.Model):
  GENDER_CHOICES = (
      ('M', 'Erkak'),
      ('F', 'Ayol'),
  )

  first_name = models.CharField(max_length=100, verbose_name='Ismi')
  last_name = models.CharField(
      max_length=100, blank=True, null=True, verbose_name='Familiyasi'
  )
  gender = models.CharField(
      max_length=1, choices=GENDER_CHOICES, verbose_name='Jinsi'
  )
  birth_year = models.IntegerField(
      blank=True, null=True, verbose_name='Tug‘ilgan yili'
  )

  # Qarindoshlik bog'lanishlari
  father = models.ForeignKey(
      'self',
      on_delete=models.SET_NULL,
      blank=True,
      null=True,
      related_name='father_children',
      verbose_name='Otasi',
  )
  mother = models.ForeignKey(
      'self',
      on_delete=models.SET_NULL,
      blank=True,
      null=True,
      related_name='mother_children',
      verbose_name='Onasi',
  )
  spouse = models.ForeignKey(
      'self',
      on_delete=models.SET_NULL,
      blank=True,
      null=True,
      related_name='spouses',
      verbose_name='Turmush o‘rtog‘i',
  )

  def __str__(self):
    return (
        f'{self.first_name} {self.last_name or ""}'
        f' ({self.birth_year or "?"})'
    )
