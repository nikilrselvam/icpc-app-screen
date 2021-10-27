# -*- coding: utf-8 -*-
#
#  gen.py
#
#  Created on 11/1/2020.
#  Copyright © 2020 Nikil Roashan Selvam. All rights reserved.

from mdutils.mdutils import MdUtils
import pandas as pd
import numpy as np
import csv
from collections import defaultdict

RELEVANT_COLS=[1,2,3,5,6,7,8,10,11,12,13,15,16,17,18]
df=pd.read_csv("responses.csv", usecols=RELEVANT_COLS, converters=defaultdict(lambda i: str),keep_default_na=False).astype('str').replace(r'^\s*$', "``No Response``", regex=True)

# numbered amongst relevant cols
BIO_COLS=[2,3,4,5]
ACM_COLS=[6,7,8,9,10,11]
ICPC_COLS=[12,13,14]

sigma=np.random.permutation(len(df))
with open('candidate_info.csv', 'w') as csvfile:
  csvwriter = csv.writer(csvfile)
  headers=['Candidate Number', 'Name', 'Email Address']
  csvwriter.writerow(headers)
  for i, candidate_num in enumerate(sigma):
    candidate_info=[i,df.iloc[candidate_num][1],df.iloc[candidate_num][0]]
    csvwriter.writerow(candidate_info)

for i, candidate_num in enumerate(sigma):
  mdFile = MdUtils(file_name='../candidates/candidate_'+str(i),title='Candidate '+str(i))
  mdFile.new_header(level=2, title="Bio",add_table_of_contents='n')
  for col in BIO_COLS:
    mdFile.new_line(df.columns[col]+ ": " + "``"+df.iloc[candidate_num][col]+"``")

  mdFile.new_header(level=2, title="General ACM Questions",add_table_of_contents='n')
  for col in ACM_COLS:
    mdFile.new_header(level=4, title=df.columns[col],add_table_of_contents='n')
    for text in df.iloc[candidate_num][col].split('\n'):
      mdFile.write(">"+text.strip()+"\n")

  mdFile.new_header(level=2, title="ICPC Questions",add_table_of_contents='n')
  for col in ICPC_COLS:
    mdFile.new_header(level=4, title=df.columns[col],add_table_of_contents='n')
    for text in df.iloc[candidate_num][col].split('\n'):
      mdFile.write(">"+text.strip()+"\n")
  mdFile.create_md_file()


