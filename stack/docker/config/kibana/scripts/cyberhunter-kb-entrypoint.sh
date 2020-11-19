#!/bin/bash

# Author: Diego Perez (@darkquasar)
# License: GPL-3.0
# StreamHunter Version: 0.0.2
# Elastic Stack Version: 7.3
# Description: Docker entrypoint to configure Elasticsearch container

# *** Configure KB Node's TLS *** #
# ******************************* #

# *** Configure KB Node's Passwords *** #
# ************************************* #

# *** Setting kibana User Password ***
until [[(curl -o /dev/null --insecure -w "{%http_code}" -u elastic:$ELASTIC_PASSWORD -H 'Content-Type:application/json' -XPUT https://cyberhunt-elasticsearch:9200/_security/user/kibana/_password?pretty -d'
  {
    "password": "$ELASTICSEARCH_PASSWORD"
  }
  ') == "200"]]; do 
  echo "Attempting to change Kibana Password. Elasticsearch not ready yet. Sleeping for 3s"
  sleep 3
done

# *** Setting logstash_System User Password ***
until [[(curl -o /dev/null --insecure -w "{%http_code}" -u elastic:$ELASTIC_PASSWORD -H 'Content-Type:application/json' -XPUT https://cyberhunt-elasticsearch:9200/_security/user/logstash_system/_password -d "{\"password\": \"$LOGSTASH_PASSWORD\"}") == "200"]]; do 
  echo "Attempting to change Kibana Password. Elasticsearch not ready yet. Sleeping for 3s"
  sleep 3
done


# *** Pass execution to regular entrypoint *** #
exec /usr/local/bin/kibana-docker