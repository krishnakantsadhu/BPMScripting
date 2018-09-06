#------------------------------------------------------------------------------
# Queue Creation
#------------------------------------------------------------------------------
def createQueueJndi(asAttrs,queueName):
	isExist = 1
	global isSkipIfExist
	global queues
	global YELLOW
	global RED
	global GREEN
	global END
	for qId in queues:
		if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
			print '%s[Waring] :  Queue Jndi (%s) already Exist%s'%(YELLOW,queueName,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
				print echoMessage,
				done = AdminTask.deleteWMQQueue(qId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
				isExist = 0
				
	if isExist == 1:	
		echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
		print echoMessage
		done = AdminTask.createWMQQueue( scopeID, asAttrs ) 
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)

#------------------------------------------------------------------------------
# Activation Spec Creation
#------------------------------------------------------------------------------
def createActivationSpec(asAttrs,activationSpecName):
	isExist = 1
	global isSkipIfExist
	global activationSpecs
	global YELLOW
	global RED
	global GREEN
	global END
	for asId in activationSpecs:
		if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
			print '%s[Waring] : Activation Specification (%s) already Exist%s'%(YELLOW,activationSpecName,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
				print echoMessage,
				done = AdminTask.deleteWMQActivationSpec(asId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
				isExist = 0
				
	if isExist == 1:
		echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
		print echoMessage,
		done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)

#------------------------------------------------------------------------------
# Queue Connection Factory Creation
#------------------------------------------------------------------------------
def createQueueConnetionFactory(asAttrs,qcfname):
	isExist = 1
	global isSkipIfExist
	global connectionFactories
	global YELLOW
	global RED
	global GREEN
	global END
	for qcfId in connectionFactories:
		if AdminConfig.showAttribute( qId, 'jndiName' ) == qcfname:
			print '%s[Waring] : Queue Connetion Factory (%s) already Exist%s'%(YELLOW,qcfname,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
				print echoMessage,
				done = AdminTask.deleteWMQConnectionFactory(qcfId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
				isExist = 0
				
	if isExist == 1:
		echoMessage = '[Info] : Creating Queue Jndi (%s)'% qcfname
		print echoMessage
		done = AdminTask.createWMQConnectionFactory( scopeID, asAttrs )
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)