clear
echo "You must provide email address and password as the two arguments to this script"
cd /var/lib/boinc-client
boinccmd --lookup_account http://setiathome.berkeley.edu $1 $2
echo "Make a note of your account key to use with the next script"

