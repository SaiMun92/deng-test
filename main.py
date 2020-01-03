import pandas as pd
from processors.name_splitter import name_splitter
from processors.name_cleaners import *
from processors.field_creators import create_field_above_100
import schedule
import time
from datetime import datetime


def main():
    current_date_and_time = datetime.today().strftime('%d%m%Y-%H%M')

    print("Importing Data")
    original_data = pd.read_csv('assets/dataset.csv')
    data = original_data.copy()

    print("Preprocessing")
    remove_rows_with_missing_name(data)
    remove_salutation(data)
    remove_position(data)
    data = name_splitter(data)

    data = create_field_above_100(data)

    print("Writing data")

    output_file = "output_" + current_date_and_time + ".csv"
    data.to_csv('assets/' + output_file, index=False)


# Run the job everyday at 1:00am
schedule.every().day.at("01:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

# main()