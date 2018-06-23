# Change these as needed
RDS_HOST=aurora-prototype.cluster-ro-cjo474vpe5k3.eu-west-1.rds.amazonaws.com"
USER=karl

TOKEN=$(aws rds generate-db-auth-token \
   --hostname $RDS_HOST \
   --port 3306 \
   --region eu-west-1 \
   --username $USER \
)

echo $TOKEN

mysql \
   --host=$RDS_HOST \
   --port=3306 \
   --ssl-ca=rds-combined-ca-bundle.pem \
   --enable-cleartext-plugin \
   --user=$USER \
   --password=$TOKEN
