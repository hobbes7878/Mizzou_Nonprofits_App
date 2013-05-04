import csv
import glob
import re

#Point to whatever folder CSVs are in. Remember to leave "\*.csv"
csv_files=glob.glob("C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\*.csv")

#divy files for each scraper
Balance_Sheet_CSVs =[]
Revenue_Expense_CSVs=[]
Officers_Trustees_CSVs=[]
Highest_Paid_CSVs=[]

for an_file in csv_files:
    if re.search("Balance_Sheet",an_file):
        Balance_Sheet_CSVs.append(an_file)
    if re.search("Revenue_Expense",an_file):
        Revenue_Expense_CSVs.append(an_file)
    if re.search("Officers_Trustees",an_file):
        Officers_Trustees_CSVs.append(an_file)
    if re.search("Highest_Paid",an_file):
        Highest_Paid_CSVs.append(an_file)

##########################################################
print "Processing Balance Sheet"
for each_file in Balance_Sheet_CSVs:
    print each_file
    csv_write_list=[]
    rows=[]
    valuesDict={}
    with open(each_file,'rb') as csvfile:
        current_csv = csv.reader(csvfile, delimiter=",")

        for row in current_csv:
            rows.append(row)

            if len(row)>2:
                if row[0] in valuesDict:
                    valuesDict[row[0]+" Liabilities"]=row[1:]
                else:
                    valuesDict[row[0]]=row[1:]


        #GET EIN and NAME in first row
        EIN_row=rows[0]
        EIN_string=EIN_row[0]
        pattern=re.compile(r'for ([A-Z].*), EIN: (\d{2}-\d{7})')
        match=re.search(pattern, EIN_string)
        Nonprof_NAME = match.group(1)
        Nonprof_EIN = match.group(2)

        Dates_list=valuesDict['Assets']

        for key in valuesDict:
            index_start=0 #index_start to get index of duplicate values in list
            for value in valuesDict[key]:
                if value == "":
                    continue
                else:
                    index=valuesDict[key].index(value,index_start)
                    index_start=index+1
                    value_set=[Nonprof_EIN,Nonprof_NAME,key,Dates_list[index],value]
                    csv_write_list.append(value_set)

### POINT TO OUTFILE ###
    with open('C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\Data\Balance_Sheet_data.csv','ab') as csvfile:
        csv_writer=csv.writer(csvfile, delimiter=",")

        for csv_flat_row in csv_write_list:
            if len(csv_flat_row)>3:
                #only write dollar amounts
                if re.search('\$',csv_flat_row[4]):
                    #don't write 'Change' amounts
                    if re.search('Change',csv_flat_row[3]):
                        continue
                    else:
                        csv_writer.writerow(csv_flat_row)
 
##########################################################
print "Processing Revenue Expense"      
for each_file in Revenue_Expense_CSVs:
    csv_write_list=[]
    rows=[]
    valuesDict={}

    with open(each_file,'rb') as csvfile:
        current_csv = csv.reader(csvfile, delimiter=",")

        for row in current_csv:
            rows.append(row)

            if len(row)>2:
                if row[0] in valuesDict:
                    valuesDict[row[0]+" Expenses"]=row[1:] 
                else:
                    valuesDict[row[0]]=row[1:]               

        #GET EIN and NAME in first row
        EIN_row=rows[0]
        EIN_string=EIN_row[0]
        pattern=re.compile(r'for ([A-Z].*), EIN: (\d{2}-\d{7})')
        match=re.search(pattern, EIN_string)
        Nonprof_NAME = match.group(1)
        Nonprof_EIN = match.group(2)

        Dates_list=valuesDict['Expenses']
        for key in valuesDict:
            index_start=0
            for value in valuesDict[key]:
                if value == "":
                    continue
                else:
                    index=valuesDict[key].index(value,index_start)
                    index_start=index
                    value_set=[Nonprof_EIN,Nonprof_NAME,key,Dates_list[index],value]
                    csv_write_list.append(value_set)

### POINT TO OUTFILE ###
    with open('C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\Data\Revenue_Expense_data.csv','ab') as csvfile:
        csv_writer=csv.writer(csvfile, delimiter=",")

        for csv_flat_row in csv_write_list:
            if len(csv_flat_row)>3:
                if re.search('\$',csv_flat_row[4]):
                    csv_writer.writerow(csv_flat_row)

