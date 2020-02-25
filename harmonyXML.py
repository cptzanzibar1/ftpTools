import xml.etree.ElementTree as ET
import copy
import os

flowCheck = input('Will file be sent from Cass (y or n): ')
flowCheck2 = input('Will files be sent to Cass (y or n): ')
testCheck = input('Is this test or prod (t or p): ')
ftpId = input('Please enter the ID: ')
cleoId = input('Please enter the Cleo mailbox: ')
utilCheck = input('Is this utilities (y or n): ')
teleCheck = input('Is this telecom (y or n): ')
dirCheck = input('Do you need folders created (y or n): ')
print('\n')
print(f'Files sent from cass: {flowCheck}')
print(f'Test or Prod: {testCheck}')
print(ftpId)
print(cleoId)
print(f'Is this utilities: {utilCheck}')
print(f'Is this telecom: {teleCheck}')
print(f'Do you need folders made: {dirCheck}')

infoConfirm = input('Is this information correct (y or n): ')

def ftpDirectory():
    if 'CS' in ftpId and 'y' in teleCheck:
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\TELECOM\\{ftpId}')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\TELECOM\\{ftpId}\\to_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\TELECOM\\{ftpId}\\to_cass_test')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\TELECOM\\{ftpId}\\from_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\TELECOM\\{ftpId}\\from_cass_test')
    elif 'CS' in ftpId and 'n' in utilCheck and 'n' in teleCheck:
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CLIENT\\{ftpId}')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CLIENT\\{ftpId}\\to_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CLIENT\\{ftpId}\\to_cass_test')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CLIENT\\{ftpId}\\from_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CLIENT\\{ftpId}\\from_cass_test')
    elif 'CS' in ftpId and 'y' in utilCheck:
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\UTILITY\\{ftpId}')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\UTILITY\\{ftpId}\\to_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\UTILITY\\{ftpId}\\to_cass_test')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\UTILITY\\{ftpId}\\from_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\UTILITY\\{ftpId}\\from_cass_test')
    elif 'CA' in ftpId:
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CARRIER\\{ftpId}')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CARRIER\\{ftpId}\\out_997')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CARRIER\\{ftpId}\\to_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\CARRIER\\{ftpId}\\to_cass_test')
    nextEntry = input('would you like to add another (y or n): ')
    if 'y' in nextEntry:
        ftpDirectory()


def updateXml(filename):
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
                                    #OUTBOUND TEST
    if 'CS' in ftpId and 'n' in utilCheck and 'n' in teleCheck and 't' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\CLIENT\{ftpId}\\from_cass_test\\"'''
            command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Stage-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
    if 'CS' in ftpId and 'y' in utilCheck and 'n' in teleCheck and 't' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
           command.text = command.text + '\n\n'
           command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\\UTILITY\{ftpId}\\from_cass_test\\"'''
           command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Stage-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
    if 'CS' in ftpId and 'n' in utilCheck and 'y' in teleCheck and 't' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
           command.text = command.text + '\n\n'
           command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\\TELECOM\{ftpId}\\from_cass_test\\"'''
           command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Stage-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
                                    #OUTBOUND PROD
    if 'CS' in ftpId and 'n' in utilCheck and 'n' in teleCheck and 'p' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\CLIENT\{ftpId}\\from_cass\\"'''
            command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Prod-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
    if 'CS' in ftpId and 'y' in utilCheck and 'n' in teleCheck and 'p' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
           command.text = command.text + '\n\n'
           command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\\UTILITY\{ftpId}\\from_cass\\"'''
           command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Prod-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
    if 'CS' in ftpId and 'n' in utilCheck and 'y' in teleCheck and 'p' in testCheck and 'y' in flowCheck:
        for command in root.iter('Commands'):
           command.text = command.text + '\n\n'
           command.text = command.text + f'''LCOPY -DEL -UNI "\\\zombie\TRANSMISSIONS\\TELECOM\{ftpId}\\from_cass\\"'''
           command.text = command.text + f''' "%dataRoot%\AS2\outbox\Cass_Cloud_Prod-AS2\%sourcefilebase%.%sourcefileext%.{cleoId}"'''
                                     #INBOUND TEST
    if 'CS' in ftpId and 'n' in utilCheck and 'n' in teleCheck and 't' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\CLIENT\{ftpId}\\to_cass_test\\%sourcefilebase%"'''
    if 'CS' in ftpId and 'y' in utilCheck and 'n' in teleCheck and 't' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\\UTILITY\{ftpId}\\to_cass_test\\%sourcefilebase%"'''
    if 'CS' in ftpId and 'n' in utilCheck and 'y' in teleCheck and 't' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\TELECOM\{ftpId}\\to_cass_test\\%sourcefilebase%"'''
                                      #INBOUND PROD
    if 'CS' in ftpId and 'n' in utilCheck and 'n' in teleCheck and 'p' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\CLIENT\{ftpId}\\to_cass\\%sourcefilebase%"'''
    if 'CS' in ftpId and 'y' in utilCheck and 'n' in teleCheck and 'p' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\\UTILITY\{ftpId}\\to_cass\\%sourcefilebase%"'''
    if 'CS' in ftpId and 'n' in utilCheck and 'y' in teleCheck and 'p' in testCheck and 'y' in flowCheck2:
        for command in root.iter('Commands'):
            command.text = command.text + '\n\n'
            command.text = command.text + f'''LCOPY -DEL -UNI "%inbox%/*.{cleoId}"'''
            command.text = command.text + f'''" \\\zombie\TRANSMISSIONS\TELECOM\{ftpId}\\to_cass\\%sourcefilebase%"'''
    tree = ET.ElementTree(root)

    with open(filename, 'wb') as fileupdate:
        tree.write(fileupdate)


if __name__ == '__main__':
    if 'y' in flowCheck and 't' in testCheck and 'y' in infoConfirm:
        updateXml(r'C:\\Users\kkohlman\AppData\Local\Programs\Python\Python37-32\Scripts\test.xml')
        #updateXml(r'\\vltraderagent\hosts\Local Commands SSH Stage.xml')
        if 'y' in dirCheck:
            ftpDirectory()
    if 'y' in flowCheck and 'p' in testCheck and 'y' in infoConfirm:
         updateXml(r'C:\\Users\kkohlman\AppData\Local\Programs\Python\Python37-32\Scripts\test.xml')
         #updateXml(r'\\vltraderagent\hosts\Local Commands SSH Prod.xml')
         if 'y' in dirCheck:
            ftpDirectory()
    if 'y' in flowCheck2 and 't' in testCheck and 'y' in infoConfirm:
        updateXml(r'C:\\Users\kkohlman\AppData\Local\Programs\Python\Python37-32\Scripts\test.xml')
        #updateXml(r'\\vltraderagent\hosts\TEST_Cass_Cloud_Stage-AS2.xml')
        if 'y' in dirCheck:
            ftpDirectory()
    if 'y' in flowCheck2 and 'p' in testCheck and 'y' in infoConfirm:
        updateXml(r'C:\\Users\kkohlman\AppData\Local\Programs\Python\Python37-32\Scripts\test.xml')
        #updateXml(r'\\vltraderagent\hosts\TEST_Cass_Cloud_Prod-AS2.xml')
        if 'y' in dirCheck:
            ftpDirectory()


    

        
