Silly little script to push Nagios alerts into Logstash via UDP

# Sample Nagios Commands
~~~~bash
define command {
    command_line                   /usr/local/bin/nagios2logstash.py --logstash-host "logstash.example.com" --logstash-port "1234" --host --hostname "$HOSTNAME$" --hoststate "$HOSTSTATE$" --hostaddress "$HOSTADDRESS$" --longdatetime="$LONGDATETIME$" --hostoutput "$HOSTOUTPUT$"
    command_name                   notify-host-by-logstash
}

define command {
    command_line                   /usr/local/bin/nagios2logstash.py --logstash-host "logstash.example.com" --logstash-port "1234" --service --servicedesc "$SERVICEDESC$" --hostalias "$HOSTALIAS$" --hostaddress "$HOSTADDRESS$" --servicestate "$SERVICESTATE$" --longdatetime "$LONGDATETIME$" --serviceoutput "$SERVICEOUTPUT$"
    command_name                   notify-service-by-logstash
}
~~~~