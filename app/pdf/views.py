from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.templatetags.static import static
from weasyprint import HTML


def index(request):
    template = get_template("pdf/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

    # return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    template_path = 'pdf/test.html'
    # context = {}  # Add any context variables you want to include

    # Build the absolute URL of the static image
    image_absolute_url = request.build_absolute_uri(static('pdf/dice.png'))

    # Add the image URL to the context, because WeasyPrint can't handle relative URLs
    context = {'image_absolute_url': image_absolute_url}

    # Render the HTML template
    template = get_template(template_path)
    html = template.render(context)

    return HttpResponse(template.render(context, request))


def download_pdf_from_template(request):
    template_path = 'pdf/index.html'
    context = {}  # Add any context variables you want to include

    # Render the HTML template
    template = get_template(template_path)
    html = template.render(context)

    # Generate the PDF
    pdf_file = HTML(string=html).write_pdf()

    # Serve the PDF as an HTTP response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    return response


def generate_pdf_from_template(request):
    template_path = 'pdf/test.html'
    # context = {}  # Add any context variables you want to include

    # Build the absolute URL of the static image
    image_absolute_url = request.build_absolute_uri(static('pdf/dice.png'))

    # Add the image URL to the context because WeasyPrint can't handle relative URLs
    context = {'image_absolute_url': image_absolute_url}

    # Render the HTML template
    template = get_template(template_path)
    html = template.render(context)

    # Generate the PDF
    pdf_file = HTML(
        string=html, base_url=request.build_absolute_uri()).write_pdf()

    # Serve the PDF as an HTTP response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    # Removed Content-Disposition header to display PDF in browser
    return response
