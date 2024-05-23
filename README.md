# Project

Project to collate total numbers of each individual part against a bill of materials
The bill of materials will be in a file named in the format 'YY-XXX-001', where Y is the year of production, X is the project number (plus 200 to make it look like they do more work), and 001, which indicates that it is the General Arrangement.

Each file contains one part and it's ingredients as a csv file named by part number, a rawing title row, and then columns under the following headers:
 - Part No - Index, irrelavent
 - Description - Necessary to have in the final list, generally irrelevant
 - Dwg Ref - Necessary to have in final list - If Source == 'B', then supplied as is. if Source == 'M' Then need to investigate the .csv file with the matching name
 - Qty - Self explanatory, or if Dan reads this, number of items
 - Source - Whether item manufactured (M - requires further investigation) or bought (B - is bottom level, quantity should be added to final list)

Requested output:
 - One file that lists all base components with their drawing_reference, their descriptions, their total quantities.
 - EXTRA CREDIT: List of drawings where each part is located and how many of each base part are in each drawing