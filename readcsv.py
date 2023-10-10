import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # 在这里处理每一行的数据
                print(row)
    except FileNotFoundError:
        print("找不到指定的文件:", file_path)
    except Exception as e:
        print("读取CSV文件时发生错误:", str(e))

# 用法示例
csv_file_path = '/home/conrad/PycharmProjects/LIDC-IDRI-Preprocessing/data/Clean/Meta/clean_meta.csv'
read_csv_file(csv_file_path)