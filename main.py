
# -*- coding: utf-8 -*-
import string
import requests
import json
import hexchat

__module_name__ = "abuseipdb"
__module_version__ = "1.0"
__module_description__ = "Python module"

def ip_info(word, word_eol, userdata):
  if word[3] == ":!abuse":
    ip = word[4]
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': '1fe37ff7b82cd6fa07325bd6fad580a105ca94ada5b03d4b5a5143d558a72fa7c7909eb33922424a'
    }
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)
    for output in decodedResponse.itervalues():
        ipAddress = output['ipAddress']
        countryCode = output['countryCode']
        abuseConfidenceScore = output['abuseConfidenceScore']
        abuse = str(abuseConfidenceScore)
    hexchat.command("PRIVMSG #altay " + 'Address: ' +ipAddress)
    hexchat.command("PRIVMSG #altay " + 'AbuseLevel: ' +abuse + ' %')
    hexchat.command("PRIVMSG #altay " + 'Country: ' +countryCode)
    hexchat.command("PRIVMSG #altay " + 'Host details on https://www.abuseipdb.com/check/' +ipAddress)
    return hexchat.EAT_ALL
hexchat.hook_server('PRIVMSG', ip_info)
hexchat.hook_print("notice", ip_info)




