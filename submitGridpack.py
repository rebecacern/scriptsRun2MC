import os, commands, time

csh_template = 'templateGridpack.csh'

mass = "130"
outdir = "submission_gridpack_test_v2_"+mass+"_July6"
model = 'ggHZ'
#powinput = "/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/ggHZ_HanythingJ_Zanything_NNPDF30_13TeV/ggHZ_HanythingJ_Zanything_NNPDF30_13TeV_M"+mass+".input"
powinput = "/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/VH_from_Hbb/ggHZ_HanythingJ_NNPDF30_13TeV_M125_Vleptonic.input"
tarball = 'ggHZ_HanythingJ_TEST_NNPDF30_13TeV_'+mass
jhuinput = 'none'

nevents = '100'
njobs = 1

if (not os.path.exists(outdir)):
    os.system('mkdir '+outdir)

startDir = os.getcwd()
os.chdir(outdir)

def processCmd(cmd, quite = 0):
    #    print cmd                                                                                                                                               
    status, output = commands.getstatusoutput(cmd)
    if (status !=0 and not quite):
        print 'Error in processing command:\n   ['+cmd+']'
        print 'Output:\n   ['+output+'] \n'
    return output

for job in range(1,njobs+1):

    os.system('mkdir job_'+str(job))
    os.chdir('job_'+str(job))

    str_job = str(job)
    csh_job = csh_template.replace('templateGridpack','jobGridpack_'+str(job))

    output = processCmd('cp ../../'+csh_template+' '+csh_job)
    output = processCmd("sed -i 's~OUTDIR~"+outdir+"~g' "+csh_job)
    output = processCmd("sed -i 's~JOBNUMBER~"+str(job)+"~g' "+csh_job)
    output = processCmd("sed -i 's~MODEL~"+str(model)+"~g' "+csh_job)
    output = processCmd("sed -i 's~TARBALL~"+str(tarball)+"~g' "+csh_job)
    output = processCmd("sed -i 's~POWHEGINPUT~"+str(powinput)+"~g' "+csh_job)
    output = processCmd("sed -i 's~JHUGEN~"+str(jhuinput)+"~g' "+csh_job)
    output = processCmd("sed -i 's~NEVENTS~"+str(nevents)+"~g' "+csh_job)
    output = processCmd("sed -i 's~SEED~10"+str(job)+"~g' "+csh_job)

    print 'submitting job',str(job)
    cmd = 'bsub -q 1nd '+csh_job
 
    output = processCmd(cmd)
    while ('error' in output):
        print 'unable to submit...'
        time.sleep(1.0);
        output = processCmd(cmd)
        if ('error' not in output):
            print output
            print 'Submitting after retry - job '+str(job)
    print output

    os.chdir(startDir+'/'+outdir)

os.chdir(startDir)