########################################################## 
print "Processing Highest Paid"
for each_file in Highest_Paid_CSVs:
    csv_write_list=[]
    rows=[]
    Values_List=[]
    with open(each_file,'rb') as csvfile:
        current_csv = csv.reader(csvfile, delimiter=",")

        Table_starts = []
        for row in current_csv:
            rows.append(row)

         #GET EIN and NAME in first row
        EIN_row=rows[0]
        EIN_string=EIN_row[0]
        pattern=re.compile(r'for ([A-Z].*), EIN: (\d{2}-\d{7})')
        match=re.search(pattern, EIN_string)
        Nonprof_NAME = match.group(1)
        Nonprof_EIN = match.group(2)

        for row in rows:
            if len(row)>=1:
                if re.match('Fiscal Year',row[0]):
                    Table_starts.append(rows.index(row))

        #Add Last Row
        Table_starts.append(len(rows)-1)

        Row_Ranges=[]
        for start in Table_starts[:-1]:
            index=Table_starts.index(start)
            Row_Ranges.append(range( start,Table_starts[index+1] ) )

        for row_range in Row_Ranges:
            #Get Year
            row=rows[row_range[0]]
            match=re.search('Fiscal Year: (\d{4})',row[0])
            Fiscal_Year=match.group(1)

            for rr in row_range:
                temp_list=[Nonprof_EIN,Nonprof_NAME,Fiscal_Year]
                row=rows[rr]
                if len(row)>2:
                    for r in row:
                        temp_list.append(r)
                Values_List.append(temp_list)

### POINT TO OUTFILE ###
    with open('C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\Data\Highest_Paid_data.csv','ab') as csvfile:
        csv_writer=csv.writer(csvfile, delimiter=",")

        for csv_flat_row in Values_List:
            if len(csv_flat_row)>3:
                csv_writer.writerow(csv_flat_row)

##########################################################
print "Processing Officers Trustees"
for each_file in Officers_Trustees_CSVs:
    csv_write_list=[]
    rows=[]
    Values_List=[]
    with open(each_file,'rb') as csvfile:
        current_csv = csv.reader(csvfile, delimiter=",")

        Table_starts = []
        for row in current_csv:
            rows.append(row)

         #GET EIN and NAME in first row
        EIN_row=rows[0]
        EIN_string=EIN_row[0]
        pattern=re.compile(r'for ([A-Z].*), EIN: (\d{2}-\d{7})')
        match=re.search(pattern, EIN_string)
        Nonprof_NAME = match.group(1)
        Nonprof_EIN = match.group(2)

        for row in rows:
            if len(row)>=1:
                if re.match('Fiscal Year',row[0]):
                    Table_starts.append(rows.index(row))

        #Add Last Row
        Table_starts.append(len(rows)-1)

        Row_Ranges=[]
        for start in Table_starts[:-1]:
            index=Table_starts.index(start)
            Row_Ranges.append(range( start,Table_starts[index+1] ) )

        for row_range in Row_Ranges:
            #Get Year
            row=rows[row_range[0]]
            match=re.search('Fiscal Year: (\d{4})',row[0])
            Fiscal_Year=match.group(1)

            for rr in row_range:
                temp_list=[Nonprof_EIN,Nonprof_NAME,Fiscal_Year]
                row=rows[rr]
                if len(row)>2:
                    for r in row:
                        temp_list.append(r)
                Values_List.append(temp_list)

### POINT TO OUTFILE ###
    with open('C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\Data\Officers_Trustees_data.csv','ab') as csvfile:
        csv_writer=csv.writer(csvfile, delimiter=",")

        for csv_flat_row in Values_List:
            if len(csv_flat_row)>3:
                csv_writer.writerow(csv_flat_row)


############################################################3
### Remove Any Duplicates from CSV Files ### STOLEN FROM INTERWEBS

### POINT TO OUTFILE ###
output_csv_files=glob.glob("C:\Dropbox\Grad School\MU\Spring 2013\Advanced Data\Test CSVs\Data\*.csv")

for outfile in output_csv_files:
    rows = csv.reader(open(outfile, "rb"))
    newrows = []
    for row in rows:
        if row not in newrows:
            newrows.append(row)
    writer = csv.writer(open(outfile, "wb"))
    writer.writerows(newrows)