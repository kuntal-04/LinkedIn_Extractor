import csv
import pandas as pd

def export_data(data, filename = "linkedin_data", filetype = "csv"):
    
    if not data:
        print("No data to export.")
        return

    if filetype == "csv":
        keys = data[0].keys()

        with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data exported successfully → {filename}.csv")


    elif filetype == "excel":
        df = pd.DataFrame(data)
        df.to_excel(f"{filename}.xlsx", index=False)

        print(f"Data exported successfully → {filename}.xlsx")


    else:
        print("Unsupported format. Choose csv or excel.")