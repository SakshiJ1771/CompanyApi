from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page")
    friends=[
        'meena',
        'zeba',
        'mithila'
    ]
    return JsonResponse(friends,safe=False)