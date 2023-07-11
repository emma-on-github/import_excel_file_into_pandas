# import pandas package as pd
import pandas as pd

# read excel file via url, specifying sheet name
df = pd.read_excel('https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1164031/disability-confident-list-of-employers.xlsx',sheet_name= 'DC Sign ups')

# filter Town/City field
df[df.Town_City=="Oxford"]
