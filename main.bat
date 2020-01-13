CLS
ping 172.18.2.213
bash -c "telnet 172.18.2.213 9010 | tee -a todayNow.txt "
SLEEP 5
bash -c "python3 filltering.py"
SLEEP 5
echo “Successful completion”
PAUSE