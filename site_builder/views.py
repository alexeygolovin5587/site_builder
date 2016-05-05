from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import *

from SiteBuilder import settings
import json

import os

import zipfile
import StringIO

import random

from django.shortcuts import redirect

# Create your views here.



def index(request):
    new_themes = Module.objects.filter(added=1)

    themes = []
    elements = {"elements": {
        "Headers":[
            {"url":"/static/elements/header10.html","height":567, "thumbnail":"/static/elements/images/thumbs/header10.png"},
            {"url":"/static/elements/header5.html","height":618, "thumbnail":"/static/elements/images/thumbs/header5.png"},
            {"url":"/static/elements/header11.html","height":708, "thumbnail":"/static/elements/images/thumbs/header11.png"},
            {"url":"/static/elements/header1.html","height":481, "thumbnail":"/static/elements/images/thumbs/header1.png"},
            {"url":"/static/elements/header6.html","height":491, "thumbnail":"/static/elements/images/thumbs/header6.png"},
            {"url":"/static/elements/header2.html","height":498, "thumbnail":"/static/elements/images/thumbs/header2.png"},
            {"url":"/static/elements/header8.html","height":633, "thumbnail":"/static/elements/images/thumbs/header8.png"},
            {"url":"/static/elements/header9.html","height":633, "thumbnail":"/static/elements/images/thumbs/header9.png"},
            {"url":"/static/elements/header3.html","height":959, "thumbnail":"/static/elements/images/thumbs/header3.png"},
            {"url":"/static/elements/header4.html","height":660, "thumbnail":"/static/elements/images/thumbs/header4.png"},
            {"url":"/static/elements/header7.html","height":715, "thumbnail":"/static/elements/images/thumbs/header7.png"},
        ],
        "Slideshow Blocks":[
            {"url":"/static/elements/slideshow1.html","height":877, "thumbnail":"/static/elements/images/thumbs/slideshow1.png", "sandbox":True, "loaderFunction":"startSlideshow"}
        ],
        "Content Sections":[
            {"url":"/static/elements/content_section1.html","height":481, "thumbnail":"/static/elements/images/thumbs/content_section1.png"},
            {"url":"/static/elements/content_section2.html","height":520, "thumbnail":"/static/elements/images/thumbs/content_section2.png"},
            {"url":"/static/elements/content_section3.html","height":774, "thumbnail":"/static/elements/images/thumbs/content_section3.png"},
            {"url":"/static/elements/content_section4.html","height":331, "thumbnail":"/static/elements/images/thumbs/content_section4.png"},
            {"url":"/static/elements/content_section5.html","height":846, "thumbnail":"/static/elements/images/thumbs/content_section5.png"},
            {"url":"/static/elements/content_section6.html","height":344, "thumbnail":"/static/elements/images/thumbs/content_section6.png"},
            {"url":"/static/elements/content_section7.html","height":344, "thumbnail":"/static/elements/images/thumbs/content_section7.png"},
            {"url":"/static/elements/content_section8.html","height":725, "thumbnail":"/static/elements/images/thumbs/content_section8.png"},
            {"url":"/static/elements/content_section9.html","height":567, "thumbnail":"/static/elements/images/thumbs/content_section9.png"},
            {"url":"/static/elements/content_section10.html","height":376, "thumbnail":"/static/elements/images/thumbs/content_section10.png"},
            {"url":"/static/elements/content_section11.html","height":376, "thumbnail":"/static/elements/images/thumbs/content_section11.png"},
        ],
        "Dividers":[
            {"url":"/static/elements/divider1.html","height":163, "thumbnail":"/static/elements/images/thumbs/divider1.png"},
            {"url":"/static/elements/divider2.html","height":163, "thumbnail":"/static/elements/images/thumbs/divider2.png"},
            {"url":"/static/elements/divider3.html","height":163, "thumbnail":"/static/elements/images/thumbs/divider3.png"},
            {"url":"/static/elements/divider4.html","height":183, "thumbnail":"/static/elements/images/thumbs/divider4.png"},
            {"url":"/static/elements/divider5.html","height":123, "thumbnail":"/static/elements/images/thumbs/divider5.png"},
            {"url":"/static/elements/divider6.html","height":60, "thumbnail":"/static/elements/images/thumbs/divider6.png"},
            {"url":"/static/elements/divider7.html","height":120, "thumbnail":"/static/elements/images/thumbs/divider7.png"}
        ],
        "Portfolios":[
            {"url":"/static/elements/portfolio1.html","height":701, "thumbnail":"/static/elements/images/thumbs/portfolio1.png"},
            {"url":"/static/elements/portfolio2.html","height":799, "thumbnail":"/static/elements/images/thumbs/portfolio2.png"},
            {"url":"/static/elements/portfolio3.html","height":516, "thumbnail":"/static/elements/images/thumbs/portfolio3.png"},
        ],
        "Team":[
            {"url":"/static/elements/team1.html","height":644, "thumbnail":"/static/elements/images/thumbs/team1.png"},
            {"url":"/static/elements/team2.html","height":810, "thumbnail":"/static/elements/images/thumbs/team2.png"},
            {"url":"/static/elements/team3.html","height":752, "thumbnail":"/static/elements/images/thumbs/team3.png"},

        ],
        "Pricing Tables":[
            {"url":"/static/elements/pricing_table1.html","height":628, "thumbnail":"/static/elements/images/thumbs/pricing_table1.png"},
            {"url":"/static/elements/pricing_table2.html","height":750, "thumbnail":"/static/elements/images/thumbs/pricing_table2.png"},
            {"url":"/static/elements/pricing_table3.html","height":721, "thumbnail":"/static/elements/images/thumbs/pricing_table3.png"},


        ],
        "Contact":[
            {"url":"/static/elements/contact1.html","height":691, "thumbnail":"/static/elements/images/thumbs/contact1.png"},
            {"url":"/static/elements/contact2.html","height":477, "thumbnail":"/static/elements/images/thumbs/contact2.png"},


        ],
        "Footers":[
            {"url":"/static/elements/footer1.html","height":294, "thumbnail":"/static/elements/images/thumbs/footer1.png"},
            {"url":"/static/elements/footer2.html","height":107, "thumbnail":"/static/elements/images/thumbs/footer2.png"},
            {"url":"/static/elements/footer3.html","height":260, "thumbnail":"/static/elements/images/thumbs/footer3.png"},
        ],

        }
    }

    master_name = ""
    for theme in new_themes:
        temp = dict()

        temp['id'] = theme.id
        temp['height'] = 700
        temp['url'] = theme.master.html_path + theme.url
        temp['thumbnail'] = theme.master.img_path + theme.thumbnail
        master_name = theme.master.name
        themes.append(temp)

    with open(settings.BASE_DIR + '/site_builder/' + settings.STATIC_URL + 'elements.json', 'wb') as json_file:
        if len(themes) > 0:
            elements['elements'][master_name] = themes

        res_str = "var _Elements = " + json.dumps(elements)
        print res_str
        json_file.write(res_str)

    v = random.randint(1, 100)

    addable_themes = Module.objects.filter(added=0)

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
def preview(request):
    content = ""
    if 'page' in request.POST:
        content = request.POST['page']

    return HttpResponse(content)

