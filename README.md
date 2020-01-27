# PCRF-Stats
By default, Cisco Policy Suite (CPS) outputs a bulk statistics CSV file to the /var/broadhop/stats/ directory 
on pcrfclient01 and pcrfclient02 VMs in five-minute intervals. These CSV files include all statistics collected 
from all VMs during the five-minute. CPS retains each bulk statistic CSV file on the pcrfclient01/02 VM for 2 days

The following list is a sample of a file name created in the /var/broadhop/stats/ directory on the pcrfclient01 VM.
				[root@pcrfclient01 stats]# pwd
				/var/broadhop/stats
				[root@pcrfclient01 stats]# ls
				bulk-pcrfclient01-201510131350.csv
        
This information is available on internet with further details, for example in CPS 19.2.0 Operations Guide @ 
https://www.cisco.com/c/en/us/td/docs/wireless/quantum-policy-suite/R19-2-0/CPS19-2-0OperationsGuide/CPS18-1-0OperationsGuide_chapter_01000.html

The purpose of this script is to extract the desired information from a bulk statistics CSV file and print in fancy (doesn't look in this view unless in the edit mode) table
Here is partial output from the script when string varible st2 is set to 'AAR' 

╒══════╤════════════════════════════════════════════════════╤══════╕
│Server│ KPI                                                │value │
╞══════╪════════════════════════════════════════════════════╪══════╡
│ pd01 │ node2.messages.e2e_IMS_Rx_AAR_2001.qns_stat.success│73369 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd01 │ node2.messages.e2e_Rx_AAR_5065.qns_stat.success    │   18 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd01 │ node4.messages.e2e_IMS_Rx_AAR_2001.qns_stat.success│72999 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd01 │ node4.messages.e2e_Rx_AAR_5065.qns_stat.success    │   12 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node2.messages.e2e_IMS_Rx_AAR_2001.qns_stat.success│73221 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node2.messages.e2e_Rx_AAR_5065.qns_stat.success    │   12 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node3.messages.e2e_IMS_Rx_AAR_2001.qns_stat.success│72793 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node3.messages.e2e_Rx_AAR_5065.qns_stat.success    │   11 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node4.messages.e2e_IMS_Rx_AAR_2001.qns_stat.success│72983 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ pd02 │ node4.messages.e2e_Rx_AAR_5065.qns_stat.success    │   13 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps01 │ node1.counters.Rx_AAR.qns_count                    │54653 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps01 │ node1.messages.diameter_Rx_AAR.qns_stat.success    │54653 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps01 │ node1.messages.in_q_Rx_AAR.qns_stat.success        │54653 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps02 │ node1.counters.Rx_AAR.qns_count                    │54625 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps02 │ node1.messages.diameter_Rx_AAR.qns_stat.success    │54625 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps02 │ node1.messages.in_q_Rx_AAR.qns_stat.success        │54625 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps04 │ node1.counters.Rx_AAR.qns_count                    │54911 │
├──────┼────────────────────────────────────────────────────┼──────┤
│ ps04 │ node1.messages.diameter_Rx_AAR.qns_stat.success    │54911 │
