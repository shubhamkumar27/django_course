from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dtext = request.GET.get('text', 'kuch nahi mila')
    removepun = request.GET.get('removepunc', 'off')
    punc = '''!"#$%&\()'*+,-./:;<=>?@[]^_`{|}~'''
    analysed = ''
    if removepun == 'on':
        print('if')
        for char in dtext:
            if (char not in punc) and (char != ' '):
                analysed = analysed + char
                length = len(analysed)
        params = {'purpose': dtext, 'analysed_text': analysed + ' : ' + str(length)}
        return render(request, 'result.html', params)
    else:
        print('else')
        #return HttpResponse("Remove punctuations was not selected")
        return render(request, 'index1.html')

def result(request):
    dtext = request.GET.get('text','kuch nahi mila')
    removepun = request.GET.get('removepunc', 'off')
    punc = '''!"#$%&\()'*+,-./:;<=>?@[]^_`{|}~'''
    analysed = ''
    if removepun == 'on':
        print('if')
        for char in dtext:
            if (char not in punc) and (char != ' '):
                analysed = analysed+char
                length = len(analysed)
        params = {'purpose': dtext, 'analysed_text' : analysed+' : '+str(length)}
        return render(request, 'result.html', params)
    else:
        print('else')
        return HttpResponse("Remove punctuations was not selected")
