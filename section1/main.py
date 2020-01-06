import pandas as pd
from processors.name_splitter import name_splitter
from processors.name_cleaners import *
from processors.field_creators import create_field_above_100
import schedule
import time
from datetime import datetime
import os


def main():
    current_date_and_time = datetime.today().strftime('%d%m%Y-%H%M')
    input_file = 'assets/input/dataset.csv'

    print("Importing Data")
    if os.path.isfile(input_file):
        original_data = pd.read_csv(input_file)
        data = original_data.copy()

        print("Preprocessing")
        remove_rows_with_missing_name(data)
        remove_salutation(data)
        remove_position(data)
        data = name_splitter(data)

        data = create_field_above_100(data)

        print("Writing data")

        output_file = "output_" + current_date_and_time + ".csv"
        data.to_csv('assets/output/' + output_file, index=False)
        print("File written")
    else:
        print("Dataset file does not exists")


# Run the job everyday at 1:01am
print("Software will run at 1:01 am ... ")
schedule.every().day.at("01:01").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

# main()