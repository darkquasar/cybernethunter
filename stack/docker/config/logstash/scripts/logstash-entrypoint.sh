#!/bin/bash
# Install Plugins Not in the Standard Bundle
 logstash-plugin install logstash-filter-alter && logstash-plugin install logstash-codec-gzip_lines && logstash-plugin install logstash-filter-i18n && logstash-plugin install logstash-filter-environment && logstash-plugin install logstash-input-wmi

# Logstash Docker Entrypoint
/usr/local/bin/docker-entrypoint
