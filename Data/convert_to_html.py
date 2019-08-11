import pandas as pd

pd.read_csv("clinicaltrial_data.csv").to_html('clinicaltrial_data.html')
pd.read_csv("mouse_drug_data.csv").to_html('mouse_drug_data.html')
