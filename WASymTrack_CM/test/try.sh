curl --header "Content-Type: application/json"   \
  --request POST   --data \
  "`cat $1`" \
  http://ar-aub.com/try
