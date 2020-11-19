# TODO
1. Run docker container (elastic) and export certs in PEM format not PK12 as it is not CURL friendly
2. Change Elasticsearch container config to match the use of PEM
3. Create new Docker image containing: stoQ + RITA (with no Zeek, only to be able to pass in pcaps and get some crunched data in return) + evtx2es + blazescan