CLS
ping 172.18.2.213
bash -c "telnet 172.18.2.213 9010 | tee -a sekarang.txt "
SLEEP 5

echo “Successful completion”
PAUSE