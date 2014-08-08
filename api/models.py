from django.db import models
from django.db import connection, transaction
from time import time

class Article(models.Model):
    def __unicode__(self):
        return self.title

    @staticmethod
    def process():
        cur = connection.cursor()
        cur.execute("SELECT * FROM order_process;")
        cur.close
        dictreturn = Article.formatqueryresult(cur)
        return dictreturn
		
		
    @staticmethod
    def client_details():
        cur = connection.cursor()
        cur.execute("SELECT * FROM client_details;")
        cur.close
        dictreturn = Article.formatqueryresult(cur)
        return dictreturn
		
    @staticmethod
    def billings():
        cur = connection.cursor()
        cur.execute("SELECT * FROM billings;")
        cur.close
        dictreturn = Article.formatqueryresult(cur)
        return dictreturn
		
    @staticmethod
    def invoice_model(id):
        cur = connection.cursor()
        cur.execute("SELECT cust_name,company_name,email,mobile,location,address,invoice_no,date,job_request,units,Amount from client_details, billings where client_details.client_id=billings.client_id and billings.client_id="+id+";")
        cur.close
        dictreturn = Article.formatqueryresult(cur)
        return dictreturn


    @staticmethod
    def formatqueryresult(cur):
        desc = cur.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cur.fetchall()
        ]

