docker run \
  -it \
  --name data-copier \
  --rm \
  --network data-copier-nw \
  -v /Users/jasminjoseph/jascode/data-engineering/Research/data/retail_db_json:/retail_db_json \
  -e BASE_DIR=/retail_db_json \
  -e DB_HOST=07f78ae4236b \
  -e DB_NAME=retail_db \
  -e DB_PASS=dbpassword \
  -e DB_PORT=5432 \
  -e DB_USER=retail_user \
  data-copier \
  python /data-copier/app/app.py departments,categories

