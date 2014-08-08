from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orderprocess.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^orderprocess/','api.views.orderprocessing'),
	url(r'^client/','api.views.clientid'),
	url(r'^billings/','api.views.billings'),
	url(r'^showorderprocess/','api.views.show_process_data'),
	url(r'^clientdetails/','api.views.clientdetails_view'),
	url(r'^billingdetails/','api.views.billings_view'),
	url(r'^generatepdf/','api.views.generate_pdf_view'),	
	url(r'^invoicedetails/','api.views.invoice_view'),
	url(r'^invoice/','api.views.invoice'),
)
