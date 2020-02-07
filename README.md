# PCRF-Stats
By default, Cisco Policy Suite (CPS) outputs a bulk statistics CSV file to the /var/broadhop/stats/ directory 
on pcrfclient01 and pcrfclient02 VMs in five-minute intervals. These CSV files include all statistics collected 
from all VMs during the five-minute. CPS retains each bulk statistic CSV file on the pcrfclient01/02 VM for 2 days

The following is an example of a file name created in the /var/broadhop/stats/ directory on the pcrfclient01 VM.

![image](https://user-images.githubusercontent.com/47313728/74007041-3aaf9780-4932-11ea-9ad4-db69bdfc45d3.png)
        
This information is available on internet with further details, for example in 
[CPS 19.2.0 Operations Guide](https://www.cisco.com/c/en/us/td/docs/wireless/quantum-policy-suite/R19-2-0/CPS19-2-0OperationsGuide/CPS18-1-0OperationsGuide_chapter_01000.html)

The purpose of this script is to extract the desired information from a bulk statistics CSV file and print in fancy table and/or create CSV file for the desired KPI. Here is partial output from the script when string varible st2 is set to 'AAR'

![image](https://user-images.githubusercontent.com/47313728/74006158-a9d7bc80-492f-11ea-93fe-2b8a64a6620f.png) 
![image](https://user-images.githubusercontent.com/47313728/74008720-6d5b8f00-4936-11ea-9e3f-af3757ae8ca9.png)
