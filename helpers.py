import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pprint import pprint

# This function gets index of list containing memory
def getkeymem(i_hits):
    # pprint(i_hits)
    count = 0
    counters = []
    for i in i_hits:
        system = i['_source'].get('system', None)
        if system is not None:
            if system.get('memory',None):
                counters.append(count)
        count = count +1
    if len(counters) == 0:
        print('No dict with the key and value combination found')
    return counters

#------------------------------------------------------------------------------

# This function gets index of list containing cpu
def getkeycpu(i_hits):
    # pprint(i_hits)
    count = 0
    counters = []
    for i in i_hits:
        system = i['_source'].get('system', None)
        if system is not None:
            if system.get('cpu',None):
                counters.append(count)
        count = count +1
    if len(counters) == 0:
        print('No dict with the key and value combination found')
    return counters

#--------------------------------------------------------------------------------------

# This function gets index of list containing filesystem
def getkeyfilesystem(i_hits):
    count = 0
    counters = []
    for i in i_hits:
        system = i['_source'].get('system', None)
        if system is not None:
            if system.get('filesystem',None):
                system1=system['filesystem']
                if system1.get('device_name',None) == 'rootfs':
                    counters.append(count)
        count = count +1
    if len(counters) == 0:
        print('No dict with the key and value combination found')
    return counters

#---------------------------------------------------------------------------------------

# Function to send alerts
def send_mail(danger_hosts):
    with open('mailconf.json') as f:
        data = f.read()
    data = json.loads(data)
    gmail = data['gmail']
    host = gmail['host']
    user = gmail['user']
    password = gmail['password']
    port = gmail['port']
    s = smtplib.SMTP(host, port)
    s.starttls()
    s.login(user, password)

    # Add mail ids in list format to whom alert mail should be sent
    TO = ['mailID1']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alert"
    msg['From'] = user
    msg['To'] = ', '.join(TO)

    # Create the body of the message (a plain-text and an HTML version).
    text = "System Alert"

    html = ["<html><body>"]

    # ------------Table for Mem Alert------------------
    if danger_hosts['mem_hostname'] != []:
        html.append("<b>Memory Alert </b><table border=1>")
        html.append("<th>Hostname</th><th>Percentage</th>")
        for i in range(0, len(danger_hosts['mem_hostname'])):
            html.append("<tr><td> {0} </td><td>{1}</td></tr>".format(str(danger_hosts['mem_hostname'][i]) , str(danger_hosts['mem_percentage'][i])))

        html.append("</table><br><br>")

    # ------------Table for Cpu Alert------------------
    if danger_hosts['cpu_hostname'] != []:
        html.append("<b>CPU Alert</b><table border=1>")
        html.append("<th>Hostname</th><th>Percentage</th>")
        for i in range(0, len(danger_hosts['cpu_hostname'])):
            html.append("<tr><td> {0} </td><td>{1}</td><tr>".format(str(danger_hosts['cpu_hostname'][i]) , str(danger_hosts['cpu_percentage'][i])))
        html.append("</table><br><br>")

    # ------------Table for Disk Alert------------------
    if danger_hosts['disk_hostname'] != []:
        html.append("<b>Disk Alert</b><table border=1>")
        html.append("<th>Hostname</th><th>Percentage</th>")
        for i in range(0, len(danger_hosts['disk_hostname'])):
            html.append("<tr><td> {0} </td><td>{1}</td><tr>".format(str(danger_hosts['disk_hostname'][i]) , str(danger_hosts['disk_percentage'][i])))
        html.append("</table>")

    else:
        pass
    html.append("</body></html>")

    html = ''.join(html)
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    ret_code = s.sendmail(user, TO, msg.as_string())

    return ret_code
