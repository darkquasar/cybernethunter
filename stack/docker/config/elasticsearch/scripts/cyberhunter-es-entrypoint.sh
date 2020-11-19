#!/bin/bash

# Author: Diego Perez (@darkquasar)
# License: GPL-3.0
# StreamHunter Version: 0.0.2
# Elastic Stack Version: 7.3
# Description: Docker entrypoint to configure Elasticsearch container

# *** Configure ES Node's TLS*** #
# On how to generate the p12 cert: https://www.elastic.co/guide/en/elasticsearch/reference/7.x/configuring-tls.html
# File was previously mounted in docker-compose.yml
# It could also be dynamically re-created with the container using elasticsearch-certuil
cp /usr/share/elasticsearch/config/certs/elastic-certificates.p12 /usr/share/elasticsearch/config/

# *** Pass execution to regular entrypoint *** #
/usr/local/bin/docker-entrypoint.sh