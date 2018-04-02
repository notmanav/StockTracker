from requests import Request, Session
import urllib3
import re

class StockPrice():

    baseurlstr="https://www.alphavantage.co/query?apikey=EWAXZU8Z9M2S7FXM&function=BATCH_STOCK_QUOTES&symbols="
    def fetchStocks(self,stocks="FB"):
        if(stocks==None):
            stocks="FB"
        rawstockslist=re.split(",|\.| ",stocks)
        stockslist=list()
        for astock in rawstockslist:
            result=re.match("^[a-zA-Z]+$",astock)
            if(result!=None):
                stockslist.append(astock)
        urlstr=self.baseurlstr+",".join(stock.strip() for stock in stockslist)
        urllib3.disable_warnings()
        
        s = Session()
        req = Request('GET',  urlstr, None, None)
        prepped = s.prepare_request(req)
        
        val=s.send(prepped,verify=False).json()
        for stock in val["Stock Quotes"]:
            stockvaluestring=Emojizer().emojize("{0:04}".format(round(float(stock["2. price"]))))
            print("{0}: :heavy_dollar_sign:{1}".format(stock["1. symbol"],stockvaluestring))
            
            
class Emojizer():
    mapping={'1':":one:",
             '2':":two:",
             '3':":three:",
             '4':":four:",
             '5':":five:",
             '6':":six:",
             '7':":seven:",
             '8':":eight:",
             '9':":nine:",
             '0':":zero:",
             '.':"."
             }
    
    mapping2={
            '1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9',
            '0':'0',
            '.':'.',
            
        }
    def emojize(self,value):
        valuearray=list(str(value))
        valuestring=""
        for value in valuearray:
            valuestring+=self.mapping2.get(value)
            valuestring+=""
        return valuestring

    