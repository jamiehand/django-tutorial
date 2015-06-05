from django.shortcuts import render  # a shortcut so I don't have to import HttpResponse, loader, or RequestContext
# from django.template import RequestContext, loader  <-- no longer needed, with "render"
from django.shortcuts import get_object_or_404 # a shortcut for 404s
from django.http import HttpResponse    # no longer needed for index, b/c of "render" <-- but keep b/c still used in
                                        # other methods
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic  # for using generic views
from django.utils import timezone

from .models import Choice, Question

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.") <-- 1st return value
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#     # template = loader.get_template('polls/index.html')  # <-- 3rd return value
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # return HttpResponse(template.render(context))
#
#     # output = ', '.join([p.question_text for p in latest_question_list]) <-- 2nd return value
#     # return HttpResponse(output)

# for generic views:
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        # return Question.objects.order_by('-pub_date')[:5]  <-- used before avoiding showing future posts
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('pub_date')[:5]

# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id) <-- 1st return value
#     # try:                                                                <-- 2nd return value
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist!")
#     # return render(request, 'polls/detail.html', {'question': question})
#     question = get_object_or_404(Question, pk=question_id)              # <-- 3rd return value
#         # get_object_or_404() takes Django model as 1st arg, and an arbitrary number of keyword args, which it passes
#         # to the get() function of the model's manager.
#     return render(request, 'polls/detail.html', {'question': question})

# for generic views:
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."          <-- 1st return value
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# for generic views:
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# remains same for generic views:
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)  <-- 1st return value
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {  # request is a HttpRequest object.
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents
        # data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        # reverse(), in this case, returns a string like "/polls/3/results/"
