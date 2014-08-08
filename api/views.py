from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import Article
import pdfcrowd
import json



def orderprocessing(request):
    return render_to_response('orderprocessing.html', {},
        RequestContext(request))
		
def invoice(request):
    return render_to_response('invoice.html', {},
        RequestContext(request))

		
def clientid(request):
    return render_to_response('clientid.html', {},
        RequestContext(request))
		
def billings(request):
    return render_to_response('billings.html', {},
        RequestContext(request))
		
		
def show_process_data(request):
    if request.method == 'GET':
        process_data_table = Article.process()
        return HttpResponse(json.dumps(process_data_table), content_type='application/json;charset=utf8')

		
def clientdetails_view(request):
    if request.method == 'GET':
        process_data_table = Article.client_details()
        return HttpResponse(json.dumps(process_data_table), content_type='application/json;charset=utf8')

def billings_view(request):
    if request.method == 'GET':
        process_data_table = Article.billings()
        return HttpResponse(json.dumps(process_data_table), content_type='application/json;charset=utf8')


def generate_pdf_view(request):
    try:
        # create an API client instance
        client = pdfcrowd.Client("bk89149", "968e68f1ee015764a0ac103a18c916b8")

        # convert a web page and store the generated PDF to a variable
        pdf = client.convertURI("http://www.google.com")

         # set HTTP response headers
        response = HttpResponse(mimetype="application/pdf")
        response["Cache-Control"] = "max-age=0"
        response["Accept-Ranges"] = "none"
        response["Content-Disposition"] = "attachment; filename=google_com.pdf"

        # send the generated PDF
        response.write(pdf)
    except pdfcrowd.Error, why:
        response = HttpResponse(mimetype="text/plain")
        response.write(why)
    return response
	
def invoice_view(request):
    if request.method == 'GET':
		id=request.GET['id']
		process_data_table = Article.invoice_model(id)
		return HttpResponse(json.dumps(process_data_table), content_type='application/json;charset=utf8')	
