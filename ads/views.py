import json

from django.http import HttpResponse, JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def main(request):
    return HttpResponse('Hello! This is main page')


@method_decorator(csrf_exempt, name='dispatch')
class AdsList(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad.objects.create(**data)
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published},
                            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesList(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({'id': category.pk,
                             'name': category.name})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(**data)
        return JsonResponse({'id': category.pk,
                             'name': category.name},
                            safe=False)


class CategoriesListMoreInfo(DetailView):
    # model = Category

    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name}, safe=False)


class AdsListMoreInfo(DetailView):
    # model = Ad

    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published},
                            safe=False)
