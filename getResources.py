#
# TODO: enter JYTHON code and save
#

# wsadmin.bat -lang jython -f C:\Projects\ARServices_Write_AP1\BPMScripting\getResources.py -username cadmin -password cadmin -tracefile /temp/wsadmin_test_1.log -appendtrace true

# print AdminConfig.list('Cell')
# print AdminConfig.list( 'MQQueue',AdminConfig.list('Cell'))

# serverId=AdminConfig.getid('/Cell:cell_name/Node:node_name/Server:server_name')

#ns = AdminConfig.getid('/Node:mynode/')
#print AdminConfig.showAttribute(ns, 'hostName')

#cellId = AdminConfig.getid('/Cell:PSCell1')
#for qId in AdminConfig.list( 'MQQueue',cellId).splitlines() :
#	print AdminConfig.showAttribute(qId,'jndiName') 
#	print AdminConfig.showAttribute(qId,'baseQueueName')
	
#for qid in AdminConfig.list( 'MQQueue',cellId ).splitlines() :
#	print AdminConfig.showall(qid)

cellId = AdminConfig.getid('/Cell:PSCell1')
#for qid in AdminConfig.list( 'MQQueueConnectionFactory', cellId ).splitlines() :
#	print qid
#	print AdminConfig.showall(qid)

for asid in  AdminConfig.list( 'J2CActivationSpec', cellId ).splitlines():
	print asid
	print AdminConfig.show(asid)

#-------------------------------------------------------------------------------
# Name: SyncNodes
# Role: Locate the non-admin nodes, and synchronize each
#-------------------------------------------------------------------------------
def SyncNodes():
	print '\nSyncNodes: Enter SynchNodes().'
  	nodes = AdminTask.listNodes()
  	for node in nodes.splitlines() :
    		if node not in [ 'was_dmgr_node', 'wps_dmgr_node' ] :
      			sync = AdminControl.completeObjectName( 'type=NodeSync,node=%s,*' % node )
      		if sync == '' :
        		print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Nodeagent appears inactive.' % node
      		else :
        		if AdminControl.invoke( sync, 'sync' ) == 'true':
          			print '\nSyncNodes: SUCCESS --- Synchronization successfull with Node', node
        		else :
          			print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Check the logs for more information.' % node
 	print '\nSyncNodes: Exit  SynchNodes().'
