# Usage: sh process_logs.sh APP_NAME SECRET_KEY OUTPUT_PATH GO_ACCESS_PARAMS
# GO_ACCESS_PARAMS can be "-oreport.html" to generate a report.

BIN_PATH="$(cd "$(dirname "$0")"; pwd)"
APP_NAME=$1
SECRET_KEY=$2
OUTPUT_PATH=$3

echo $BIN_PATH
echo $BIN_PATH/get_sae_logs.py --appname="$APP_NAME" \
  --from_date=`date -d '1 day ago' '+%Y%m%d'` \
  --to_date=`date -d '1 day ago' '+%Y%m%d'` \
  --secret_key=$SECRET_KEY \
  --output_path=${OUTPUT_PATH} 

ALL_OUTPUT=${OUTPUT_PATH}/acc*/*

cat "${ALL_OUTPUT}" | goaccess  --log-format='%^ %h %^ %T [%d:%t %^] %^ %^ %^ %m %U %H %s %b "%R" "%u" %^' --date-format='%d/%b/%Y' --time-format='%H:%M:%S' -a --enable-panel=OS --real-os $4
#cat $@ | goaccess  --log-format='%^ %h %^ %T [%d:%t %^] %^ %^ %^ %m %U %H %s %b "%R" "%u" %^' --date-format='%d/%b/%Y' --time-format='%H:%M:%S' -a --real-os -o report.html
