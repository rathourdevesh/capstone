cd ../
pid=`pf -ef | grep django | awk '{print $1}'`
kill $pid
rm -rf capstone