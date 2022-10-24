import os
import pandas as pd


def get_json_reader(base_dir, table_name, chunk_size=1000):
    file_name = os.listdir(f'{base_dir}/{table_name}')[0]
    fp = f'{base_dir}/{table_name}/{file_name}'
    return pd.read_json(fp,lines=True,chunksize=chunk_size)


if __name__=='__main__':
    base_dir = os.environ.get('BASE_DIR')
    table_name = os.environ.get('TABLE_NAME')
    json_reader = get_json_reader(base_dir,table_name)

    for idx,df in enumerate(json_reader):
        print(f"No: of records in chunks with {idx} is {df.shape[0]}")
