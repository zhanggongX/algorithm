from django.shortcuts import render

def myFilter(request):
    values = {}
    values['value1'] = 'hello'

    values['value2'] = 'WORLD'
    values['value3'] = 'abcdefg'
    return render(request, 'filter.html', values)