print "#----------------------------------- Creating testQ1 ------------------------------------------------"
echoMessage="Saving to master repository..."
print echoMessage
print '.' * (70 - len(echoMessage)),
print '[ DONE ]'
scopeID = AdminConfig.getid('/Cell:PSCell1')

queues = AdminConfig.list('MQQueue',cellId).splitlines()
connectionFactories = AdminConfig.list( 'MQQueueConnectionFactory', cellId ).splitlines()
activationSpecs =  AdminConfig.list( 'J2CActivationSpec', cellId ).splitlines()

# ------------------------------------------------------
# QUEUE JNDI CREATION
#mqqAttrs = '-name Export_test1_1_RQO -jndiName jms\Export_test1_1_RQO -queueName TEST.1.1.RQO '
#mqqAttrs += '-customProperties [[MDREAD YES] [MDMSGCTX SET_ALL_CONTEXT] [MSGBODY MQ] [MDWRITE YES]]'
 for qid in AdminConfig.list( 'MQQueue', scopeID ).splitlines() :
    if AdminConfig.showAttribute( qid, 'name' ) == qname and isSkipIfExist == False:
	AdminTask.deleteWMQConnectionFactory()
	
#if AdminTask.createWMQQueue( scopeID, mqqAttrs ) :
#	print '\ncreateMQ: SUCCESS ---Created the Queue JNDI "jms\Export_test1_1_RQO" at specified scope'
#else :
#	print '\ncreateMQ: ERROR --- Unable to create the Queue "jms\Export_test1_1_RQO" at specifie scope. Check the logs for more information.'

#AdminConfig.save() 
# -------------------------------------------------------
# QCF Creation
#qcfAttrs = '-type QCF -name test_qcf -jndiName jndi\\test_qcf -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
#qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
#qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
#if AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs ) :
#	print '\ncreateCF: SUCCESS ---Created the QCF "jndi\\test_qcf" at specified scope' 
#else :
#      	print '\ncreateCF: ERROR --- Unable to create the QCF "jndi\\test_qcf" at specifie scope. Check the logs for more information.'
#AdminConfig.save()  

#--------------------------------------------------------


asAttrs = '-name test_as -jndiName jms/test_as -destinationJndiName jms\Export_test1_1_RQO  -destinationType javax.jms.Queue -qmgrName MQ1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTE.DEF.SVRCONN '
asAttrs += '-stopEndpointIfDeliveryFails false '
asAttrs += '-customProperties [[useJNDI true][maxPoolDepth 3]]'

AdminTask.deleteWMQQueue(scopeID)

if AdminTask.createWMQActivationSpec( scopeID, asAttrs ) :
	print '\ncreateMQ: SUCCESS ---Created the Actication Spec "jms/test_as" at specified scope'
else :
	print '\ncreateMQ: ERROR --- Unable to create the Queue %s at specifie scope. Check the logs for more information.' 

AdminConfig.save() 

