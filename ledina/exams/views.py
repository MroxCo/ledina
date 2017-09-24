from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from django.template.loader import render_to_string


from .models import Exam, ExamFile, ExamComment
from .forms import ExamForm, FileForm

SUBJECTS = ['Matematika', 'Slovenščina', 'Angleščina', 'Drugi-jezik', 'Biologija','Kemija', 'Fizika', 'Zgodovina', 'Geografija']
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'pdf']


def letnik(request, letnik_id):
    return render(request, 'classes_base.html', {
        'letnik_id': letnik_id,
        'LETTERS': LETTERS,
        'SUBJECTS': SUBJECTS,})

def subject(request, letnik_id, classes_id, subject_id):
    if subject_id in SUBJECTS:
        path = letnik_id + '/' + classes_id + '/' + subject_id 
        exams = Exam.objects.filter(exam_path=path).order_by('exam_number')
        full_path = request.get_full_path
        context = {
        'letnik_id': letnik_id,
        'classes_id': classes_id, 
        'subject_id': subject_id,
        'path': path,
        'exams': exams,
        'full_path': full_path,
        }
        ref = request.GET.get('ref', None)
        if ref is not None and ref.isdigit():
        	context['ref'] = int(ref)
        	return render(request, 'tests.html', context)
        else:
        	return render(request, 'tests.html', context)
    else:
        raise Http404("Stran ne obstaja")


def create_exam(request, letnik_id, classes_id, subject_id):
    if subject_id in SUBJECTS:
        if request.user.is_authenticated():
            if request.method == 'POST':
                path = letnik_id + '/' + classes_id + '/' + subject_id
                formone = ExamForm(request.POST or None, request.FILES or None)
                formtwo = FileForm(request.POST or None, request.FILES or None)
                if formone.is_valid() and formtwo.is_valid():
                    files = request.FILES.getlist('exam_file')
                    if len(files) > 8:
                        return JsonResponse({'error': 'Naložite lahko največ 8 datotek'})
                    exam_form = formone.save(commit=False)
                    exam_form.exam_user = request.user
                    exam_form.exam_path = path
                    exam_form.save()
                    exam_id = exam_form.id
                    exam = get_object_or_404(Exam, id=exam_id)
                    for file in files: 
                        instance = ExamFile(
                            exam_file=file,
                            exam=exam,
                            )
                        instance.save()
                    return JsonResponse({'success': 'success'})
                else:
                    return JsonResponse({ 'error': 'Datoteka mora biti tipa JPG, JPEG ali PNG'})
        else:
            return JsonResponse({ 'error': 'Za dodajanje testov se morate prijaviti'})
    raise Http404("Stran ne obstaja")


def mark_exam(request, letnik_id, classes_id, subject_id):
    exam_id = request.GET.get('exam')
    exam = get_object_or_404(Exam, id=exam_id)
    user = request.user
    if user in exam.exam_mark.all():
        exam.exam_mark.remove(user)
        return JsonResponse({"mark": "unmarked"})
    else:
        exam.exam_mark.add(user)
        return JsonResponse({"mark": "marked"})


def remove_exam(request, letnik_id, classes_id, subject_id):
    if request.method == 'POST':
        exam_id = request.POST.get('exam')
        exam = get_object_or_404(Exam, id=exam_id)
        if exam.exam_user == request.user:
            exam.delete()
            return JsonResponse({"success": "success"})


def comment(request, letnik_id, classes_id, subject_id):
        if request.method == 'POST':
            exam_id = request.POST.get('exam_id')
            exam = get_object_or_404(Exam, id=exam_id)
            comment = request.POST.get('post')
            comment = comment.strip()
            if len(comment) > 0:
                instance = ExamComment(
                    exam=exam,
                    comment=comment,
                    comment_user=request.user)
                instance.save()
                comments = ExamComment.objects.filter(exam=exam)
                return render(request, 'exam_partial_comment.html', {'comments': comments})
        else:
            exam_id = request.GET.get('exam_id')
            exam = get_object_or_404(Exam, id=exam_id)
            comments = ExamComment.objects.filter(exam=exam)
            return render(request, 'exam_partial_comment.html', {'comments': comments})


def remove_comment(request, letnik_id, classes_id, subject_id):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(ExamComment, id=comment_id)
        if comment.comment_user == request.user:
            comment.delete()
            return JsonResponse({"success": "success"})




