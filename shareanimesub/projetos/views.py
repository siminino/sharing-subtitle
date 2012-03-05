from django.template.response import TemplateResponse

def view_test(request):
    return TemplateResponse(request, 'base.html')

