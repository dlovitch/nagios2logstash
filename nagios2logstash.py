#! /usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#
# ©2015 David Lovitch <dlovitch@gmail.com>
#
##############################################################################

import sys # should always exist
try:
    import socket
    import argparse
    import syslog
    import json
except ImportError:
    sys.exit('Failed to import at least one module, exiting.')

parser = argparse.ArgumentParser(description="Nagios to Logstash")
parser.add_argument("--logstash-host", help="Logstash hostname", required=True)
parser.add_argument("--logstash-port", help="Logstash port", required=True)
parser_notificationtype = parser.add_mutually_exclusive_group(required=True)
parser_notificationtype.add_argument("--host", help="Host notification", action="store_true")
parser_notificationtype.add_argument("--service", help="Service Notification", action="store_true")
parser.add_argument("--hostaddress", help="Host address")
parser.add_argument("--longdatetime", help="Date/time")
parser_hostnotification = parser.add_argument_group('Host Notification', 'Host notifications')
parser_hostnotification.add_argument("--hostname", help="Hostname")
parser_hostnotification.add_argument("--hoststate", help="Host state")
parser_hostnotification.add_argument("--hostoutput", help="Host output")
parser_servicenotification = parser.add_argument_group('Service Notification', 'Service notifications')
parser_servicenotification.add_argument("--servicedesc", help="Service description")
parser_servicenotification.add_argument("--hostalias", help="Host alias")
parser_servicenotification.add_argument("--servicestate", help="Service state")
parser_servicenotification.add_argument("--serviceoutput", help="Service output")

cmdargs = parser.parse_args()
argsdict = vars(parser.parse_args())

message = {}

if cmdargs.host:
    if (    cmdargs.hostname        == None or
            cmdargs.hoststate       == None or
            cmdargs.hostaddress     == None or
            cmdargs.hostoutput      == None or
            cmdargs.longdatetime    == None
            ):
        syslog.syslog(syslog.LOG_ERR,'host notification argument missing')
        sys.exit('host notification argument missing')
    else:
        message['message_source']   = 'nagios'
        message['notificationtype'] = 'host'
        message['hostname']         = argsdict['hostname']
        message['hoststate']        = argsdict['hoststate']
        message['hostaddress']      = argsdict['hostaddress']
        message['hostoutput']       = argsdict['hostoutput']
        message['longdatetime']     = argsdict['longdatetime']

if cmdargs.service:
    if (    cmdargs.servicedesc     == None or
            cmdargs.hostalias       == None or
            cmdargs.hostaddress     == None or
            cmdargs.servicestate    == None or
            cmdargs.longdatetime    == None or
            cmdargs.serviceoutput   == None
            ):
        syslog.syslog(syslog.LOG_ERR,'service notification argument missing')
        sys.exit('service notification argument missing')
    else:
        message['message_source']   = 'nagios'
        message['notificationtype'] = 'service'
        message['servicedesc']      = argsdict['servicedesc']
        message['hostalias']        = argsdict['hostalias']
        message['hostaddress']      = argsdict['hostaddress']
        message['servicestate']     = argsdict['servicestate']
        message['longdatetime']     = argsdict['longdatetime']
        message['serviceoutput']    = argsdict['serviceoutput']

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(json.dumps(message), (cmdargs.logstash_host, int(cmdargs.logstash_port)))