from io import BytesIO
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from doctors.models import Prescription
from doctors.models import  Prescription,Prescription_medicine,Prescription_test
from hospitals.models import Patient
from datetime import datetime

# The render_to_pdf function is defined to convert an HTML template into a PDF. Here's what it does:

# It takes two parameters: template_src (the path to the HTML template) and context_dict (a dictionary containing the context variables for rendering the template) {like, patient, prescription, prescription_test, prescription medicine}.
# It loads the HTML template using get_template.
# It renders the HTML template with the provided context using template.render.
# It creates a BytesIO object to store the PDF output.
# It uses pisa.pisaDocument to convert the rendered HTML into a PDF and stores the result in the result object.
# If there are no errors during the PDF generation, it returns an HttpResponse with the PDF content and sets the content type to "application/pdf". Otherwise, it returns None.

def render_to_pdf(template_src, context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="aplication/pdf")
    return None



def prescription_pdf(request,pk):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        prescription = Prescription.objects.get(prescription_id=pk)
        prescription_medicine = Prescription_medicine.objects.filter(prescription=prescription)
        prescription_test = Prescription_test.objects.filter(prescription=prescription)
        current_date = datetime.date.today()
        context={'patient':patient,'current_date' : current_date,'prescription':prescription,'prescription_test':prescription_test,'prescription_medicine':prescription_medicine}
        pdf=render_to_pdf('prescription_pdf.html', context)
        if pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            content="inline; filename=report.pdf"
            # response['Content-Disposition']= content
            return response
        return HttpResponse("Not Found")
