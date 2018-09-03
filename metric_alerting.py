import requests
import json
import smtplib
from time import sleep, time
from elasticsearch import Elasticsearch
from pprint import pprint
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from helpers import getkeymem, getkeycpu, getkeyfilesystem, send_mail
from globals import payload, headers, docvalue_fields, url

while True:
    # Setting
    LTE = (int(time())*1000)
    GTE = LTE-60000
    body = """{ "query": { "bool": { "must": [{ "range": { "@timestamp": { "gte": "MY_GTE", "lte": "MY_LTE", "format": "epoch_millis" } } }], "filter": [], "should": [], "must_not": [] } } }"""
    index = """metricbeat-6.2.2-DATE"""
    body = body.replace("MY_GTE", str(GTE))
    body = body.replace("MY_LTE", str(LTE))
    today = date.today()
    dat = today.strftime('%Y.%m.%d')
    index = index.replace('DATE',dat)

    # connecting to host
    try:
      es = Elasticsearch([{'host': '<ip>'}], http_auth=('<user>','<password>'))
      print ("Connected", es.info())
    except Exception as ex:
      print ("Error:", ex)

    # Elastic Searching through index
    es_res = es.search(index=index, ignore_unavailable="true", preference="1528194190389", version="true", size="500", sort='[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}]', _source=['*'], stored_fields=["*"], docvalue_fields=docvalue_fields, body=body)

    hits=es_res['hits']
    i_hits=hits['hits']
#    pprint (i_hits)
    # Setting Threshold Values and Initialising
    threshold_val_mem = 65
    threshold_val_cpu = 65
    threshold_val_disk = 65
    danger_hosts = dict()
    danger_hosts['mem_hostname'] = []
    danger_hosts['mem_percentage'] = []
    danger_hosts['cpu_percentage'] = []
    danger_hosts['cpu_hostname'] = []
    danger_hosts['disk_percentage'] = []
    danger_hosts['disk_hostname'] = []


#---------------Memory Utilization-------------------
    count_mem_list = getkeymem(i_hits)
    for count_mem in count_mem_list:
        sys = i_hits[count_mem]['_source']['system']
        mem_percentage = sys['memory']['actual']['used']['pct'] * 100
        mem_host_name = i_hits[count_mem]['_source']['beat']['hostname']
        if mem_percentage > threshold_val_mem:
            danger_hosts['mem_hostname'].append(mem_host_name)
            danger_hosts['mem_percentage'].append(mem_percentage)

#------------------CPU Utilization-------------------
    count_cpu_list = getkeycpu(i_hits)
    for count_cpu in count_cpu_list:
            sys1 = i_hits[count_cpu]['_source']['system']
            cpu_percentage = sys1['cpu']['total']['pct'] * 100
            cpu_host_name = i_hits[count_cpu]['_source']['beat']['hostname']
            if cpu_percentage > threshold_val_cpu:
                danger_hosts['cpu_hostname'].append(cpu_host_name)
                danger_hosts['cpu_percentage'].append(cpu_percentage)

#------------------Disk Utilization-------------------
    count_disk_list = getkeyfilesystem(i_hits)
    for count_disk in count_disk_list:
            sys1 = i_hits[count_disk]['_source']['system']
            disk_percentage = sys1['filesystem']['used']['pct'] * 100
            disk_host_name = i_hits[count_disk]['_source']['beat']['hostname']
            if disk_percentage > threshold_val_disk:
                danger_hosts['disk_hostname'].append(disk_host_name)
                danger_hosts['disk_percentage'].append(disk_percentage)

    # Condition to check if their are any entries in the dictionary , if yes send alert through mail
    if len(danger_hosts) > 0:
        print (danger_hosts)
        if danger_hosts['mem_hostname'] or danger_hosts['cpu_hostname'] or danger_hosts['disk_hostname'] != []:
            ret_code = send_mail(danger_hosts)
        sleep(3600)
        # Loops after every hour
