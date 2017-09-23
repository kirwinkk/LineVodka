# -*- coding: utf-8 -*-
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + "謝謝加入~~ Thanks for add\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 0:
            if msg.contentType == 0:
                if msg.text == "mid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "me":
                    sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
                if msg.text == "gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                else:
                    pass
            else:
                pass
	elif msg.contentType == 16:
                    msg.contentType = 0
                        msg.text = "文章網址 URL\n" + msg.contentMetadata["postEndUrl"] + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]"
                    else:
                        msg.text = "文章網址 URL\n" + msg.contentMetadata["postEndUrl"] + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]"
                    sendMessage(msg.to,msg.text)
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "mid":
                    sendMessage(msg.to, msg.from_)
		if msg.text == "Mid":
                    sendMessage(msg.to, msg.from_)
		if msg.text == "作者":
                    sendMessage(msg.to,"[半垢作者]:\n 戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    sendMessage(msg.to, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
		if msg.text == "Author":
                    sendMessage(msg.to,"[半垢作者]:\n 戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    sendMessage(msg.to, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
		if msg.text == "作成者":
                    sendMessage(msg.to,"[半垢作者]:\n 戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    sendMessage(msg.to, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
		if msg.text == "author":
                    sendMessage(msg.to,"[半垢作者]:\n 戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    sendMessage(msg.to, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
		if msg.text == "Ps":
                    sendMessage(msg.to,"戦神実験版-注意事項\n\n1. 禁止在副本or私訊發出指令\n2.打完指令若沒反應,請耐心等待,禁止不斷輸入指令\n3.10人以下群組會造成機器不穩定\n4.當伺服器不穩,機器也會不穩,請見諒\n\n仍有疑問請詢問作者\n戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "ps":
                    sendMessage(msg.to,"戦神実験版-注意事項\n\n1. 禁止在副本or私訊發出指令\n2.打完指令若沒反應,請耐心等待,禁止不斷輸入指令\n3.10人以下群組會造成機器不穩定\n4.當伺服器不穩,機器也會不穩,請見諒\n\n仍有疑問請詢問作者\n戦神:http://line.me/ti/p/4-ZKcjagH0\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if msg.text == "gid":
                    sendMessage(msg.to, msg.to)
		if msg.text == "Gid":
                    sendMessage(msg.to, msg.to)
		if msg.text == "kicker":
                    sendMessage(msg.to,"Error")
		if msg.text == "Kicker":
                    sendMessage(msg.to,"Error")
		elif msg.text in ["Sp","Speed","speed"]:
                    start = time.time()
                    sendMessage(msg.to, "BG戦神Bot讀取中...")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time) + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		elif ("Mid:" in msg.text):
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = client.getContact(key1)
                    sendMessage(msg.to,"" +  key1)
		elif ("Gn:" in msg.text):
                    group = client.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    client.updateGroup(group)
                else:
                    sendMessage(msg.to,"><")
		elif "TL:" in msg.text:
                    tl_text = msg.text.replace("TL:","")
                    sendMessage(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"] + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")

		if msg.text == "Ver":
                    sendMessage(msg.to,"戦神実験版\n\n[版本version]\n実験版ver.5.2.3\n\n[版本詳情]\n実験版\n 5.1.0\n   刪除偵測退群回覆\n   刪除偵測被踢回覆\n 5.2.0\n   修改細部程序\n   修改Nk錯誤程序\n   增加ps指令\n\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "ver":
                    sendMessage(msg.to,"戦神実験版\n\n[版本version]\n実験版ver.5.2.3\n\n[版本詳情]\n実験版\n 5.1.0\n   刪除偵測退群回覆\n   刪除偵測被踢回覆\n 5.2.0\n   修改細部程序\n   修改Nk錯誤程序\n   增加ps指令\n\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if msg.text == "ginfo":
                    group = client.getGroup(msg.to)
                    md = "戦神実験版V5.2.3-群組詳情\n\n" + "[群組名稱]\n" + group.name + "\n\n[gid]\n" + group.id + "\n\n[群組照片]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\n群組URL: 開啟中\n"
                    else: md += "\n\n群組URL: 關閉中\n"
                    if group.invitee is None: md += "\n成員人數: " + str(len(group.members)) + "人\n\n招待中: 0人"
                    else: md += "\n成員人數: " + str(len(group.members)) + "人\n招待中: " + str(len(group.invitee)) + "人\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]"
                    sendMessage(msg.to,md)
		if msg.text == "Ginfo":
                    group = client.getGroup(msg.to)
                    md = "戦神実験版V5.2.3-群組詳情\n\n" + "[群組名稱]\n" + group.name + "\n\n[gid]\n" + group.id + "\n\n[群組照片]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\n群組URL: 開啟中\n"
                    else: md += "\n\n群組URL: 關閉中\n"
                    if group.invitee is None: md += "\n成員人數: " + str(len(group.members)) + "人\n\n招待中: 0人"
                    else: md += "\n成員人數: " + str(len(group.members)) + "人\n招待中: " + str(len(group.invitee)) + "人\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]"
                    sendMessage(msg.to,md)
		if msg.text == "help":
                    sendMessage(msg.to,"戦神実験版Ver5.2.3-[help]\n\n[help] 查看指令\n[ver] 查看版本\n[ps] 重要注意事項!\n[author] 此半垢作者連結\n[mid] 查看自己mid\n" + "[gid] 查看群組gid\n" + "[me︎] 送出自己的友資\n[ginfo] 查看群組詳細資料\n" + "[url] 取得群組網址\n[urlon] 開啟群組網址\n[urloff] 關閉群組網址\n[invite:] 利用mid邀請\n[kick:] 利用mid踢人\n" + 
				"[Nk:] 利用名字其中一個字踢人\n" + "[cancel] 取消全部邀請\n[bot] 追加保護\n[kicker] 查看追加保護狀態\n[show:] 顯示mid友資\n[set] 設定已讀點\n[read] 顯示已讀用戶\n[time] 顯示現在時間\n[gift] 發送禮物\n\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if msg.text == "Help":
                    sendMessage(msg.to,"戦神実験版Ver5.2.3-[help]\n\n[help] 查看指令\n[ver] 查看版本\n[ps] 重要注意事項!\n[author] 此半垢作者連結\n[mid] 查看自己的mid\n" + "[gid] 查看群組的gid\n" + "[me︎] 送出自己的友資\n[ginfo] 查看群組詳細資料\n" + "[url] 取得群組網址\n[urlon] 開啟群組網址\n[urloff] 關閉群組網址\n[invite:] 利用mid邀請\n[kick:] 利用mid踢人\n" + 
				"[Nk:] 利用名字其中一個字踢人\n" + "[cancel] 取消全部邀請\n[bot] 追加保護\n[kicker] 查看追加保護狀態\n[show:] 顯示mid的友資\n[set] 設定已讀點\n[read] 顯示已讀用戶\n[time] 顯示現在時間\n[gift] 發送禮物\n\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if "gname:" in msg.text:
                    key = msg.text[22:]
                    group = client.getGroup(msg.to)
                    group.name = key
                    client.updateGroup(group)
                    sendMessage(msg.to,"Group Name"+key+"Canged to")
                if msg.text == "url":
                    sendMessage(msg.to,"此群網址URL")
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to) + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "Url":
                    sendMessage(msg.to,"此群網址URL")
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to) + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")

		if msg.text == "urlon":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "URL為開啟狀態")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "已開啟URL\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "Urlon":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "URL為開啟狀態")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "已開啟URL\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if msg.text == "urloff":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "URL為關閉狀態")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "已關閉URL\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "Urloff":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "URL為關閉狀態")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "已關閉URL\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if "kick:" in msg.text:
                    key = msg.text[5:]
                    client.kickoutFromGroup(msg.to, [key])
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+" 掰掰\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")

                elif "Nk:" in msg.text:
                    print "ok"
                    _name = msg.text.replace("Nk:","")
                    gs = client.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"戦神找不到用戶><")
                    else:
                        for target in targets:
                            try:
                                client.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:

                if msg.text == "cancel":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "戦神發現...招待中沒人><\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + "人 已被戦神取消(´∀｀)♡\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "c":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "戦神發現...招待中沒人><\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + "人 已被戦神取消(´∀｀)♡\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "Cancel":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "戦神發現...招待中沒人><\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + "人 已被戦神取消(´∀｀)♡\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
		if msg.text == "C":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "戦神發現...招待中沒人><\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + "人 已被戦神取消(´∀｀)♡\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if "invite:" in msg.text:
                    key = msg.text[-33:]
                    client.findAndAddContactsByMid(key)
                    client.inviteIntoGroup(msg.to, [key])
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+" 已被招待\n" + "[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if msg.text == "me":
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': msg.from_}
                    client.sendMessage(M)
		    contact = client.getContact(Mids[kazu])
                    sendMessage(msg.to, "[名字]\n" + contact.displayName + "\n\n[戦神実験版" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                if "show:" in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")
                if msg.text == "time":
                    sendMessage(msg.to, "戦神実験版[" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "]")
                if msg.text == "gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
		if msg.text == "Gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                if msg.text == "set":
                    sendMessage(msg.to, "已抓已讀點♪\n\n" + "[戦神" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "]")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
		if msg.text == "Set":
                    sendMessage(msg.to, "已抓已讀點♪\n\n" + "[戦神" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "]")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
                if msg.text == "read":
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        sendMessage(msg.to, "戦神実験版-已讀詳情\n" + "已讀的人 %s\n\n已讀不回的人\n%s >< ♪\n\n抓已讀點的時間:\n[%s]"  % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "還沒抓已讀點喔♪")
		if msg.text == "Read":
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        sendMessage(msg.to, "戦神実験版-已讀詳情\n" + "已讀的人 %s\n\n已讀不回的人\n%s >< ♪\n\n抓已讀點的時間:\n[%s]"  % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "還沒抓已讀點喔♪")
			
		elif "Mk:@" in msg.text:
                       nk0 = msg.text.replace("Mk:@","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = client.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"戦神找不到用戶><")
                           pass
                       else:
                           for target in targets:
                                try:
                                    client.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
				
		else:
                    pass
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()
