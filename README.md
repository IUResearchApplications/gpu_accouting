# gpu_accounting

This script uses the NVidia API to track the usage of GPU's in a SLURM system.  It should be run as a SLURM epilog.
It uses the Python on the current path and expects to have the MySQL and NVidia utils available.
The configuration file should be set up with the correct SLURM database information and placed in /etc.

When it is running, users, admins, and scripts can find the GPU data with the command

```sacct -o AdminComment```
