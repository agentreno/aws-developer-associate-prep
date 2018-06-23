# Necessary because CloudFormation doesn't support resource properties for this
aws rds modify-db-cluster \
  --db-cluster-identifier aurora-prototype \
  --enable-iam-database-authentication \
  --apply-immediately

DB_CLUSTER_ID=$(aws rds describe-db-clusters \
  --db-cluster-identifier aurora-prototype \
  --query 'DBClusters[0].Endpoint' \
	| sed s/\"//g
)

mysql -u root -h $DB_CLUSTER_ID -p -e \
  "CREATE USER karl IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS'"

# Must use SSL when connecting with IAM auth, need certs
wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
