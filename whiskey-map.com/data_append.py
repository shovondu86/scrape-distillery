import csv
import os

csv_file = "distilleries.csv"

def append_to_csv(data):
    # Check if file exists
    file_exists = os.path.isfile(csv_file)

    # Read existing headers (if file exists)
    if file_exists:
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader, [])
            data = {key: data.get(key, "") for key in headers}
    else:
        headers = data.keys()

    # Read existing data if headers need updating
    rows = []
    if file_exists:
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)  # Store old data

    # Append new data
    rows.append(data)

    # Write updated data back to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  # Write headers if file is new
        writer.writerows(rows)  # Write all data back

    print(f"Data appended to {csv_file}")

# Your dictionary data
datalist = {
  'dis_name': 'Borders',
  'instagram_link': 'https://www.instagram.com/thebordersdistillery',
  'short_info': '',
  'region': '',
  'founded': '',
  'owner': '',
  'status': 'operational',
  'website': 'www.thebordersdistillery.com',
  'open_for_visits': '',
  'capacity': '',
  'types': 'single malt',
  'cereals': '',
  'water': '',
  'longitude': '-2.78878',
  'latitude': '55.42475'
}

# Append the entire dictionary instead of filtering
#append_to_csv(datalist)
