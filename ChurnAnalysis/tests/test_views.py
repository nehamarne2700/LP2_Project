from django.test import TestCase,Client
from django.urls import reverse
import json

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.blank_url=reverse('blank')
        self.login_url=reverse('login')
        self.main_url=reverse('main')
        self.predict_url=reverse('predict')
        self.detailsForm_url=reverse('detailsForm')
        self.graph_url=reverse('graph')
        self.help_url=reverse('help')
        self.admin_url=reverse('admin')

    def test_blank_GET(self):
        responce=self.client.get(self.blank_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'blank.html')
        print('Test : test_blank_GET')

    def test_login_GET(self):
        responce=self.client.get(self.login_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'login.html')
        print('Test : test_login_GET')

    def test_main_admin_POST(self):
        responce=self.client.post(self.main_url,{
            'username':'admin',
            'password':'admin'
        })

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'admin.html')
        print('Test : test_main_admin_POST')

    def test_main_user_POST(self):
        responce=self.client.post(self.main_url,{
            'username':'7590-VHVEG',
            'password':'7590-VHVEG'
        })

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'customer.html')
        print('Test : test_main_user_POST')

    def test_main_falsedata_POST(self):
        responce=self.client.post(self.main_url,{
            'username':'neha',
            'password':'neha'
        })

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'login.html')
        print('Test : test_main_falsedata_POST')

    def test_predict_POST(self):
        responce=self.client.post(self.predict_url,{
            'cname':'neha',
            'cid':'123neha',
            'gender':'female',
            'senior':'no',
            'partner':'no',
            'dependents':'no',
            'tenure':'9',
            'service':'yes',
            'mlines':'no',
            'iservice':'dsl',
            'olsecurity':'no',
            'olbackup':'no',
            'protection':'no',
            'tsupport':'no',
            'stv':'no',
            'smovie':'no',
            'contract':'mtm',
            'billing':'yes',
            'pmethod':'echeck',
            'mcharge':'50',
            'tcharge':'70'
        })

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'predResult.html')
        print('Test : test_predict_POST')

    def test_detailsForm_GET(self):
        responce=self.client.get(self.detailsForm_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'predForm.html')
        print('Test : test_detailsForm_GET')

    def test_graph_GET(self):
        responce=self.client.get(self.graph_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'graph.html')
        print('Test : test_graph_GET')

    def test_help_GET(self):
        responce=self.client.get(self.help_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'help.html')
        print('Test : test_help_GET')
    
    def test_admin_GET(self):
        responce=self.client.get(self.admin_url)

        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,'admin.html')
        print('Test : test_admin_GET')

    
    