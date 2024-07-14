from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from .models import Content

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
    contents_list = Content.objects.select_related('creator').order_by('id').all()
    for content in contents_list:
        content.is_video = content.url.lower().endswith(VIDEO_EXTENSIONS)
    contents = get_paginated_contents(contents_list, request.GET.get('page'))
    return render(request, 'content_list.html', {'contents': contents})

def filtered_content(request, platform):
    if platform == 'all':
        contents_list = Content.objects.select_related('creator').order_by('id').all()
    else:
        contents_list = Content.objects.select_related('creator').order_by('id').filter(creator__platform=platform)
    
    contents = get_paginated_contents(contents_list, request.GET.get('page'))
    for content in contents:
        content.is_video = content.url.lower().endswith(VIDEO_EXTENSIONS)

    return render(request, 'content_list.html', {'contents': contents})
