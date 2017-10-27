import csv
import datetime

def convert_date_format(input_datetime):

    if input_datetime == '':
        return input_datetime
    else:
        print(input_datetime)
        iso_datetime = datetime.datetime.strptime(input_datetime, '%m/%d/%Y').date().isoformat()
        print(iso_datetime)

        return iso_datetime


# Record the number of Tissue for each participants
with open('source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_tissue = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Tissue':

            print(row)

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
with open('source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_plasma = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Plasma':

            print(row)

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

with open('source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_buffy_coat = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Buffy Coat':

            print(row)

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


with open('source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_saliva = dict()

    for row in csvreader:

        if row['Primary Sample Type'] == 'Saliva':

            print(row)

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

with open('source_vba.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    vba_inserted = set()

    for row in csvreader:
        #print(row)

        if row['Sample Name'] not in vba_inserted:

            aliquot_counter = 1
            participant_insert = "INSERT INTO participants (`last_modification`, `created`, `modified`) VALUES (NOW(), NOW(), NOW());"
            list_of_statements.append(participant_insert)

            vba_num = row['Sample Name'][0:3] + "000" + row['Sample Name'][3:]
            consent_id = "PBC000" + row['Sample Name'][3:]
            acquisition_label = "000" + row['Sample Name'][3:]
            #print(vba_num)
            misc_identifier_insert = "INSERT INTO misc_identifiers (`identifier_value`, `misc_identifier_control_id`, `participant_id`, `flag_unique`) VALUES ('" + vba_num + "', 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 1);"
            list_of_statements.append(misc_identifier_insert)

            consent_masters_insert = "INSERT INTO consent_masters (`consent_status`, `participant_id`, `consent_control_id`) VALUES ('obtained', (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), 2);"
            list_of_statements.append(consent_masters_insert)

            cd_bcca_breast_insert = "INSERT INTO cd_bcca_breast (`consent_id`, `bcb_study_type`, `consent_master_id`, `dt_created`) VALUES ('" + consent_id + "', 'ttr', (SELECT `id` FROM consent_masters ORDER BY `id` DESC LIMIT 1), '2010-01-01 00:00:00');"
            list_of_statements.append(cd_bcca_breast_insert)

            collections_insert = "INSERT INTO collections (`acquisition_label`, `bank_id`, `collection_property`, `collection_notes`, `participant_id`, `consent_master_id`) VALUES ('" + acquisition_label + "', 1, 'participant collection', '', (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM consent_masters ORDER BY `id` DESC LIMIT 1));"
            list_of_statements.append(collections_insert)

            view_collections_insert = "INSERT INTO view_collections (`collection_id`, `bank_id`, `participant_id`, `consent_master_id`, `acquisition_label`, `collection_property`, `collection_notes`, `created`) SELECT `id`, `bank_id`, `participant_id`, `consent_master_id`, `acquisition_label`, `collection_property`, `collection_notes`, `created` FROM collections ORDER BY `id` DESC LIMIT 1;"
            list_of_statements.append(view_collections_insert)


            if row['Sample Name'] in vba_saliva:

                sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`) VALUES ('" + \
                                        row['Sample Name'] + "',126, 'saliva', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1));"
                list_of_statements.append(sample_masters_insert)

                sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(sample_masters_update)

                # Need to check blood's preparation date
                specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(specimen_details_insert)

                view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_category`)" \
                                      " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL, 'saliva', 126, `id`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(view_samples_insert)

                sd_spe_salivas_insert = "INSERT INTO sd_spe_salivas (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(sd_spe_salivas_insert)


                for record in vba_saliva[row['Sample Name']]:
                    print(record['Preparation Date'])
                    # input("Stop")
                    aliquot_barcode = acquisition_label + 'SL' + '000' + str(aliquot_counter)
                    aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`) VALUES ('" + aliquot_barcode + "', '" + \
                                             record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 126 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + \
                                             record['Preparation Date'] + " 00:00:00" + "', 'c');"
                    list_of_statements.append(aliquot_masters_insert)
                    ad_tubes_insert = "INSERT INTO ad_tubes (`aliquot_master_id`) SELECT `id` FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(ad_tubes_insert)

                    view_aliquots_insert = "INSERT INTO view_aliquots (`aliquot_master_id`, `sample_master_id`, `collection_id`, `bank_id`, `participant_id`, `participant_identifier`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `barcode`, `filemaker_barcode`, `aliquot_type`, `aliquot_control_id`, `in_stock`, `has_notes`) " \
                                           "SELECT `id`, `sample_master_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `participant_identifier` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), 'saliva', 126, NULL, NULL, 'saliva', 126, `barcode`, `filemaker_barcode`, 'tube', 16, `in_stock`, 'n' FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_aliquots_insert)
                    aliquot_counter = aliquot_counter + 1





            if row['Sample Name'] in vba_plasma or row['Sample Name'] in vba_buffy_coat:


                sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`) VALUES ('" + \
                                        row['Sample Name'] + "',2, 'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1));"
                list_of_statements.append(sample_masters_insert)

                sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(sample_masters_update)

                #Need to check blood's preparation date
                specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(specimen_details_insert)

                view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_category`)" \
                                      " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL,'blood', 2, `id`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                list_of_statements.append(view_samples_insert)

                sd_spe_bloods_insert = "INSERT INTO sd_spe_bloods (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                list_of_statements.append(sd_spe_bloods_insert)




                if row['Sample Name'] in vba_plasma:
                    # Create Plasma Sample and Aliquots
                    #input("Ready?")
                    #for item in vba_plasma[row['Sample Name']]:
                        #print(item)
                    #input("Stop")



                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_id`, `initial_specimen_sample_type`, `collection_id`, `parent_id`, `parent_sample_type`) VALUES ('" + \
                                            row['Sample Name'] + "',9, (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1) ,'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1),'blood');"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`;"
                    list_of_statements.append(sample_masters_update)

                    # Need to check blood's preparation date
                    derivative_details_insert = "INSERT INTO derivative_details (`creation_datetime`, `sample_master_id`) VALUES (NOW(), (SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(derivative_details_insert)


                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_category`)" \
                                          " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, 2, 'blood', 2, 'plasma', 9, `id`,'derivative' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_der_plasmas_insert = "INSERT INTO sd_der_plasmas (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(sd_der_plasmas_insert)


                    for record in vba_plasma[row['Sample Name']]:
                        print(record['Preparation Date'])
                        #input("Stop")
                        aliquot_barcode = acquisition_label + 'PL' + '000' + str(aliquot_counter)
                        aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`) VALUES ('" + aliquot_barcode + "', '" + \
                                             record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 9 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + record['Preparation Date'] + " 00:00:00" + "', 'c');"
                        list_of_statements.append(aliquot_masters_insert)
                        ad_tubes_insert = "INSERT INTO ad_tubes (`aliquot_master_id`) SELECT `id` FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(ad_tubes_insert)

                        view_aliquots_insert = "INSERT INTO view_aliquots (`aliquot_master_id`, `sample_master_id`, `collection_id`, `bank_id`, `participant_id`, `participant_identifier`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `barcode`, `filemaker_barcode`, `aliquot_type`, `aliquot_control_id`, `in_stock`, `has_notes`) " \
                                           "SELECT `id`, `sample_master_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `participant_identifier` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), 'blood', 2, 'blood', 2, 'plasma', 9, `barcode`, `filemaker_barcode`, 'tube', 16, `in_stock`, 'n' FROM aliquot_masters ORDER BY `id` DESC LIMIT 1;"
                        list_of_statements.append(view_aliquots_insert)
                        aliquot_counter = aliquot_counter + 1

                if row['Sample Name'] in vba_buffy_coat:

                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_id`, `initial_specimen_sample_type`, `collection_id`, `parent_id`, `parent_sample_type`) VALUES ('" + \
                                            row['Sample Name'] + "',137, (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1) ,'blood', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT sample_master_id FROM view_samples WHERE `sample_type` = 'blood' ORDER BY sample_master_id DESC LIMIT 1),'blood');"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`;"
                    list_of_statements.append(sample_masters_update)

                    # Need to check blood's preparation date
                    derivative_details_insert = "INSERT INTO derivative_details (`creation_datetime`, `sample_master_id`) VALUES (NOW(), (SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(derivative_details_insert)

                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`, `sample_type`, `sample_control_id`, `sample_code`, `sample_category`)" \
                                          " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, 'blood', 2,'buffy coat', 137, `id`, 'derivative' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_der_buffy_coats_insert = "INSERT INTO sd_der_buffy_coats (`sample_master_id`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1));"
                    list_of_statements.append(sd_der_buffy_coats_insert)

                    for record in vba_buffy_coat[row['Sample Name']]:
                        print(record['Preparation Date'])
                        # input("Stop")
                        aliquot_barcode = acquisition_label + 'BC' + '000' + str(aliquot_counter)
                        aliquot_masters_insert = "INSERT INTO aliquot_masters (`barcode`, `filemaker_barcode`, `aliquot_control_id`, `collection_id`, `sample_master_id`, `in_stock`, `storage_datetime`, `storage_datetime_accuracy`) VALUES ('" + aliquot_barcode + "', '" + \
                                                 record['Barcode'] + "',16, (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1), (SELECT `id` FROM sample_masters WHERE sample_control_id = 137 ORDER BY `id` DESC LIMIT 1), 'yes - available', '" + \
                                                 record['Preparation Date'] + " 00:00:00" + "', 'c');"
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

                    sample_masters_insert = "INSERT INTO sample_masters (`sample_label`, `sample_control_id`, `initial_specimen_sample_type`, `collection_id`) VALUES ('" + row['Sample Name'] + "',3, 'tissue', (SELECT `id` FROM collections ORDER BY `id` DESC LIMIT 1));"
                    list_of_statements.append(sample_masters_insert)

                    sample_masters_update = "UPDATE sample_masters SET `sample_code` = `id`, `initial_specimen_sample_id` = `id` WHERE sample_masters.sample_code = '' AND sample_masters.initial_specimen_sample_id IS NULL ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(sample_masters_update)

                    specimen_details_insert = "INSERT INTO specimen_details (`sample_master_id`, `reception_datetime`, `reception_datetime_accuracy`) VALUES ((SELECT `id` FROM sample_masters ORDER BY id DESC LIMIT 1), '" + record['Preparation Date'] + " 00:00:00" + "','c');"
                    list_of_statements.append(specimen_details_insert)

                    view_samples_insert = "INSERT INTO view_samples (`sample_master_id`, `initial_specimen_sample_id`, `collection_id`, `bank_id`, `participant_id`, `acquisition_label`, `initial_specimen_sample_type`, `initial_specimen_sample_control_id`, `parent_sample_type`, `parent_sample_control_id`,`sample_type`, `sample_control_id`, `sample_code`, `sample_category`)" \
                                        " SELECT `id`, `initial_specimen_sample_id`, `collection_id`, 1, (SELECT `id` FROM participants ORDER BY `id` DESC LIMIT 1), (SELECT `acquisition_label` FROM collections ORDER BY `id` DESC LIMIT 1), `initial_specimen_sample_type`, `sample_control_id`, NULL, NULL,'tissue', 3, `id`, 'specimen' FROM sample_masters ORDER BY `id` DESC LIMIT 1;"
                    list_of_statements.append(view_samples_insert)

                    sd_spe_tissues_insert = "INSERT INTO sd_spe_tissues (`sample_master_id`, `tissue_nature`, `pathology_reception_datetime`, `pathology_reception_datetime_accuracy`) VALUES ((SELECT id FROM sample_masters ORDER BY id DESC LIMIT 1), '" + record['Tissue Nature'] + "','" + row['Preparation Date'] + " 00:00:00" + "','c' );"
                    list_of_statements.append(sd_spe_tissues_insert)

            vba_inserted.add(row['Sample Name'])


filename = 'vba_participants_for_import' + '.sql'
print(list_of_statements)
for row in list_of_statements:
    print(row)
with open(filename, 'w', newline='') as file_handler:
    for item in list_of_statements:
        file_handler.write("{}\n".format(item))
