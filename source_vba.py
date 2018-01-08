import csv
import datetime

def convert_date_format(input_datetime, dob=False):

    if input_datetime == '':
        return input_datetime
    else:
        #print(input_datetime)

        if dob is True:
            try:
                iso_datetime = datetime.datetime.strptime(input_datetime, '%m/%d/%Y').date().isoformat()
                #iso_datetime_dob = datetime.timedelta()
                #print('Converting Datetime')
                iso_datetime_dob = '19' + iso_datetime[2:]
                #print(iso_datetime_dob)
                #input("Check DOB")
                return iso_datetime_dob
            except ValueError:
                iso_datetime = datetime.datetime.strptime(input_datetime, '%d-%b-%y').date().isoformat()
                #print('Converting Datetime')
                iso_datetime_dob = '19' + iso_datetime[2:]
                #print(iso_datetime_dob)
                #input("Check DOB")
                return iso_datetime_dob
        else:
            try:
                iso_datetime = datetime.datetime.strptime(input_datetime, '%m/%d/%Y').date().isoformat()
                #print(iso_datetime)
                return iso_datetime
            except ValueError:
                iso_datetime = datetime.datetime.strptime(input_datetime, '%d-%b-%y').date().isoformat()
                #print(iso_datetime)
                return iso_datetime

def convert_or_datetime(or_date, or_time):

    if or_date == '':
        #iso_datetime = ''
        iso_datetime = 'NULL'
    elif or_time == '':
        iso_datetime = datetime.datetime.strptime(or_date, '%d-%b-%y').date().isoformat() + ' 00:00:00'
    else:
        or_datetime = or_date + ' ' + or_time
        iso_datetime = datetime.datetime.strptime(or_date, '%d-%b-%y').date().isoformat() + ' ' + or_time + ':00'

    return iso_datetime

def convert_her2(her2_status):
    # Options are Equivocal, Low, Negative, Positive

    if her2_status in {'equiv', 'equiv.', 'Equivocal'}:
        return 'Equivocal'
    elif her2_status in {'low'}:
        return 'Low'
    elif her2_status in {'-', 'neg'}:
        return 'Negative'
    elif her2_status in {'2+', '+', 'pos', 'med', 'high', 'pos.'}:
        return 'Positive'
    else:
        return ''

