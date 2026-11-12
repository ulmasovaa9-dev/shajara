from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  # Admin ro'yxatida ko'rinadigan ustunlar
  list_display = (
      'id',
      'first_name',
      'last_name',
      'gender',
      'birth_year',
      'father',
      'mother',
      'spouse',
  )

  # Qaysi ustunlar bo'yicha qidirish mumkinligi
  search_fields = ('first_name', 'last_name')

  # Yon panelda jinsi bo'yicha filtrlash
  list_filter = ('gender', 'birth_year')

  # Maydonlarni tartibga solish (agar kerak bo'lsa)
  fields = (
      'first_name',
      'last_name',
      'gender',
      'birth_year',
      'father',
      'mother',
      'spouse',
  )