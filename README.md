# icpc-app-screen
- Convenient tool for speeding up the intern/officer applicant review process.
- Eliminates the pain from reading application responses off Google Sheets.
- Generates a markdown file for each applicant, containing all their individual responses. Personal identifiers such as name and email address are stripped away.

## Required Files
``responses.csv``: csv containing applicant responses from the Google Form.

## Run
- ``pip3 install -r requirements.txt``
- ``python3 gen.py``

## Output
- ``candidates``: directory containing markdown versions of the applicant responses (ordered by a random permutation).
- ``candidate_info.csv``: csv file containing details of the (permuted) applicants.

Note: The ``RELEVANT_COLS`` list and related constants in  ``gen.py`` must be tweaked to represent the columns to be contained in the markdown.