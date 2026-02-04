# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from io import BytesIO

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
Input_Datasets = dataiku.Folder("Input Data")
Input_Datasets_info = Input_Datasets.get_info()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
file_paths = Input_Datasets.list_paths_in_partition()
first_file_path = file_paths[0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
with Input_Datasets.get_download_stream(first_file_path) as f:
    data = f.read()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = pd.read_csv(BytesIO(data))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['total'] = df['tshirt_price'] * df['tshirt_quantity']

# update text category description
df['tshirt_category'] = df['tshirt_category'].str.replace('Wh ', 'White ')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
processed_dataset_df = df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
# Dataset processed_data renamed to t_shirt_data by neba.nfonsang on 2024-09-16 20:58:07
processed_dataset = dataiku.Dataset("t_shirt_data")
processed_dataset.write_with_schema(processed_dataset_df)

