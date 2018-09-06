# Purpose --- To deploy EAR file on Server
# Date   ----  2/11/2011
#version   --- 1.0
import sys
from time import sleep

def DeployOnServer(earlocation, appName, nodeName, serverName, virtualHost, webNode1, webSrv1):
   #--------------------------------------------------------------
   # do some sanity checking
   #     -- do we have a node by this name?
   #--------------------------------------------------------------
   cellName = AdminControl.getCell()
   print cellName
   node = AdminConfig.getid("/Node:" + nodeName + "/")
   print " checking for existence of node " + nodeName
   if len(node) == 0:
      print " Error -- node not found for name " + nodeName
      return
   else:
      print " "+nodeName+" does exists so deployment process will start "
   #---------------------------------------------------------------------------------------
   # Here we specify ear file location and server where we wish to deploy the ear file
   #----------------------------------------------------------------------------------------
   defapp = earlocation
   servOpt1 = "WebSphere:cell=" + cellName + ",node=" + nodeName + ",server=" + serverName
   servOpt2 = "+WebSphere:cell=" + cellName + ",node=" + webNode1 + ",server=" + webSrv1
   servOpt = servOpt1+servOpt2
   serv = ["-target", servOpt]
#---------------------------------------------------------
#  print "-------------------------------------------------------------"
#  print "These are the options we are passing to deploy the EAR file."
#  print " -------------------------------------------------------------"

   nameOpt = ["-appname", appName]
   nodeOpt = ["-node", nodeName]
   serverOpt1 = ["-server", serverName]

   mapVhOptValus = [[".*",".*", virtualHost]]
   mapVhOpt = ["-MapWebModToVH", mapVhOptValus]
   appOptions = []
   appOptions.extend(nameOpt)
   appOptions.extend(nodeOpt)
   appOptions.extend(serverOpt1)
   appOptions.extend(mapVhOpt)
   print appOptions
   AdminApp.install(defapp, appOptions)

   #---------------------------------------------------------
   # Save all the changes
   #---------------------------------------------------------
   print "Deploy: saving the configuration"
   AdminConfig.save()
   sleep(20)
#----------------------------------------------------------------------
# check if the application is ready to start. If ready then start it
#------------------------------------------------------------------------
def startAppOnServer():
   appready = AdminApp.isAppReady(appName)
   print appready
   if appready == 'false':
                sleep(40)
                appready = AdminApp.isAppReady(appName)
                print appready
   else:
                print "starting the application "+appName+" on "+serverName+" "
                appManager = AdminControl.queryNames("type=ApplicationManager,process="+ serverName +",*")
                if appManager == "":
                        print "Please make sure whether Application Server is up and running before starting the applicaiton "
                        print " Or There could be something wrong with installated EAR file "
                AdminControl.invoke(appManager, 'startApplication', appName)
                appstate = AdminControl.completeObjectName("type=Application,name="+appName+",*")
                if appstate != "":
                        print ""+ appName +" started "

# ----------------------------------------------------------------------------------------------------------------------------
# This function verifies whether Application is already deployed or not. If already deployed it will be uninstalled first
# -----------------------------------------------------------------------------------------------------------------------------
def appexist():
   print " checking for the "+appName+" applicaiton whether it is already exists or not"
   apps = AdminApp.list().split(lineSeparator)
   for applist in apps:
    if applist == appName:
        print "Application is already installed so It will be uninstalled first "
        AdminApp.uninstall(appName)
        AdminConfig.save()
    else:
        print " ------------------------------------------------"
        print " "+appName+" doesn't exists now so it will be deployed "


#----------------------------------------------------------------------------------------
#Main codes start here....
# ----------------------------------------------------------------------------------------
if (len(sys.argv) !=7):
        print " Please enter correct arguments "
        print " ex: DeployEAROnServer.py /usr/IBM/AppServer/installableApps/sample.ear sample mynode server1 virtualHost webserverNode webserver"
else:
        earlocation = sys.argv[0]
        appName = sys.argv[1]
        nodeName = sys.argv[2]
        serverName = sys.argv[3]
        virtualHost = sys.argv[4]
        webNode1 = sys.argv[5]
        webSrv1 = sys.argv[6]
        print "EARfilelocation :" +earlocation
        print "Application Name : " +appName
        print "Node Name : " +nodeName
        print "Server Name : " +serverName
        print "Virtual Host :" +virtualHost
        print "WebServerNode :" +webNode1
        print "WebServer : " +webSrv1
        appexist()
        DeployOnServer(earlocation, appName, nodeName, serverName, virtualHost, webNode1, webSrv1)
        execfile('/usr/IBM/WebSphere/wasadm/scripts/jython/syncNode.py')
startAppOnServer()



