import os
import shutil
from datetime import datetime

import pymongo
import pandas as pd
import pymysql

# 获取当前日期
current_date = datetime.now().strftime("%Y%m%d")

# ------------------MongoDB 连接信息------------------
mongo_host = "192.168.2.14"
mongo_port = 27018
mongo_username = "root"
mongo_password = "123456"
mongo_database = "db_haodf"
mongo_collection = 'disease_page'
mongo_collection_list = ['disease_page']
mongo_backup_dir = "/home/lym/db_backup/storage"
# mongo_backup_dir = "E:\Project\ScrapyProject\others\storage"

# 删除目录下的所有文件
if os.path.exists(mongo_backup_dir):
    shutil.rmtree(mongo_backup_dir)
os.makedirs(mongo_backup_dir)

# 连接 MongoDB
client = pymongo.MongoClient(mongo_host, mongo_port, username=mongo_username, password=mongo_password)
db = client[mongo_database]

for collection_unit in mongo_collection_list:
    collection = db[collection_unit]
    # 执行查询并转换为 DataFrame
    cursor = collection.find()
    data = list(cursor)
    print(f'Number of documents retrieved from MongoDB: {len(data)}')  # 调试输出
    df = pd.DataFrame(data)
    # 将 DataFrame 保存到 CSV 文件
    csv_file_path = os.path.join(mongo_backup_dir, f'mongo_{mongo_database}_{collection_unit}_{current_date}.csv')
    df.to_csv(csv_file_path, index=False)
    print(f'MongoDB 数据库已备份到 {csv_file_path}')

# ------------------MySQL 连接信息------------------
mysql_host = '192.168.1.204'
mysql_port = 3308
mysql_user = 'root'
mysql_password = '123456'
mysql_database = 'db_haodf'
mysql_table_list = ['disease_answer', 'disease_page', 'disease_user']
mysql_backup_dir = "/home/lym/db_backup/storage"
# mysql_backup_dir = "E:\Project\ScrapyProject\others\storage"

# 连接 MySQL
conn = pymysql.connect(
    host=mysql_host,
    port=mysql_port,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
cursor = conn.cursor()

for table_unit in mysql_table_list:
    # 执行查询
    query = f'SELECT * FROM {table_unit}'
    cursor.execute(query)
    # 获取字段名
    field_names = [i[0] for i in cursor.description]
    # 将查询结果保存到 DataFrame
    data = cursor.fetchall()
    print(f'Number of rows retrieved from MySQL: {len(data)}')  # 调试输出
    df = pd.DataFrame(data, columns=field_names)
    # 将 DataFrame 保存到 CSV 文件
    csv_file_path = os.path.join(mysql_backup_dir, f'mysql_{mysql_database}_{table_unit}_{current_date}.csv')
    df.to_csv(csv_file_path, index=False)
    print(f'MySQL 数据库已备份到 {csv_file_path}')

# 关闭连接
cursor.close()
conn.close()
