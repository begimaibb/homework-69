import json
from django.http import JsonResponse


def add(request, *args, **kwargs):
    if request.method == 'POST':
        a = request.form.get('a: ')
        b = request.form.get('b: ')
        answer = int(a) + int(b)
        answer_as_json = json.dumps(answer)
        response = JsonResponse(answer_as_json)
        return response


def subtract(request):
    if request.method == 'POST':
        a = request.form.get('a: ')
        b = request.form.get('b: ')
        answer = int(a) - int(b)
        answer_as_json = json.dumps(answer)
        response = JsonResponse(answer_as_json)
        return response


def multiply(request):
    if request.method == 'POST':
        a = request.form.get('a: ')
        b = request.form.get('b: ')
        answer = int(a) * int(b)
        answer_as_json = json.dumps(answer)
        response = JsonResponse(answer_as_json)
        return response


def divide(request):
    if request.method == 'POST':
        a = request.form.get('a: ')
        b = request.form.get('b: ')
        if int(b) == 0:
            response = JsonResponse({'error': 'You cannot divide into 0!!'})
            response.status_code = 400
            return response
        answer = int(a) / int(b)
        answer_as_json = json.dumps(answer)
        response = JsonResponse(answer_as_json)
        return response
