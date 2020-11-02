# icpc-app-screen
- Convenient tool for speeding up the intern/officer review process. 
- Eliminates the pain from reading application responses off Google Sheets. 
- Generates a markdown file for each applicant, containing their all their individual responses. Personal identifiers such as name and email address are stripped away. 

## Required Files
``responses.csv``: csv containing applicant responses

## Run
- ``pip3 install -r requirements.txt``
- ``python3 gen.py``

## Output
- ``candidates``: directory containing markdown versions of the applicant responses (in random order).
- ``candidate_info.csv``: csv file containing details of the (permuted) applicant.
