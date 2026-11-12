from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Person


# 1. Shajaradagi barcha shaxslarni ro'yxat ko'rinishida chiqarish
def get_family_tree_data(request):
  persons = Person.objects.all()

  tree_data = []
  for person in persons:
    tree_data.append({
        'id': person.id,
        'name': f'{person.first_name} {person.last_name or ""}',
        'gender': person.gender,
        'birthYear': person.birth_year,
        'fatherId': person.father.id if person.father else None,
        'motherId': person.mother.id if person.mother else None,
        'spouseId': person.spouse.id if person.spouse else None,
    })

  return render(request, 'shajara/tree.html', {'tree_data': tree_data})


# 2. Yangi qarindosh qo'shish
def add_person_view(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    gender = request.POST.get('gender')
    birth_year = request.POST.get('birth_year') or None

    father_id = request.POST.get('father')
    mother_id = request.POST.get('mother')
    spouse_id = request.POST.get('spouse')

    father = Person.objects.filter(id=father_id).first() if father_id else None
    mother = Person.objects.filter(id=mother_id).first() if mother_id else None
    spouse = Person.objects.filter(id=spouse_id).first() if spouse_id else None

    Person.objects.create(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        birth_year=birth_year,
        father=father,
        mother=mother,
        spouse=spouse,
    )
    return redirect('family_tree_url')

  persons = Person.objects.all()
  return render(request, 'shajara/add_person.html', {'persons': persons})


# 3. Shaxsning batafsil ma'lumotlari va farzandlarini ko'rish
def person_detail_view(request, pk):
  person = get_object_or_404(Person, pk=pk)
  children = Person.objects.filter(Q(father=person) | Q(mother=person))

  context = {
      'person': person,
      'children': children,
  }
  return render(request, 'shajara/person_detail.html', context)


# 4. Qarindoshni o'chirish
def delete_person_view(request, pk):
  person = get_object_or_404(Person, pk=pk)
  person.delete()
  return redirect('family_tree_url')