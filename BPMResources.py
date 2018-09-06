###################################### Run script ##################################################
## Go to dmgr bin folder and use below command to run the jython scrit                            ##
## wsadmin.sh -lang jython -user <<user_name>> -password <<password>> -f <<path of script file>>  ##
####################################################################################################




# ----------------------- Activation Spec  Export_test1_1_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Export_test1_1_AS -jndiName jms\Export_test1_1_AS -destinationJndiName jms\Export_test1_1_RQO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Export_test1_1_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Export_test1_2_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Export_test1_2_AS -jndiName jms\Export_test1_2_AS -destinationJndiName jms\Export_test1_2_RQO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Export_test1_2_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test1_3_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test1_3_AS -jndiName jms\Import_test1_3_AS -destinationJndiName jms\Import_test1_3_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test1_3_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test1_1_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test1_1_AS -jndiName jms\Import_test1_1_AS -destinationJndiName jms\Import_test1_1_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test1_1_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test1_2_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test1_2_AS -jndiName jms\Import_test1_2_AS -destinationJndiName jms\Import_test1_2_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test1_2_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Export_test_1_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Export_test_1_AS -jndiName jms\Export_test_1_AS -destinationJndiName jms\Export_test_1_RQO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Export_test_1_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test_3_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test_3_AS -jndiName jms\Import_test_3_AS -destinationJndiName jms\Import_test_3_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test_3_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test_1_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test_1_AS -jndiName jms\Import_test_1_AS -destinationJndiName jms\Import_test_1_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test_1_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Import_test_2_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Import_test_2_AS -jndiName jms\Import_test_2_AS -destinationJndiName jms\Import_test_2_RPO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Import_test_2_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Activation Spec  Export_test_2_AS------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
asAttrs = '-name Export_test_2_AS -jndiName jms\Export_test_2_AS -destinationJndiName jms\Export_test_2_RQO -qmgrName QM1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
echoMessage='Creating Activation Specification (Export_test_2_AS)' 
print echoMessage,
AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- QCF Creation Export_test1_1_QCF------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
qcfAttrs = '-type QCF -name Export_test1_1_QCF -jndiName jms\Export_test1_1_QCF -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
echoMessage='Creating Queue Connection Factory (Export_test1_1_QCF)'
print echoMessage,
AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- QCF Creation Export_test1_2_QCF------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
qcfAttrs = '-type QCF -name Export_test1_2_QCF -jndiName jms\Export_test1_2_QCF -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
echoMessage='Creating Queue Connection Factory (Export_test1_2_QCF)'
print echoMessage,
AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- QCF Creation Import_test1_1_QCF------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
qcfAttrs = '-type QCF -name Import_test1_1_QCF -jndiName jms\Import_test1_1_QCF -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
echoMessage='Creating Queue Connection Factory (Import_test1_1_QCF)'
print echoMessage,
AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- QCF Creation Export_test_1_QCF------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
qcfAttrs = '-type QCF -name Export_test_1_QCF -jndiName jms\Export_test_1_QCF -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
echoMessage='Creating Queue Connection Factory (Export_test_1_QCF)'
print echoMessage,
AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- QCF Creation Import_test_1_QCF------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
qcfAttrs = '-type QCF -name Import_test_1_QCF -jndiName jms\Import_test_1_QCF -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN '
qcfAttrs += '-customProperties [[cust1 val1] [cust2 val2] [cust3 MQ] [cust4 val4]]'
echoMessage='Creating Queue Connection Factory (Import_test_1_QCF)'
print echoMessage,
AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
# ----------------------- Queue JNDI Creation Import_test1_2_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_2_RQI -jndiName jms\Import_test1_2_RQI -queueName TEST.1.2.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_2_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test1_2_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_2_RPO -jndiName jms\Import_test1_2_RPO -queueName TEST.1.2.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_2_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test_1_RQO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test_1_RQO -jndiName jms\Export_test_1_RQO -queueName TEST.1.RQO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test_1_RQO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test_1_RPI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test_1_RPI -jndiName jms\Export_test_1_RPI -queueName TEST.1.RPI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test_1_RPI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_3_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_3_RQI -jndiName jms\Import_test_3_RQI -queueName TEST.3.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_3_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_3_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_3_RPO -jndiName jms\Import_test_3_RPO -queueName TEST.3.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_3_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_1_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_1_RQI -jndiName jms\Import_test_1_RQI -queueName TEST.1.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_1_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_1_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_1_RPO -jndiName jms\Import_test_1_RPO -queueName TEST.1.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_1_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_2_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_2_RQI -jndiName jms\Import_test_2_RQI -queueName TEST.2.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_2_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_2_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_2_RPO -jndiName jms\Import_test_2_RPO -queueName TEST.2.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_2_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test_2_RQO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test_2_RQO -jndiName jms\Export_test_2_RQO -queueName TEST.2.RQO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test_2_RQO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test_4_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test_4_RQI -jndiName jms\Import_test_4_RQI -queueName TEST.4.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test_4_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test1_1_RQO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test1_1_RQO -jndiName jms\Export_test1_1_RQO -queueName TEST.1.1.RQO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test1_1_RQO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test1_1_RPI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test1_1_RPI -jndiName jms\Export_test1_1_RPI -queueName TEST.1.1.RPI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test1_1_RPI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test1_2_RQO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test1_2_RQO -jndiName jms\Export_test1_2_RQO -queueName TEST.1.2.RQO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test1_2_RQO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Export_test1_2_RPI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Export_test1_2_RPI -jndiName jms\Export_test1_2_RPI -queueName TEST.1.2.RPI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Export_test1_2_RPI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test1_3_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_3_RQI -jndiName jms\Import_test1_3_RQI -queueName TEST.1.3.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_3_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test1_3_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_3_RPO -jndiName jms\Import_test1_3_RPO -queueName TEST.1.3.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_3_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test1_1_RQI------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_1_RQI -jndiName jms\Import_test1_1_RQI -queueName TEST.1.1.RQI '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_1_RQI")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

# ----------------------- Queue JNDI Creation Import_test1_1_RPO------------------------------------------------------
scopeID=AdminConfig.getid('/Cell:PSCell1')
mqqAttrs = '-name Import_test1_1_RPO -jndiName jms\Import_test1_1_RPO -queueName TEST.1.1.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
echoMessage='Creating Queue JNDI (Import_test1_1_RPO")'
print echoMessage,
AdminTask.createWMQQueue( scopeID, mqqAttrs )
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

echoMessage="Saving to master repository"
print echoMessage,
AdminConfig.save() 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

echoMessage="Synchronizing nodes"
print echoMessage,
#SyncNodes()
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
print ' *** End of script ***'

#-------------------------------------------------------------------------------
# Name: SyncNodes
#-------------------------------------------------------------------------------
def SyncNodes():
	nodes = AdminTask.listNodes()
	for node in nodes.splitlines() :
		if node not in [ 'was_dmgr_node', 'wps_dmgr_node' ] :
			sync = AdminControl.completeObjectName( 'type=NodeSync,node=%s,*' % node )
			if sync == '' :
				print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Nodeagent appears inactive.' % node
			else :
				if AdminControl.invoke( sync, 'sync' ) == 'true':
					print 'Synchronization successfully with Node %s.' % node
				else :
					print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Check the logs for more information.' % node
