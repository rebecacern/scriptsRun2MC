#!/bin/csh
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_THISJOB/
eval `scram runtime -csh`
cd -
cp -r /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/MCFM-7.0 .
chmod 755 MCFM-7.0
cd MCFM-7.0/Bin
rm *.lhe
rm *.top
rm *.C
cp input.TEMPLATE input.DAT
sed -i 's~NEVENTS~EVENTSPERJOB~g' input.DAT
sed -i 's~JOBNUMBER~THISJOB~g' input.DAT
sed -i 's~PROCESS~THISPROCESS~g' input.DAT
sed -i 's~WIDTH~ANOMWIDTH~g' input.DAT
setenv LD_LIBRARY_PATH {$LD_LIBRARY_PATH}:/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms/lib
./mcfm
sleep 10
setenv lhefile `ls *.lhe`
echo $lhefile
cmsStage $lhefile EOSDIR
