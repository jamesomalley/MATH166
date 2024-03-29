# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:46:47 2023

@author: James
"""
import requests
from bs4 import BeautifulSoup

tickers = ['ARKK',
'GUNR',
'KWEB',
'CIBR',
'ICLN',
'PAVE',
'FDN',
'IGF',
'GNR',
'LIT',
'IGM',
'NFRA',
'TAN',
'ARKG',
'IFRA',
'PHO',
'BOTZ',
'KOMP',
'QCLN',
'ITB',
'HACK',
'LCTU',
'URA',
'ROBO',
'FIW',
'MOO',
'ARKW',
'FNGU',
'XHB',
'CGW',
'PABU',
'ARKQ',
'CRBN',
'DRIV',
'URNM',
'ARKF',
'IGE',
'BUG',
'PBW',
'GRID',
'FIVG',
'GII',
'NANR',
'EMQQ',
'PNQI',
'ACES',
'IHAK',
'EMCR',
'LCTD',
'IPAY',
'NXTG',
'METV',
'BLOK',
'IDRV',
'FINX',
'SARK',
'XRT',
'MSOS',
'TECB',
'BULZ',
'CNRG',
'CWEB',
'SNSR',
'GINN',
'IYZ',
'IRBO',
'ERTH',
'ESPO',
'FTRI',
'FAN',
'PIO',
'ARKX',
'VEGI',
'MJ',
'GTEK',
'ROBT',
'NZAC',
'PBD',
'SMOG',
'GNOM',
'WOOD',
'KARS',
'PRNT',
'ETHO',
'HERO',
'GSFP',
'NAIL',
'BATT',
'RTH',
'SOCL',
'IDNA',
'GBUY',
'OGIG',
'MJUS',
'FNGD',
'WEBL',
'HAP',
'AIQ',
'FNGO',
'LEGR',
'DTEC',
'CTEC',
'NETZ',
'MILN',
'USNZ',
'IZRL',
'KGRN',
'NZUS',
'FMIL',
'ECON',
'TMAT',
'BLCN',
'SAMT',
'INCO',
'RNRG',
'EVX',
'NXTE',
'VEGN',
'XTL',
'AGNG',
'FNGS',
'CUT',
'NLR',
'HAIL',
'TIME',
'BKCH',
'BITQ',
'GAMR',
'FDRV',
'UFO',
'EBLU',
'JZRO',
'EBIZ',
'TARK',
'GXTG',
'RETL',
'WEBS',
'POTX',
'FRNW',
'CARZ',
'YOLO',
'HDRO',
'HYDR',
'FEDM',
'GRES',
'ECLN',
'ENTR',
'HJEN',
'HOMZ',
'MOON',
'FDNI',
'WFH',
'FITE',
'WCBR',
'CNBS',
'GENY',
'INNO',
'DAPP',
'FEUS',
'SIMS',
'THNQ',
'FDIG',
'NERD',
'NBCT',
'SXUS',
'EMIF',
'SSPX',
'JCTR',
'XWEB',
'BFIT',
'TEMP',
'ERSX',
'WUGI',
'UBOT',
'THCX',
'FTAG',
'CCSO',
'ROKT',
'GK',
'FMQQ',
'LRNZ',
'URNJ',
'BERZ',
'CRPT',
'KOIN',
'FMET',
'FNGG',
'TRFM',
'BTEK',
'UPWD',
'CIRC',
'TOKE',
'WNDY',
'BKGI',
'MOTO',
'HELX',
'BLLD',
'OARK',
'NBDS',
'GCLN',
'BUYZ',
'BAD',
'VICE',
'IQM',
'WTAI',
'GPAL',
'STCE',
'FFND',
'AQWA',
'HLGE',
'HART',
'TCHI',
'BYOB',
'RBLD',
'BNE',
'KTEC',
'KBUY',
'KROP',
'XPND',
'IVEG',
'IBLC',
'GBLD',
'NDIV',
'IWTR',
'SOLR',
'WGMI',
'MTVR',
'NTZG',
'NBCC',
'IVRS',
'OCEN',
'ISHP',
'CLNR',
'WBAT',
'FWD',
'EATV',
'KLIP',
'SYNB',
'MSOX',
'LITP',
'GAST',
'OBOR',
'RAYS',
'FEEM',
'EFRA',
'BECO',
'KLNE',
'GFOF',
'BNGE',
'MVPS',
'GLIF',
'VCLO',
'BPAY',
'YUMY',
'ORFN',
'PSDN',
'VCAR',
'VCLN',
'ILDR',
'EVAV',
'EDUT',
'ENRG',
'SATO',
'SPRX',
'IWFH',
'SUBS',
'WDNA',
'EWEB',
'BCDF',
'EMFQ',
'VMAT',
'RNWZ',
'KGHG',
'VR',
'BLKC',
'BSEA',
'GRNR',
'AHOY',
'BULD',
'KGRO',
'WEED',
'ARVR',
'DGIN',
'INQQ',
'DAM',
'RNEW',
'GRZZ',
'TRFK',
'NZRO',
'PUNK',
'IBIT',
'ODDS',
'TWEB',
'SWEB',
'FIXT',
'DKRB',
'KCAL',
'UAV',
'RESI',
'BIDS',
'ION',
'BWEB',
'VERS',
'OND',
'TINY',
'CTEX',
'UCYB',
'SULR',
'ANEW',
'CCON',
'PAWZ',
'EMTY',
'TOLZ']


for x in tickers:
    URL = "https://etfdb.com/etf/"+x+"/#etf-ticker-profile"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("span", class_="text-right")
    results = str(results[2])
    print(results[25:37])
#results = soup.select_one("span.class.text-right:nth-of-type(2)").get_text(strip=True)
