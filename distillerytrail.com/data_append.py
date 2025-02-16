import csv

def append_to_csv(dataList):
    # open CSV file and read header
  with open("WhiskeyMaps - Attributes.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Get the first row as header

    # Ensure dataList contains the same keys as header
    dataList = {key: dataList.get(key, "") for key in header}  # Fill missing keys with empty string

    # Append row to CSV
    try:
        with open("WhiskeyMaps - Attributes.csv", "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writerow(dataList)
    except Exception as e:
        print(f"Error appending to CSV: {e}")