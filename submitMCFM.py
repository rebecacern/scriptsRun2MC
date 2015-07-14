import os, commands, time

ch = '2l'
process = '61.ENMN'
outdir = 'submission_MCFM_ggWW_'+ch+'_July14'
csh_template = 'templateMCFM.csh'
neventsper =2000
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

    if (job>1): continue
    
    os.system('mkdir job_'+str(job))
    os.chdir('job_'+str(job))

    str_job = str(job)
    csh_job = csh_template.replace('templateMCFM','jobLHE_'+str(job))

    output = processCmd('cp ../../'+csh_template+' '+csh_job)
    output = processCmd("sed -i 's~OUTDIR~"+outdir+"~g' "+csh_job)
    output = processCmd("sed -i 's~EVENTSPERJOB~"+str(neventsper)+"~g' "+csh_job)
    output = processCmd("sed -i 's~THISJOB~"+str(job)+"~g' "+csh_job)
    output = processCmd("sed -i 's~THISPROCESS~"+str(process)+"~g' "+csh_job)

    if (str(process).startswith("132")):
        output = processCmd("sed -i 's~ANOMWIDTH~1.0d0~g' "+csh_job)
    else:
        output = processCmd("sed -i 's~ANOMWIDTH~0.9771908764d0~g' "+csh_job)

    print 'submitting job',str(job)

    cmd = 'bsub -q 8nh '+csh_job
   
    

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
