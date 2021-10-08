#import os
from lxml import etree    #import cElementTree as ET
#import csv
#import logging
import pandas as pd
import time

#-------------------------------
def find_nth(str, sub_str, n):
    start = str.find(sub_str)
    #print (start)
    while start >= 0 and n > 1:
        start = str.find(sub_str, start+1,len(str))
        #print (start)
        n -= 1
    return start
#---------------------------
def infa_corr_excel(wf_logdir,sn_logdir,wf_prmfile,sn_prmfile,sn_srcpath,sn_tgtpath,sn_baddir,sn_cachdir,sn_map_c,sn_comm_c,sn_trans_ver,sn_verbose,sn_cnt,wf_cnt,mp_cnt):
    " This function for writing into excel file"
    # Create a Pandas dataframe from the data.
   #logger.debug("writing into excel")
    labels1 = ['Folder name', 'Workflow name', 'Workflow lg file name', 'Workflow dir path']
    labels2 = ['Folder name', 'Workflow name','Instance name','Reusable', 'Session Log File Name', 'Session Log File Dir']
    labels3 = ['Folder name','Workflow name','Instance name','Reusable','Sess Parm file name']
    labels4 = ['Folder name', 'Workflow name','Workflow Parm File Name']
    labels5 = ['Folder name','Workflow name','Session name','Source file Directory','File name']
    labels6 = ['Folder name','Workflow name','Session name','Target file Directory','File name']
    labels7 = ['Folder name','Workflow name','Session name','Instance name','Reject file Directory','Reject File name']
    labels8 = ['Folder name','Workflow name','Session name','Mapping name','Transformation name','Type','Transformation cacheDirectory']
    labels9 = ['Folder name', 'Workflow name', 'Mapping name', 'Attribute name','Parameter or Variable','Default Value']
    labels10 = ['Folder name', 'Workflow name', 'Task Name', 'Task Type','Task value','Task Instance Name']
    labels11 = ['Folder name', 'Workflow name', 'Session name', 'Transformation name','Override Tracing']
    labels12 = ['Folder name', 'Workflow name', 'Session name','Override Tracing']
    labels13 = ['Folder name','Total session count']
    labels14 = ['Folder name','Total workflow count']
    labels15 = ['Folder name','Total mapping count']
    
    #ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #ts = datetime.datetime.now().timestamp()
    #print (ts)
    Excel_name = "C:/Users/Manali.Ghosh/Desktop/Tracing_level/CMD Task and Verbose.XML" + timestr +".xlsx"
    writer = pd.ExcelWriter(Excel_name, engine='xlsxwriter')
    wb  = writer.book
    header_format = wb.add_format({
        'bold': True,
        'size': 25,
        'font_color': 'green',
        'border': 1})
    
    wflog_hdr2 = "A" + str(wf_logdir[2]+3)
    snlog_hdr2 = "A" + str(sn_logdir[2]+3)
    wfprm_hdr2 = "A" + str(wf_prmfile[2]+3)
    snprm_hdr2 = "A" + str(sn_prmfile[2]+3)
    snsrc_hdr2 = "A" + str(sn_srcpath[2]+3)
    sntgt_hdr2 = "A" + str(sn_tgtpath[2]+3)
    snbad_hdr2 = "A" + str(sn_baddir[2]+3)
    sncach_hdr2 = "A" + str(sn_cachdir[2]+3)
    
    wflogdir = "D4:D" + str(wf_logdir[2])
    snlogdir = "F4:F" + str(sn_logdir[2])
    wfprmfl = "C4:C" + str(wf_prmfile[2])
    snprmfl = "E4:E" + str(sn_prmfile[2])
    snsrcph = "D4:D" + str(sn_srcpath[2])
    sntgtph = "D4:D" + str(sn_tgtpath[2])
    snbaddir = "E4:E" + str(sn_baddir[2])
    sncachdir = "G4:G" + str(sn_cachdir[2])
    
    format1 = wb.add_format({'bg_color': 'yellow'})
    
    #Workflow log file directory
    df1c = pd.DataFrame.from_records(wf_logdir[0], columns=labels1)
    df1c.to_excel(writer, sheet_name='Workflow Log File Path',startrow=wf_logdir[2]+4,index=False)
    worksheet1 = writer.sheets['Workflow Log File Path']
    worksheet1.write(wflog_hdr2,'Correct Workflow Log File Path', header_format)
    
    df1ic = pd.DataFrame.from_records(wf_logdir[1], columns=labels1)
    df1ic.to_excel(writer, sheet_name='Workflow Log File Path',startrow=2,index=False)
    worksheet1.write('A1','Incorrect Workflow Log File Path', header_format)
    worksheet1.set_column('B:F', 35)
    worksheet1.set_column('A:A', 12)
    worksheet1.conditional_format(wflogdir, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Session log file directory
    df2c = pd.DataFrame.from_records(sn_logdir[0], columns=labels2)
    df2c.to_excel(writer, sheet_name='Session Log File Path',startrow=sn_logdir[2]+4,index=False)
    worksheet2 = writer.sheets['Session Log File Path']
    worksheet2.write(snlog_hdr2,'Correct Session Log File Path', header_format)
    
    df2ic = pd.DataFrame.from_records(sn_logdir[1], columns=labels2)
    df2ic.to_excel(writer, sheet_name='Session Log File Path',startrow=2,index=False)
    worksheet2.write('A1','Incorrect Session Log File Path', header_format)
    worksheet2.set_column('B:F', 35)
    worksheet2.set_column('A:A', 12)
    worksheet2.conditional_format(snlogdir, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Workflow parmeter file
    df3c = pd.DataFrame.from_records(wf_prmfile[0], columns=labels4)
    df3c.to_excel(writer, sheet_name='Workflow level parameter file',startrow=wf_prmfile[2]+4,index=False)
    worksheet3 = writer.sheets['Workflow level parameter file']
    worksheet3.write(wfprm_hdr2,'Workflow level parameter file values', header_format)
    
    df3ic = pd.DataFrame.from_records(wf_prmfile[1], columns=labels4)
    df3ic.to_excel(writer, sheet_name='Workflow level parameter file',startrow=2,index=False)
    worksheet3.write('A1','Workflow level parameter file override values', header_format)
    worksheet3.set_column('B:C', 40)
    worksheet3.set_column('A:A', 12)
    worksheet3.conditional_format(wfprmfl, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Session parmeter file 
    df4c = pd.DataFrame.from_records(sn_prmfile[0], columns=labels3)
    df4c.to_excel(writer, sheet_name='Session level parameter file',startrow=sn_prmfile[2]+4,index=False)
    worksheet4 = writer.sheets['Session level parameter file']
    worksheet4.write(snprm_hdr2,'Session level parameter file values', header_format) 
    worksheet4.set_column('B:F', 35)
    worksheet4.set_column('A:A', 12)
    
    df4ic = pd.DataFrame.from_records(sn_prmfile[1], columns=labels3)
    df4ic.to_excel(writer, sheet_name='Session level parameter file',startrow=2,index=False)
    worksheet4.write('A1','Session level parameter file override values', header_format)
    worksheet4.conditional_format(snprmfl, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Session with source path
    df5c = pd.DataFrame.from_records(sn_srcpath[0], columns=labels5)
    df5c.to_excel(writer, sheet_name='Session with source path',startrow=sn_srcpath[2]+4,index=False)
    worksheet5 = writer.sheets['Session with source path']
    worksheet5.write(snsrc_hdr2,'Session with correct source directory path', header_format)
    worksheet5.set_column('B:F', 35)
    worksheet5.set_column('A:A', 12)
    
    df5ic = pd.DataFrame.from_records(sn_srcpath[1], columns=labels5)
    df5ic.to_excel(writer, sheet_name='Session with source path',startrow=2,index=False)
    worksheet5.write('A1','Session with incorrect source directory path', header_format)
    worksheet5.conditional_format(snsrcph, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Session with target path
    df6c = pd.DataFrame.from_records(sn_tgtpath[0], columns=labels6)
    df6c.to_excel(writer, sheet_name='Session with target path',startrow=sn_tgtpath[2]+4,index=False)
    worksheet6 = writer.sheets['Session with target path']
    worksheet6.write(sntgt_hdr2,'Session with correct target directory path', header_format)
    worksheet6.set_column('B:F', 35)
    worksheet6.set_column('A:A', 12)
    
    df6ic = pd.DataFrame.from_records(sn_tgtpath[1], columns=labels6)
    df6ic.to_excel(writer, sheet_name='Session with target path',startrow=2,index=False)
    worksheet6.write('A1','Session with incorrect target directory path', header_format)
    worksheet6.conditional_format(sntgtph, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Session with bad file path
    df7c = pd.DataFrame.from_records(sn_baddir[0], columns=labels7)
    df7c.to_excel(writer, sheet_name='Session with bad file path',startrow=sn_baddir[2]+4,index=False)
    worksheet7 = writer.sheets['Session with bad file path']
    worksheet7.write(snbad_hdr2,'Session with correct bad file path', header_format)
    worksheet7.set_column('B:F', 35)
    worksheet7.set_column('A:A', 12)
    
    df7ic = pd.DataFrame.from_records(sn_baddir[1], columns=labels7)
    df7ic.to_excel(writer, sheet_name='Session with bad file path',startrow=2,index=False)
    worksheet7.write('A1','Session with incorrect bad file path', header_format)
    worksheet7.conditional_format(snbaddir, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #List of cache transformations
    df8c = pd.DataFrame.from_records(sn_cachdir[0], columns=labels8)
    df8c.to_excel(writer, sheet_name='List of cache transformations',startrow=sn_cachdir[2]+4,index=False)
    worksheet8 = writer.sheets['List of cache transformations']
    worksheet8.write(sncach_hdr2,'List of transformations with correct cache directory path', header_format)
    worksheet8.set_column('B:F', 35)
    worksheet8.set_column('A:A', 12)
    
    df8ic = pd.DataFrame.from_records(sn_cachdir[1], columns=labels8)
    df8ic.to_excel(writer, sheet_name='List of cache transformations',startrow=2,index=False)
    worksheet8.write('A1','List of transformations with incorrect cache directory path', header_format)
    worksheet8.conditional_format(sncachdir, {'type': 'text',
                                            'criteria': 'begins with',
                                            'value' : '$',
                                            'format':  format1})
    
    #Mapping variables and parameters
    df9 = pd.DataFrame.from_records(sn_map_c, columns=labels9)
    df9.to_excel(writer, sheet_name='Mapping with variables',startrow=2,index=False)
    worksheet9 = writer.sheets['Mapping with variables']
    worksheet9.write('A1','Mapping with persistent variables and Parameters', header_format)
    worksheet9.set_column('B:F', 35)
    worksheet9.set_column('A:A', 12)
    
    #Command task with hard coded values
    df10 = pd.DataFrame.from_records(sn_comm_c, columns=labels10)
    df10.to_excel(writer, sheet_name='Command task',startrow=2,index=False)
    worksheet10 = writer.sheets['Command task']
    worksheet10.write('A1','Command task with hardcoded paths', header_format)
    worksheet10.set_column('B:F', 35)
    worksheet10.set_column('A:A', 12)
    
    #Transformation level verbose tracing
    df11 = pd.DataFrame.from_records(sn_trans_ver, columns=labels11)
    df11.to_excel(writer, sheet_name='Transformation Tracing',startrow=2,index=False)
    worksheet11 = writer.sheets['Transformation Tracing']
    worksheet11.write('A1','Transformation Level Verbose Tracing', header_format)
    worksheet11.set_column('B:F', 35)
    worksheet11.set_column('A:A', 12)
    
    #Session level verbose tracing
    df12 = pd.DataFrame.from_records(sn_verbose, columns=labels12)
    df12.to_excel(writer, sheet_name='Session Tracing',startrow=2,index=False)
    worksheet12 = writer.sheets['Session Tracing']
    worksheet12.write('A1','Session Level Verbose Tracing', header_format)
    worksheet12.set_column('B:F', 35)
    worksheet12.set_column('A:A', 12)
    
    #Session count
    df13 = pd.DataFrame.from_records(sn_cnt, columns=labels13)
    df13.to_excel(writer, sheet_name='Session Count',startrow=2,index=False)
    worksheet13 = writer.sheets['Session Count']
    worksheet13.write('A1','Session Count by project folder', header_format)
    worksheet13.set_column('A:C', 18)
    
    #Workflow count
    df14 = pd.DataFrame.from_records(wf_cnt, columns=labels14)
    df14.to_excel(writer, sheet_name='Workflow Count',startrow=2,index=False)
    worksheet14 = writer.sheets['Workflow Count']
    worksheet14.write('A1','Workflow Count by project folder', header_format)
    worksheet14.set_column('A:C', 18)
    
    #Mapping count
    df15 = pd.DataFrame.from_records(mp_cnt, columns=labels15)
    df15.to_excel(writer, sheet_name='Mapping Count',startrow=2,index=False)
    worksheet15 = writer.sheets['Mapping Count']
    worksheet15.write('A1','Mapping Count by project folder', header_format)
    worksheet15.set_column('A:C', 18)
    
    writer.save()
    writer.close()
    #format1 = wb.add_format({"bold": True, 'font_color': '#9C0006'})
    #format2 = wb.add_format({"bold": True, 'font_color': 'green'})
    
    
    #worksheet.set_column('B:B', 18, format1)
    #worksheet.set_column('C:C', 18, format2)
    
    # Write the column headers with the defined format.
    #worksheet.conditional_format('B2:B8', {'type': '3_color_scale'}) 

#------------------------------    
def parseXML_wf_logdir(xml_file):
    """
    Parse XML with ElementTree
    """
    file_name = xml_file
    #full_file = os.path.abspath(os.path.join(file_name))
    #tree = ET.parse(full_file)
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(file_name,parser=parser)
    root = tree.getroot()
    
    wf_lst_c=[]
    wf_lst_ic=[]
    n=3
    for child in root:
       for folder in child.iter('FOLDER'):
            wf_nm=[]            
            fl=folder.get('NAME')
            wf_nm.append(fl)
            #print (fl)
            
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wf_nm.append(workflow.get('NAME'))
                 #wn = workflow.get('NAME')
                 #print (wn)
                 for workattrb in workflow.iter('ATTRIBUTE'):
                      if workattrb.get('NAME') == "Workflow Log File Name":
                          wf_nm.append(workattrb.get('VALUE'))
                      if workattrb.get('NAME') == "Workflow Log File Directory":
                          wf_nm.append(workattrb.get('VALUE'))
                          wldn = workattrb.get('VALUE')
                          if wldn.find("\\") > 0:
                             wlfn = wldn[wldn.find("\\")+1 : len(wldn)-1]
                          elif wldn.find("/")> 0:
                              wlfn = wldn[wldn.find("/")+1 : len(wldn)-1]
                          else:
                              wlfn = wldn
                          #print (wlfn)
                 if wlfn == fl:
                    obj1 = tuple(wf_nm)
                    wf_lst_c.append(obj1)
                    wf_nm.clear()
                    wf_nm.append(fl)
                 else:
                     obj1 = tuple(wf_nm)
                     wf_lst_ic.append(obj1)
                     n = n+1
                     wf_nm.clear()
                     wf_nm.append(fl)
            
            wf_nm.clear()
            #print (wf_lst_c)
    return (wf_lst_c,wf_lst_ic,n)

#---------------------------------
def parseXML_sn_logdir(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
                     
    sn_lst_c=[]
    sn_lst_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]
            fl=folder.get('NAME')           
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              
                              if wltn == wtn:
                                  for wktskinst in wklet.iter('TASKINSTANCE'):
                                      wty = wktskinst.get('TASKTYPE')
                                      if wty == "Session":
                                          tn = wktskinst.get('TASKNAME')
                                          nm = wktskinst.get('NAME')
                                          rs = wktskinst.get('REUSABLE')
                                          #print (tn)
                                          slfn1 = ""
                                          for log in wktskinst.iter('ATTRIBUTE'):
                                              if log.get('NAME') == "Session Log File Name":
                                                  slfn1 = log.get('VALUE')
                                                  
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              #print (sn)
                                              if sn == tn:
                                                  for attrib in session.iter('ATTRIBUTE'):
                                                      if attrib.get('NAME') == "Session Log File Name":
                                                          slfn2 = attrib.get('VALUE')
                                                          if nm == tn:
                                                              slfn = slfn2
                                                          else:
                                                              slfn = slfn1
                                                      if attrib.get('NAME') == "Session Log File directory":
                                                          ldn = attrib.get('VALUE')
                                                          if ldn.find("/") > 0:
                                                              dfn = ldn[ldn.find("/")+1:len(ldn)-1]
                                                          elif ldn.find("\\") > 0:
                                                              dfn = ldn[ldn.find("\\")+1:len(ldn)-1]
                                                          else:
                                                              dfn = ldn
                                                              
                                                  sn_nm.extend((fl,wn,nm,rs,slfn,ldn))        
                                                          
                                                  if dfn == fl or ldn == "":
                                                      #print (sn_nm)
                                                      obj1 = tuple(sn_nm)
                                                      sn_lst_c.append(obj1)
                                                      sn_nm.clear()
                                                  else:
                                                      obj1 = tuple(sn_nm)
                                                      sn_lst_ic.append(obj1)
                                                      n = n+1
                                                      #print (sn_nm)
                                                      sn_nm.clear()              
                                                        
                      elif ty == "Session":
                          nm = taskinst.get('NAME')
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          slfn1 = ""
                          for log in taskinst.iter('ATTRIBUTE'):
                              if log.get('NAME') == "Session Log File Name":
                                   slfn1 = log.get('VALUE')
                          
                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 if sn == tn:
                                    for logdir in wsn.iter('ATTRIBUTE'):
                                         if logdir.get('NAME') == "Session Log File Name":
                                             slfn = logdir.get('VALUE')
                                         if logdir.get('NAME') == "Session Log File directory":
                                             ldn = logdir.get('VALUE')
                                             if ldn.find("/") > 0 :
                                                 dfn = ldn[ldn.find("/")+1:len(ldn)-1]
                                             elif ldn.find("\\") > 0:
                                                 dfn = ldn[ldn.find("\\")+1:len(ldn)-1]
                                             else:
                                                 dfn = ldn
                                           
                                    sn_nm.extend((fl,wn,nm,rs,slfn,ldn))
                                    
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     for logdir in session.iter('ATTRIBUTE'):
                                         if logdir.get('NAME') == "Session Log File Name":
                                             slfn2 = logdir.get('VALUE')
                                             if nm == tn:
                                                slfn = slfn2
                                             else:
                                                 slfn = slfn1
                                                 
                                         if logdir.get('NAME') == "Session Log File directory":
                                             ldn = logdir.get('VALUE')
                                             if ldn.find("/") > 0:
                                                 dfn = ldn[ldn.find("/")+1:len(ldn)-1]
                                             elif ldn.find("\\") > 0:
                                                 dfn = ldn[ldn.find("\\")+1:len(ldn)-1]
                                             else:
                                                 dfn = ldn
                                                 
                                     sn_nm.extend((fl,wn,nm,rs,slfn,ldn))  
                    
                          if dfn == fl or ldn == "":
                             #print(sn_nm)
                             obj1 = tuple(sn_nm)
                             sn_lst_c.append(obj1)
                             sn_nm.clear()
                          else:
                             obj1 = tuple(sn_nm)
                             sn_lst_ic.append(obj1)
                             n = n+1
                             sn_nm.clear()

    return (sn_lst_c,sn_lst_ic,n)

#----------------------------------------------
def parseXML_wf_parmfile(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
    
    wf_parm_c=[]
    wf_parm_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            wf_nm=[]          
            fl=folder.get('NAME')
            
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                wn = workflow.get('NAME') 
                for workattrb in workflow.iterfind('ATTRIBUTE'):
                      if workattrb.get('NAME') == "Parameter Filename":
                          wpf = workattrb.get('VALUE')
                          if wpf.find("\\") > 0:
                              wlfn = wpf[find_nth(wpf,"\\", 2)+1 : find_nth(wpf,"\\", 3)]
                          elif wpf.find("/") > 0:
                              wlfn = wpf[find_nth(wpf,"/", 2)+1 : find_nth(wpf,"/", 3)]
                          else:
                              wlfn = wpf
                          wf_nm.extend((fl,wn,wpf))
                if wlfn == fl or wlfn == "":
                    obj1 = tuple(wf_nm)
                    wf_parm_c.append(obj1)
                    wf_nm.clear()
                else:
                     obj1 = tuple(wf_nm)
                     wf_parm_ic.append(obj1)
                     n = n+1
                     wf_nm.clear()
            
    return (wf_parm_c,wf_parm_ic,n)
        
#----------------------------------------------
def parseXML_sn_parmfile(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
    
    sn_parm_c=[]
    sn_parm_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]
            fl=folder.get('NAME')
         
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          #print (wtn)
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              
                              if wltn == wtn:
                                  for wktskinst in wklet.iter('TASKINSTANCE'):
                                      wty = wktskinst.get('TASKTYPE')
                                      if wty == "Session":
                                          tn = wktskinst.get('TASKNAME')
                                          nm = wktskinst.get('NAME')
                                          rs = wktskinst.get('REUSABLE')
                                          
                                          pf2 = ""
                                          for log in wktskinst.iter('ATTRIBUTE'):
                                              if log.get('NAME') == "Parameter Filename":
                                                  pf2 = log.get('VALUE')
                                                  
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              if sn == tn:
                                                  for attrib in session.iter('ATTRIBUTE'):
                                                      if attrib.get('NAME') == "Parameter Filename":
                                                          pf1 = attrib.get('VALUE')
                                                          if nm == tn or pf2 == "":
                                                              pf = pf1
                                                              if pf1.find("/") > 0:
                                                                  pffn = pf1[find_nth(pf1,"/", 2)+1 : find_nth(pf1,"/", 3)]
                                                              elif pf1.find("\\") > 0:
                                                                  pffn = pf1[find_nth(pf1,"\\", 2)+1 : find_nth(pf1,"\\", 3)]
                                                              else:
                                                                  pffn = pf1
                                                          else:
                                                              pf = pf2
                                                              if pf2.find("/") > 0 :
                                                                  pffn = pf2[find_nth(pf2,"/", 2)+1 : find_nth(pf2,"/", 3)]
                                                              elif pf2.find("\\") > 0:
                                                                  pffn = pf2[find_nth(pf2,"\\", 2)+1 : find_nth(pf2,"\\", 3)]
                                                              else:
                                                                  pffn = pf2
                                                                  
                                                  sn_nm.extend((fl,wn,nm,rs,pf))
                                                  
                                                  if pffn == fl or pf == "":
                                                      #print (sn_nm)
                                                      obj1 = tuple(sn_nm)
                                                      sn_parm_c.append(obj1)
                                                      sn_nm.clear()
                                                  else:
                                                      obj1 = tuple(sn_nm)
                                                      sn_parm_ic.append(obj1)
                                                      n = n+1
                                                      #print (sn_nm)
                                                      sn_nm.clear()
                                                      
                      elif ty == "Session":
                          nm = taskinst.get('NAME')
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          
                          pf2 = ""
                          for log in taskinst.iter('ATTRIBUTE'):
                              if log.get('NAME') == "Parameter Filename":
                                   pf2 = log.get('VALUE')
                                            
                          if rs == "NO":
                             for wsession in workflow.findall('SESSION'):
                                  sn = wsession.get('NAME')
                                  if sn == tn:
                                     for logdir in wsession.iter('ATTRIBUTE'):
                                         if logdir.get('NAME') == "Parameter Filename":
                                             pf = logdir.get('VALUE')
                                             if pf.find("/") > 0:
                                                 pffn = pf[find_nth(pf,"/", 2)+1 : find_nth(pf,"/", 3)]
                                             elif pf.find("\\") > 0:
                                                 pffn = pf[find_nth(pf,"\\", 2)+1 : find_nth(pf,"\\", 3)]
                                             else:
                                                 pffn = pf
                                                 
                                     sn_nm.extend((fl,wn,nm,rs,pf))   
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     for logdir in session.iter('ATTRIBUTE'):
                                         if logdir.get('NAME') == "Parameter Filename":
                                             pf1 = logdir.get('VALUE')
                                             if nm == tn or pf2 == "":
                                                 pf = pf1
                                                 if pf1.find("/") > 0:
                                                     pffn = pf1[find_nth(pf1,"/", 2)+1 : find_nth(pf1,"/", 3)]
                                                 elif pf1.find("\\") > 0:
                                                     pffn = pf1[find_nth(pf1,"\\", 2)+1 : find_nth(pf1,"\\", 3)]
                                                 else:
                                                     pffn = pf1                                                 
                                             else:
                                                 pf = pf2
                                                 if pf2.find("/") > 0 :
                                                     pffn = pf2[find_nth(pf2,"/", 2)+1 : find_nth(pf2,"/", 3)]
                                                 elif pf2.find("\\") > 0:
                                                     pffn = pf2[find_nth(pf2,"\\", 2)+1 : find_nth(pf2,"\\", 3)]
                                                 else:
                                                     pffn = pf2 
                                                                                                 
                                     sn_nm.extend((fl,wn,nm,rs,pf))
                          if pffn == fl or pf == "":
                              obj1 = tuple(sn_nm)
                              sn_parm_c.append(obj1)
                              #print (sn_nm)
                              sn_nm.clear()
                          else:
                             obj1 = tuple(sn_nm)
                             #print (sn_nm)
                             sn_parm_ic.append(obj1)
                             n = n+1
                             sn_nm.clear()
    #print (sn_parm_c)
    return (sn_parm_c,sn_parm_ic,n)    
        
#---------------------------------
def parseXML_sn_srcdir(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()                 
    
    sn_src_c=[]
    sn_src_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]            
            fl=folder.get('NAME')

            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              if wltn == wtn:
                                  for tskinst in wklet.iter('TASKINSTANCE'):
                                      wty = tskinst.get('TASKTYPE')
                                      
                                      if wty == "Session":
                                          tn = tskinst.get('TASKNAME')
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              #sn_nm.append(sn)
                                              if sn == tn:
                                                  for sesext in session.iter('SESSIONEXTENSION'):
                                                      if sesext.get('DSQINSTTYPE') == "Source Qualifier" and sesext.get('NAME') == "File Reader":
                                                          for attrb in sesext.iter('ATTRIBUTE'):
                                                              if attrb.get('NAME') == "Source file directory":
                                                                  srcd = attrb.get('VALUE')
                                                                  if srcd.find("\\") > 0:
                                                                     srfn = srcd[find_nth(srcd,"\\", 2)+1 : find_nth(srcd,"\\", 3)]
                                                                  elif srcd.find("/") > 0:
                                                                     srfn = srcd[find_nth(srcd,"/", 2)+1 : find_nth(srcd,"/", 3)]
                                                                  else:
                                                                      srfn = srcd
                                                     
                                                              if attrb.get('NAME') == "Source filename":
                                                                  sfn = attrb.get('VALUE')
                                                          sn_nm.extend((fl,wn,sn,srcd,sfn))
                                                          
                                                          if srfn == fl or srfn == "":
                                                              obj1 = tuple(sn_nm)
                                                              sn_src_c.append(obj1)
                                                              #print (sn_nm)
                                                              sn_nm.clear()
                                                          else:
                                                              #print (sn_nm)
                                                              obj1 = tuple(sn_nm)
                                                              sn_src_ic.append(obj1)
                                                              n = n+1
                                                              sn_nm.clear()
                                                            
                      elif ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          
                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 if sn == tn:
                                    for sesext in wsn.iter('SESSIONEXTENSION'):
                                         if sesext.get('DSQINSTTYPE') == "Source Qualifier" and sesext.get('NAME') == "File Reader":
                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Source file directory":
                                                     srcd = attrb.get('VALUE')
                                                     if srcd.find("/") > 0:
                                                        srfn = srcd[find_nth(srcd,"/", 2)+1 : find_nth(srcd,"/", 3)]
                                                     elif srcd.find("\\") > 0:
                                                        srfn = srcd[find_nth(srcd,"\\", 2)+1 : find_nth(srcd,"\\", 3)]
                                                     else:
                                                         srfn = srcd
                                                     
                                                 if attrb.get('NAME') == "Source filename":
                                                      sfn = attrb.get('VALUE')
                                             sn_nm.extend((fl,wn,sn,srcd,sfn))
                                             
                                             if srfn == fl or srfn == "":
                                                 #print(sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_src_c.append(obj1)
                                                 sn_nm.clear()
                                             else:
                                                 obj1 = tuple(sn_nm)
                                                 sn_src_ic.append(obj1)
                                                 n = n+1
                                                 sn_nm.clear()
                                 
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     for sesext in session.iter('SESSIONEXTENSION'):
                                         if sesext.get('DSQINSTTYPE') == "Source Qualifier" and sesext.get('NAME') == "File Reader":
                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Source file directory":
                                                     srcd = attrb.get('VALUE')
                                                     if srcd.find("/") > 0:
                                                         srfn = srcd[find_nth(srcd,"/", 2)+1 : find_nth(srcd,"/", 3)]
                                                     elif srcd.find("\\") > 0:
                                                         srfn = srcd[find_nth(srcd,"\\", 2)+1 : find_nth(srcd,"\\", 3)]
                                                     else:
                                                         srfn = srcd
                                                     
                                                 if attrb.get('NAME') == "Source filename":
                                                      sfn = attrb.get('VALUE')                                      
                                             sn_nm.extend((fl,wn,sn,srcd,sfn))
                                             
                                             if srfn == fl or srfn == "":
                                                 #print(sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_src_c.append(obj1)
                                                 sn_nm.clear()
                                             else:
                                                 #print (sn_mnm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_src_ic.append(obj1)
                                                 n = n+1
                                                 sn_nm.clear()                                               
    #print (sn_src_c)
    return (sn_src_c,sn_src_ic,n)

#--------------------------------------
def parseXML_sn_tgtdir(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
                
    sn_tgt_c=[]
    sn_tgt_ic=[] 
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]
            fl=folder.get('NAME')
                        
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              
                              if wltn == wtn:
                                  for tskinst in wklet.iter('TASKINSTANCE'):
                                      wty = tskinst.get('TASKTYPE')
                                      if wty == "Session":
                                          tn = tskinst.get('TASKNAME')
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              if sn == tn:
                                                  for sesext in session.iter('SESSIONEXTENSION'):
                                                      if sesext.get('NAME') == "File Writer":
                                                          for attrb in sesext.iter('ATTRIBUTE'):
                                                              if attrb.get('NAME') == "Output file directory":
                                                                  tgtd = attrb.get('VALUE')
                                                                  if tgtd.find("\\") > 0:
                                                                      tgfn = tgtd[find_nth(tgtd,"\\", 1)+1 : find_nth(tgtd,"\\", 2)]
                                                                  elif tgtd.find("/") > 0:
                                                                       tgfn = tgtd[find_nth(tgtd,"/", 1)+1 : find_nth(tgtd,"/", 2)]
                                                                  else:
                                                                      tgfn = tgtd
                                                     
                                                              if attrb.get('NAME') == "Output filename":
                                                                  tfn = attrb.get('VALUE')
                                                                  
                                                          sn_nm.extend((fl,wn,sn,tgtd,tfn)) 
                                                          
                                                          if tgfn == fl or tgtd == "":
                                                                  obj1 = tuple(sn_nm)
                                                                  sn_tgt_c.append(obj1)
                                                                  #print (sn_nm)
                                                                  sn_nm.clear()
                                                          else:
                                                              obj1 = tuple(sn_nm)
                                                              sn_tgt_ic.append(obj1)
                                                              n = n+1
                                                              #print (sn_nm)
                                                              sn_nm.clear()
                                              
                      elif ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')

                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 #sn_nm.append(sn)
                                 if sn == tn:
                                    for sesext in wsn.iter('SESSIONEXTENSION'):
                                         if sesext.get('NAME') == "File Writer":
                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Output file directory":
                                                     tgtd = attrb.get('VALUE')
                                                     if tgtd.find("/") > 0:
                                                         tgfn = tgtd[find_nth(tgtd,"/", 1)+1 : find_nth(tgtd,"/", 2)]
                                                     elif tgtd.find("\\") > 0:
                                                         tgfn = tgtd[find_nth(tgtd,"\\", 1)+1 : find_nth(tgtd,"\\", 2)]
                                                     else:
                                                         tgfn = tgtd
                                                     
                                                 if attrb.get('NAME') == "Output filename":
                                                      tfn = attrb.get('VALUE')
                                                      #sn_nm.append(tfn)
                                             sn_nm.extend((fl,wn,sn,tgtd,tfn))
                                             
                                             if tgfn == fl or tgfn == "":
                                                 #print(sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_tgt_c.append(obj1)
                                                 sn_nm.clear()
                                             else:
                                                 #print (sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_tgt_ic.append(obj1)
                                                 n = n+1
                                                 sn_nm.clear()
                                 
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     for sesext in session.iter('SESSIONEXTENSION'):
                                         if sesext.get('NAME') == "File Writer":
                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Output file directory":
                                                     tgtd = attrb.get('VALUE')
                                                     if tgtd.find("\\") > 0:
                                                        tgfn = tgtd[find_nth(tgtd,"\\", 1)+1 : find_nth(tgtd,"\\", 2)]
                                                     elif tgtd.find("/") > 0:
                                                         tgfn = tgtd[find_nth(tgtd,"/", 1)+1 : find_nth(tgtd,"/", 2)]
                                                     else:
                                                         tgfn = tgtd
                                                     
                                                 if attrb.get('NAME') == "Output filename":
                                                      tfn = attrb.get('VALUE')                                     
                                             sn_nm.extend((fl,wn,sn,tgtd,tfn))
                                             
                                             if tgfn == fl or tgfn == "":
                                                 #print(sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_tgt_c.append(obj1)
                                                 sn_nm.clear()
                                             else:
                                                 #print (sn_nm)
                                                 obj1 = tuple(sn_nm)
                                                 sn_tgt_ic.append(obj1)
                                                 n = n+1
                                                 sn_nm.clear()                    
    #print (sn_tgt_c)        
    return (sn_tgt_c,sn_tgt_ic,n)
        
#------------------------------------
def parseXML_sn_baddir(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()                 
    
    sn_bad_c=[]
    sn_bad_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]           
            fl=folder.get('NAME')

            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              
                              if wltn == wtn:
                                  for tskinst in wklet.iter('TASKINSTANCE'):
                                      wty = tskinst.get('TASKTYPE')
                                      if wty == "Session":
                                          tn = tskinst.get('TASKNAME')
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              if sn == tn:
                                                  for sesext in session.iter('SESSIONEXTENSION'):
                                                      if sesext.get('NAME') == "File Writer" or sesext.get('NAME') == "Relational Writer":
                                                          sint = sesext.get('SINSTANCENAME')
                                                          for attrb in sesext.iter('ATTRIBUTE'):
                                                              if attrb.get('NAME') == "Reject file directory":
                                                                  rejd = attrb.get('VALUE')
                                                                  if rejd.find("/") > 0:
                                                                     refn = rejd[find_nth(rejd,"/", 1)+1 : find_nth(rejd,"/", 2)]
                                                                  elif rejd.find("\\") > 0:
                                                                     refn = rejd[find_nth(rejd,"\\", 1)+1 : find_nth(rejd,"\\", 2)]
                                                                  else:
                                                                      refn = rejd
                                                     
                                                              if attrb.get('NAME') == "Reject filename":
                                                                  rfn = attrb.get('VALUE') 
                                                                  
                                                          sn_nm.extend((fl,wn,sn,sint,rejd,rfn))
                                                          
                                                          if refn == fl or refn == "":
                                                             obj1 = tuple(sn_nm)
                                                             sn_bad_c.append(obj1)
                                                             #print (sn_nm)
                                                             sn_nm.clear()
                                                          else:
                                                              obj1 = tuple(sn_nm)
                                                              sn_bad_ic.append(obj1)
                                                              n = n+1
                                                              sn_nm.clear()    
                      if ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          
                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 if sn == tn:
                                    for sesext in wsn.iter('SESSIONEXTENSION'):
                                         if sesext.get('NAME') == "File Writer" or sesext.get('NAME') == "Relational Writer":
                                             sint = sesext.get('SINSTANCENAME')
                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Reject file directory":
                                                     rejd = attrb.get('VALUE')
                                                     if rejd.find("/") > 0:
                                                        refn = rejd[find_nth(rejd,"/", 1)+1 : find_nth(rejd,"/", 2)]
                                                     elif rejd.find("\\") > 0:
                                                        refn = rejd[find_nth(rejd,"\\", 1)+1 : find_nth(rejd,"\\", 2)]
                                                     else:
                                                         refn = rejd
                             
                                                 if attrb.get('NAME') == "Reject filename":
                                                      rfn = attrb.get('VALUE')

                                             sn_nm.extend((fl,wn,sn,sint,rejd,rfn))
                                             
                                             if refn == fl or refn == "":
                                                 obj1 = tuple(sn_nm)
                                                 sn_bad_c.append(obj1)                                                 
                                                 sn_nm.clear()
                                             else:
                                                 obj1 = tuple(sn_nm)
                                                 sn_bad_ic.append(obj1)
                                                 n = n+1            
                                                 sn_nm.clear()                                          
                                                 
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     for sesext in session.iter('SESSIONEXTENSION'):
                                         if sesext.get('NAME') == "File Writer" or sesext.get('NAME') == "Relational Writer":
                                             sint = sesext.get('SINSTANCENAME')

                                             for attrb in sesext.iter('ATTRIBUTE'):
                                                 if attrb.get('NAME') == "Reject file directory":
                                                     rejd = attrb.get('VALUE')
                                                     if rejd.find("/") > 0:
                                                        refn = rejd[find_nth(rejd,"/", 1)+1 : find_nth(rejd,"/", 2)]
                                                     elif rejd.find("\\") > 0:
                                                         refn = rejd[find_nth(rejd,"\\", 1)+1 : find_nth(rejd,"\\", 2)]
                                                     else:
                                                         refn = rejd
                                                     
                                                 if attrb.get('NAME') == "Reject filename":
                                                      rfn = attrb.get('VALUE')
                                       
                                             sn_nm.extend((fl,wn,sn,sint,rejd,rfn))
                                             
                                             if refn == fl or refn == "":
                                                 obj1 = tuple(sn_nm)
                                                 sn_bad_c.append(obj1)
                                                 #print (sn_nm)
                                                 sn_nm.clear()
                                             else:
                                                 obj1 = tuple(sn_nm)
                                                 sn_bad_ic.append(obj1)
                                                 n = n+1
                                                 sn_nm.clear()                                                                                                 
                 
    #print (sn_bad_c)
    return (sn_bad_c,sn_bad_ic,n)
        
#--------------------------------------------------
def parseXML_trans_cachedir(xml_file):
    """
    Parse XML with ElementTree
    """
    # open a file for writing
    
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()                
    
    sn_cach_c=[]
    sn_cach_ic=[]
    n = 3
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]           
            fl=folder.get('NAME')
                        
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                         wtn = taskinst.get('TASKNAME')
                         for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              
                              if wltn == wtn:
                                  for tskinst in wklet.iter('TASKINSTANCE'):
                                      wty = tskinst.get('TASKTYPE')
                                      
                                      if wty == "Session":
                                          tn = tskinst.get('TASKNAME')
                                          
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              mn = session.get('MAPPINGNAME')
                                              
                                              if sn == tn:
                                                   for sesext in session.iter('SESSTRANSFORMATIONINST'):
                                                       tsnm = sesext.get('TRANSFORMATIONNAME')
                                                       tsty =  sesext.get('TRANSFORMATIONTYPE')                                            
                                                       for attrb in sesext.iter('ATTRIBUTE'):
                                                           atn = attrb.get('NAME')
                                                           if atn == "Cache Directory" or atn == "Lookup cache directory name":
                                                               cachd = attrb.get('VALUE')
                                                               if cachd.find("/") > 0:
                                                                  cafn = cachd[find_nth(cachd,"/", 1)+1 : find_nth(cachd,"/", 2)]
                                                               elif cachd.find("\\") > 0:
                                                                   cafn = cachd[find_nth(cachd,"\\", 1)+1 : find_nth(cachd,"\\", 2)]
                                                               else:
                                                                   cafn = cachd
                                                               
                                                               sn_nm.extend((fl,wn,tn,mn,tsnm,tsty,cachd))
                                                     
                                                               if cafn == fl or cachd == "":
                                                                   obj1 = tuple(sn_nm)
                                                                   sn_cach_c.append(obj1)
                                                                   #print (sn_nm)
                                                                   sn_nm.clear()
                                                               else:
                                                                   obj1 = tuple(sn_nm)
                                                                   sn_cach_ic.append(obj1)
                                                                   n = n+1
                                                                   #print (sn_nm)
                                                                   sn_nm.clear()
                                                  
                          
                      elif ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          
                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 mn = wsn.get('MAPPINGNAME')
                                 
                                 if sn == tn:
                                    for sesext in wsn.iter('SESSTRANSFORMATIONINST'):
                                         tsnm = sesext.get('TRANSFORMATIONNAME')
                                         tsty =  sesext.get('TRANSFORMATIONTYPE')
                                             
                                         for attrb in sesext.iter('ATTRIBUTE'):
                                             atn = attrb.get('NAME')
                                             if atn == "Cache Directory" or atn == "Lookup cache directory name":
                                                 cachd = attrb.get('VALUE')
                                                 if cachd.find("/") > 0:
                                                    cafn = cachd[find_nth(cachd,"/", 1)+1 : find_nth(cachd,"/", 2)]  
                                                 elif cachd.find("\\") > 0:
                                                    cafn = cachd[find_nth(cachd,"\\", 1)+1 : find_nth(cachd,"\\", 2)] 
                                                 else:
                                                     cafn = cachd
                                                     
                                                 sn_nm.extend((fl,wn,tn,mn,tsnm,tsty,cachd))
                                                     
                                                 if cafn == fl or cachd == "":
                                                     obj1 = tuple(sn_nm)
                                                     sn_cach_c.append(obj1)
                                                     #print (sn_nm)
                                                     sn_nm.clear()                                                     
                                                     
                                                 else:
                                                     obj1 = tuple(sn_nm)
                                                     sn_cach_ic.append(obj1) 
                                                     n = n+1
                                                     #print (sn_nm)
                                                     sn_nm.clear()                                                     
                                                 
                          elif rs == "YES":
                              for sess in folder.findall('SESSION'):
                                 sn = sess.get('NAME')
                                 mn = sess.get('MAPPINGNAME')
                                 if sn == tn:
                                    for sesext in sess.iter('SESSTRANSFORMATIONINST'):
                                         tsnm = sesext.get('TRANSFORMATIONNAME')
                                         tsty =  sesext.get('TRANSFORMATIONTYPE')
                                             
                                         for attrb in sesext.iter('ATTRIBUTE'):
                                             atn = attrb.get('NAME')
                                             if atn == "Cache Directory" or atn == "Lookup cache directory name":
                                                 cachd = attrb.get('VALUE')
                                                 if cachd.find("/") > 0:
                                                    cafn = cachd[find_nth(cachd,"/", 1)+1 : find_nth(cachd,"/", 2)]
                                                 elif cachd.find("\\") > 0:
                                                     cafn = cachd[find_nth(cachd,"\\", 1)+1 : find_nth(cachd,"\\", 2)]
                                                 else:
                                                     cafn = cachd
                                                     
                                                 sn_nm.extend((fl,wn,tn,mn,tsnm,tsty,cachd))
                                                     
                                                 if cafn == fl or cachd == "":
                                                     obj1 = tuple(sn_nm)
                                                     sn_cach_c.append(obj1)
                                                     #print (sn_nm)
                                                     sn_nm.clear()                                                     
                                                     
                                                 else:
                                                    obj1 = tuple(sn_nm)
                                                    sn_cach_ic.append(obj1)
                                                    n = n+1          
                                                    sn_nm.clear()                                                                                             
    #print (sn_cach_c)
    return (sn_cach_c,sn_cach_ic,n)

#-------------------------------
def parseXML_map_var(xml_file):
    """
    Parse XML with ElementTree
    """
    # open a file for writing
    
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()                 
    
    #n = 3
    sn_map_c=[]
    mapp_list=[]
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]
            fl=folder.get('NAME')
                        
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 #print (wn)
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      
                      if ty == "Worklet":
                          wtn = taskinst.get('TASKNAME')
                          for wklet in folder.findall('WORKLET'):
                              wltn = wklet.get('NAME')
                              if wltn == wtn:
                                  for tskinst in wklet.iter('TASKINSTANCE'):
                                      wty = tskinst.get('TASKTYPE')
                                      if wty == "Session":
                                          tn = tskinst.get('TASKNAME')
                                          for session in folder.findall('SESSION'):
                                              sn = session.get('NAME')
                                              if sn == tn:
                                                  smn = session.get('MAPPINGNAME')
                                                  mapp_list.append(smn)                                                 
                          
                      elif ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          tn = taskinst.get('TASKNAME')
                          
                          if rs == "NO":
                             for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 if sn == tn:
                                    smn = wsn.get('MAPPINGNAME') 
                                    mapp_list.append(smn)
                                                 
                          elif rs == "YES":
                              for session in folder.findall('SESSION'):
                                 sn = session.get('NAME')
                                 if sn == tn:
                                     smn = session.get('MAPPINGNAME')
                                     mapp_list.append(smn)

                 for mappnm in set(mapp_list):
                     #print (mappnm)
                     for mapp in folder.findall('MAPPING'):
                          mn = mapp.get('NAME')
                          if mappnm == mn:
                              for mapvar in mapp.findall('MAPPINGVARIABLE'):
                                  an = mapvar.get('NAME')
                                  isprm = mapvar.get('ISPARAM')
                                  if isprm == "YES":
                                      prm = "Parameter"
                                  else:
                                      prm = "Variable"
                                  deflt = mapvar.get('DEFAULTVALUE')
                                                 
                                  sn_nm.extend((fl,wn,mappnm,an,prm,deflt))
                                  obj = tuple(sn_nm)
                                  sn_map_c.append(obj)
                                  sn_nm.clear()
                 mapp_list.clear()    
                                            
    #print (n)
    return (sn_map_c) 
                  
#-------------------------------
def parseXML_comm_tsk(xml_file):
    """
    Parse XML with ElementTree
    """
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()                
    
    sn_comm_c=[]
    cm_list = ['rm ','rmdir ','gzip ','mv ','cat ','chmod ','ftp ','cp ','unset ','cat ','ls ','cd ','ll ']
    for child in root:
       for folder in child.iter('FOLDER'):
            sn_nm=[]
            fl=folder.get('NAME')
                        
            #Parsing for workflow log file path
            for workflow in folder.iter('WORKFLOW'):
                 wn = workflow.get('NAME')
                 #print (wn)
                 for taskinst in workflow.iter('TASKINSTANCE'):
                      ty = taskinst.get('TASKTYPE')
                      tn = taskinst.get('TASKNAME')
                      tin = taskinst.get('NAME')
                      if ty == "Command":
                          rs = taskinst.get('REUSABLE')
                          for cmd in workflow.findall('TASK'):
                              ctn = cmd.get('NAME')
                              if ctn == tn:
                                  for value in cmd.findall('VALUEPAIR'):
                                      val = value.get('VALUE')
                                      for str1 in cm_list:
                                          if val.find(str1) >= 0:
                                              sn_nm.extend((fl,wn,ctn,rs,val,tin))
                                              #print (sn_nm)
                                              obj = tuple(sn_nm)
                                              sn_comm_c.append(obj)
                                              sn_nm.clear()
                                              break
                                      print (sn_comm_c)    
                          
                      if ty == "Session":
                          rs = taskinst.get('REUSABLE')
                          if rs == "YES":
                              for sescom in taskinst.iterfind('SESSIONCOMPONENT/TASK'):
                                  ctn = sescom.get('NAME')
                                  trs = sescom.get('REUSABLE')
                                  for value in sescom.findall('VALUEPAIR'):
                                      val = value.get('VALUE')
                                      if ctn.find("command") >0:
                                          for str1 in cm_list:
                                              if val.find(str1) >= 0:
                                                  sn_nm.extend((fl,wn,ctn,trs,val,tin))
                                                  #print (sn_nm)
                                                  obj = tuple(sn_nm)
                                                  sn_comm_c.append(obj)
                                                  sn_nm.clear()
                                                  break
                               
                          if rs == "NO":
                               for wsn in workflow.findall('SESSION'):
                                 sn = wsn.get('NAME')
                                 if sn == tn:
                                      for sescom in wsn.iterfind('SESSIONCOMPONENT/TASK'):
                                          ctn = sescom.get('NAME')
                                          #cty = sescom.get('TYPE')
                                          trs = sescom.get('REUSABLE')
                                          for value in sescom.findall('VALUEPAIR'):
                                              val = value.get('VALUE')
                                          if ctn.find("command") >0:
                                             for str1 in cm_list:
                                                 if val.find(str1) >= 0:
                                                     sn_nm.extend((fl,wn,ctn,trs,val,tin))
                                                     #print (sn_nm)
                                                     obj = tuple(sn_nm)
                                                     sn_comm_c.append(obj)
                                                     sn_nm.clear()
                                                     break
                                            
                   
    #print (sn_comm_c)                                        
    return (sn_comm_c) 

#-------------------------------

def parseXML_Tranformation_tracing(xml_file):
    
    # open a file file for writing
    
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
    
    sn_trans_ver=[]
   
    for child in root:
        for folder in child.iter('FOLDER'):
            trans_tracing=[]   
            fl=folder.get('NAME')
        
        #Parsing inside workflow
            for workflow in folder.iter('WORKFLOW'):
                z1 = workflow.get('NAME') 
                
                for taskinst in workflow.iter('TASKINSTANCE'):
                    ty = taskinst.get('TASKTYPE')
               
            #Worklet logic that is if tasktype is worklet
                    if ty == "Worklet":
                        tn = taskinst.get('TASKNAME')
                        for wrklet in folder.iter('WORKLET'):
                            wk_nm = wrklet.get('NAME')
                            if  wk_nm == tn:
                            
                                for tsk_inst in wrklet.iter('TASKINSTANCE'):
                                    ty1 = tsk_inst.get('TASKTYPE')
                                    if ty1 == "Session":
                                        tn1 = tsk_inst.get('TASKNAME')
                                    
                                    #reusable code
                                        for session1 in folder.findall('SESSION'):
                                            sn1 = session1.get('NAME')
                                            if sn1 == tn1:
                                                mp_s1 = session1.get('MAPPINGNAME')
                                                for mapping1 in folder.iter('MAPPING'):
                                                    mp_t1 = mapping1.get('NAME')
                                                
                                                    if mp_t1 == mp_s1:
                                                        for transformation1 in mapping1.iter('TRANSFORMATION'):               
                                                            t1=transformation1.get('NAME')
                                                            #appending all transformation name to a list
                                                            #trans_list.append(t1)
                                                        
                                                            for trans_attr1 in transformation1:
                                                                if trans_attr1.get('NAME') == "Tracing Level":
                                                                    if trans_attr1.get('VALUE') == "Verbose Data":
                                                                        tt1=trans_attr1.get('VALUE')
                                                                    
                                                                    
                                                                        trans_tracing.extend((fl,z1,tn1,t1,tt1))
                                                                        obj = tuple(trans_tracing)
                                                                        sn_trans_ver.append(obj)
                                                                        trans_tracing.clear()           
                                
                    #if tasktype is session    
                    elif ty == "Session":
                        tn = taskinst.get('TASKNAME')
                        rs = taskinst.get('REUSABLE')
                    
                        #if reusable          
                        if rs == "YES":
                            for session in folder.findall('SESSION'):
                                sn = session.get('NAME')
                                if sn == tn:
                                    mp_s = session.get('MAPPINGNAME')
                                    for mapping in folder.iter('MAPPING'):
                                        mp_t=mapping.get('NAME')
                                    
                                        if mp_t == mp_s:
                                            for transformation in mapping.iter('TRANSFORMATION'):                
                                                t=transformation.get('NAME')
                                                #trans_list.append(t)
                                            
                                                for trans_attr in transformation:
                                                    if trans_attr.get('NAME') == "Tracing Level":
                                                        if trans_attr.get('VALUE') == "Verbose Data":
                                                            tt=trans_attr.get('VALUE')
                                                    
                                                            trans_tracing.extend((fl,z1,tn,t,tt))   
                                                            obj = tuple(trans_tracing)
                                                            sn_trans_ver.append(obj)
                                                            trans_tracing.clear() 
                                                    
                                                    
                 #if not reusable
                        if rs == "NO":
                            for wsn in workflow.findall('SESSION'):
                                sn=wsn.get('NAME')
                                if sn == tn:
                                    mp = wsn.get('MAPPINGNAME')
                                    for mapping1 in folder.iter('MAPPING'):
                                        mpt_1=mapping1.get('NAME')
                                        if mpt_1 == mp:
                                            for transformation in mapping1.iter('TRANSFORMATION'):
                                                t=transformation.get('NAME')
                                                #trans_list.append(t)
                                            
                                                for trans_attr in transformation:
                                                    if trans_attr.get('NAME') == "Tracing Level":
                                                        if trans_attr.get('VALUE') == "Verbose Data":
                                                            tt1=trans_attr.get('VALUE')                       
                
                                                            trans_tracing.extend((fl,z1,tn,t,tt1))   
                                                            obj = tuple(trans_tracing)
                                                            sn_trans_ver.append(obj) 
                                                            trans_tracing.clear()     
                                                        
    #trans_list.clear()
    return (sn_trans_ver)   

#-------------------------------
def parseXML_session_tracing(xml_file):
    
    # open a file file for writing
    
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot() 
    
    sn_verbose=[]
    
    for child in root:
        for folder in child.iter('FOLDER'):
            trans_tracing=[]   
            f1=folder.get('NAME')
        
            #Parsing inside workflow
            for workflow in folder.iter('WORKFLOW'):
                z1 = workflow.get('NAME') 
                
                for taskinst in workflow.iter('TASKINSTANCE'):
                    ty = taskinst.get('TASKTYPE')
                
                    if ty == "Worklet":
                        tn = taskinst.get('TASKNAME')
                        for wrklet in folder.iter('WORKLET'):
                            wk_nm = wrklet.get('NAME')
                            if  wk_nm == tn:
                            
                                for tsk_inst in wrklet.iter('TASKINSTANCE'):
                                    ty1 = tsk_inst.get('TASKTYPE')
                                    if ty1 == "Session":
                                        tn1 = tsk_inst.get('TASKNAME')
                                    
                                        for session1 in folder.findall('SESSION'):
                                            sn1 = session1.get('NAME')
                                            if sn1 == tn1:
                                                for configreference1 in session1.iter('CONFIGREFERENCE'):
                                                    config_type1 = configreference1.get('TYPE')
                                                    if config_type1 == "Session config":    
                                                        confg1 = configreference1.get('REFOBJECTNAME')
                                        
                                                        for config1 in folder.iter('CONFIG'):
                                                            cg_nm1 = config1.get('NAME')
                                                            if cg_nm1 == confg1:
                                                                for config_attr1 in config1:
                                                                    if config_attr1.get('NAME') == "Override tracing":
                                                                        if config_attr1.get('VALUE') == "Verbose Data":
                                                                            c11 = config_attr1.get('VALUE')
                                                                        
                                                                            trans_tracing.extend((f1,z1,tn,c11))   
                                                                            obj = tuple(trans_tracing)
                                                                            sn_verbose.append(obj)
                                                                            trans_tracing.clear()
                                                           
                    if ty == "Session":
                        tn = taskinst.get('TASKNAME')
                        rs = taskinst.get('REUSABLE')
                    
                        if rs == "YES":
                            for session in folder.findall('SESSION'):
                                sn = session.get('NAME')
                                if sn == tn:
                                    for configreference in session.iter('CONFIGREFERENCE'):
                                        config_type = configreference.get('TYPE')
                                        if config_type == "Session config":    
                                            confg = configreference.get('REFOBJECTNAME')
                                        
                                            #if confg == 'default_session_config':
                                            for config in folder.iter('CONFIG'):
                                                cg_nm = config.get('NAME')
                                                if cg_nm == confg:
                                                    for config_attr1 in config:
                                                        if config_attr1.get('NAME') == "Override tracing":
                                                            if config_attr1.get('VALUE') == "Verbose Data":
                                                                c1 = config_attr1.get('VALUE')
                                                        
                                                   
                                                                trans_tracing.extend((f1,z1,tn,c1))   
                                                                obj = tuple(trans_tracing)
                                                                sn_verbose.append(obj) 
                                                                trans_tracing.clear()
                                                        
                        if rs == "NO":
                            for wsn in workflow.findall('SESSION'):
                                sn=wsn.get('NAME')
                                if sn == tn:
                                    for session in workflow.iter('SESSION'):
                                        for configreference in session.iter('CONFIGREFERENCE'):
                                            config_type = configreference.get('TYPE')
                                            if config_type == "Session config":    
                                                confg = configreference.get('REFOBJECTNAME')
                                        
                                            #if confg == 'default_session_config':
                                                for config in folder.iter('CONFIG'):
                                                    cg_nm = config.get('NAME')
                                                    if cg_nm == confg:
                                                        for config_attr in config:
                                                            if config_attr.get('NAME') == "Override tracing":
                                                                if config_attr.get('VALUE') == "Verbose Data":
                                                                    c2 = config_attr.get('VALUE')
                                                   
                                                                    trans_tracing.extend((f1,z1,tn,c2))   
                                                                    obj = tuple(trans_tracing)
                                                                    sn_verbose.append(obj)
                                                                    trans_tracing.clear()
                                
                           
    return (sn_verbose)                        
#------------------------------------
def parseXML_count_validation(xml_file):
    """
    Parse XML with ElementTree
    """
    # open a file for writing
    
    parser = etree.XMLParser(ns_clean=True,recover = True)
    tree = etree.parse(xml_file,parser=parser)
    root = tree.getroot()
    
    sn_cnt=[]
    wf_cnt=[]
    mp_cnt=[]
    for child in root:
        for folder in child.iter('FOLDER'):
            sn_nm=[]
            mp_nm=[]
            wf_nm=[]
        
            fl = folder.get('NAME')
            sn_nm.append(fl)
            wf_nm.append(fl)
            mp_nm.append(fl)
        
            mp_ct = len(folder.findall('MAPPING'))
            mp_nm.append(mp_ct)
            wf_ct = len(folder.findall('WORKFLOW'))
            wf_nm.append(wf_ct)
        
            count_session=len(folder.findall('SESSION'))
            #print(count_session)    
        
            var = 0
            for workflow in folder.iter('WORKFLOW'):           
                count_session2=len(workflow.findall('SESSION')) 
                #print(count_session2)      
        
                var = var + count_session2
        
            var2 = count_session + var
            #print (var2)
            sn_nm.append(var2)
        
            obj1 = tuple(sn_nm)
            obj2 = tuple(wf_nm)
            obj3 = tuple(mp_nm)
        
            sn_cnt.append(obj1)
            wf_cnt.append(obj2)
            mp_cnt.append(obj3)
        
        return (sn_cnt,wf_cnt,mp_cnt)
    
#----------------------------------------------------                  
if __name__ == "__main__":
         file_name = "C:/Users/Manali.Ghosh/Desktop/Tracing_level/CMD Task and Verbose.XML"
         
         #logger = logging.getLogger('validation')
         #Workflow log file validation
         wf_logdir = parseXML_wf_logdir(file_name) 
         #print (wf_lst_c)
         #print (wf_lst_ic)
         #logger.info("This is debug message" + str(wf_logdir[2]))
         #Session log file validation
         sn_logdir = parseXML_sn_logdir(file_name)
         #print (sn_lst_c)
         #print (sn_lst_ic)
         
         #Workflow parameter file validation
         wf_prmfile = parseXML_wf_parmfile(file_name)
         #print (wf_parm_c)
         #print (wf_parm_ic)
         #logger.error("This is debug2 message")
         #Session parameter file validation
         sn_prmfile = parseXML_sn_parmfile(file_name)
         #print (sn_parm_c)
         #print (sn_parm_ic)
         
         #Session source path validation
         sn_srcpath = parseXML_sn_srcdir(file_name) 
         #print (sn_src_c)
         #print (sn_src_ic)
         
         #Session target path vaidation
         sn_tgtpath = parseXML_sn_tgtdir(file_name)
         #print (sn_tgt_c)
         #print (sn_tgt_ic)
         
         #Session bad file path validation
         sn_baddir = parseXML_sn_baddir(file_name)
         #print (sn_bad_c)
         #print (sn_bad_ic)
         
         #List of transformations using cache directory
         sn_cachdir = parseXML_trans_cachedir(file_name) 
         #print (sn_cach_c)
         #print (sn_cach_ic)
         
         #Mapping variables and parameters
         sn_map_c = parseXML_map_var(file_name)
         #print (sn_map_c)
         
         #Command task with hard coded values
         sn_comm_c = parseXML_comm_tsk(file_name) 
         
         #Transformation level verbose tracing
         sn_trans_ver = parseXML_Tranformation_tracing(file_name)
         
         #Session level verbose tracing
         sn_verbose = parseXML_session_tracing(file_name)
         
         #Workflow, Session and Mapping count by folder
         sn_cnt,wf_cnt,mp_cnt = parseXML_count_validation(file_name)
         #print(sn_cnt)
         #print(wf_cnt)
         #print(mp_cnt)
         
         #Writing correct paths details into excel file
         infa_corr_excel(wf_logdir,sn_logdir,wf_prmfile,sn_prmfile,sn_srcpath,sn_tgtpath,sn_baddir,sn_cachdir,sn_map_c,sn_comm_c,sn_trans_ver,sn_verbose,sn_cnt,wf_cnt,mp_cnt)
         
        





