#!/bin/csh                  
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/
eval `scram runtime -csh`
cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/*.sh .
cp -r /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/patches/ .
./create_powheg_tarball.sh slc6_amd64_gcc481/powheg/V2.0/src powhegboxV2_May2015 MODEL POWHEGINPUT TARBALL JHUGEN NEVENTS SEED
ls -d powhegboxV2_May2015/work/POWHEG-BOX/*/ | grep -v "MODEL" | xargs rm -r
