from django.test import SimpleTestCase
from django.urls import reverse,resolve
from ChurnAnalysis.views import blank,login,main,loadCSV,detailsForm,predict,graph,help,admin

class TestUrls(SimpleTestCase):

    def test_blank_url_resolves(self):
        #assert 1==2
        url=reverse('blank')
        self.assertEquals(resolve(url).func,blank)
        print('Test : test_blank_url_resolves')

    def test_login_url_resolves(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)
        print('Test : test_login_url_resolves')

    def test_main_url_resolves(self):
        url=reverse('main')
        self.assertEquals(resolve(url).func,main)
        print('Test : test_main_url_resolves')

    def test_loadCSV_url_resolves(self):
        url=reverse('loadCSV')
        self.assertEquals(resolve(url).func,loadCSV)
        print('Test : test_loadCSV_url_resolves')

    def test_detailsForm_url_resolves(self):
        url=reverse('detailsForm')
        self.assertEquals(resolve(url).func,detailsForm)
        print('Test : test_detailsForm_url_resolves')

    def test_predict_url_resolves(self):
        url=reverse('predict')
        self.assertEquals(resolve(url).func,predict)
        print('Test : test_predict_url_resolves')

    def test_graph_url_resolves(self):
        url=reverse('graph')
        self.assertEquals(resolve(url).func,graph)
        print('Test : test_graph_url_resolves')

    def test_help_url_resolves(self):
        url=reverse('help')
        self.assertEquals(resolve(url).func,help)
        print('Test : test_help_url_resolves')

    def test_admin_url_resolves(self):
        url=reverse('admin')
        self.assertEquals(resolve(url).func,admin)
        print('Test : test_admin_url_resolves')
    