# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"44528","system":"gprdproduct"},{"code":"56065","system":"gprdproduct"},{"code":"54606","system":"gprdproduct"},{"code":"48221","system":"gprdproduct"},{"code":"818","system":"gprdproduct"},{"code":"56165","system":"gprdproduct"},{"code":"61155","system":"gprdproduct"},{"code":"48431","system":"gprdproduct"},{"code":"56097","system":"gprdproduct"},{"code":"39652","system":"gprdproduct"},{"code":"65925","system":"gprdproduct"},{"code":"54819","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lipid-lowering-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lipid-lowering-agents-sugarfree---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lipid-lowering-agents-sugarfree---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lipid-lowering-agents-sugarfree---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
