from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


from django.contrib import admin
from sigma.models import Quote

class Quotes(admin.ModelAdmin):
    list_display = ('id', 'author', 'author_quote')
    list_display_links = ('id', 'author')
    search_fields = ('author',)

admin.site.register(Quote, Quotes)

'''
def RetornaDf():

    quote = []
    author = []
    for i in range(1, 11):
        html = urlopen(f'https://quotes.toscrape.com/page/{i}/')
        bs = BeautifulSoup(html, 'html.parser')
        quote += bs.find_all('span', {'class':'text'})
        author += bs.find_all('small', {'class':'author'})
    
    df = pd.DataFrame()
    df['author']=author
    df['quote']=quote

    for i in range(len(df)):
        df['author'][i]=author[i].text
        df['quote'][i]=quote[i].text

    return(df)

dataframe = RetornaDf()
for i in range(len(dataframe)):
    b = Quote(author=dataframe['author'][i], author_quote=dataframe['quote'][i])
    b.save()
'''