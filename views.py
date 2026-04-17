from django.shortcuts import render, get_object_or_404
from .models import Course, Enrollment, Submission, Choice

# Submit exam
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # get user enrollment
    enrollment = Enrollment.objects.get(user=request.user, course=course)

    # create submission
    submission = Submission.objects.create(enrollment=enrollment)

    # get selected choices
    selected_ids = request.POST.getlist('choice')

    for choice_id in selected_ids:
        choice = Choice.objects.get(id=int(choice_id))
        submission.choices.add(choice)

    # redirect to result page
    return show_exam_result(request, course_id, submission.id)


# Show result
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    total_grade = 0
    user_grade = 0

    for choice in selected_choices:
        question = choice.question
        total_grade += question.grade

        if choice.is_correct:
            user_grade += question.grade

    context = {
        'course': course,              # ✅ required
        'selected_ids': selected_ids,  # ✅ required
        'grade': user_grade,           # ✅ required
        'possible': total_grade        # ✅ required
    }

    return render(request, 'exam_result_bootstrap.html', context)
