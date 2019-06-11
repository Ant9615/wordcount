from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def counter(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    ctx = {
        'fulltext': full_text,
        'total': len(word_list),
        'dict': word_dictionary.items()
    }

    return render(request, 'counter.html', ctx)
