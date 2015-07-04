Silly little script to push Nagios alerts into Logstash via UDP

# Example Nagios Command

~~~~bash
nagios2logstash.py --logstash-host ingress-udp.flume.prd.atl.3dna.io --logstash-port 4092 --host --hostname "$HOSTNAME$" --hoststate "$HOSTSTATE$" --hostaddress "$HOSTADDRESS" --longdatetime="$LONGDATETIME$" --hostoutput "$SERVICEOUTPUT"

nagios2logstash.py --logstash-host logstash.example.com --logstash-port 1234 --service --servicedesc "$SERVICEDESC$" --host "$HOSTALIAS$" --hostaddress "$HOSTADDRESS" --servicestate "$SERVICESTATE$" --longdatetime="$LONGDATETIME$" --serviceoputput "$SERVICEOUTPUT"
~~~~