@csrf_exempt
def add_themes(request):
    id = request.POST['theme']

    theme = Module.objects.filter(id=id)[0]

    theme.added = 1
    theme.save()

    return redirect('/')

@csrf_exempt
def delete_themes(request):
    id= int(request.POST['id'])

    theme = Module.objects.filter(id=id)[0]

    theme.added = 0
    theme.save()

    new_themes = Module.objects.filter(added=0)

    themes = []
    for theme in new_themes:
        temp = dict()

        temp['id'] = theme.id
        temp['name'] = theme.name

        themes.append(temp)

    return HttpResponse(json.dumps(themes))

@csrf_exempt
def iupload(request):
    img_dir = settings.BASE_DIR + '/site_builder/' + settings.STATIC_URL + 'elements/images/uploads/'
    allowed_types = ["image/jpeg", "image/gif", "image/png", "image/svg", "application/pdf"];

    res = dict()
    res['response'] = "The uploaded file couldn't be saved. Please make sure you have provided a correct upload folder and that the upload folder is writable."
    res['code'] = 0

    obj = request.FILES['imageFileField']

    if obj.content_type in allowed_types:
        fd = open(img_dir + obj.name, 'wb')
        for chunk in obj.chunks():
            fd.write(chunk)
        fd.close()
        res['response'] = settings.STATIC_URL + "elements/images/uploads/" + obj.name
        res['code'] = 1
    else:
        res['response'] = "File type not allowed"
        res['code'] = 0

    return HttpResponse(json.dumps(res))

@csrf_exempt
def save_html(request):
    res = request

    for page in request.POST:
        if 'pages' in page:
            file_name = page.split('[')[1][:-1] + '.html'
            content = request.POST['doctype'].encode('utf8').strip() + "\n" + request.POST[page].encode('utf8').strip()

            # Save html files in sqlite database
            html_obj = Html.objects.filter(name=file_name)
            if len(html_obj) > 0:
                html_obj = html_obj[0]
            else:
                html_obj = Html()

            html_obj.name = file_name
            html_obj.content = content
            html_obj.save()


    return HttpResponse(content)

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            if '.html' not in filename:
                file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.