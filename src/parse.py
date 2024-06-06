# 1. Read `official.xls` and open the sheet named `배정한자`
# 2. Transform the data into a CSV file with following columns:
#    - 급수 -> level
#    - 한자 -> hanja
#    - 대표훈음 -> meaning
#    - 부수 -> radical
#    - 획수 -> strokes
#    - 총획 -> total_strokes
#    - 대표음 -> main_sound
# 3. Write the transformed data into a CSV file

import pandas as pd

# Read the Excel file

path = 'official.xls'
df = pd.read_excel(path, sheet_name='배정한자')

# Rename the columns as specified

df.rename(columns={
    '급수': 'level',
    '한자': 'hanja',
    '대표훈음': 'meaning',
    '부수': 'radical',
    '획수': 'strokes',
    '총획': 'total_strokes',
    '대표음': 'main_sound'
}, inplace=True)

# Drop 음표 column

df.drop('음표', axis=1, inplace=True)

# Convert 급수 with a dictionary

level_dict = {

    0: '특급',
    2: '특급Ⅱ',
    10: '1급',
    12: '2급',
    20: '2급',
    30: '3급',
    32: '3급Ⅱ',
    40: '4급',
    42: '4급Ⅱ',
    50: '5급',
    52: '5급Ⅱ',
    60: '6급',
    62: '6급Ⅱ',
    70: '7급',
    72: '7급Ⅱ',
    80: '8급'

}

df['level'] = df['level'].map(level_dict)

def process_대표훈음(meanings):
    meanings = meanings.replace("(:)", "").replace(":", "")
    meanings = [process_meaning(meaning) for meaning in meanings.split('|')]
    return meanings

def process_meaning(meaning):
    try:
        hun, doc = meaning.strip().rsplit(' ', 1)
    except ValueError:
        hun, doc = meaning[:-1], meaning[-1]

    hun = [_hun.strip() for _hun in hun.strip().split('/')]
    doc = [_doc.strip() for _doc in doc.strip().split('/')]

    return [
        hun, doc
    ]

df['meaning'] = df['meaning'].apply(process_대표훈음)

# Write the transformed DataFrame to a new CSV file

df.to_csv('transformed_data.csv', index=False)