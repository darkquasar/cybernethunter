# CyberNetHunter

## Purpose
CyberNetHunter is a cyber tool stack for the Incident Responder and Threat Hunter. The aim is to integrate tightly with Jupyter Notebooks and facilitate regular tasks that can be tedious during Incidents. The stack aims to include:

1. A python package (`cybrhunter`) that can be also used from the commandline
2. A few docker stacks to complement regular analysis requirements (elk, BlueSpawn, SysmonSearch, Stoq, etc.)
3. Powershell scripts that can be called from Jupyter to execute triage and analysis tasks in Active Directory environments
4. Streaming via benthos and kafka for data enrichment

# TODO

1. Add [BlueSpawn](https://github.com/ION28/BLUESPAWN/tree/master/BLUESPAWN-win-client?s=09)
2. Create Jupyter Notebooks with analysis of [Boss of the SOC](https://botes.gitbook.io/botes-dataset/) dataset
3. Add [SysmonSearch](https://blogs.jpcert.or.jp/en/2020/04/sysmonsearch-v20-released.html) from JPCert to CyBrElastic
