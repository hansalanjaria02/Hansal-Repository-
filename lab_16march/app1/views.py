from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

# 2. CREATE: Naya student add karne ke liye
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'forms.html', {'form': form})

# 3. UPDATE: Student ki details badalne ke liye
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # instance=student likhne se form mein purana data pehle se bhara hua aayega
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'forms.html', {'form': form})

# 4. DELETE: Student ko remove karne ke liye
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})
