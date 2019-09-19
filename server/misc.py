import csv

# For exact mapping from district number to locations
# refer to https://www.mingproperty.sg/singapore-district-code/

d = {}

with open('postal_code_to_area.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            pass
        else:
            d[row[0]] = {"Postal Sector": row[1].replace(' ', '').split(','), "General Location": row[2].replace(' ','').split(',')}

def get_district_code(postal_code: str):
    first_two = postal_code[0:2]
    for item in d:
        if first_two in d[item]['Postal Sector']:
            return {"District Code": item, "General Location": d[item]['General Location']}

print(get_district_code(postal_code='123456'))