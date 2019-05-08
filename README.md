# gpu_accounting

This script uses the NVidia API to track the usage of GPU's in a SLURM system.  It should be run as a SLURM epilog.
It uses the Python on the current path and expects to have the MySQL and NVidia utils available.
The configuration file should be set up with the correct SLURM database information and placed in /etc.

When it is running, users, admins, and scripts can find the GPU data with the command

```sacct -o AdminComment```

The gpu2csv script will convert sacct data to a CSV for easier processing.

```
$ gpu2csv --help
usage: gpu2csv [-h] [-s STARTDATE] [-i]

View Slurm GPU data

optional arguments:
  -h, --help            show this help message and exit
  -s STARTDATE, --startdate STARTDATE
                        The Start Date - format YYYY-MM-DD
  -i, --stdin           Use stdin for input instead of calling sacct
$ gpu2csv
user,jobid,pid,time,gpuUtilization,serial,maxMemoryUsage,memoryUtilization
steige,918,406341,21493,38,0323818055423,657.0,0
steige,918,406041,274671,35,0323818055423,15511.0,0
steige,918,406612,369965,33,0323818055423,15511.0,0
$ gpu2csv --startdate 2019-05-06
user,jobid,pid,time,gpuUtilization,serial,maxMemoryUsage,memoryUtilization
tjo,906,214376,210856,0,0424218019550,463.0,0
tjo,906,19919,210868,0,0424218019550,0.0,0
steige,915,345135,1009018,59,0323818055423,15629.0,5
steige,915,346244,1128679,27,0323818055423,15599.0,8
steige,915,349860,1496995,97,0323818055423,15599.0,27
```
