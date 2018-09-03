<h2> Metric Alerting System </h2>
<h3>metric-alerting.py - Main script</h3>
<h3>config.py - Endpoint url</h3>
<h3>globals.py - contains global declarations</h3>
<h3>helpers.py - contains functions</h3>
<h3>mailconf.json - contains mailing details</h3>
<br>
<br>
<h3>To configure mail</h3>
-- In **mailconf.json** <br>
    1.) Add mail id through which you wish to send mail.<br>
    2.) Add Password og the above mentioned mail id.<br>
<br>
<br>
-- In **helpers.py**<br>
    - In function **send_mail()**<br>
        1.) add mail ids to whom mail should be sent in list named **TO = ['mail ID']**<br> 


-> Install the requirements using pip3        
<br>
-> activate virtualenv
<br>
-- $ source env/bin/activate

Run python3 metric_alerting.py