def map_surgeon_and_oncologist(person):

    if person == '' or person == '.':

        return {'Surgeon': '', 'Oncologist': '', 'Study': ''}

    else:
        surgeons_ref = {'A Macneill': {'Surgeon': 'Dr. Andrea MacNeill', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'A Mcfadden': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'al-mansoor': {'Surgeon': '', 'Oncologist': 'Dr. Margaret Knowling', 'Study': 'TTR', 'Comments': 'Thoracentesis specimens'},
                        'Beardsley': {'Surgeon': '', 'Oncologist': 'Dr. Hagen Kennecke', 'Study': 'TTR', 'Comments': ''},
                        'bilogy of breast study': {'Surgeon': '', 'Oncologist': '', 'Study': 'Biology of Breast', 'Comments': ''},
                        'bryce': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Thoracentesis specimens'},
                        'C. Ho': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Paracentesis specimen'},
                        'C Ho': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Paracentesis specimen'},
                        'chai': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'Xenograft', 'Comments': ''},
                        'cheifetz': {'Surgeon': 'Dr. Rona Cheifetz', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'chia': {'Surgeon': '', 'Oncologist': 'Dr. Stephen Chia', 'Study': 'TTR', 'Comments': 'Thora/Paracentesis specimens'},
                        'Chia': {'Surgeon': '', 'Oncologist': 'Dr. Stephen Chia', 'Study': '', 'Comments': ''},
                        'chia/gelmon': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'TTR', 'Comments': 'Paracentesis'},
                        'colin marr': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'Xenograft', 'Comments': ''},
                        'colin  marr': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'Xenograft', 'Comments': ''},
                        'davis': {'Surgeon': 'Dr. Noelle Davis', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Dr Gelmon': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': '', 'Comments': ''},
                        'Dr. H. Lim': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Paracentesis'},
                        'Dr H Lim': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Paracentesis'},
                        'G McGregor': {'Surgeon': 'Dr. Gregor McGregor', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Gelm': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'TTR', 'Comments': 'Thoracentesis'},
                        'gelmon': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'TTR', 'Comments': 'Thora/Paracentesis'},
                        'Gelmon': {'Surgeon': '', 'Oncologist': 'Dr. Karen Gelmon', 'Study': 'TTR', 'Comments': ''},
                        'H Lim': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Thoracentesis'},
                        'H. Lim': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': 'Thoracentesis'},
                        'hamilton': {'Surgeon': 'Dr. Trevor Hamilton', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Hamilton': {'Surgeon': 'Dr. Trevor Hamilton', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'howdle': {'Surgeon': '', 'Oncologist': 'Dr. Caroline Lohrisch', 'Study': 'TTR', 'Comments': 'Paracentesis'},
                        'kennecke': {'Surgeon': '', 'Oncologist': 'Dr. Hagen Kennecke', 'Study': 'TTR', 'Comments': ''},
                        'Kennecke': {'Surgeon': '', 'Oncologist': 'Dr. Hagen Kennecke', 'Study': 'TTR', 'Comments': ''},
                        'Knowling': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Lam': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Lim': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'lohrisch': {'Surgeon': '', 'Oncologist': 'Dr. Caroline Lohrisch', 'Study': 'TTR', 'Comments': ''},
                        'Lohrisch': {'Surgeon': '', 'Oncologist': 'Dr. Caroline Lohrisch', 'Study': 'TTR', 'Comments': ''},
                        'lymburner': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'M Knowling': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'm knowling': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'MacNeil': {'Surgeon': 'Dr. Andrea MacNeill', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Mc Fadden': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Mcfadden': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'McConnell': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Mcconnell': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'McFadden': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'mcfadden': {'Surgeon': 'Dr. Andrew McFadden', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'N Davis': {'Surgeon': 'Dr. Noelle Davis', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'R Cheifetz': {'Surgeon': 'Dr. Rona Cheifetz', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'S Wilson': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'shenkier': {'Surgeon': '', 'Oncologist': 'Dr. Tamara Shenkier', 'Study': 'TTR', 'Comments': ''},
                        'Shenkier': {'Surgeon': '', 'Oncologist': 'Dr. Tamara Shenkier', 'Study': 'TTR', 'Comments': ''},
                        'Simard': {'Surgeon': 'Dr. Laurie Simard', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Simmons': {'Surgeon': '', 'Oncologist': 'Dr. Christine Simmons', 'Study': 'TTR', 'Comments': ''},
                        'Sun/Bryce': {'Surgeon': '', 'Oncologist': 'Dr. Sophie Sun', 'Study': '', 'Comments': ''},
                        'TNBC study': {'Surgeon': '', 'Oncologist': '', 'Study': 'TNBC', 'Comments': ''},
                        'U Kuusk': {'Surgeon': 'Dr. Urva Kuusk', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Villa': {'Surgeon': '', 'Oncologist': 'Dr. Diego Villa', 'Study': 'TTR', 'Comments': ''},
                        'Wilson': {'Surgeon': '', 'Oncologist': '', 'Study': 'TTR', 'Comments': ''},
                        'Xenograft': {'Surgeon': '', 'Oncologist': '', 'Study': 'Xenograft', 'Comments': ''},
                        'xenograft': {'Surgeon': '', 'Oncologist': '', 'Study': 'Xenograft', 'Comments': ''}}

        return surgeons_ref[person]


# Store the records that have issues in this set:
ttr_records_w_errors = set()

# This step is for finding disagreement between the Consent ID and the Acquisition ID in the records
with open('./data/ttr_nurse_log_20171023.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        #print(row)


        if row['ConsentID'] != row['AcquisitionID']:

            if 'TTRBR' in row['ConsentID'] and 'VBA' in row['AcquisitionID']:

                consent_id_num = row['ConsentID'].replace('TTRBR', '')
                acq_id_num = row['AcquisitionID'].replace('VBA', '')
                #print(int(consent_id_num))
                #print(int(acq_id_num))
                if int(consent_id_num) != int(acq_id_num):
                    print(row['ConsentID'], row['AcquisitionID'])
                    ttr_records_w_errors.add(row['AcquisitionID'])

            else:
                print(row['ConsentID'], row['AcquisitionID'])
                ttr_records_w_errors.add(row['AcquisitionID'])

# This is to check if every VBA record in the inventory has a patient record
with open('./data/ttr_nurse_log_20171023.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    patient_ids = dict()

    for row in csvreader:
        #print(row)

        patient_ids[row['AcquisitionID']] = row['PHN']


with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    inventory_without_patients = []

    for row in csvreader:
        if row['Sample Name'] in patient_ids.keys():
            pass
        else:
            inventory_without_patients.append(row['Sample Name'])
            ttr_records_w_errors.add(row['Sample Name'])


print('Inventory Without Patients')
print(inventory_without_patients)

input("TTR Validation Ends Here")

#Record participant data from TTR log here

print(ttr_records_w_errors)
input('Above is the TTR Nurse Records with errors')

with open('./data/ttr_nurse_log_20171023.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    ttr_participants = dict()
    ttr_consent = dict()

    for row in csvreader:

        if row['AcquisitionID'] not in ttr_records_w_errors:
            #print(row)
            participant_data = dict()
            participant_data['BCCA ID'] = row['Agency_ID']
            participant_data['PHN'] = row['PHN']
            participant_data['First Name'] = row['FName']
            participant_data['Middle Name'] = row['MiddleName']
            participant_data['Nick Name'] = row['NickName']
            participant_data['Last Name'] = row['LName']
            participant_data['Donor Sequence Number'] = row['ï»¿Donor Sequence Number']

            if row['Gender'] == 'Female':
                participant_data['Gender'] = 'f'
            elif row['Gender'] == 'Male':
                participant_data['Gender'] = 'm'
            else:
                participant_data['Gender'] = ''

            participant_data['DOB'] = convert_date_format(row['DOB'], True)

            participant_data['Primary Diagnosis'] = row['PrimaryDiagnosis']
            participant_data['Primary Path Number'] = row['primaryPathNumber']
            participant_data['Primary Hospital'] = row['PrimaryHospital']

            participant_data['Study Type'] = map_surgeon_and_oncologist(row['Surgeon'])['Study']


            #participant_data[] = row['CurrentDiagnosis']

            #participant_data[] = row['HomePhone']
            #participant_data[] = row['WorkPhone']
            #participant_data[] = row['CellPhone']

            participant_data['OR Hospital'] = row['ORFacility']
            #participant_data['OR Date and Time'] = row['ORDate']
            #participant_data['OR Date and Time'] = row['ORTime']
            #or_datetime = row['ORDate'] + ' ' + row['ORTime']
            #print('OR DateTime')
            #print(convert_or_datetime(row['ORDate'], row['ORTime']))
            participant_data['OR Date and Time'] = convert_or_datetime(row['ORDate'], row['ORTime'])


            participant_data['Notes'] = "Referral Datetime:" + row['Referral date/time'] + "," + row['Time of Referral'] + ", Method of Referral: " + row['Method of referral'] + ", ACAppDateTime:" + row['ACApptDate'] + "," + row['ACApptTime'] + ", TTRApptDateTime:" + row['TTRApptDate'] + "," + row['TTRApptTime'] + ", TTRApptSite:" + row['TTRApptSite']


            #participant_data[] = row['Referral date/time']
            #participant_data[] = row['Time of Referral']
            #participant_data[] = row['Method of referral']
            #participant_data[] = row['ACApptDate']
            #participant_data[] = row['ACApptTime']
            #participant_data[] = row['TTRApptDate']
            #participant_data[] = row['TTRApptTime']
            #participant_data[] = row['TTRApptSite']


            participant_data['No Surgery'] = row['NoSurgery']

            #participant_data[] = row['DonorClosed']
            #participant_data[] = row['PostOp']
            #participant_data[] = row['Reason questnre declined']
            #participant_data[] = row['QuestionnaireFileName']
            #participant_data[] = row['QuestionnaireFilePath']
            #participant_data[] = row['accessing']
            #participant_data[] = row['trans_dd']

            participant_data['Final Diagnosis'] = row['final_diagnosis']
            participant_data['No Sample Reason'] = row['No_sample_Reason']

            # Options are Equivocal, Low, Negative, Positive
            participant_data['Original ER'] = convert_her2(row['original_ER'])
            participant_data['Original PR'] = convert_her2(row['original_PR'])
            participant_data['HER2 FISH'] = convert_her2(row['her2_FISH'])
            participant_data['HER2 IHC'] = convert_her2(row['her2_IHC'])




            #Consent
            consent_data = dict()

            if row['ConsentDenied'] == 'TRUE':
                consent_data['Consent Status'] = 'denied'
            elif row['Revoked'] == 'TRUE':
                consent_data['Consent Status'] = 'withdrawn'
            else:
                consent_data['Consent Status'] = 'obtained'

            if row['FluidCollected'] == 'TRUE':
                consent_data['Fluid Collected'] = 'y'
            else:
                consent_data['Fluid Collected'] = 'n'

            if row['BloodCollected'] == 'TRUE':
                consent_data['Blood Collected'] = 'y'
            else:
                consent_data['Blood Collected'] = 'n'

            if row['SalivaCollected'] == 'TRUE':
                consent_data['Saliva Collected'] = 'y'
            else:
                consent_data['Saliva Collected'] = 'n'

            if row['ContactGenetic'] == 'TRUE':
                consent_data['Genetic Research Status'] = 'y'
            else:
                consent_data['Genetic Research Status'] = 'n'

            if row['PathSPEC'] == '':
                print("it is empty!")
                consent_data['Path SPEC'] = row['PathSPEC']
            else:
                print("Not Empty")
                consent_data['Path SPEC'] = row['PathSPEC']
                print(consent_data['Path SPEC'])

            consent_data['Fluid Type'] = row['FluidType']
            consent_data['Cancer Type'] = row['Cancer Type']
            consent_data['Date Consent Signed or Declined'] = convert_date_format(row['Date Consent signed'])
            consent_data['Reason Consent Declined'] = row['Reason consent declined']
            consent_data['Notes'] = row['Referral Notes']
            consent_data['Pathologist'] = row['Pathologist']
            #consent_data['Person Obtaining Consent'] = row['TTR Nurse']
            consent_data['Person Obtaining Consent'] = 'clinical nurse'

            #consent_data['Study Type'] = map_surgeon_and_oncologist(row['Surgeon'])['Study']
            consent_data['Surgeon'] = map_surgeon_and_oncologist(row['Surgeon'])['Surgeon']
            consent_data['Study Type'] = map_surgeon_and_oncologist(row['Surgeon'])['Study']

            #consent_data['Date Consent Denied'] = row['DateConsentDenied']

            ttr_participants[row['AcquisitionID']] = participant_data
            ttr_consent[row['AcquisitionID']] = consent_data

input("TTR Participant Import Ends Here")

# Record the number of Tissue for each participants
with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_tissue = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Tissue':

            #print(row)

            if row['Sample Name'] in vba_tissue:

                tissue_prop = dict()
                tissue_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                tissue_prop['Barcode'] = row['Barcode']

                if 'Tumour' in row['Keywords']:
                    tissue_prop['Tissue Nature'] = 'tumor'
                else:
                    tissue_prop['Tissue Nature'] = 'normal'


                vba_tissue[row['Sample Name']].append(tissue_prop)
                #print(vba_tissue[row['Sample Name']])
            else:
                #print(row['Preparation Date'])
                tissue_prop = dict()
                tissue_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                tissue_prop['Barcode'] = row['Barcode']

                if 'Tumour' in row['Keywords']:
                    tissue_prop['Tissue Nature'] = 'tumor'
                else:
                    tissue_prop['Tissue Nature'] = 'normal'

                vba_tissue[row['Sample Name']] = [tissue_prop]
                #print(vba_tissue[row['Sample Name']])



print(vba_tissue)
#input("Finished recording the number of tissues, continue?")
# Record the number of Plasma
with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_plasma = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Plasma':

            #print(row)

            if row['Sample Name'] in vba_plasma:

                plasma_prop = dict()
                plasma_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                plasma_prop['Barcode'] = row['Barcode']

                vba_plasma[row['Sample Name']].append(plasma_prop)
                #print(vba_tissue[row['Sample Name']])
            else:
                #print(row['Preparation Date'])
                plasma_prop = dict()
                plasma_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                plasma_prop['Barcode'] = row['Barcode']

                vba_plasma[row['Sample Name']] = [plasma_prop]
                #print(vba_tissue[row['Sample Name']])


print(vba_plasma)
#input("Finished recording the number of plasma, continue?")

with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_buffy_coat = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Buffy Coat':

            #print(row)

            if row['Sample Name'] in vba_buffy_coat:

                buffy_coat_prop = dict()
                buffy_coat_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                buffy_coat_prop['Barcode'] = row['Barcode']

                vba_buffy_coat[row['Sample Name']].append(buffy_coat_prop)
                #print(vba_tissue[row['Sample Name']])
            else:
                #print(row['Preparation Date'])
                buffy_coat_prop = dict()
                buffy_coat_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                buffy_coat_prop['Barcode'] = row['Barcode']

                vba_buffy_coat[row['Sample Name']] = [buffy_coat_prop]
                #print(vba_tissue[row['Sample Name']])

print(vba_buffy_coat)
#input("Finished recording the number of plasma, continue?")


with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_saliva = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Saliva':

            #print(row)

            if row['Sample Name'] in vba_saliva:

                saliva_prop = dict()
                saliva_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                saliva_prop['Barcode'] = row['Barcode']

                vba_saliva[row['Sample Name']].append(saliva_prop)
                #print(vba_tissue[row['Sample Name']])
            else:
                #print(row['Preparation Date'])
                saliva_prop = dict()
                saliva_prop['Preparation Date'] = convert_date_format(row['Preparation Date'])
                saliva_prop['Barcode'] = row['Barcode']

                vba_saliva[row['Sample Name']] = [saliva_prop]

print(vba_saliva)
input("Finished recording the number of saliva, continue?")

#Store list of SQL statements
list_of_statements = []

with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_inserted = set()

    for row in csvreader:
        #print(row)

        if row['Sample Name'] not in vba_inserted and row['Sample Name'] not in {'VBA0862', 'VBA0896', 'VBA0909', 'VBA0927'}:

            aliquot_counter = 1
            #participant_insert = "INSERT INTO participants (`last_modification`, `created`, `modified`) VALUES (NOW(), NOW(), NOW());"
            #list_of_statements.append(participant_insert)

            participant_insert = "INSERT INTO participants (`study_type`, `first_name`,`middle_name`,`last_name`,`bcb_nick_name`," \
                                 "`phn`,`date_of_birth`,`date_of_birth_accuracy`,`sex`," \
                                 "`notes`,`final_diagnosis`,`primary_diagnosis`,`primary_path_number`,`primary_hospital`,`or_hospital`," \
                                 "`original_er`,`original_pr`,`her2_fish`, `her2_ihc`,`no_sample_reason`," \
                                 "`or_datetime`,`participant_identifier`," \
                                 "`last_modification`,`created`, `created_by`, `modified`, `modified_by`) VALUES " + " ('TTR', '" + ttr_participants[row['Sample Name']]['First Name'] + "','" + ttr_participants[row['Sample Name']]['Middle Name'] + "','" + ttr_participants[row['Sample Name']]['Last Name'] + "','" + ttr_participants[row['Sample Name']]['Nick Name'] + "','" + ttr_participants[row['Sample Name']]['PHN'] + "','" + ttr_participants[row['Sample Name']]['DOB'] + "', 'c','" + ttr_participants[row['Sample Name']]['Gender'] + "','" + ttr_participants[row['Sample Name']]['Notes'] + "','" + ttr_participants[row['Sample Name']]['Final Diagnosis'] + "','" + ttr_participants[row['Sample Name']]['Primary Diagnosis'] \
            + "','" + ttr_participants[row['Sample Name']]['Primary Path Number'] + "','" + ttr_participants[row['Sample Name']]['Primary Hospital'] + "','" + ttr_participants[row['Sample Name']]['OR Hospital'] \
            + "','" + ttr_participants[row['Sample Name']]['Original ER'] + "','" + ttr_participants[row['Sample Name']]['Original PR'] \
            + "','" + ttr_participants[row['Sample Name']]['HER2 FISH'] + "','" + ttr_participants[row['Sample Name']]['HER2 IHC'] + "','" + ttr_participants[row['Sample Name']]['No Sample Reason'] \
            + "','" + ttr_participants[row['Sample Name']]['OR Date and Time'] + "','" + ttr_participants[row['Sample Name']]['BCCA ID'] + "', NOW(), NOW(), 4, NOW(), 4);"
            list_of_statements.append(participant_insert)

            vba_num = row['Sample Name'][0:3] + "000" + row['Sample Name'][3:]
            consent_id = "PBC000" + row['Sample Name'][3:]
            acquisition_label = "000" + row['Sample Name'][3:]
            #print(vba_num)
            misc_identifier_insert = "INSERT INTO misc_identifiers (`identifier_value`, `misc_identifier_control_id`, `participant_id`, `flag_unique`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + vba_num + "', 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 1, NOW(), 4, NOW(), 4);"
            list_of_statements.append(misc_identifier_insert)

            consent_masters_insert = "INSERT INTO consent_masters (`consent_status`, `consent_signed_date`, `reason_denied`, `notes`, `participant_id`, `consent_control_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + ttr_consent[row['Sample Name']]['Consent Status'] + "','" + ttr_consent[row['Sample Name']]['Date Consent Signed or Declined'] + "','" + ttr_consent[row['Sample Name']]['Reason Consent Declined'] + "','" + ttr_consent[row['Sample Name']]['Notes'] + "',(SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 2, NOW(), 4, NOW(), 4);"

            list_of_statements.append(consent_masters_insert)

            cd_bcca_breast_insert = "INSERT INTO cd_bcca_breast (`consent_id`, `bcb_study_type`," \
                                    "`bcb_path_spec`, `bcb_pathologist`, `bcb_cancer_type`, `bcb_consenting_person`, `genetic_research_status`, `blood_status`, `saliva_status`, `fluid_status`, `fluid_type`, `medical_oncologists_vc`," \
                                    "`consent_master_id`, `dt_created`) VALUES ('" + consent_id + "','" + ttr_consent[row['Sample Name']]['Study Type'] + "','" + \
                                    ttr_consent[row['Sample Name']]['Path SPEC'] + "','" + ttr_consent[row['Sample Name']]['Pathologist'] + "','" + ttr_consent[row['Sample Name']]['Cancer Type'] + "','" + ttr_consent[row['Sample Name']]['Person Obtaining Consent'] + "','" + ttr_consent[row['Sample Name']]['Genetic Research Status'] + "','" + ttr_consent[row['Sample Name']]['Blood Collected'] + "','" + ttr_consent[row['Sample Name']]['Saliva Collected'] + "','" + ttr_consent[row['Sample Name']]['Fluid Collected'] + "','" + ttr_consent[row['Sample Name']]['Fluid Type'] + "','" + ttr_consent[row['Sample Name']]['Surgeon'] + "', (SELECT `id` FROM consent_masters ORDER BY `id` DESC LIMIT 1), '2010-01-01 00:00:00');"


            list_of_statements.append(cd_bcca_breast_insert)

            collections_insert = "INSERT INTO collections (`acquisition_label`, `bank_id`, `collection_property`, `collection_notes`, `participant_id`, `consent_master_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + acquisition_label + "', 1, 'participant collection', '', (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM consent_masters ORDER BY `id` DESC LIMIT 1), NOW(), 4, NOW(), 4);"
            list_of_statements.append(collections_insert)

            view_collections_insert = "INSERT INTO view_collections (`collection_id`, `bank_id`, `participant_id`, `consent_master_id`, `acquisition_label`, `collection_property`, `collection_notes`, `created`) SELECT `id`, `bank_id`, `participant_id`, `consent_master_id`, `acquisition_label`, `collection_property`, `collection_notes`, `created` FROM collections ORDER BY `id` DESC LIMIT 1;"
            list_of_statements.append(view_collections_insert)


            if row['Sample Name'] in vba_saliva:

                sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + \
                                        row['Sample Name'] + "',126, 'saliva', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), NOW(), 4, NOW(), 4);"
                list_of_statements.append(sample_masters_insert)

                sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(sample_masters_update)

                # Need to check blood's preparation date
                specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(specimen_details_insert)

                view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_label`, `sample_category`)" \
                                      " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL, 'saliva', 126, `id`, `sample_label`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(view_samples_insert)

                sd_spe_salivas_insert = "INSERT INTO sd_spe_salivas (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(sd_spe_salivas_insert)


                for record in vba_saliva[row['Sample Name']]:
                    #print(record['Preparation Date'])
                    # input("Stop")
                    aliquot_barcode = acquisition_label + 'SL' + '000' + str(aliquot_counter)
                    aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + aliquot_barcode + "', '" + \
                                             record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 126 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + \
                                             record['Preparation Date'] + " 00:00:00" + "', 'c', NOW(), 4, NOW(), 4);"
                    list_of_statements.append(aliquot_masters_insert)
                    ad_tubes_insert = "INSERT INTO ad_tubes (`aliquot_master_id`) SELECT `id` FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(ad_tubes_insert)

                    view_aliquots_insert = "INSERT INTO view_aliquots (`aliquot_master_id`, `sample_master_id`, `collection_id`, `bank_id`, `participant_id`, `participant_identifier`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `barcode`, `filemaker_barcode`, `aliquot_type`, `aliquot_control_id`, `in_stock`, `has_notes`) " \
                                           "SELECT `id`, `sample_master_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `participant_identifier` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), 'saliva', 126, NULL, NULL, 'saliva', 126, `barcode`, `filemaker_barcode`, 'tube', 16, `in_stock`, 'n' FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_aliquots_insert)
                    aliquot_counter = aliquot_counter + 1





            if row['Sample Name'] in vba_plasma or row['Sample Name'] in vba_buffy_coat:


                sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + \
                                        row['Sample Name'] + "',2, 'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), NOW(), 4, NOW(), 4);"
                list_of_statements.append(sample_masters_insert)

                sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(sample_masters_update)

                #Need to check blood's preparation date
                specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(specimen_details_insert)

                view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_label`, `sample_category`)" \
                                      " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL,'blood', 2, `id`, `sample_label`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(view_samples_insert)

                sd_spe_bloods_insert = "INSERT INTO sd_spe_bloods (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(sd_spe_bloods_insert)




                if row['Sample Name'] in vba_plasma:
                    # Create Plasma Sample and Aliquots
                    #input("Ready?")
                    #for item in vba_plasma[row['Sample Name']]:
                        #print(item)
                    #input("Stop")



                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_id`, `initial_specimen_sample_type`, `collection_id`, `parent_id`, `parent_sample_type`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + \
                                            row['Sample Name'] + "',9, (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1) ,'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1),'blood', NOW(), 4, NOW(), 4);"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`;"
                    list_of_statements.append(sample_masters_update)

                    # Need to check blood's preparation date
                    derivative_details_insert = "INSERT INTO derivative_details (`creation_datetime`, `sample_master_id`) VALUES (NOW(), (SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(derivative_details_insert)


                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_label`, `sample_category`)" \
                                          " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, 2, 'blood', 2, 'plasma', 9, `id`, `sample_label`, 'derivative' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_der_plasmas_insert = "INSERT INTO sd_der_plasmas (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(sd_der_plasmas_insert)


                    for record in vba_plasma[row['Sample Name']]:
                        #print(record['Preparation Date'])
                        #input("Stop")
                        aliquot_barcode = acquisition_label + 'PL' + '000' + str(aliquot_counter)
                        aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + aliquot_barcode + "', '" + \
                                             record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 9 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + record['Preparation Date'] + " 00:00:00" + "', 'c', NOW(), 4, NOW(), 4);"
                        list_of_statements.append(aliquot_masters_insert)
                        ad_tubes_insert = "INSERT INTO ad_tubes (`aliquot_master_id`) SELECT `id` FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(ad_tubes_insert)

                        view_aliquots_insert = "INSERT INTO view_aliquots (`aliquot_master_id`, `sample_master_id`, `collection_id`, `bank_id`, `participant_id`, `participant_identifier`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `barcode`, `filemaker_barcode`, `aliquot_type`, `aliquot_control_id`, `in_stock`, `has_notes`) " \
                                           "SELECT `id`, `sample_master_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `participant_identifier` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), 'blood', 2, 'blood', 2, 'plasma', 9, `barcode`, `filemaker_barcode`, 'tube', 16, `in_stock`, 'n' FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(view_aliquots_insert)
                        aliquot_counter = aliquot_counter + 1

                if row['Sample Name'] in vba_buffy_coat:

                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_id`, `initial_specimen_sample_type`, `collection_id`, `parent_id`, `parent_sample_type`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + \
                                            row['Sample Name'] + "',137, (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1) ,'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1),'blood', NOW(), 4, NOW(), 4);"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`;"
                    list_of_statements.append(sample_masters_update)

                    # Need to check blood's preparation date
                    derivative_details_insert = "INSERT INTO derivative_details (`creation_datetime`, `sample_master_id`) VALUES (NOW(), (SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(derivative_details_insert)

                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_label`, `sample_category`)" \
                                          " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, 'blood', 2,'buffy coat', 137, `id`, `sample_label`, 'derivative' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_der_buffy_coats_insert = "INSERT INTO sd_der_buffy_coats (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(sd_der_buffy_coats_insert)

                    for record in vba_buffy_coat[row['Sample Name']]:
                        #print(record['Preparation Date'])
                        # input("Stop")
                        aliquot_barcode = acquisition_label + 'BC' + '000' + str(aliquot_counter)
                        aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + aliquot_barcode + "', '" + \
                                                 record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 137 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + \
                                                 record['Preparation Date'] + " 00:00:00" + "', 'c', NOW(), 4, NOW(), 4);"
                        list_of_statements.append(aliquot_masters_insert)
                        ad_tubes_insert = "INSERT INTO ad_tubes (`aliquot_master_id`) SELECT `id` FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(ad_tubes_insert)

                        view_aliquots_insert = "INSERT INTO view_aliquots (`aliquot_master_id`, `sample_master_id`, `collection_id`, `bank_id`, `participant_id`, `participant_identifier`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `barcode`, `filemaker_barcode`, `aliquot_type`, `aliquot_control_id`, `in_stock`, `has_notes`) " \
                                               "SELECT `id`, `sample_master_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `participant_identifier` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), 'blood', 2, 'blood', 2, 'buffy coat', 137, `barcode`, `filemaker_barcode`, 'tube', 65, `in_stock`, 'n' FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(view_aliquots_insert)
                        aliquot_counter = aliquot_counter + 1

            # Tissue

            if row['Sample Name'] in vba_tissue:

                #input("An item")
                for record in vba_tissue[row['Sample Name']]:

                    #print(record)

                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + row['Sample Name'] + "',3, 'tissue', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), NOW(), 4, NOW(), 4);"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(sample_masters_update)

                    specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`, `reception_datetime`, `reception_datetime_accuracy`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1), '" + record['Preparation Date'] + " 00:00:00" + "','c');"
                    list_of_statements.append(specimen_details_insert)

                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`,`sample_type`, `sample_control_id`, `sample_code`, `sample_label`, `sample_category`)" \
                                        " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL,'tissue', 3, `id`, `sample_label`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_spe_tissues_insert = "INSERT INTO sd_spe_tissues (`sample_master_id`, `tissue_nature`, `pathology_reception_datetime`, `pathology_reception_datetime_accuracy`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1), '" + record['Tissue Nature'] + "','" + convert_date_format(row['Preparation Date']) + " 00:00:00" + "','c' );"
                    list_of_statements.append(sd_spe_tissues_insert)

            vba_inserted.add(row['Sample Name'])


filename = './export/vba_participants_for_import' + '.sql'
#print(list_of_statements)
for row in list_of_statements:
    print(row)
with open(filename, 'w', newline='') as file_handler:
    for item in list_of_statements:
        file_handler.write("{}\n".format(item))



#Begin work on participants without inventory

with open('./data/source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    sample_names = set()

    for row in csvreader:
        sample_names.add(row['Sample Name'])

print('All the sample names')
print(sample_names)

with open('./data/ttr_nurse_log_20171023.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    temp = set()

    for row in csvreader:
        if row['AcquisitionID'] not in sample_names:
            temp.add(row['AcquisitionID'])

print('These participants have no inventory')
print(sorted(temp))

temp_check = []
for row in temp:
    if 'VBA' in row:
        #print(row)
        temp_check.append(row)
print(len(temp_check))

# Create SQL statement for inserting VBA Participants that declined consent
list_of_statements_for_participants_no_samples = []
for row in temp:

    #VBA 863 has duplicates
    if 'VBA' in row and row not in {'VBA863'}:


        if len(row) < 7:
            print(row[-3:])
            print('VBA0' + row[-3:])
            vba_num = 'VBA0' + row[-3:]
            print(ttr_participants[row]['First Name'])

        else:
            vba_num = row

        participant_insert = "INSERT INTO participants (`study_type`, `first_name`,`middle_name`,`last_name`,`bcb_nick_name`," \
                             "`phn`,`date_of_birth`,`date_of_birth_accuracy`,`sex`," \
                             "`notes`,`final_diagnosis`,`primary_diagnosis`,`primary_path_number`,`primary_hospital`,`or_hospital`," \
                             "`original_er`,`original_pr`,`her2_fish`, `her2_ihc`,`no_sample_reason`," \
                             "`or_datetime`,`participant_identifier`," \
                             "`last_modification`,`created`, `created_by`, `modified`, `modified_by`) VALUES " + " ('TTR', '" + \
                             ttr_participants[vba_num]['First Name'] + "','" + \
                             ttr_participants[vba_num]['Middle Name'] + "','" + \
                             ttr_participants[vba_num]['Last Name'] + "','" + \
                             ttr_participants[vba_num]['Nick Name'] + "','" + \
                             ttr_participants[vba_num]['PHN'] + "','" + ttr_participants[vba_num][
                                 'DOB'] + "', 'c','" + ttr_participants[vba_num]['Gender'] + "','" + \
                             ttr_participants[vba_num]['Notes'] + "','" + \
                             ttr_participants[vba_num]['Final Diagnosis'] + "','" + \
                             ttr_participants[vba_num]['Primary Diagnosis'] \
                             + "','" + ttr_participants[vba_num]['Primary Path Number'] + "','" + \
                             ttr_participants[vba_num]['Primary Hospital'] + "','" + \
                             ttr_participants[vba_num]['OR Hospital'] \
                             + "','" + ttr_participants[vba_num]['Original ER'] + "','" + \
                             ttr_participants[vba_num]['Original PR'] \
                             + "','" + ttr_participants[vba_num]['HER2 FISH'] + "','" + \
                             ttr_participants[vba_num]['HER2 IHC'] + "','" + \
                             ttr_participants[vba_num]['No Sample Reason'] \
                             + "','" + ttr_participants[vba_num]['OR Date and Time'] + "','" + \
                             ttr_participants[vba_num]['BCCA ID'] + "', NOW(), NOW(), 4, NOW(), 4);"
        list_of_statements_for_participants_no_samples.append(participant_insert)

        vba_num_for_misc_identifier = vba_num[0:3] + "000" + vba_num[3:]
        consent_id = "PBC000" + vba_num[3:]
        acquisition_label = "000" + vba_num[3:]
        misc_identifier_insert = "INSERT INTO misc_identifiers (`identifier_value`, `misc_identifier_control_id`, `participant_id`, `flag_unique`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + vba_num_for_misc_identifier + "', 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 1, NOW(), 4, NOW(), 4);"
        list_of_statements_for_participants_no_samples.append(misc_identifier_insert)


        consent_masters_insert = "INSERT INTO consent_masters (`consent_status`, `consent_signed_date`, `reason_denied`, `notes`, `participant_id`, `consent_control_id`, `created`, `created_by`, `modified`, `modified_by`) VALUES ('" + \
                                 ttr_consent[vba_num]['Consent Status'] + "','" + \
                                 ttr_consent[vba_num]['Date Consent Signed or Declined'] + "','" + \
                                 ttr_consent[vba_num]['Reason Consent Declined'] + "','" + \
                                 ttr_consent[vba_num][
                                     'Notes'] + "',(SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 2, NOW(), 4, NOW(), 4);"

        list_of_statements_for_participants_no_samples.append(consent_masters_insert)


        cd_bcca_breast_insert = "INSERT INTO cd_bcca_breast (`consent_id`, `bcb_study_type`," \
                                "`bcb_path_spec`, `bcb_pathologist`, `bcb_cancer_type`, `bcb_consenting_person`, `genetic_research_status`, `blood_status`, `saliva_status`, `fluid_status`, `fluid_type`, `medical_oncologists_vc`, " \
                                "`consent_master_id`, `dt_created`) VALUES ('" + consent_id + "','" + ttr_consent[vba_num]['Study Type'] + "','" + \
                                ttr_consent[vba_num]['Path SPEC'] + "','" + ttr_consent[vba_num]['Pathologist'] + "','" + ttr_consent[vba_num]['Cancer Type'] + "','" + \
                                ttr_consent[vba_num]['Person Obtaining Consent'] + "','" + \
                                ttr_consent[vba_num]['Genetic Research Status'] + "','" + \
                                ttr_consent[vba_num]['Blood Collected'] + "','" + \
                                ttr_consent[vba_num]['Saliva Collected'] + "','" + \
                                ttr_consent[vba_num]['Fluid Collected'] + "','" + \
                                ttr_consent[vba_num]['Fluid Type'] + "','" + ttr_consent[vba_num]['Surgeon'] + "', (SELECT `id` FROM consent_masters ORDER BY `id` DESC LIMIT 1), '2010-01-01 00:00:00');"

        list_of_statements_for_participants_no_samples.append(cd_bcca_breast_insert)


filename = './export/vba_participants_no_samples_for_import' + '.sql'
#print(list_of_statements)
for row in list_of_statements_for_participants_no_samples:
    print(row)
with open(filename, 'w', newline='') as file_handler:
    for item in list_of_statements_for_participants_no_samples:
        file_handler.write("{}\n".format(item))




