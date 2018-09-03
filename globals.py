from config import CONFIG_URL

url = CONFIG_URL

payload = """{\"index\":[\"metricbeat-*\"],\"ignore_unavailable\":true,\"preference\":1528443186620}\n{\"version\":true,\"size\":500,\"sort\":[{\"system.process.cpu.start_time\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"system.process.cpu.start_time\",\"interval\":\"30s\",\"time_zone\":\"Asia/Kolkata\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[\"@timestamp\",\"ceph.monitor_health.last_updated\",\"docker.container.created\",\"docker.healthcheck.event.end_date\",\"docker.healthcheck.event.start_date\",\"docker.image.created\",\"kubernetes.container.start_time\",\"kubernetes.event.metadata.timestamp.created\",\"kubernetes.node.start_time\",\"kubernetes.pod.start_time\",\"kubernetes.system.start_time\",\"mongodb.status.background_flushing.last_finished\",\"mongodb.status.local_time\",\"php_fpm.pool.start_time\",\"postgresql.activity.backend_start\",\"postgresql.activity.query_start\",\"postgresql.activity.state_change\",\"postgresql.activity.transaction_start\",\"postgresql.bgwriter.stats_reset\",\"postgresql.database.stats_reset\",\"system.process.cpu.start_time\"],\"query\":{\"bool\":{\"must\":[{\"match_all\":{}},{\"range\":{\"system.process.cpu.start_time\":{\"gte\":1528442289971,\"lte\":1528443189971,\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\n"""

headers = {
    'accept': "application/json, text/plain, */*",
    'origin': "http://18.188.186.25:5601",
    'kbn-version': "6.2.4",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
    'content-type': "application/x-ndjson",
    'referer': "http://18.188.186.25:5601/app/kibana",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'cache-control': "no-cache",
    "Authorization" : "Basic c21va2U6aW5ub3ZhY2NlcjEyMw=="
    }

docvalue_fields = """["@timestamp","ceph.monitor_health.last_updated","docker.container.created","docker.healthcheck.event.end_date","docker.healthcheck.event.start_date","docker.image.created","kubernetes.container.start_time","kubernetes.event.metadata.timestamp.created","kubernetes.node.start_time","kubernetes.pod.start_time","kubernetes.system.start_time","mongodb.status.background_flushing.last_finished","mongodb.status.local_time","php_fpm.pool.start_time","postgresql.activity.backend_start","postgresql.activity.query_start","postgresql.activity.state_change","postgresql.activity.transaction_start","postgresql.bgwriter.stats_reset","postgresql.database.stats_reset","system.process.cpu.start_time"]"""
