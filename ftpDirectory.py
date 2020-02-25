import os
def ftpDirectory():
    ftpId = input('Please enter the ID: ')
    utilCheck = input('Is this utilities (y or n): ')
    teleCheck = input('Is this telecom (y or n): ')
    globalCheck = input('Is this global (y or n): ')
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
    elif 'Y' in globalCheck:
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\GLOBAL\\{ftpId}')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\GLOBAL\\{ftpId}\\out_997')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\GLOBAL\\{ftpId}\\to_cass')
        os.makedirs(f'\\\zombie\\TRANSMISSIONS\\GLOBAL\\{ftpId}\\to_cass_test')
    nextEntry = input('would you like to add another (y or n): ')
    if 'y' in nextEntry:
        ftpDirectory()
    
        
ftpDirectory()





