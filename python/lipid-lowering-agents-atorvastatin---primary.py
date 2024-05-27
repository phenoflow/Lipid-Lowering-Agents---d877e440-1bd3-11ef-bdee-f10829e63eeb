# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"56182","system":"gprdproduct"},{"code":"53890","system":"gprdproduct"},{"code":"58742","system":"gprdproduct"},{"code":"60989","system":"gprdproduct"},{"code":"66963","system":"gprdproduct"},{"code":"60607","system":"gprdproduct"},{"code":"53772","system":"gprdproduct"},{"code":"59776","system":"gprdproduct"},{"code":"52821","system":"gprdproduct"},{"code":"52459","system":"gprdproduct"},{"code":"5775","system":"gprdproduct"},{"code":"57836","system":"gprdproduct"},{"code":"57117","system":"gprdproduct"},{"code":"62476","system":"gprdproduct"},{"code":"63249","system":"gprdproduct"},{"code":"58418","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lipid-lowering-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lipid-lowering-agents-atorvastatin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lipid-lowering-agents-atorvastatin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lipid-lowering-agents-atorvastatin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