#---------------------------------------------------------  
"""
def createMQ( scopeID, name, roles ) :
  if len( roles ) != 3 :
    print '\ncreateMQ: ERROR --- Unexpected roles specified:', roles
    return 1

  mqqAttrs = '-name %(name)s -jndiName %(qjndiname)s -queueName %(qname)s -qmgr %(qManager)s '
  mqqAttrs += '-customProperties [[MDREAD YES] [MDMSGCTX SET_ALL_CONTEXT] [MSGBODY MQ] [MDWRITE YES]]'

  for qid in AdminConfig.list( 'MQQueue', scopeID ).splitlines() :
    if AdminConfig.showAttribute( qid, 'name' ) == qname :
      print '\ncreateMQ: INFO --- MQ Queue %s is already configured at specified scope. Skipping the MQ Queue creation.' % qname
      print '-' * 50
      print 'ConfigID:', qid
      print AdminConfig.show( qid )
      print '-' * 50
      return 1
  else :
    attr = mqqAttrs % locals()
    print '\ncreateMQ Debug: AdminTask.createWMQQueue( "%s", "%s" )' % ( scopeID, attr )
    if AdminTask.createWMQQueue( scopeID, attr ) :
      print '\ncreateMQ: SUCCESS ---Created the Queue %s at specified scope' % qname
      return 0
    else :
      print '\ncreateMQ: ERROR --- Unable to create the Queue %s at specifie scope. Check the logs for more information.' % qname
      return 1
      
      
#-------------------------------------------------------------------------------
# Name: createQCF
# Role: Function used to create the specified AS
# Note: Return 0 == Success; 1 == Failure
#-------------------------------------------------------------------------------
def createQCF( scopeID, name, roles ) :
	if len( roles ) != 6 :
    print '\ncreateCF: ERROR --- Unexpected roles specified:', roles
    return 1

  cfjndiname, qManager, wmqtrnprt, mqHostname, mqPort, mqSvrChl = roles

  mqqAttrs = '-type QCF -name %(name)s -jndiName %(cfjndiname)s -qmgrName %(qManager)s -wmqTransportType %(wmqtrnprt)s '
  mqqAttrs += '-qmgrHostname %(mqHostname)s -qmgrPortNumber %(mqPort)s -qmgrSvrconnChannel %(mqSvrChl)s '

  for qid in AdminConfig.list( 'MQQueueConnectionFactory', scopeID ).splitlines() :
    if AdminConfig.showAttribute( qid, 'name' ) == name :
      print '\ncreateAS: INFO --- CF %s is already configured at specified scope. Skipping the AS creation.' % name
      print '-' * 50
      print 'ConfigID:', qid
      print AdminConfig.show( qid )
      print '-' * 50
      return 1
  else :
    attr = mqqAttrs % locals()
    print '\ncreateAS Debug: AdminTask.createWMQConnectionFactory( "%s", "%s" )' % ( scopeID, attr )
    if AdminTask.createWMQConnectionFactory( scopeID, attr ) :
      print '\ncreateCF: SUCCESS ---Created the CF %s at specified scope' % name
      return 0
    else :
      print '\ncreateCF: ERROR --- Unable to create the CF %s at specifie scope. Check the logs for more information.' % name
      return 1
      
      
#-------------------------------------------------------------------------------
# Name: createCF
# Role: Function used to create the specified AS
# Note: Return 0 == Success; 1 == Failure
#-------------------------------------------------------------------------------
def createCF( scopeID, name, roles ) :
	if len( roles ) != 6 :
    print '\ncreateCF: ERROR --- Unexpected roles specified:', roles
    return 1

  cfjndiname, qManager, wmqtrnprt, mqHostname, mqPort, mqSvrChl = roles

  mqqAttrs = '-type CF -name %(name)s -jndiName %(cfjndiname)s -qmgrName %(qManager)s -wmqTransportType %(wmqtrnprt)s '
  mqqAttrs += '-qmgrHostname %(mqHostname)s -qmgrPortNumber %(mqPort)s -qmgrSvrconnChannel %(mqSvrChl)s '

  for qid in AdminConfig.list( 'MQConnectionFactory', scopeID ).splitlines() :
    if AdminConfig.showAttribute( qid, 'name' ) == name :
      print '\ncreateAS: INFO --- CF %s is already configured at specified scope. Skipping the AS creation.' % name
      print '-' * 50
      print 'ConfigID:', qid
      print AdminConfig.show( qid )
      print '-' * 50
      return 1
  else :
    attr = mqqAttrs % locals()
    print '\ncreateAS Debug: AdminTask.createWMQConnectionFactory( "%s", "%s" )' % ( scopeID, attr )
    if AdminTask.createWMQConnectionFactory( scopeID, attr ) :
      print '\ncreateCF: SUCCESS ---Created the CF %s at specified scope' % name
      return 0
    else :
      print '\ncreateCF: ERROR --- Unable to create the CF %s at specifie scope. Check the logs for more information.' % name
      return 1
      
#-------------------------------------------------------------------------------
# Name: createAS
# Role: Function used to create the specified AS
# Note: Return 0 == Success; 1 == Failure
#-------------------------------------------------------------------------------
def createAS( scopeID, name, roles ) :
  if len( roles ) != 7 :
    print '\ncreateAS: ERROR --- Unexpected roles specified:', roles
    return 1

  asjndiname, desjndiname, qManager, wmqtrnprt, mqHostname, mqPort, mqSvrChl = roles

  mqqAttrs = '-name %(name)s -jndiName %(asjndiname)s -destinationJndiName %(desjndiname)s -destinationType javax.jms.Queue -qmgrName %(qManager)s -wmqTransportType %(wmqtrnprt)s '
  mqqAttrs += '-qmgrHostname %(mqHostname)s -qmgrPortNumber %(mqPort)s -qmgrSvrconnChannel %(mqSvrChl)s -stopEndpointIfDeliveryFails false '

  for qid in AdminConfig.list( 'J2CActivationSpec', scopeID ).splitlines() :
    if AdminConfig.showAttribute( qid, 'name' ) == name :
      print '\ncreateAS: INFO --- AS %s is already configured at specified scope. Skipping the AS creation.' % name
      print '-' * 50
      print 'ConfigID:', qid
      print AdminConfig.show( qid )
      print '-' * 50
      return 1
  else :
    attr = mqqAttrs % locals()
    print '\ncreateAS Debug: AdminTask.createWMQActivationSpec( "%s", "%s" )' % ( scopeID, attr )
    if AdminTask.createWMQActivationSpec( scopeID, attr ) :
      print '\ncreateAS: SUCCESS ---Created the AS %s at specified scope' % name
      return 0
    else :
      print '\ncreateAS: ERROR --- Unable to create the AS %s at specifie scope. Check the logs for more information.' % name
      return 1      
"""

""" INSTALL ear and start stop ear

earLoc='/home/artifacts/Statement-bva-application.ear'

appName='Statement-bva'

cellName=AdminControl.getCell()

nodeName=AdminControl.getNode()

appManager=AdminControl.queryNames('cell='+cellName+',node='+nodeName+',type=ApplicationManager,process=server1,*')

print appManager

#AdminControl.invoke(appManager , 'stopApplication',appName)

print AdminApp.uninstall(appName)

AdminConfig.save()

print AdminApp.install(earLoc)

AdminConfig.save()

AdminControl.invoke(appManager , 'startApplication',appName) 

======================


appName = "CL01ASRShipEAR" 
earPath = "/apps/WebSphere/AppServer/local/v70/migration/ASR/current/ASRInternal_vsb4-6-18.ear"

print("appName is "+appName)
print("earPath is "+earPath)

### VARIABLES ###
contentType = "app"
installOpts = "update"
cmdOptions = ["-operation", installOpts, "-contents", earPath, "-update.ignore.new"]
### VARIABLES ###

AdminApp.update(appName, contentType, cmdOptions)
AdminConfig.save()

"""