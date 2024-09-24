import csv

#with open("stock_data.csv", "r") as file:
 #   reader = DictReader(file)
  #  for row in reader:
   #     print(row)

with open("OutPut.txt", "w") as file:
    writer = csv.writer(file, delimiter=":")
    writer.writerow(["name", "age", "city"])
    writer.writerow(["manu","18","kannur"])

with open("DictOutPut.txt", "w") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "name", "age": 22, "city":"kannur"})


try:
    with open("stock_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error as e:
    print(f"ERROR reading csv file :{e}")
except FileNotFoundError:
    print(f"Not a such a file is found")
except Exception:
    print("somthing went wrong")