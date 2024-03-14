from django.http import HttpResponse


def url(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return HttpResponse(f"Hello {name}! {message}")