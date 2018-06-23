#!/usr/bin/env python
import boto3
import pymysql

endpoint = 'aurora-prototype.cluster-cjo474vpe5k3.eu-west-1.rds.amazonaws.com'
user = 'karl'

client = boto3.client('rds', region_name='eu-west-1')
token = client.generate_db_auth_token(endpoint, 3306, user)
ssl = {'ca': 'rds-combined-ca-bundle.pem'}
conn = pymysql.connect(endpoint, db='mysql', port=3306, user=user, password=token, ssl=ssl)

with conn.cursor() as cursor:
    sql = 'SELECT user()'
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

conn.close()
