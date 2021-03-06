from WMCore.Configuration import Configuration
name = 'WWW'
steam_dir = 'xulyu'

config = Configuration()
config.section_("General")
config.General.requestName   = 'M2500_R0-5_off_pri'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFchs.txt','Summer16_07Aug2017_V11_MC_L2Relative_AK4PFchs.txt','Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFchs.txt','Summer16_07Aug2017_V11_MC_L1FastJet_AK8PFchs.txt','Summer16_07Aug2017_V11_MC_L2Relative_AK8PFchs.txt','Summer16_07Aug2017_V11_MC_L3Absolute_AK8PFchs.txt','Summer16_07Aug2017_V11_MC_L1FastJet_AK8PFPuppi.txt','Summer16_07Aug2017_V11_MC_L2Relative_AK8PFPuppi.txt','Summer16_07Aug2017_V11_MC_L3Absolute_AK8PFPuppi.txt','Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFPuppi.txt','Summer16_07Aug2017_V11_MC_L2Relative_AK4PFPuppi.txt','Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFPuppi.txt','L1PrefiringMaps_new.root']
#config.JobType.inputFiles = ['PHYS14_25_V2_All_L1FastJet_AK4PFchs.txt','PHYS14_25_V2_All_L2Relative_AK4PFchs.txt','PHYS14_25_V2_All_L3Absolute_AK4PFchs.txt','PHYS14_25_V2_All_L1FastJet_AK8PFchs.txt','PHYS14_25_V2_All_L2Relative_AK8PFchs.txt','PHYS14_25_V2_All_L3Absolute_AK8PFchs.txt']
# Name of the CMSSW configuration file
#config.JobType.psetName    = 'bkg_ana.py'
config.JobType.psetName    = 'analysis.py'
#config.JobType.allowUndistributedCMSSW = True
config.JobType.sendExternalFolder = True
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.inputDataset = '/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/VVV_herwig_1500_05_miniaod/qiguo-crab_VVV_herwig_MiniAOD_1500-05_x32Q45_v3f-2_userf-05265a4e675f881e1e171fd06785811b/USER'
config.Data.userInputFiles =[
'/store/user/qiguo/crab/herwig/VVV_herwig_2500_05_miniaod/crab_VVV_herwig_MiniAOD_2500-05_x32Q45_v3f-2_userf/191201_073600/0000/B2G-RunIISummer16MiniAODv2-02570_1.root',
'/store/user/qiguo/crab/herwig/VVV_herwig_2500_05_miniaod/crab_VVV_herwig_MiniAOD_2500-05_x32Q45_v3f-2_userf/191201_073600/0000/B2G-RunIISummer16MiniAODv2-02570_2.root',
'/store/user/qiguo/crab/herwig/VVV_herwig_2500_05_miniaod/crab_VVV_herwig_MiniAOD_2500-05_x32Q45_v3f-2_userf/191201_073600/0000/B2G-RunIISummer16MiniAODv2-02570_3.root'
]
#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob =50
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outLFNDirBase = '/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/STEAM/' + steam_dir + '/' + name + '/'
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'M2500_R0-5_off_pri'


config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
