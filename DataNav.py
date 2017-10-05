#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:27:09 2017

@author: massimo
"""

import pandas as pd
import numpy as np
import functools as ft

# ***************************** GEO ******************************************
#dfgeo = pd.read_csv('../GEO/allCountries.txt', sep='\t', encoding = "ISO-8859-1")
#dftz = pd.read_csv('../GEO/timeZones.txt', sep='\t', encoding = "ISO-8859-1")
#dfgeoinfo = pd.read_csv('../GEO/geo_info.csv', sep=';', encoding = "ISO-8859-1")
#dfcountinfo = pd.read_csv('../GEO/countryInfo_filt.txt', sep='\t')
#
#dftz_filt = dftz[['CountryCode','TimeZoneId','rawOffset (independant of DST)']]
#dfgeoinfo_filt = dfgeoinfo[['ALPHA2','ALPHA3','latitude','longitude']]
#dfcountinfo_filt = dfcountinfo[['ISO','ISO3','Country', 'Capital','Area(in sq km)','Population','Continent','CurrencyCode', 'CurrencyName']]
#
#dftz_filt.set_index(['CountryCode'])
#dfgeoinfo_filt.set_index(['ALPHA2'])
#dfcountinfo_filt.set_index(['ISO'])
#result_part = pd.merge(dfcountinfo_filt, dfgeoinfo_filt, left_on=['ISO'], right_on=['ALPHA2'], how='outer')
#result_final = pd.merge(result_part, dftz_filt,  left_on=['ISO'], right_on=['CountryCode'], how='outer')
#result_final.drop(['ALPHA2','ALPHA3','CountryCode'],axis=1,inplace=True)
#result_final.to_csv('./geo_ds.csv',sep=';',encoding = "ISO-8859-1")

df_geo_ds = pd.read_csv('./geo_ds.csv', sep=';', encoding = "ISO-8859-1")

# ***************************** IMF *******************************************
df_imf = pd.read_csv('./imf_weo_ds.csv',sep=';', encoding = "ISO-8859-1")
df_filt = df_imf[['ISO','Country','Units','Scale','2000','2001', '2002',
       '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015','Estimates Start After','WEO Subject Code','Subject Descriptor','Subject Notes']].copy()

#Popolazione
df_filt_pop = df_filt[df_filt['WEO Subject Code']=='LP']

#Impiegati
df_filt_empl = df_filt[df_filt['WEO Subject Code']=='LE']

#Tasso di disoccupazione
df_filt_unempl_rate = df_filt[df_filt['WEO Subject Code']=='LUR']

#GDP
df_filt_gdp_cp = df_filt[df_filt['WEO Subject Code']=='NGDP_R']

#GDP procapita
df_filt_gdp_xc_cp = df_filt[df_filt['WEO Subject Code']=='NGDPRPC']

#df_filt_italy = df_filt[df_filt['Country']=='Italy']
#
#print(df_filt_pop.head(10))
#
#print(dfrel.head(10))
#
#df_filt_pop.set_index(['Country'])
#dfrel.set_index(['Country'])
#
#result = pd.merge(df_filt_pop, dfrel, on='Country', how='outer')
#
#
#print(result.head(10))



#df_filt = df_filt[(df_filt['Units']=='U.S. dollars')|(df_filt['Units']=='Persons')]

#print(df_filt[df_filt['Country']=='Italy'])

# ***************************** WHO *******************************************
#MORT_CHILD_AC_LOW_RESP_INFECTIONS.csv
#MORT_CHILD_BIRTH_ASPHYXIA_TRAUMA.csv
#MORT_CHILD_BIRTH_PERINATAL_NUTRITIONAL.csv
#MORT_CHILD_BIRTH_SEPSIS_INFECTIONS.csv
#MORT_CHILD_CONGENITAL_ANOM.csv
#MORT_CHILD_DIARRHOEAL-DIS.csv
#MORT_CHILD_HIV-AIDS.csv
#MORT_CHILD_INJURIES.csv
#MORT_CHILD_MALARIA.csv
#MORT_CHILD_MEASLES.csv
#MORT_CHILD_MENINGITIS-ENCEPH.csv
#MORT_CHILD_OTHER.csv
#MORT_CHILD_PERTUSSIS.csv
#MORT_CHILD_PREMATURITY.csv
#
#df_mc_lowresp = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_AC_LOW_RESP_INFECTIONS.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_asph = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_BIRTH_ASPHYXIA_TRAUMA.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_perin = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_BIRTH_PERINATAL_NUTRITIONAL.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_sepsis = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_BIRTH_SEPSIS_INFECTIONS.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_cong = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_CONGENITAL_ANOM.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_diar = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_DIARRHOEAL-DIS.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_hiv = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_HIV-AIDS.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_inj = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_INJURIES.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_malaria = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_MALARIA.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_meas = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_MEASLES.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_menin = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_MENINGITIS-ENCEPH.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_oth = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_OTHER.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_pert = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_PERTUSSIS.csv', sep=',', encoding = "ISO-8859-1")
#df_mc_prem = pd.read_csv('../WHO/COUNTRIES/MORT_CHILD_PREMATURITY.csv', sep=',', encoding = "ISO-8859-1")
#
#df_mc_all_list = [df_mc_lowresp, df_mc_asph, df_mc_perin, df_mc_sepsis, df_mc_cong, df_mc_diar, df_mc_hiv, df_mc_inj, df_mc_malaria, df_mc_meas, df_mc_menin, df_mc_oth, df_mc_pert, df_mc_prem]
#df_final = ft.reduce(lambda left,right: pd.merge(left,right,on=['Country','Year']), df_mc_all_list)
#
#df_final.to_csv('../WHO/COUNTRIES/MORT_CHILD_DS.csv',sep=';',encoding = "ISO-8859-1")
#
#
df_who = pd.read_csv('./MORT_CHILD_DS.csv', sep=';', encoding = "ISO-8859-1")


# ***************************** REL *******************************************

df_rel = pd.read_csv('./religions_corr_ds.csv', sep=';', encoding = "ISO-8859-1")