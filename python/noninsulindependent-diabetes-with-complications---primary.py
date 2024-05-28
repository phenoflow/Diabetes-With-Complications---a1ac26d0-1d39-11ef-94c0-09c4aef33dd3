# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"C109100","system":"readv2"},{"code":"C109C00","system":"readv2"},{"code":"C108100","system":"readv2"},{"code":"C108700","system":"readv2"},{"code":"C108D00","system":"readv2"},{"code":"C109600","system":"readv2"},{"code":"C108F00","system":"readv2"},{"code":"C108H00","system":"readv2"},{"code":"C108200","system":"readv2"},{"code":"C108000","system":"readv2"},{"code":"C109E00","system":"readv2"},{"code":"C109000","system":"readv2"},{"code":"E11.3","system":"readv2"},{"code":"E11.4","system":"readv2"},{"code":"E10.2","system":"readv2"},{"code":"E11.2","system":"readv2"},{"code":"E10.4","system":"readv2"},{"code":"E10.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-with-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["noninsulindependent-diabetes-with-complications---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["noninsulindependent-diabetes-with-complications---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["noninsulindependent-diabetes-with-complications---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
