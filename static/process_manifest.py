#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from xml.etree import ElementTree

PACKAGE_TAB = "package" #包名标签
MANIFEST_TAB = "manifest"
USES_PERMISSION_TAB = "uses-permission"
APPLICATION_TAB = "application"
META_DATA_TAB = "meta-data"
ACTIVITY_TAB = "activity"
SERVICE_TAB = "service"
RECEIVER_TAB = "receiver"
PROVIDER_TAB = "provider"

class ProcessManifest:
    
    def __init__(self):
        self.packageName = ""  
        self.launcherActivity = ""
        self.activityInfor = []
        self.serviceInfor = []
        self.receiverInfor = []
        self.providerInfor = []
        self.metaDataDict = {}
        self.usesPermission = []
        self.adJsonInfor = [""]
        
    def ParseManifestFile(self, filePath):
        '''
        函数功能：对AndroidManifest.xml文件进行解析
        '''
        print "[filePath]:" + filePath
        root = ElementTree.parse(filePath)
        
        node = root.getiterator(MANIFEST_TAB)
        
        #获得package信息
        if node[0].attrib.has_key(PACKAGE_TAB):
            self.packageName = node[0].attrib[PACKAGE_TAB]
           
            
        subNode = node[0].getchildren()
                
        for subNodeItem in subNode:
            #获取uses-permission信息
            if subNodeItem.tag==USES_PERMISSION_TAB:
                permissionValue = subNodeItem.attrib.values()
                self.usesPermission.append(permissionValue[0])
                
            #获取安排偏离擦提哦你 标签信息
            if subNodeItem.tag==APPLICATION_TAB: 
                self.ParseApplicationTab(subNodeItem)
                

        
        
    def ParseApplicationTab(self, applicationNode):
        '''
        函数功能：对application标签进行解析
        '''
        activityName =""
        for appNodeItem in applicationNode:
            #处理meta-data（元数据）标签信息
            if appNodeItem.tag==META_DATA_TAB:
                tempMetaData = appNodeItem.attrib.values()
                self.metaDataDict[tempMetaData[1]]=tempMetaData[0]
            
            
            #处理activity标签信息
            elif appNodeItem.tag==ACTIVITY_TAB:
                pass
                tempActivity = appNodeItem.attrib   
                
                #获取activity的名称信息
                for keyItem in tempActivity:
                    if keyItem.find("name")!= -1:
                        activityName = tempActivity[keyItem]
                        self.activityInfor.append(activityName)
                
                #获得activity下面的intent-filter信息
                for intentFilter in appNodeItem:
                    for categoryInfor in intentFilter:
                         intentKey = categoryInfor.tag
                         intentValue = categoryInfor.attrib.values()[0]
                         if intentKey=="category" and intentValue=="android.intent.category.LAUNCHER":
                            self.launcherActivity = activityName
            #处理service标签
            elif appNodeItem.tag==SERVICE_TAB:
                tempService = appNodeItem.attrib   
                for keyItem in tempService:
                    if keyItem.find("name")!= -1:
                        ServiceName = tempService[keyItem]
                        self.serviceInfor.append(ServiceName)
                        #print "[service]" + ServiceName
                        
                        
            #处理receiver标签信息
            elif appNodeItem.tag==RECEIVER_TAB:
                tempReceiver = appNodeItem.attrib   
                for keyItem in tempReceiver:
                    if keyItem.find("name")!= -1:
                        receiverName = tempReceiver[keyItem]
                        self.receiverInfor.append(receiverName)
                        #print "[receiver]" + receiverName
                        
            #处理provider标签信息            
            elif appNodeItem.tag==PROVIDER_TAB:
                tempProvider = appNodeItem.attrib   
                for keyItem in tempProvider:
                    if keyItem.find("name")!= -1:
                        providerName = tempProvider[keyItem]
                        self.providerInfor.append(providerName)
                        #print "[provider]" + providerName
        
            else:
                print appNodeItem.tag
            
   
#        <service android:name="com.yintong.secure.customize.qihoo.service.PayService" android:exported="false">
#            <intent-filter>
#                <action android:name="com.yintong.secure.customize.qihoo.IPayService" />
#            </intent-filter>
#        </service>
   
        
    def CutSmartKey(self, longKey):
        '''
        函数功能：将长key值，抽取出短的key值
        参数：longKey 长key的字符串
        '''    
    
    def TestShow(self):
        print  "[PackageName]:%s" %(self.packageName)
        print  "[UsesPermissionValueList]:"
        for permission in self.usesPermission:
            print "\t %s" %(permission)
    
        print "[MetaData infor]:"
        for metaDataItem in self.metaDataDict:
            print "\t %s = %s" %(metaDataItem, self.metaDataDict[metaDataItem])
            
        
        print "[Activity Infor]:"
        for activityItem in self.activityInfor:
            print "\t " + activityItem
            
        print "[Service Infor]:"
        for serviceItem in self.serviceInfor:
            print "\t " + serviceItem            
 
        print "[Receiver Infor]:"
        for receiverItem in self.receiverInfor:
            print "\t " + receiverItem              


        print "[Providerr Infor]:"
        for providerItem in self.providerInfor:
            print "\t " + providerItem      
                        

            
        print "[launcherActivity]:"   + self.launcherActivity
 
    
def main():
        

    processManifest = ProcessManifest()
    #processManifest.ParseManifestFile("/home/anbc/test/123/AndroidManifest.xml")
    processManifest.ParseManifestFile("/home/anbc/test/360MobileSafe/AndroidManifest.xml")
    processManifest.TestShow()




if __name__ == '__main__':
    main() 