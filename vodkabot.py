# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.lib.Gen.ttypes import Message
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,datetime
import subprocess,re,os
reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

print client._loginresult()
print "Login successfull"

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
	if op.type == 13:
           client.getGroup(op.param1)
           client.acceptGroupInvitation(op.param1)
	   group = client.getGroup(op.param1)
           gMembMids = [contact.mid for contact in group.invitee]
           for _mid in gMembMids:
               client.cancelGroupInvitation(op.param1,[_mid])
           sendMessage(op.param1, "ℬᎶ戦神Bot作者:")
	   sendMessage(op.param1, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
           
	   client.leaveGroup(op.param1)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return

tracer.addOpInterrupt(13, NOTIFIED_INVITE_INTO_GROUP)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, "ℬᎶ戦神Bot作者:")
        sendMessage(op.param1, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    if not op.param2 in ["uc216d8664c4e1f43772c98b1b0b8956e"]:
	try:
	   if op.type == 19:
	      client.kickoutFromGroup(op.param1,[op.param2])
	      client.inviteIntoGroup(op.param1,[op.param3])
	except Exception, e:
	   print 'failed'

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)


while True:
    tracer.execute()
