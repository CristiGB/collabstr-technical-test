from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Content
from django.shortcuts import render

VIDEO_EXTENSIONS = ('.mp4', '.webm', '.ogg', '.avi', '.mov', '.flv', '.wmv')

def get_paginated_contents(queryset, page_number):
    paginator = Paginator(queryset, 30)  

    try:
        contents = paginator.page(page_number)
    except PageNotAnInteger:
        contents = paginator.page(1) 
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)

    return contents

def content_list(request):
    print("aui")
    contents_list = Content.objects.select_related('creator').order_by('id').all()
    for content in contents_list:
        content.is_video = content.url.lower().endswith(VIDEO_EXTENSIONS)
    contents = get_paginated_contents(contents_list, request.GET.get('page'))
    return render(request, 'content_list.html', {'contents': contents,'platform': 'all'})


def filtered_content(request, platform):
    print("aaa,", platform)
    if platform == 'all':
        contents_list = Content.objects.select_related('creator').order_by('id').all()
    else:
        contents_list = Content.objects.select_related('creator').order_by('id').filter(creator__platform=platform)
    
    page = request.GET.get('page', 1)
    contents = get_paginated_contents(contents_list, page)
    
    for content in contents:
        content.is_video = content.url.lower().endswith(VIDEO_EXTENSIONS)

    return render(request, 'content_list.html', {'contents': contents, 'platform': platform})