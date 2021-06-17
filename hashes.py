"""
File : hashes.py
Author : me

count up the number of records in each of the categories and then display the totals of each

Categories:
Preschool
1st-4th
5th-6th
7th-8th
9th
10th
11th
12th
HS-grad
Some-college
Assoc-voc
Assoc-acdm
Bachelors
Prof-school
Masters
Doctorate
"""
census_record = '.\census.csv'
# education_level = {'Preschool': 0, '1st-4th': 0, '5th-6th': 0, '7th-8th': 0, '9th': 0, '10th': 0, '11th': 0, '12th': 0, 'HS-grad': 0, 'Some-college': 0, 'Assoc-voc': 0, 'Assoc-acdm': 0, 'Bachelors': 0, 'Prof-school': 0, 'Masters': 0, 'Doctorate': 0}
education_level = {}

with open(census_record) as census:
    for line in census:
        strip_line = line.strip()
        data = strip_line.split(',')
        education = data[3].strip()
        # print(education)
        if education not in education_level:
            education_level[education] = 1
        elif education in education_level:
            education_level[education] += 1

for level, num in education_level.items():
    print(f'{num} -- {level}')
