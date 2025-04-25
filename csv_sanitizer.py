import csv
import argparse
import pandas as pd
parser=argparse.ArgumentParser(description="Cleans CSV files")
parser.add_argument("-c","--column_names",nargs="+",action="store",help="All expected names for columns")
parser.add_argument("--fix_column_names",action="store_true",help="Match column names to expected column names (fixes casing and spacing issues)")
parser.add_argument("--duplicate_rows",action="store_true",help="Remove duplicate rows in selected or in all columns")
parser.add_argument("--select_columns",nargs="+",default="all",action="store",help="Select specific columns to clean, default = all (insert names of columns)")
parser.add_argument("--remove_rows",action="store_true",help="Remove rows that have missing values")
parser.add_argument("--fix_data_types",action="store_true",help="Change values to correct data types")
parser.add_argument("--types",action="store",help="Expected data types for each column")
parser.add_argument("-i","--input_file",action="store",help="Input file")
parser.add_argument("-o","--output_file",action="store_true",help="Output file")
parser.add_argument("-t","--trim_whitespace",action="store_true",help="Remove leading and trailing whitespace from all strings")
parser.add_argument("--space_replace",default="_",action="store",help="What to replace spaces with in column names (default = _)")
parser.add_argument("--remove_bad_rows",action="store_true",help="Remove rows containing incorrect value types that can't be converted")

args=parser.parse_args()

def select_columns(file):
    if args.select_columns=="all":
        return list(file.columns)
    else:
        return list(args.select_columns)

"""def column_types():
    return list(args.types)"""

def file_input(file):
    return pd.read_csv(file)

def file_output(file):
    file.reset_index(drop=True)
    new_file_name="cleaned_"+file_name
    file.to_csv(new_file_name,index=False)
    return new_file_name

"""def type_convert(file):
    counter=0
    for column in file.columns:
        

        counter+=1"""
def whitespace_remover(file_whitespace):
    for x in file_whitespace.columns:
        if file_whitespace[x].dtype=="object":
            try:
                file_whitespace[x]=file_whitespace[x].map(str.strip)
            except:
                pass
        else:
            pass
    return file_whitespace

#def remove_duplicate_rows(file_duplicates):

def column_name_fix(file_name_fix):
    columns_list=list(file_name_fix.columns)
    names_list=list(args.column_names)
    for x in range(len(columns_list)):
        columns_list[x]=columns_list[x].replace(" ",args.space_replace)
        for y in range(len(names_list)):
            if (columns_list[x]).lower()==(names_list[y]).lower():
                columns_list[x]=names_list[y]
    file_name_fix.columns=columns_list
    return file_name_fix

def rows_remove(file_rows_remove):
    file_rows_remove=file_rows_remove.dropna(subset=columns_selected)
    return file_rows_remove

def empty_remove(file_empty_rows):
    file_empty_rows=file_empty_rows.dropna(how="all")
    return file_empty_rows

if len(args.input_file)>0:
    file_name=args.input_file
    file_new=file_input(args.input_file)
file_new=empty_remove(file_new)
columns_selected=select_columns(file_new)
#types_columns=column_types()
if args.trim_whitespace:
    file_new=whitespace_remover(file_new)
if args.fix_column_names:
    file_new=column_name_fix(file_new)
if args.remove_rows:
    file_new=rows_remove(file_new)
if args.output_file:
    print(file_output(file_new))
    print(file_new)

    










    




