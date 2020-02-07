# PCRF-Stats
By default, Cisco Policy Suite (CPS) outputs a bulk statistics CSV file to the /var/broadhop/stats/ directory 
on pcrfclient01 and pcrfclient02 VMs in five-minute intervals. These CSV files include all statistics collected 
from all VMs during the five-minute. CPS retains each bulk statistic CSV file on the pcrfclient01/02 VM for 2 days

The following list is a sample of a file name created in the /var/broadhop/stats/ directory on the pcrfclient01 VM.
				[root@pcrfclient01 stats]# pwd
				/var/broadhop/stats
				[root@pcrfclient01 stats]# ls
				bulk-pcrfclient01-201510131350.csv
        
This information is available on internet with further details, for example in 
[CPS 19.2.0 Operations Guide](https://www.cisco.com/c/en/us/td/docs/wireless/quantum-policy-suite/R19-2-0/CPS19-2-0OperationsGuide/CPS18-1-0OperationsGuide_chapter_01000.html)

The purpose of this script is to extract the desired information from a bulk statistics CSV file and print in fancy table. Here is partial output from the script when string varible st2 is set to 'AAR'

![image](https://user-images.githubusercontent.com/47313728/74006158-a9d7bc80-492f-11ea-93fe-2b8a64a6620f.png)
