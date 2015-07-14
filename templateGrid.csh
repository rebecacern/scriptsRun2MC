#!/bin/csh                  
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/
eval `scram runtime -csh`
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/tmp/
./runcmsgrid.sh 150000 12312 1 
