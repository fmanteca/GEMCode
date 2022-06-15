# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2bis.py --filein file:step3.root --fileout file:step2bis.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic --step L1 --geometry DB:Extended --era Run3 --python_filename step2bis_L1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

options = VarParsing('analysis')
options.register ("test", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runOnData", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runOnRaw", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runAna", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("run3", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("crab", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("ShowerSource", 0, VarParsing.multiplicity.singleton, VarParsing.varType.int)
options.parseArguments()

process_era = Run3
if not options.run3:
      process_era = Run2_2018

process = cms.Process("ReL1", process_era)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('GEMCode.GEMValidation.MuonNtuplizer_cff')

nEvents = -1
if options.test:
    nEvents = 100

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nEvents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source(
      "PoolSource",
      fileNames = cms.untracked.vstring(
            #"file:/uscms/home/menendez/nobackup/Trigger/Data/28BC606A-86A3-E811-A897-02163E00B16E.root"
            #"file:/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_12_0_0_pre2/src/132B0128-FF59-DB4A-A3AD-AF4D8B4D21D2.root"
            "file:/eos/uscms/store/data/Run2018D/EphemeralZeroBias2/RAW/v1/000/320/673/00000/06B5F1BD-5695-E811-B52D-FA163EADBDBF.root"
            #"/store/user/nimenend/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/200710_130547/0000/step2_1.root"
    ),
    secondaryFileNames = cms.untracked.vstring(),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2bis.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule(
      "PoolOutputModule",
      dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-DIGI-L1'),
            filterName = cms.untracked.string('')
      ),
      fileName = cms.untracked.string('file:step2bis_run3.root'),
      outputCommands = cms.untracked.vstring('keep *'),
      splitLevel = cms.untracked.int32(0)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana_muonshower.root")
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
if options.runOnData:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
else:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

from GEMCode.GEMValidation.cscTriggerCustoms import runOn110XMC, runOn110XMC_IgnoreIncorrectGEMDB
if options.runOnRaw:
    process = runOn110XMC_IgnoreIncorrectGEMDB(process, options.crab)

from GEMCode.GEMValidation.sampleProductionCustoms import dropNonMuonCollections
process = dropNonMuonCollections(process)

# the analyzer configuration
ana = process.MuonNtuplizer
ana.verbose = 1
if options.runOnData:
      ana.runSim = False
      ana.useGEMs = False
ana.genParticle.pdgIds = cms.vint32(6000113, -6000113, 9000006, -9000006, 9000007, -9000007)
ana.genParticle.stableParticle = False
ana.genParticle.verbose = 0
ana.simTrack.minEta = 0.9
ana.simTrack.maxEta = 2.4
ana.simTrack.minPt = 5
#ana.simTrack.verbose = 1
ana.simTrack.pdgIds = cms.vint32(6000113, -6000113, 9000006, -9000006, 9000007, -9000007)
ana.cscSimHit.simMuOnly = False
ana.cscSimHit.discardEleHits = False
ana.gemStripDigi.matchDeltaStrip = 2
ana.gemStripDigi.matchToSimLink = False

ana.gemStripDigi.run = False
ana.gemPadDigi.run = False
ana.gemPadCluster.run = False
ana.gemCoPadDigi.run = False

ana.cscLCT.addGhostLCTs = cms.bool(True)
ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","ReL1")
ana.cscShower.verbose = 1
ana.emtfShower.verbose = 1
ana.muonShower.verbose = 1
## turn off GEM

if options.runOnRaw:
      process.simCscTriggerPrimitiveDigis.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
      process.simCscTriggerPrimitiveDigis.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"
      #process.simCscTriggerPrimitiveDigisCath.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
      #process.simCscTriggerPrimitiveDigisCath.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"
      #process.simCscTriggerPrimitiveDigisAnod.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
      #process.simCscTriggerPrimitiveDigisAnod.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"
      ana.gemStripDigi.inputTag = "muonGEMDigis"
      ana.cscStripDigi.inputTag = "muonCSCDigis:MuonCSCStripDigi"
      ana.cscWireDigi.inputTag = "muonCSCDigis:MuonCSCWireDigi"
      ana.cscComparatorDigi.inputTag = "muonCSCDigis:MuonCSCComparatorDigi"
      #ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

process.MuonNtuplizerCath = process.MuonNtuplizer.clone()
anaCath = process.MuonNtuplizerCath
anaCath.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisCath","","ReL1")
anaCath.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisCath","","ReL1")
anaCath.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisCath","","ReL1")
anaCath.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisCath","MPCSORTED","ReL1")
anaCath.cscShower.inputTag = "simCscTriggerPrimitiveDigisCath"
anaCath.emtfShower.inputTag = cms.InputTag("simEmtfShowersCath","EMTF")
anaCath.muonShower.inputTag = "simGmtShowerDigisCath"
process.MuonNtuplizerAnod = process.MuonNtuplizer.clone()
anaAnod = process.MuonNtuplizerAnod
anaAnod.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisAnod","","ReL1")
anaAnod.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisAnod","","ReL1")
anaAnod.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisAnod","","ReL1")
anaAnod.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisAnod","MPCSORTED","ReL1")
anaAnod.cscShower.inputTag = "simCscTriggerPrimitiveDigisAnod"
anaAnod.emtfShower.inputTag = "simEmtfShowersAnod:EMTF"
anaAnod.muonShower.inputTag = "simGmtShowerDigisAnod"

## customize unpacker
process.SimL1Emulator = cms.Sequence(process.SimL1TMuonTask)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
if not options.run3:
      process.raw2digi_step = cms.Path(process.muonCSCDigis)


process.simCscTriggerPrimitiveDigis.commonParam.runME11ILT =False
process.simCscTriggerPrimitiveDigisCath = process.simCscTriggerPrimitiveDigis.clone()
process.simCscTriggerPrimitiveDigisAnod = process.simCscTriggerPrimitiveDigis.clone()
process.simCscTriggerPrimitiveDigis.showerParam.source =2
process.simCscTriggerPrimitiveDigisCath.showerParam.source =0
process.simCscTriggerPrimitiveDigisAnod.showerParam.source =1
process.simEmtfShowersCath = process.simEmtfShowers.clone()
process.simEmtfShowersCath.CSCShowerInput = cms.InputTag(
	'simCscTriggerPrimitiveDigisCath')
process.simEmtfShowersAnod = process.simEmtfShowers.clone()
process.simEmtfShowersAnod.CSCShowerInput = cms.InputTag(
	'simCscTriggerPrimitiveDigisAnod')
process.simGmtShowerDigisCath = process.simGmtShowerDigis.clone()
process.simGmtShowerDigisCath.showerInput = cms.InputTag(
	'simEmtfShowersCath','EMTF')
process.simGmtShowerDigisAnod = process.simGmtShowerDigis.clone()
process.simGmtShowerDigisAnod.showerInput = cms.InputTag(
	'simEmtfShowersAnod','EMTF')
process.L1simulation_step = cms.Path(
      process.simCscTriggerPrimitiveDigis *
      process.simCscTriggerPrimitiveDigisCath *
      process.simCscTriggerPrimitiveDigisAnod *
      process.simEmtfShowers *
      process.simEmtfShowersCath *
      process.simEmtfShowersAnod *
      process.simGmtShowerDigis *
      process.simGmtShowerDigisCath *
      process.simGmtShowerDigisAnod
)
process.ana_step = cms.Path(process.MuonNtuplizer)
process.ana_step_cath = cms.Path(process.MuonNtuplizerCath)
process.ana_step_anod = cms.Path(process.MuonNtuplizerAnod)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule()
## unpack
if options.runOnRaw:
    process.schedule.extend([process.raw2digi_step])

## l1
process.schedule.extend([process.L1simulation_step])

## analysis
if options.runAna:
    process.schedule.extend([process.ana_step])
    process.schedule.extend([process.ana_step_cath])
    process.schedule.extend([process.ana_step_anod])


## endjob
process.schedule.extend([process.endjob_step])

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
