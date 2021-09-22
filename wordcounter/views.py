from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')


def about(request):
    
    return render(request, 'about.html')

def count(request):
    words = {}
    user_text = request.GET["usertext"]
    split_text = user_text.split()

    for word in split_text:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    
    sorted_words = sorted(words.items(), key= operator.itemgetter(1), reverse= True)
    return render(request, 'count.html', {"usertext":  user_text, "words" : sorted_words, "count_No" : len(split_text)})