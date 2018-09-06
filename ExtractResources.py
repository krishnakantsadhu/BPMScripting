###################################### Extract Resources ###########################################
## Author : Krishnakant Sadhu									  ##	
## Version : 1.0 										  ##
## Usage : Go to dmgr bin folder and use below command to run the jython scrit                    ##
## wsadmin.sh -lang jython -user <<user_name>> -password <<password>> -f <<path of script file>>  ##
####################################################################################################

# Add ears in arry
ears = ['TestModule']

cellName = AdminControl.getCell()
#print cellName
scope = '/Cell:%s'%cellName
cellId = AdminConfig.getid(scope)
#print cellid
queues = AdminConfig.list('MQQueue',cellId).splitlines()
connectionFactories = AdminConfig.list( 'MQQueueConnectionFactory', cellId ).splitlines()
activationSpecs =  AdminConfig.list( 'J2CActivationSpec', cellId ).splitlines()
flag = 0
print  '\n\033[91m Extract Resources Running...\n\033[0m'
for ear in ears:
	#print '\n--------------------------------- %s -----------------------------'%ear
	imports = AdminTask.listSCAImports(['-moduleName',ear,'-applicationName','%sApp'%ear ]).splitlines
	for imp in imports(0):
		scaCompoment = imp.strip()
		mqBindings = AdminTask.showSCAImportMQBinding('[-moduleName %s -import %s -javaFormat true -showAdvanced true -applicationName %sApp ]'%(ear,imp,ear)).splitlines 
		for mqBinding in mqBindings(0):
			resources = mqBinding[1:-1].split(",")
			if flag == 0 :
				print 'EAR Name,SCA Compoment,Connetion Factory,Qcf Qmgr Name,Qcf Qmgr Hostname,Qcf Qmgr PortNumber,Qcf Qmgr Channel,Activation Spec,Activation Spec Qmgr Name,Activation Spec Qmgr Hostname,Activation Spec Qmgr PortNumber,Activation Spec Qmgr Channel,Sender QueueJndi,Sender Queue,Receiver QueueJndi,Receiver Queue'
				flag = 1
			
			connetionFactory=''
			qcfQmgrName=''
			qcfQmgrHostname=''
			qcfQmgrPortNumber=''
			qcfQmgrSvrconnChannel=''
				
			activationSpec=''
			asQmgrName=''
			asQmgrHostname=''
			asQmgrPortNumber=''
			asQmgrSvrconnChannel=''
				
			senderQueueJndi=''
			senderQueue=''
				
			receiverQueueJndi=''
			receiverQueue=''
			for resource in resources:
								
				key, value = resource.split('=')
				
				key = key.strip()
				value = value.strip()
				
				if key == 'connection.factory':
					connetionFactory = value
					for qcfId in connectionFactories :
						if AdminConfig.showAttribute(qcfId,'jndiName')==connetionFactory:
							qcfQmgrName = AdminConfig.showAttribute(qcfId,'queueManager')
							qcfQmgrHostname = AdminConfig.showAttribute(qcfId,'host')
							qcfQmgrPortNumber = AdminConfig.showAttribute(qcfId,'port')
							qcfQmgrSvrconnChannel = AdminConfig.showAttribute(qcfId,'channel')
							
				if key == 'activation.specification':
					activationSpec = value
					for asId in activationSpecs :
						if AdminConfig.showAttribute(asId,'jndiName')==activationSpec:
							propList = AdminConfig.showAttribute(asId, 'resourceProperties')[1:-1].split()
    							for prop in propList :
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'queueManager':
        								asQmgrName = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'hostName':
        								asQmgrHostname = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'port':
        								asQmgrPortNumber = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'channel':
        								asQmgrSvrconnChannel = AdminConfig.showAttribute(prop, 'value')
				if key == 'send.destination':
					senderQueueJndi = value
					for qId in queues :
						if AdminConfig.showAttribute(qId,'jndiName')==senderQueueJndi:
							senderQueue = AdminConfig.showAttribute(qId,'baseQueueName')
			
				if key == 'receive.destination':
					receiverQueueJndi = value
					for qId in queues :
						if AdminConfig.showAttribute(qId,'jndiName')==receiverQueueJndi:
							receiverQueue = AdminConfig.showAttribute(qId,'baseQueueName')
			print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (ear,scaCompoment,connetionFactory,qcfQmgrName,qcfQmgrHostname,qcfQmgrPortNumber,qcfQmgrSvrconnChannel,activationSpec,asQmgrName,asQmgrHostname,asQmgrPortNumber, asQmgrSvrconnChannel,senderQueueJndi,senderQueue,receiverQueueJndi,receiverQueue)
			

	exports = AdminTask.listSCAExports(['-moduleName',ear,'-applicationName','%sApp'%ear ]).splitlines
	for exp in exports(0):
		scaCompoment = exp.strip()
		mqBindings = AdminTask.showSCAExportMQBinding('[-moduleName %s -export %s -javaFormat true -showAdvanced true -applicationName %sApp ]'%(ear,exp.strip(),ear)).splitlines 
		for mqBinding in mqBindings(0):
			resources = mqBinding[1:-1].split(",")
			if flag == 0 :
				print 'EAR Name,SCA Compoment,Connetion Factory,Qcf Qmgr Name,Qcf Qmgr Hostname,Qcf Qmgr PortNumber,Qcf Qmgr Channel,Activation Spec,Activation Spec Qmgr Name,Activation Spec Qmgr Hostname,Activation Spec Qmgr PortNumber,Activation Spec Qmgr Channel,Sender QueueJndi,Sender Queue,Receiver QueueJndi,Receiver Queue'
				flag = 1
				
			connetionFactory=''
			qcfQmgrName=''
			qcfQmgrHostname=''
			qcfQmgrPortNumber=''
			qcfQmgrSvrconnChannel=''
				
			activationSpec=''
			asQmgrName=''
			asQmgrHostname=''
			asQmgrPortNumber=''
			asQmgrSvrconnChannel=''
				
			senderQueueJndi=''
			senderQueue=''
				
			receiverQueueJndi=''
			receiverQueue=''
				
			for resource in resources:
				
				key, value = resource.split('=')
				
				key = key.strip()
				value = value.strip()
				
				if key == 'connection.factory':
					connetionFactory = value
					for qcfId in connectionFactories :
						if AdminConfig.showAttribute(qcfId,'jndiName')==connetionFactory:
							qcfQmgrName = AdminConfig.showAttribute(qcfId,'queueManager')
							qcfQmgrHostname = AdminConfig.showAttribute(qcfId,'host')
							qcfQmgrPortNumber = AdminConfig.showAttribute(qcfId,'port')
							qcfQmgrSvrconnChannel = AdminConfig.showAttribute(qcfId,'channel')
							
				if key == 'activation.specification':
					activationSpec = value
					for asId in activationSpecs :
						if AdminConfig.showAttribute(asId,'jndiName')==activationSpec:
							propList = AdminConfig.showAttribute(asId, 'resourceProperties')[1:-1].split()
    							for prop in propList :
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'queueManager':
        								asQmgrName = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'hostName':
        								asQmgrHostname = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'port':
        								asQmgrPortNumber = AdminConfig.showAttribute(prop, 'value')
        							if AdminConfig.showAttribute(prop, 'name').strip() == 'channel':
        								asQmgrSvrconnChannel = AdminConfig.showAttribute(prop, 'value')

				if key == 'send.destination':
					senderQueueJndi = value
					for qId in queues :
						if AdminConfig.showAttribute(qId,'jndiName')==senderQueueJndi:
							senderQueue = AdminConfig.showAttribute(qId,'baseQueueName')
			
				if key == 'receive.destination':
					receiverQueueJndi = value
					for qId in queues :
						if AdminConfig.showAttribute(qId,'jndiName')==receiverQueueJndi:
							receiverQueue = AdminConfig.showAttribute(qId,'baseQueueName')
			print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (ear,scaCompoment,connetionFactory,qcfQmgrName,qcfQmgrHostname,qcfQmgrPortNumber,qcfQmgrSvrconnChannel,activationSpec,asQmgrName,asQmgrHostname,asQmgrPortNumber, asQmgrSvrconnChannel,senderQueueJndi,senderQueue,receiverQueueJndi,receiverQueue)

	
class color:
	PURPLE = '\033[95m'
   	CYAN = '\033[96m'
   	DARKCYAN = '\033[36m'
   	BLUE = '\033[94m'
   	GREEN = '\033[92m'
   	YELLOW = '\033[93m'
   	RED = '\033[91m'
   	BOLD = '\033[1m'
   	UNDERLINE = '\033[4m'
   	END = '\033[0m'	
