from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import Html

from SiteBuilder import settings
import json

import os

import zipfile
import StringIO

# Create your views here.


def index(request):

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
def preview(request):
    content = ""
    if 'page' in request.POST:
        content = request.POST['page']

    return HttpResponse(content)


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
    assets_dir = settings.BASE_DIR + '/site_builder/' + settings.STATIC_URL + 'elements/'

    filenames = get_filepaths(assets_dir)

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")


    req = request

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)

        # Get relative path
        relative_path = fdir.split('//')[1]
        zip_path = os.path.join(relative_path, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

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

            zf.writestr(file_name, content)

    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


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