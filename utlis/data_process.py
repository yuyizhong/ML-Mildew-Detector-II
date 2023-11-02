import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime


def download_df_as_csv(df):
    """
    download dataframe and save it as csv file
    """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv_data = df.to_csv(index=False)
    csv_encoded = csv_data.encode('utf-8')
    b64_encoded = base64.b64encode(csv_encoded).decode('utf-8')
    href = (
        f'<a href="data:file/csv;base64,{b64_encoded}" '
        f'download="Report_{datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href
