from django.shortcuts import render
import operator
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    text = request.GET['fulltext']

    word_list = text.split()#split 띄어쓰기별로 배열에 넣어줌

    dictionary = {}#= {} dictionary 함수 초기화

    for a in word_list:
        if a in dictionary:
        #a = {사과, 포도, 딸기} 
        #dictionary = {{key값, key에 있는 숫자값}}
            dictionary[a] += 1
        else:
            dictionary[a] = 1

    maxTotal = highest=max(dictionary.items(), key = lambda x: x[1])[0]
    sort = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True) #내림차순, 오름차순(faslse)



    return render(request, 'result.html', {'text' : text, 'total' : word_list, 'sort':sort,'maxTotal':maxTotal, 'dictionary' : dictionary.items() })
