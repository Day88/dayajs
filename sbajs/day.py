#GUNAKAN SEBAIK2NYA
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime, timedelta
#from tmp.Instagram import InstagramScraper
#from instagram import Instagram
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from googletrans import Translator
from threading import Thread,Event
import wikipedia as wiki
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
import json, requests, LineService
from thrift.transport import THttpClient
from zalgo_text import zalgo
requests.packages.urllib3.disable_warnings()

_session = requests.session()
botStart = time.time()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


cl = LINE('dayherfendi@gmail.com','nday12345')



cl.log("Auth Token : " + str(cl.authToken))



sw = LINE('mjv63316@cuoly.com','nday12345')



sw.log("authToken: " + sw.authToken)



#==========SB_TEMPLATE========







oepoll = OEPoll(cl)



call = cl



creator = ["u3c6a69b0777a3920490c1affb7c7da0f"]

owner = ["u3c6a69b0777a3920490c1affb7c7da0f"]

admin = ["u3c6a69b0777a3920490c1affb7c7da0f"]

staff = ["u3c6a69b0777a3920490c1affb7c7da0f"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl]
Bots = [mid,Zmid]
Saints = admin + owner + staff
admin = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
offbot = []
#============
sp_merah = {"type": "separator","color": "#FF2800"}
sp_kuning = {"type": "separator","color": "#FFFD00"}
sp_hijau = {"type": "separator","color": "#83FF00"}
sp_biru = {"type": "separator","color": "#00DAFF"}
sp_ungu = {"type": "separator","color": "#C323FF"}
sp_ping = {"type": "separator","color": "#FF17CE"}
sp_putih = {"type": "separator","color": "#F8F8FF"}
warna3 = (sp_merah,sp_kuning,sp_hijau,sp_biru,sp_ungu,sp_ping,sp_putih)
sp_kia = random.choice(warna3)
#===
settings = {
    "welcome": False,
    "leave": False,
    "mid": False,
    "size": "micro",
    "keyCommand": "dent",
    "commentPost": "ʟⁱᵏᵉ ʟⁱᵏᵉ & ʟⁱᵏᵉ ᴀʲᵃ - ʙʏ : dprokiller",
    "Aip": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": {},
    "postingan":{},
    "checkPost": False,
    "autoRead": False,
    "autoJoinTicket": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changevp": False,
    "changeCover":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "delFriend":False,
    "addadmin":False,
    "delladmin":False,
    "checkmid": False,
    "getMid": False,
    "invite":False,
    "Invi":False,
    "staff":{},
    "Timeline": False,
    "likePost": False,
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "readPoint":{},
    "readMember":{},
    "lang":False,
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "tumbal":True,
    "proJS":True,
    "backup":True,
    "contact":False,
    "autoRead": False,
    "autoBlock": False,
    "autoJoin":True,
    "autoAdd":False,
    'autoCancel':{"on":True, "members":1},
    "autoReject":False,
    "autoLeave":False,
    "detectMention":False,
    "detectMention2":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "Unsend":False,
    "responsmule":True,
    "ytube":True,
    "tiktok":True,
    "notif":True,
    "sticker":False,
    "selfbot":True,
    "clear":"santet",
    "tagall":"all",
    "mention":"ɴɢɪɴɪᴘ ᴍᴜʟᴜ ᴄᴏʟᴏᴋ ɴɪʜ",
    "Respontag":"🛡ʜᴀᴅɪʀ ᴋᴀɴɢᴇɴ ʏᴀ ᴛᴀɢ ᴍᴜʟᴜ",
    "Respontag2":"🛡ᴛᴀɢ ʟᴀɢɪ ᴋᴇᴘʟᴇᴛ ɴɪʜ",
    "welcome":"🛡sᴀʟᴋᴇɴ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴋᴀ",
    "autoLeave":"🛡sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴋᴀ ᴛᴛᴅᴊ ʏᴀ",
    "comment":"ʜᴀᴅɪʀ ɴʏɪᴍᴀᴋ☺☺ʟɪᴋᴇ ʟɪᴋᴇ ʙʏ:dprokiller",
    "message1":"ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\nCreator:http://line.me/ti/p/~dproteam",
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
clProfile = cl.getProfile()
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
           
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def picFinder(name):    
        try:
            rgram = requests.get('http://www.instagram.com/{}'.format(name))
            rgram.raise_for_status()
            selenaSoup=BeautifulSoup(rgram.text,'html.parser')
            pageJS = selenaSoup.select('script')
            for i, j in enumerate(pageJS):
                pageJS[i]=str(j)
            picInfo = sorted(pageJS,key=len, reverse=True)[0]
            allPics = json.loads(str(picInfo)[52:-10])['entry_data']['ProfilePage'][0]
            return allPics
        except requests.exceptions.HTTPError:
            return '\t \t ### ACCOUNT MISSING ###'
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          print ("✪[]► Like Success")
        except:
          pass
      else:
          print ("Already Liked")
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:













        error.write("\n[ {} ] {}".format(str(time), text))

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info

    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')
                     
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
def NoteCreate(to,cmd,msg):
	h = []
	s = []
	if cmd == 'tagnote':
		sakui = cl.getProfile()
		group = cl.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
		data = nama
		k = len(data)//20
		for aa in range(k+1):
			nos = 0
			if aa == 0:dd = '╭─[ Mention Note ]';no=aa
			else:dd = '';no=aa*20
			msgas = dd
			for i in data[aa*20 : (aa+1)*20]:
				no+=1
				if no == len(data):msgas+='\n│{}. @  \n╰─[ Mention Note ]'.format(no)
				else:msgas+='\n│{}. @'.format(no)
			msgas = msgas
			for i in data[aa*20 : (aa+1)*20]:
				gg = []
				dd = ''
				for ss in msgas:
					if ss == '@':
						dd += str(ss)
						gg.append(dd.index('@'))
						dd = dd.replace('@',' ')
					else:
						dd += str(ss)
				s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
				nos +=1
			h = cl.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
#=====
def RmentionMembers(to, mid):
    try:
        arrData = ""
        textx = "     [Total {} Butir]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "╚══[Ternak {} aman]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error) 
def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ Sini Gabung Chat ka 😊..\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = (str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
    #    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost


#=====DEF HELP MENU =======
def sendTextTemplatelike(to, text): #autolike
    data = {
                                "type": "flex",
                                "altText": "mimik cucu ",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#800000"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "80px",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "4px",
        "offsetStart": "4px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "offsetTop": "3px",
            "offsetStart": "0px",
            "color": "#0000ff"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "23px",
        "backgroundColor": "#ff7f00",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "87px",
        "offsetStart": "2px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(timeNow.strftime('%A')),
            "size": "xs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "0px",
            "offsetBottom": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "offsetTop": "4px",
        "offsetStart": "97px",
        "cornerRadius": "8px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(datetime.strftime(timeNow,'%H:%M:%S')),
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetBottom": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "24px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(datetime.strftime(timeNow,'%d-%m-%Y')),
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "45px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ᴄʜᴅ-ʙᴏᴛs",
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "3px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "65px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xxs",
            "weight": "bold",
            "style": "normal",
            "align": "start",
            "offsetTop": "5px",
            "offsetStart": "2px",
            "color": "#ffd700",
            "wrap": True
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "61px",
        "offsetStart": "9px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "3px",
    "borderColor": "#0000ff",
    "cornerRadius": "10px",
    "position": "relative"
  },
  "action": {
    "type": "uri",
    "label": "action",
    "uri": "http://linecorp.com/"
  },
  "styles": {
    "body": {
      "backgroundColor": "#800000"
    }
  }
}
}
    cl.postTemplate(to, data)                                      

def sendTextTemplate25(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "➥ daychosal》》》",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#ffffff"            
      },
      {
        "type": "separator",
        "color": "#ffffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#ffffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ⁴",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#ffffff"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dprokiller88",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#ffffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#33ffff",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#ffffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ffffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#ffffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#ffffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#ccffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://www.youtube.com/channel/UC2dxt9FfRfijNyHyGeQHhdQ?view_as=subscriber"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dprokiller88",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__H__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
#=========DEF
def sendTextTemplate(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "➥ daychosal》》》",
                                       "contents": 
{
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#ffffff"
              }
            ],
            "cornerRadius": "10px",
            "height": "68px",
            "borderColor": "#9900cc",
            "borderWidth": "2px",
            "offsetTop": "-20px",
            "offsetStart": "10px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "height": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "-1px",
            "offsetStart": "15px"
          }
        ],
        "position": "absolute",
        "borderColor": "#9900cc",
        "borderWidth": "2px",
        "cornerRadius": "8px",
        "backgroundColor": "#3300CC",
        "offsetTop": "10px",
        "offsetStart": "40px",
        "width": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "D'PRO SELFBOT",
            "size": "xs",
            "color": "#ffffff",
            "wrap": True,
            "offsetStart": "10px"
          }
        ],
        "position": "absolute",
        "backgroundColor": "#336600",
        "borderWidth": "2px",
        "borderColor": "#9900cc",
        "cornerRadius": "8px",
        "offsetTop": "35px",
        "offsetStart": "40px",
        "width": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "gravity": "top",
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "line://nv/profilePopup/mid=u09925db4c6578a2c83e58abe002c358f",
            }
          }
        ],
        "position": "absolute",
        "borderWidth": "4px",
        "borderColor": "#9900cc",
        "cornerRadius": "100px",
        "height": "55px",
        "width": "55px",
        "offsetTop": "6px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#9900cc",
    "cornerRadius": "20px",
    "height": "72px",
    "backgroundColor": "#000000"
  },
  "styles": {
    "body": {
      "backgroundColor": "#cc00ff"
    }
    },
  }
}
    cl.postTemplate(to, data)
def sendTextTemplate23(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "➥ daychosal》》》",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "color": "#ffffff",
            "align": "start",
            "size": "xxs",
            "gravity": "center",
            "weight": "bold",
            "style": "normal",
            "wrap": True,
            "offsetTop": "-15px",
            "offsetStart": "-5px"
          }
        ],
        "backgroundColor": "#000000",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#000000",
                "size": "xxs",
                "wrap": True,
                "weight": "regular",
                "style": "italic",
                "align": "center"
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "2px",
            "offsetTop": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "122px",
            "offsetTop": "5px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xxs",
                "color": "#ffffff",
                "weight": "regular",
                "style": "normal",
                "align": "center",
                "offsetTop": "5px",
                "offsetStart": "0px"
              }
            ],
            "width": "90px",
            "height": "30px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "backgroundColor": "#ff0000",
            "cornerRadius": "5px",
            "offsetTop": "5px",
            "offsetStart": "32px"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      },
      "styles": {
        "header": {
          "backgroundColor": "#000000"
        },
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                cl.postTemplate(to, data)
def sendTextTemplate2(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "➥ daychosal》》》",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"text": "D'PRO SELFBOT",
"size": "xxs",
"align": "center",
"color": "#ccff00",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#ffffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"text": text,
"size": "xxs",
#"align": "center",
"color": "#ccffff",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#ffffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dprokiller88",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___H___",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
def sendtextTemplate102(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "➥ daychosal》》》",
                                        "contents": {

  "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ɴᴏᴛɪғ ʏᴏᴜᴛᴜʙᴇ",
                "size": "xxs",
                "color": "#ffd700",
                "offsetStart": "6px",
                "offsetBottom": "1px"
              }
            ],
            "cornerRadius": "10px",
            "borderColor": "#00ff00",
            "borderWidth": "1px",
            "position": "absolute",
            "offsetStart": "17px",
            "width": "84px",
            "offsetTop": "2px",
            "backgroundColor": "#000000",
            "height": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
                "size": "full",
                "position": "absolute",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#00ff00",
            "borderWidth": "1px",
            "offsetTop": "136px",
            "width": "110px",
            "height": "22px",
            "offsetStart": "4px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-Fyon2B_00WQ/XxPBd5bnV0I/AAAAAAAAApg/wZZpkw2S0DIZO_AgqC_7qWi3zIuzYiwxACLcBGAsYHQ/s1280/line_488255574809316.jpg",
                "size": "full",
                "aspectMode": "cover",
                "position": "absolute",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#ffd700",
            "borderWidth": "1px",
            "width": "20px",
            "height": "20px",
            "offsetTop": "137px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-S-_MFy_Qk5M/XwJU9mbqPqI/AAAAAAAAAgw/pQw5WeJVcvUVeL29lWf8iOeY2IvAnegdwCK4BGAsYHg/s348/image_search_1593988303982.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "15px",
            "borderWidth": "1px",
            "borderColor": "#ffd700",
            "offsetTop": "137px",
            "offsetStart": "27px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-wcq1-qxJb-g/XwJW3OvJeoI/AAAAAAAAAhM/ihonLdoYlgA1lhl4j80V_4Iluq0oPN3HACK4BGAsYHg/s225/image_search_1593988502290.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://wa.me/+60195161755"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#ffd700",
            "cornerRadius": "15px",
            "offsetTop": "137px",
            "offsetStart": "49px"

          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-D3VAN2MNn24/XvbZ7PoNLiI/AAAAAAAAAWM/ISFYDGJaZc4OUpdKVBU9KMSwFDcfX94qACK4BGAsYHg/s1080/image_search_1593235242702.jpg593819842325.jpg",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://smule.com/1his_nurch"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#ffd700",
            "cornerRadius": "14px",
            "offsetTop": "137px",
            "offsetStart": "71px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-Hm0GY1OIkTw/XwEFtP5YiFI/AAAAAAAAAcU/D9yHhaSzW2A5CT5EOXBIXf6Jhmb8UvOBACK4BGAsYHg/s1200/image_search_1593819769369.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "offsetTop": "137px",
            "cornerRadius": "15px",
            "borderColor": "#ffd700",
            "borderWidth": "1px",
            "offsetStart": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  D'PRO SELFBOT ",
                "size": "xxs",
                "color": "#ffd700",
                "offsetStart": "9px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                },
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "offsetTop": "160px",
            "width": "110px",
            "offsetStart": "4px",
            "height": "15px",
            "backgroundColor": "#000000",
            "offsetBottom": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": text,
                "color": "#ffd700",
                "size": "xxs",
                "offsetStart": "6px",
                "offsetTop": "3px",
                "wrap": True,
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "10px",
            "offsetTop": "19px",
            "offsetStart": "4px",
            "width": "110px",
            "height": "115px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#ffd700",
            "borderWidth": "1px",
            "width": "15px",
            "height": "15px",
            "offsetTop": "2px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "cornerRadius": "15px",
            "borderWidth": "1px",
            "borderColor": "#ffd700",
            "offsetTop": "2px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#00ff00",
        "borderWidth": "1px"
      }
    }
  } 
                cl.postTemplate(to, data)
def sendtextTemplatenur(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "➥ daychosal》》》",
                                        "contents": {

  "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
             "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  ɴᴏᴛɪғ sᴍᴜʟᴇ ",
                "size": "xxs",
                "color": "#ffffff",
                "offsetStart": "6px",
                "offsetBottom": "1px"
              }
            ],
            "cornerRadius": "10px",
            "borderColor": "#c2ff0a",
            "borderWidth": "1px",
            "position": "absolute",
            "offsetStart": "17px",
            "width": "84px",
            "offsetTop": "2px",
            "backgroundColor": "#000000",
            "height": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-cThzrvzC960/Xwe80YzsO_I/AAAAAAAAAjQ/wq8E3735U98UsaI_1iIDiODR44gju9-hQCLcBGAsYHQ/s960/image_search_1594342391590.jpg",
                "size": "full",
                "position": "absolute",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#c2ff0a",
            "borderWidth": "1px",
            "offsetTop": "136px",
            "width": "110px",
            "height": "22px",
            "offsetStart": "4px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-Fyon2B_00WQ/XxPBd5bnV0I/AAAAAAAAApg/wZZpkw2S0DIZO_AgqC_7qWi3zIuzYiwxACLcBGAsYHQ/s1280/line_488255574809316.jpg",
                "size": "full",
                "aspectMode": "cover",
                "position": "absolute",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#c2ff0a",
            "borderWidth": "1px",
            "width": "20px",
            "height": "20px",
            "offsetTop": "137px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-S-_MFy_Qk5M/XwJU9mbqPqI/AAAAAAAAAgw/pQw5WeJVcvUVeL29lWf8iOeY2IvAnegdwCK4BGAsYHg/s348/image_search_1593988303982.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "15px",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "offsetTop": "137px",
            "offsetStart": "27px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-wcq1-qxJb-g/XwJW3OvJeoI/AAAAAAAAAhM/ihonLdoYlgA1lhl4j80V_4Iluq0oPN3HACK4BGAsYHg/s225/image_search_1593988502290.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://wa.me/+60195161755"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "cornerRadius": "15px",
            "offsetTop": "137px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-D3VAN2MNn24/XvbZ7PoNLiI/AAAAAAAAAWM/ISFYDGJaZc4OUpdKVBU9KMSwFDcfX94qACK4BGAsYHg/s1080/image_search_1593235242702.jpg593819842325.jpg",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://smule.com/1his_nurch"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "cornerRadius": "14px",
            "offsetTop": "137px",
            "offsetStart": "71px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-Hm0GY1OIkTw/XwEFtP5YiFI/AAAAAAAAAcU/D9yHhaSzW2A5CT5EOXBIXf6Jhmb8UvOBACK4BGAsYHg/s1200/image_search_1593819769369.png",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "offsetTop": "137px",
            "cornerRadius": "15px",
            "borderColor": "#c2ff0a",
            "borderWidth": "1px",
            "offsetStart": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  D'PRO SELFBOT ",
                "size": "xxs",
                "color": "#ffffff",
                "offsetStart": "9px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                },
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "offsetTop": "160px",
            "width": "110px",
            "offsetStart": "4px",
            "height": "15px",
            "backgroundColor": "#000000",
            "offsetBottom": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": text,
                "color": "#ffffff",
                "size": "xxs",
                "offsetStart": "6px",
                "offsetTop": "3px",
                "wrap": True,
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "cornerRadius": "10px",
            "offsetTop": "19px",
            "offsetStart": "4px",
            "width": "110px",
            "height": "115px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "cornerRadius": "15px",
            "borderColor": "#c2ff0a",
            "borderWidth": "1px",
            "width": "15px",
            "height": "15px",
            "offsetTop": "2px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "cornerRadius": "15px",
            "borderWidth": "1px",
            "borderColor": "#c2ff0a",
            "offsetTop": "2px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#c2ff0a",
        "borderWidth": "1px"
      }
    }
  } 
                cl.postTemplate(to, data)   
def sendTextTemplate1(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "➥ daychosal》》》",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "color": "#ffffff",
            "align": "center",
            "size": "xxs",
            "gravity": "center",
            "weight": "bold",
            "style": "italic",
            "wrap": True,
            "offsetTop": "-15px",
            "offsetStart": "-5px"
          }
        ],
        "backgroundColor": "#000000",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#000000",
                "size": "xxs",
                "wrap": True,
                "weight": "regular",
                "style": "italic",
                "align": "center"
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "2px",
            "offsetTop": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "122px",
            "offsetTop": "5px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xxs",
                "color": "#ffffff",
                "weight": "regular",
                "style": "normal",
                "align": "center",
                "offsetTop": "5px",
                "offsetStart": "0px"
              }
            ],
            "width": "90px",
            "height": "30px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "backgroundColor": "#ff0000",
            "cornerRadius": "5px",
            "offsetTop": "5px",
            "offsetStart": "32px"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      },
      "styles": {
        "header": {
          "backgroundColor": "#000000"
        },
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                cl.postTemplate(to, data)                               
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd 

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1,"ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴏɴ \nᴄᴏᴍᴇɴ ᴅɪ ᴛʟ ᴋʟᴏ ᴀᴅᴀ ᴘᴇʀʟᴜ")
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"ɴʏᴜʟɪᴋ ɴᴊɪʀʀʀʀ" +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"ᴛʜᴀɴᴋs" + str(ginfo.name))

        if op.type == 13:
            if wait["autoJoin"] and mid in op.param3:
                group = cl.getGroup(op.param1)
                group.notificationDisabled = False
                cl.acceptGroupInvitation(op.param1)
                cl.updateGroup(group)
                ginfo = cl.getGroup(op.param1)
                data = {
                        "type": "flex",
                        "altText": "susu",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/424Krqf/wp2672654-1.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "makasih udah diinvite dimari salken kk smua.kalau ada janda cantik bagi satu buat belajar kojom",
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "D'PRO SELFBOT",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message1"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message1"])

        if op.type == 13:
            if mid in op.param3:
               if wait["autoReject"] == True:
                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       cl.rejectGroupInvitation(op.param1)

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
        if op.type == 32:
            if Zmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[Zmid])
                            cl.sendMessage(op.param1,"✔")
                    except:
                            pass
                        
            if op.param3 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 32:
            if wait["backup"] == True:
              if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                    	pass
                return

        #     if op.type == 19 or op.type == 32:
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.acceptGroupInvitation(op.param1)
                        sw.findAndAddContactsByMid(op.param3)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)                
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                    except:
                    	pass

        if op.type == 19 or op.type == 32:
            if op.param3 in creator:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 19 or op.type == 32:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀʏᴀ ɪʟᴀɴɢ':
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs\nᴘᴇɴɢɪʀɪᴍ: "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\nᴊᴀᴍ sʜᴀʀᴇ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ik = str(ika.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ika.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                           else:
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                ika1 = "🚹{}".format(str(ika.displayName))
                                ika2 = "🏠:{}".format(str(ginfo.name))
                                ika3 = "🕙{}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                seber = "═══「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」═══\n{}".format(str(msg_dict[msg_id]["text"]))
                                data = {
                                        "type": "flex",
                                        "altText": "🔰D'PRO☆SELFBOT🔰",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(str(ika.pictureStatus)),
            "type": "image",
            "size": "xxs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": ika1,
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": ika3, #"🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"🕙"),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": ika2, #"{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#ffff00",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": seber,
           "size": "xxs",
       #   "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dayqincay",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~dayqincay",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___AdHipatiH___",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(at, data)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯」\n"
                                ret_ += "┣[]►🚹: {}".format(str(ryan.displayName))
                                ret_ += "\n┣[]►🏠: {}".format(str(ginfo.name))
                                ret_ += "\n┣[]►🕘: {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sendTextTemplate2(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'ɢᴀᴍʙᴀʀʏᴀ ᴅɪʙᴀᴡᴀʜ',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯]"
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ: {}".format(pkg_id)
                   ret_ += "\n┣[]►ᴜʀʟ:{}".format(pkg_id)
                   ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
        #=====                            
        if op.type == 26:
            msg = op.message
            sender = msg._from
            to = msg.to
            if msg.contentType == 6:
             if wait["notif"] == True:
                 a = cl.getContact(sender)
                 if msg.toType == 2:
                     b = msg.contentMetadata['GC_EVT_TYPE']
                     c = msg.contentMetadata["GC_MEDIA_TYPE"]
                     if c == "VIDEO" and b == "S":                    	
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 
 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIF CALL VIDEO",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#fefffc",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)
                
                     if c == "VIDEO" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName                            
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 
 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIF CALL VIDEO",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#fefffc",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#d4ff12",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)
                
                     if c == "AUDIO" and b == "S":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName                            
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 
 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIF CALL AUDIO",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokkiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#fefffc",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)
                
                     if c == "AUDIO" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName                            
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 
 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIF CALL AUDIO",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~reva-nabil"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#fefffc",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)
                
                     if c == "LIVE" and b == "S":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName                            
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 

 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "LIVE SHOW GC",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#d4ff12",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)
                
                     if c == "LIVE" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         cl.getGroup(to).name
                         cl.getContact(msg._from).displayName                            
                         data = {
                                       "type": "flex",
                                        "altText": "➥ 𝐓𝐄𝐀𝐌_D.PRO 》》》",
                                        "contents": { 
 
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-QG1NqhXZrqQ/XxTk1iI86FI/AAAAAAAAArA/vAnHDNpEaucXlTAvcn0Vcyrw2o9KYmuSACLcBGAsYHQ/s560/wallpaper-whatsapp-keren-3d-hd-Custom-30864.jpgistic-tunnel-background-drawings_csp51534593.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "LIVE SHOW GC",
                "color": "#00ff00",
                "align": "center",
                "size": "xxs",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "height": "20px",
            "width": "114px",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "backgroundColor": "#ff0000",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ :"+ datetime.strftime(timeNow,'%m-%d-/20')+"⌚:"+ datetime.strftime(timeNow,'%H:%M'),
                "color": "#00ff00",
                "size": "xxs",
                "offsetStart": "1px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "height": "15px",
            "offsetTop": "24px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "borderWidth": "1px",
            "width": "114px",
            "offsetTop": "41px",
            "offsetStart": "2px",
            "height": "80px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~dprokiller88"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}".format(cl.getContact(msg._from).displayName),
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "10px",
                "offsetBottom": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "borderColor": "#d4ff12",
            "borderWidth": "1px",
            "offsetTop": "123px",
            "offsetStart": "2px",
            "width": "114px",
            "height": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                "size": "xxs",
                "color": "#00ff00",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "width": "113px",
            "height": "17px",
            "borderColor": "#d4ff12",
            "offsetTop": "139px",
            "offsetStart": "3px",
            "cornerRadius": "10px",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D''PRO BOTS",
                "color": "#00ff00",
                "size": "xs",
                "offsetStart": "3px",
                "offsetTop": "0px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "84px",
            "height": "20px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "offsetTop": "156px",
            "offsetStart": "17px",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320014407e18d3946b2c6870a1e16fa0.gif",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokilller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "15px",
            "offsetTop": "159px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-geF7ZO6MNWU/XxTd-MrS_iI/AAAAAAAAAqc/Jia7ijeeUPUO9GQSeCc4xzsgCv4UWvx7ACLcBGAsYHQ/s334/1513037674_320",
                "size": "full",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "15px",
            "height": "15px",
            "borderWidth": "1px",
            "borderColor": "#d4ff12",
            "cornerRadius": "10px",
            "offsetTop": "159px",
            "offsetStart": "102px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#d4ff12",
        "borderWidth": "1px"
      }
    }
  }    
                         cl.postTemplate(to, data)                 
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                welcomeMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                        "type": "flex",
                        "altText": "susu",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/424Krqf/wp2672654-1.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["welcome"],
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "D'PRO SELFBOT",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
              #  cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                leaveMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                        "type": "flex",
                        "altText": "susu",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": cover,
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/424Krqf/wp2672654-1.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["autoLeave"],
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "D'PRO SELFBOT",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)

        #===cctv
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        cover = cl.getProfileCoverURL(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        data = {
                                "type": "flex",
                                "altText": "Hancur Hatiku",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/9Hcjxrz/Cute-Animals-Collection-13.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{} ".format(cl.getContact(op.param2).displayName),
            "size": "xs",
            "color": "#FF2800",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "15px"
          }
        ],
        "position": "absolute",
        "width": "140px",
        "height": "25px",
        "borderWidth": "2px",
        "cornerRadius": "10px",
        "offsetTop": "67px",
        "offsetStart": "14px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "3px",
        "borderColor": "#FF2800",
        "cornerRadius": "100px",
        "offsetTop": "42px",
        "offsetStart": "3px"
 #     },
    #  {
    #    "type": "box",
   #     "layout": "vertical",
  #      "contents": [
      #    {
        #    "type": "image",
          #  "url": "https://i.imgur.com/UeHKURR.png",
       #     "size": "full",
       #     "aspectRatio": "1:1",
        #    "aspectMode": "cover",
       #     "align": "center",
      #      "margin": "md"
       #   }
      #  ],
      #  "width": "95px",
       # "height": "30px",
      #  "borderWidth": "2px",
      #  "cornerRadius": "0px",
      #  "offsetTop": "3px",
        #"position": "absolute",
        #"offsetStart": "60px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["mention"],
            "size": "xxs",
            "color": "#FF2800",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True
          }
        ],
        "position": "absolute",
        "width": "84px",
        "height": "20px",
        "borderWidth": "2px",
        "cornerRadius": "5px",
        "offsetTop": "8px",
        "offsetStart": "65px"
      }
    ],
    "paddingAll": "0px",
    "width": "160px",
    "height": "100px",
    "borderWidth": "3px",
    "borderColor": "#FF2800",
    "cornerRadius": "15px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://linecorp.com/"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#FF2800"
    }
  }
}
}
                        cl.postTemplate(op.param1, data)
  
#========={{{{{MENTION}}}}}===========
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if settings ["Aip"] == True:
                if msg.text in ["clearall","Ratakan!","!bumm",".tes","@zona","!otong","!curut","Cleanse","!cleanse",".cleanse","#jembut","!kickall",".kickall","mayhem","Ratakan","bubarkan","Nuke","nuke",".nuke","Bypass","bypass",".bypass","#bypass","#jancok","hancurkan","!malam","winebot",".malam","bubar",".bubar","86"]:
                    cl.kickoutFromGroup(receiver,[sender])
            if wait["selfbot"] == True:
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	cl.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "Bagi Bagi Coin Gratis",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "offsetTop": "5px",
            "offsetStart": "8px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#566788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "168px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "31px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": wait["Respontag"],
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "30px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "32px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": cover,
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "122px",
            "height": "122px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "69px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TAG 100C",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "1px",
                "offsetStart": "26px"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "width": "95px",
            "offsetTop": "154px",
            "offsetStart": "55px",
            "height": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "25px"
              }
            ],
            "position": "absolute",
            "width": "100px",
            "height": "20px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "offsetTop": "132px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "72px",
            "height": "72px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "101px",
            "offsetStart": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " RESPONTAG ",
                "size": "xs",
                "offsetTop": "3px",
                "offsetStart": "1px",
                "color": "#ffffff"
              }
            ],
            "width": "114px",
            "height": "25px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "    D'PRO BOT",
                "size": "xs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "0px"
              }
            ],
            "width": "92px",
            "height": "25px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~dprokiller88"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "aspectRatio": "1:1",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "121px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "position": "absolute",
            "offsetStart": "13px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "offsetStart": "121px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#330033",
        "cornerRadius": "10px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        }
      }
    },
  ]
}
}
                           cl.postTemplate(to, data)
                        #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"155808605","STKPKGID":"6700627","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate1(msg.to,"j̸͟͞a̸͟͞n̸͟͞g̸͟͞a̸͟͞n̸͟͞ t̸͟͞a̸͟͞g̸͟͞ g̸͟͞u̸͟͞a̸͟͞ n̸͟͞a̸͟͞n̸͟͞t̸͟͞i̸͟͞ k̸͟͞e̸͟͞j̸͟͞i̸͟͞t̸͟͞a̸͟͞k̸͟͞")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "🔰D'PRO☆SELFBOT🔰",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSlAYhp6Fav-3Oh35aW19Aq1DCBA7ulrrZnE6hHar-UMit1G8eT",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u09925db4c6578a2c83e58abe002c358f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u1baf174ebb65fb22d2b133499e445485",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u09925db4c6578a2c83e58abe002c358f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u09925db4c6578a2c83e58abe002c358f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u09925db4c6578a2c83e58abe002c358f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʀᴇsᴘᴏɴ²", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/+60196161755",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~dprokiller88",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/___AdHipatiH___",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "131px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag2"],
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
"backgroundColor": "#ff0000",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(contact.displayName),
"weight": "bold",
"color": "#ccffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                           cl.postTemplate(to, data)
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n°❂° STKID : " + msg.contentMetadata["STKID"] + "\n°❂° STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n°❂° STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
        #
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = client.getContact(sender)
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠❂🇮🇩➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠❂🇮🇩➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠❂🇮🇩➢ Tulisan :\n╠❂🇮🇩➢ {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendpostTemplate(to, data)
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Done Like")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplatelike(to, "❂🇮🇩➢ Done Like")
            except Exception as error:
                logError(error)   

            if msg.contentType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            sendTextTemplate1(msg.to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  sendTextTemplate1(msg.to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break
                                  
               if msg.contentType == 13:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴊᴇᴘɪᴛ ᴊᴏᴍʙʟᴏ\n➡" + _name)
                                wait["Invi"] = False
                                break
#=============MEDIA FOTOBOT=============

               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate1(msg.to,"Send gambarnya...")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate1(msg.to,"ᴠɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ ᴅᴏɴᴇ")
               if msg.contentType == 1:
                  if msg._from in admin:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ɢᴀᴍʙᴀʀ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in admin:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in admin:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in admin:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate1(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate1(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate1(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["delFriend"] == True:
                      cl.deleteContact(msg.contentMetadata["mid"])
                      cl.sendReplyMention(msg_id, to, "Udh Euyyy @!", [sender])

                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate1(msg.to,"ᴡᴇs ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅sᴛᴀғғ ᴅɪʜᴀᴘᴜs")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅ᴀᴅᴍɪɴ ᴅɪʜᴀᴘᴜs")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate1(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate1(msg.to,"❎Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate1(msg.to,"✅Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate1(msg.to,"✅Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate2(msg.to,"✅Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate2(msg.to,"✅Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate1(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendTextTemplate1(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")
               if msg.contentType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ᴘɪᴄᴛ ɢʀᴜᴘ")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate1(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path5 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to, "Sukses..")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "keybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = keybot()
                               sendTextTemplate25(msg.to, str(helpMessage))
                        if cmd == "bot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate1(msg.to, "ʙᴏᴛ ᴡᴇs ᴏɴ")
                        elif cmd == "bot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate25(msg.to, "ʙᴏᴛ ᴡᴇs ᴍᴏᴅᴀʀ")
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	sendTextTemplate1(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")
                        elif cmd == "help creator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage1 = helpcreator()
                               sendTextTemplate25(msg.to, str(helpMessage1))
                        elif cmd == "help setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage2 = helpsetting()
                               sendTextTemplate25(msg.to, str(helpMessage2))
                        elif cmd == "help media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage3 = media()
                               sendTextTemplate25(msg.to, str(helpMessage3))
                        elif cmd == "help group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage4 = helpgroup()       
                               sendTextTemplate25(msg.to, str(helpMessage4))
                        elif cmd == "help admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage5 = helpadmin()
                               sendTextTemplate25(msg.to, str(helpMessage5))
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "➥ 􀰂􀰂͜͡ ⃟ཽ ⃟ ⃟ཽ ⃟̷̡͈͙̖̳̬̼͓̌̓͐̂͗͢͝ͅ҉̵̵̧̹͖̤̝͎̖͂̾͐̈̔̎̌̍͒͌͒͡҉̵̛̖͖̊̄̃͆͋͒̃ͅ➴̴̗̟̭̠̳͚͊̐͐͂̆̓҉̶̶̢̡̛̳̬̞̲̹̘̄̿͒̓̓̓̀́̓͜͜͝ͅͅ҉̷̨̡̨̹̯̗͕̟̩͚̎̂daychosal΃ཽᬽ͢͢􏿿 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴍᴇ\n◯ ᴄᴠᴘ\n◯ sᴇᴛᴛɪɴɢ\n◯ ʀᴜɴᴛɪᴍᴇ\n◯ sᴘᴇᴇᴅ\n◯ sᴘ\n◯ sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n◯ ʙʏᴇᴍᴇ\n◯ ʀᴇᴊᴇᴄᴛ\n◯ ғʀɪᴇɴᴅʟɪsᴛ", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ʙᴏᴛᴀᴅᴅ @\n◯ ʙᴏᴛᴅᴇʟʟ @\n◯ sᴛᴀғғ @\n◯ sᴛᴀғᴅᴇʟʟ @\n◯ ᴀᴅᴍɪɴᴅᴇʟʟ @\n◯ ᴀᴅᴍɪɴ @\n◯ ʀᴇʙᴏᴏᴛ\n◯ ʙᴀɴ:ᴏɴ\n◯ ʙʟᴄ\n◯ ʙᴀɴ:", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ɢᴍɪᴅ\n◯ ɢᴇᴛ ɪᴅ\n◯ ɢᴇᴛᴍɪᴅ\n◯ ɢᴇᴛʙɪᴏ\n◯ ɢᴇᴛɪɴғᴏ\n◯ ɢᴇᴛᴘʀᴏғɪʟᴇ\n◯ ɢᴇᴛᴘɪᴄᴛᴜʀᴇ\n◯ ɪɴғᴏ\n◯ ᴋᴇᴘᴏ\n◯ ᴘᴘᴠɪᴅᴇᴏ", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴄᴇᴋ sɪᴅᴇʀ\n◯ ᴄᴇᴋ ʟᴇᴀᴠᴇ\n◯ ᴄᴇᴋ ᴘᴇsᴀɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ²\n◯ sᴇᴛ sɪᴅᴇʀ:\n◯ sᴇᴛ ᴘᴇsᴀɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ²:\n◯ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴅᴅsᴛɪᴄᴋᴇʀ\n◯ ᴀᴅᴅᴍᴘ3\n◯ ᴀᴅᴅᴀᴜᴅɪᴏ\n◯ ᴀᴅᴅɪᴍɢ\n◯ ᴅᴇʟʟsᴛɪᴄᴋᴇʀ\n◯ ᴅᴇʟʟᴀᴜᴅɪᴏ\n◯ ᴅᴇʟʟᴍᴘ3\n◯ ᴅᴇʟʟᴠɪᴅᴇᴏ\n◯ Dellimg\n◯ ʟɪsᴛsᴛɪᴄᴋᴇʀ", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴊsɴᴀᴍᴇ:\n◯ ᴀᴊsғᴏᴛᴏ\n◯ ᴀᴊs ᴄᴀɴᴄᴇʟ\n◯ /perkosa\n◯ ᴀᴊs ᴀʙsᴇɴ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴄᴀɴᴄᴇʟᴀʟʟ\n◯ ᴄʀᴏᴛ\n◯ ɢᴋɪᴄᴋ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋᴏɴᴛᴀᴋ\n◯ ᴄᴏɴᴛᴀᴄᴛ:\n◯ ɢɴᴀᴍᴇ\n◯ ᴍʏᴍɪᴅ\n◯ ᴍʏʙɪᴏ\n◯ ᴍʏғᴏᴛᴏ\n◯ ᴍʏɴᴀᴍᴇ\n◯ ᴍʏᴘʀᴏғɪʟᴇ\n◯ ᴍʏᴘɪᴄᴛᴜʀᴇ\n◯ ᴍʏᴄᴏᴠᴇʀ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ sᴇᴛ ʟᴇᴀᴠᴇ:\n◯ ʟɪᴋᴇ ᴏɴ/ᴏғғ\n◯ ᴘᴏsᴛ ᴏɴ/ᴏғғ\n◯ sᴛɪᴄᴋᴇʀ ᴏɴ/ᴏғғ\n◯ ɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ\n◯ ᴜɴsᴇɴᴅ ᴏɴ/ᴏғғ\n◯ ʀᴇsᴘᴏɴ ᴏɴ/ᴏғғ\n◯ ʀᴇsᴘᴏɴ² ᴏɴ/ᴏғғ\n◯ ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ/ᴏғғ\n◯ ᴡᴇʟᴄᴏᴍᴇ ᴏɴ/ᴏғғ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Listimage\n◯ Listvideo\n◯ Listaudio\n◯ Listmp3\n◯ Lihat\n◯ Cctv metro\n◯ Ocmp4\n◯ Joox\n◯ mp4\n◯ mp3", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋɪᴄᴋ @\n◯ !sᴛᴀʏ\n◯ ᴊs ɪɴ-ᴏᴜᴛ\n◯ ɢʟɪsᴛᴊs\n◯ ᴋ1-ɪɴᴠɪᴛ\n◯ ᴀᴅᴅᴀsɪs\n◯ ʙʀᴏᴀᴅᴄᴀsᴛ:\n◯ ɢʀᴜᴘᴘɪᴄᴛ\n◯ ɪɴғᴏɢʀᴏᴜᴘ ɴᴏ\n◯ ɪɴғᴏᴍᴇᴍ ɴᴏ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == "help js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "➥ 􀰂􀰂͜͡ ⃟ཽ ⃟ ⃟ཽ ⃟̷̡͈͙̖̳̬̼͓̌̓͐̂͗͢͝ͅ҉̵̵̧̹͖̤̝͎̖͂̾͐̈̔̎̌̍͒͌͒͡҉̵̛̖͖̊̄̃͆͋͒̃ͅ➴̴̗̟̭̠̳͚͊̐͐͂̆̓҉̶̶̢̡̛̳̬̞̲̹̘̄̿͒̓̓̓̀́̓͜͜͝ͅͅ҉̷̨̡̨̹̯̗͕̟̩͚̎̂dprokiller΃ཽᬽ͢͢􏿿 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ !khilaf\n◯ !hancurakan\n◯ !cancell\n◯ ᴘᴀss ɴᴏ\n◯ Join in no\n◯ Qr no\n◯ Canellgc: no\n◯ Kick\n◯ Gkick\n◯ !ciak/bypas", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd.startswith("menu "):
                           if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                ky = key["MENTIONEES"][0]["M"]                
                                m = cl.getContact(ky)                                
                                data = {
                                       "type": "flex",
                                       "altText": "➥ 􀰂􀰂͜͡ ⃟ཽ ⃟ ⃟ཽ ⃟̷̡͈͙̖̳̬̼͓̌̓͐̂͗͢͝ͅ҉̵̵̧̹͖̤̝͎̖͂̾͐̈̔̎̌̍͒͌͒͡҉̵̛̖͖̊̄̃͆͋͒̃ͅ➴̴̗̟̭̠̳͚͊̐͐͂̆̓҉̶̶̢̡̛̳̬̞̲̹̘̄̿͒̓̓̓̀́̓͜͜͝ͅͅ҉̷̨̡̨̹̯̗͕̟̩͚̎̂dprokiller΃ཽᬽ͢͢􏿿 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴍᴇ\n◯ ᴄᴠᴘ\n◯ sᴇᴛᴛɪɴɢ\n◯ ʀᴜɴᴛɪᴍᴇ\n◯ sᴘᴇᴇᴅ\n◯ sᴘ\n◯ sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n◯ ʙʏᴇᴍᴇ\n◯ ʀᴇᴊᴇᴄᴛ\n◯ ғʀɪᴇɴᴅʟɪsᴛ", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ʙᴏᴛᴀᴅᴅ @\n◯ ʙᴏᴛᴅᴇʟʟ @\n◯ sᴛᴀғғ @\n◯ sᴛᴀғᴅᴇʟʟ @\n◯ ᴀᴅᴍɪɴᴅᴇʟʟ @\n◯ ᴀᴅᴍɪɴ @\n◯ ʀᴇʙᴏᴏᴛ\n◯ ʙᴀɴ:ᴏɴ/ᴏғғ\n◯ ʙʟᴄ\n◯ ʙᴀɴ:", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ɢᴍɪᴅ\n◯ ɢᴇᴛ ɪᴅ\n◯ ɢᴇᴛᴍɪᴅ\n◯ ɢᴇᴛʙɪᴏ\n◯ ɢᴇᴛɪɴғᴏ\n◯ ɢᴇᴛᴘʀᴏғɪʟᴇ\n◯ ɢᴇᴛᴘɪᴄᴛᴜʀᴇ\n◯ ɪɴғᴏ\n◯ ᴋᴇᴘᴏ\n◯ ᴘᴘᴠɪᴅᴇᴏ", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴄᴇᴋ sɪᴅᴇʀ\n◯ ᴄᴇᴋ ʟᴇᴀᴠᴇ\n◯ ᴄᴇᴋ ᴘᴇsᴀɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ²\n◯ sᴇᴛ sɪᴅᴇʀ:\n◯ sᴇᴛ ᴘᴇsᴀɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ²:\n◯ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴅᴅsᴛɪᴄᴋᴇʀ ᴏɴ/ᴏғғ\n◯ ᴀᴅᴅᴍᴘ3 ᴏɴ/ᴏғғ\n◯ ᴀᴅᴅᴀᴜᴅɪᴏ ᴏɴ/ᴏғғ\n◯ ᴀᴅᴅɪᴍɢ ᴏɴ/ᴏғғ\n◯ Dellsticker\n◯ Dellaudio\n◯ Dellmp3\n◯ Dellvideo\n◯ Dellimg\n◯ Liststicker", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴊsɴᴀᴍᴇ:\n◯ ᴀᴊsғᴏᴛᴏ\n◯ ᴀᴊs ᴄᴀɴᴄᴇʟ\n◯ ᴀᴊs ᴋɪᴄᴋᴀʟ\n◯ ᴀᴊs ᴀʙsᴇɴ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴄᴀɴᴄᴇʟᴀʟʟ\n◯ ᴄʀᴏᴛ\n◯ ɢᴋɪᴄᴋ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋᴏɴᴛᴀᴋ\n◯ ᴄᴏɴᴛᴀᴄᴛ:\n◯ ɢɴᴀᴍᴇ\n◯ ᴍʏᴍɪᴅ\n◯ ᴍʏʙɪᴏ\n◯ ᴍʏғᴏᴛᴏ\n◯ ᴍʏɴᴀᴍᴇ\n◯ ᴍʏᴘʀᴏғɪʟᴇ\n◯ ᴍʏᴘɪᴄᴛᴜʀᴇ\n◯ ᴍʏᴄᴏᴠᴇʀ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ sᴇᴛ ʟᴇᴀᴠᴇ:\n◯ ʟɪᴋᴇ ᴏɴ/ᴏғғ\n◯ ᴘᴏsᴛ ᴏɴ/ᴏғғ\n◯ sᴛɪᴄᴋᴇʀ ᴏɴ/ᴏғғ\n◯ ɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ\n◯ ᴜɴsᴇɴᴅ ᴏɴ/ᴏғғ\n◯ ʀᴇsᴘᴏɴ ᴏɴ/ᴏғғ\n◯ ʀᴇsᴘᴏɴ2 ᴏɴ/ᴏғғ²\n◯ ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ/ᴏғғ\n◯ ᴡᴇʟᴏᴄᴏᴍᴇ ᴏɴ/ᴏғғ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Listimage\n◯ Listvideo\n◯ Listaudio\n◯ Listmp3\n◯ Lihat\n◯ Cctv metro\n◯ Ocmp4\n◯ Joox\n◯ mp4\n◯ mp3", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋɪᴄᴋ @\n◯ !sᴛᴀʏ\n◯ ᴊs ɪɴ-ᴏᴜᴛ\n◯ ɢʟɪsᴛᴊs\n◯ ᴋ1-ɪɴᴠɪᴛ\n◯ ᴀᴅᴅᴀsɪs\n◯ ʙʀᴏᴀᴅᴄᴀsᴛ:\n◯ ɢʀᴜᴘᴘɪᴄᴛ\n◯ ɪɴғᴏɢʀᴏᴜᴘ ɴᴏ\n◯ ɪɴғᴏᴍᴇᴍ ɴᴏ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                                cl.postTemplate(to, data)                                                                
                      
                        elif cmd.startswith("rname "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.renameContact(ls,sep[1])
                                        cl.sendReplyMention(msg_id, to, "Succes change @! display name to {}".format(sep[1]), [ls])

                        elif cmd == "setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                cover = cl.getProfileCoverURL(sender)
                                listTimeLiking = time.time()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = ""
                                if settings["checkPost"] == True: md+="║║⏹️ Post : ✅\n"
                                else: md+="║║⏹️ Post : ❌\n"
                                if wait["likeOn"] == True: md+="║║⏹️ Like : ✅\n"
                                else: md+="║║⏹️ Like ❌\n"
                                if wait["contact"] == True: md+="║║⏹️ Contact : ✅\n"
                                else: md+="║║⏹️ Contact : ❌\n"
                                if wait["Mentionkick"] == True: md+="║║⏹️ Notag : ✅\n"
                                else: md+="║║⏹️ Notag : ❌\n"
                                if wait["detectMention"] == True: md+="║║⏹️ Respontag : ✅\n"
                                else: md+="║║⏹️ Respontag : ❌\n"
                                if wait["detectMention2"] == True: md+="║║⏹️ Respontag2 : ✅\n"
                                else: md+="║║⏹️ Respontag2 : ❌\n"
                                if wait["Unsend"] == True: md+="║║⏹️ Unsend : ✅\n"
                                else: md+="║║⏹️ Unsend : ❌\n"
                                if wait["autoAdd"] == True: md+="║║⏹️ Autoadd : ✅\n"
                                else: md+="║║⏹️ Autoadd : ❌\n"
                                if wait["autoLeave"] == True: md+="║║⏹️ Autoleave : ✅\n"
                                else: md+="║║⏹️ Autoleave : ❌\n"
                                if wait["autoJoin"] == True: md+="║║⏹️ Autojoin : ✅\n"
                                else: md+="║║⏹️ Autojoin : ❌\n"
                                if wait["sticker"] == True: md+="║║⏹️ Sticker : ✅\n"
                                else: md+="║║⏹️ Sticker ❌\n"
                                if settings["autoJoinTicket"] == True: md+="║║⏹️ Jointicket : ✅\n"
                                else: md+="║║⏹️ Jointicket : ❌\n"
                                if wait["autoReject"] == True: md+="║║⏹️ Autoreject : ✅\n"
                                else: md+="║║⏹️ Autoreject : ❌\n"
                                if wait["autoBlock"] == True: md+="║║⏹️ Autoblock : ✅\n"
                                else: md+="║║⏹️ Autoblock : ❌\n"
                                if settings["welcome"] == True: md+="║║⏹️ Welcome : ✅\n"
                                else: md+="║║⏹️ Welcome : ❌\n"
                                sendTextTemplate23(msg.to, "╔════════════════\n"+ md +"╚════════════════")

                        elif text.lower() == "mid":
                          if wait["selfbot"] == True:
                               middd = "Name : " +cl.getContact(msg._from).displayName + "\nMid : " +msg._from
                               cl.sendMessage(msg.to,middd)

                        elif ("Gname " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gname ","")
                              cl.updateGroup(X)

                        elif "Gruppict" in msg.text:
                          if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                cl.sendImageWithURL(msg.to,path)

                        elif "Getprofile " in msg.text:
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        profile = cl.getContact(mention['M'])
                                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                                    except Exception as e:
                                        pass

                        elif "Getinfo " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            try:
                                sendTextTemplate1(msg.to,"Nama:\n" + contact.displayName)
                                sendTextTemplate1(msg.to,"Bio:\n" + contact.statusMessage)
                                cl.sendImageWithURL(msg.to,image)
                            except:
                                pass

                        elif cmd == 'listblock':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            sendTextTemplate2(to, msgs)

                        elif "Getbio " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            try:
                                sendTextTemplate1(msg.to,contact.statusMessage)
                            except:
                                sendTextTemplate1(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

                        elif text.lower() == 'kalender':
                          if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendTextTemplate2(msg.to, readTime)

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "myname":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))

                        elif cmd == "mybio":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ sᴛᴀᴛᴜs ʟɪɴᴇ ]\n{}".format(contact.statusMessage))

                        elif cmd == "Picture":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideo":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mycover":
                          if msg._from in admin:
                            channel = cl.getProfileCoverURL(sender)
                            path = str(channel)
                            cl.sendImageWithURL(to, path)

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate00(group," " + str(pesan))
                                 #"""
                        elif cmd.startswith("brc: "):
                            if msg._from in creator or msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = cl.getGroupIdsJoined()
                                for group in groups:
                                    try:
                                        time.sleep(0/200)
                                        cl.sendMessage(group, "🔊ʙʀᴏᴀᴅᴄᴀsᴛ 🔊\n\n {}".format(str(txt)))
                                    except:pass  
#broadcast
                        elif cmd.startswith("broadcast1: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group, "  🔊ʙʀᴏᴀᴅᴄᴀsᴛ 🔊\n\n" + str(pesan))

                        elif cmd == "Profile":
                          if msg._from in admin:
                            text = "~ Profile ~"
                            contact = cl.getContact(sender)
                            cover = cl.getProfileCoverURL(sender)
                            result = "╔══[ Details Profile ]"
                            result += "\n├≽ Display Name : @!"
                            result += "\n├≽ Mid : {}".format(contact.mid)
                            result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                            result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n├≽ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            cl.sendMentionWithFooter(to, text, result, [sender])

                        elif cmd.startswith("block"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "sᴜᴋsᴇs ʙʟᴏᴄᴋ ᴋᴏɴᴛᴀᴋ" + str(contact.displayName) + "ᴍᴀsᴜᴋ ᴅᴀғᴛᴀʀ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif cmd.startswith("addme "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "ʙᴇʀʜᴀsɪʟ ᴀᴅᴅ" + str(contact.displayName) + "ᴋᴜʀɪɴᴇᴍ ᴅᴜʟᴜ ʏᴀᴄʜ")

                        elif "Getmid " in msg.text:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        cl.sendMessage(msg.to,str(mention['M']))
                                    except Exception as e:
                                        pass

                        elif "Contact: " in msg.text:
                           if msg._from in admin:
                              mmid = msg.text.replace("Contact: ","")
                              msg.contentType = 13
                              msg.contentMetadata = {"mid":mmid}
                              cl.sendMessage(msg.to, None, contentMetadata={'mid': mmid}, contentType=13)
                              path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                              image = 'http://dl.profile.line.naver.jp'+path
                              cl.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("kontak"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.sendContact(to,str(ls))

                        elif cmd.startswith("ppvideo"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(to, str(path))

                        elif text.lower() == wait["clear"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"mantan berhasil disantet")
                               except:
                                   pass

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate1(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               sendTextTemplate1(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "/reboot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate23(msg.to, "ʀᴇsᴛᴀʀᴛ ʙᴏᴛ")
                               wait["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ʙᴏs")
#============================ABOUT====================================
                        elif cmd == "about":
                                groups = cl.getGroupIdsJoined()
                                contacts = cl.getAllContactIds()
                                blockeds = cl.getBlockedContactIds()
                                crt = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                supp = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nâ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ᴀʙᴏᴜᴛ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "D'PRO\nSELFBOT\nTEAM\nANU",
            "size": "xxs",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": " {}".format(cl.getProfile().displayName),
                "size": "xxs",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "text": "ɢʀᴏᴜᴘ: {}".format(str(len(groups))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ғʀɪᴇɴᴅ: {}".format(str(len(contacts))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ʙʟᴏᴄᴋ: {}".format(str(len(blockeds))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "D'PRO",
        "size": "xxs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~dprokiller88"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "SELFBOT",
        "size": "xxs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~dprokiller88"
        },
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)
                        
                        elif cmd == "order" or text.lower() == 'bot':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://b.top4top.io/p_1632lq3m10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": ",D'PRO SELFBOT",
            "size": "lg",
            "color": "#000000",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "248px",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#ff0000",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "282px",
        "height": "40px",
        "backgroundColor": "#00fdff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "List Bot",
            "size": "lg",
            "color": "#00fdff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "198px",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "140px",
        "height": "45px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Harga Bots",
            "size": "lg",
            "color": "#00fdff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "198px",
        "offsetStart": "149px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "140px",
        "height": "45px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Selfbot Temp",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Sel Temp Ajs",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Sel Asis Ajs",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Pro rom chat",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "HelperGolang",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          }
        ],
        "position": "absolute",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "120px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Rp.50K",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.100",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.150",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.PmC",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.350",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          }
        ],
        "position": "absolute",
        "offsetStart": "169px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "120px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.pananat.net/wp-content/uploads/2019/03/LINE-logo-text-official.png",
            "offsetBottom": "15px"
          },
          {
            "type": "image",
            "url": "https://j.top4top.io/p_1594yrvef1.jpg",
            "size": "full",
            "offsetBottom": "35px",
            "aspectRatio": "2:3"
          }
        ],
        "position": "absolute",
        "offsetStart": "118px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "60px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Tak Ada Yang Sempurna",
                "color": "#000000",
                "align": "center",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#00fdff",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Terimakasih Buat Famz Bots Atas Suport Dan Ilmu Yang Kalian Berikan Semoga Kita Semua Masih Bisa Terus Berkarya ..Amiin..",
                "color": "#000000",
                "align": "center",
                "weight": "bold",
                "size": "xxs",
                "style": "italic",
                "wrap": True
              }
            ],
            "backgroundColor": "#ffffff",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "height": "54px"
          }
        ],
        "position": "absolute",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "282px",
        "height": "82px",
        "offsetTop": "208px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.dlpng.com/static/png/6843063_preview.png",
            "size": "full",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://youtu.be/L2_hbANTrkM"
            }
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "80px",
        "offsetTop": "150px",
        "offsetStart": "230px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#00fdff",
    "borderWidth": "2px",
    "cornerRadius": "15px"
  }
}



                                cl.postFlex(to, data) 
    #==========$=/////####                             
                        elif cmd == "!stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])                                 
                                except:
                                    pass
                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    nur = ["u1baf174ebb65fb22d2b133499e445485"]
                                    cl.inviteIntoGroup(msg.to, nur)                                 
                                except:
                                    pass
                        elif cmd == "js in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "js out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
#=======                                           
                        elif cmd == "byme":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(sender)
                                G = cl.getGroup(to)
                                data = {
                                "type": "flex",
                                "altText": "nurch",
                                "contents": {
"type": "carousel",
"contents": [
{

"type": "bubble",
"size": "nano",
"body": {
"backgroundColor": "#ff0000",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://des.chinabrands.com/uploads/pdm-desc-pic/Clothing/image/2017/05/10/1494385657631195.gif",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "4:4",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u1baf174ebb65fb22d2b133499e445485",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #https://obs.line-scdn.net/{}".format(cl.getContact(sender).displayName),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "http://www.mawoenabraids.com/images/ajax-circular.gif",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u1baf174ebb65fb22d2b133499e445485",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🖐️ ɪᴢɪɴ ᴘᴀᴍɪᴛ",
"weight": "bold",
"color": "#ff0000",
"align": "center",
"size": "xxs",
"offsetTop": "3px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "9px",
#"backgroundColor": "#33ffff",
"offsetStart": "7px",
"height": "20px",
"width": "80px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~dprokiller88",   
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/___H___",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
},{
"type": "image",
 "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "9px",
"offsetStart": "90px",
"height": "200px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🕘 "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ff00ff",
"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "87px",
#"backgroundColor": "#ff0000",
"offsetStart": "1px",
"height": "15px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ff00ff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "98px",
#"backgroundColor": "#0000ff",
"offsetStart": "7px",
"height": "15px",
"width": "90px"
}
],
#"backgroundColor": "#ff0000",
"paddingAll": "0px"
}
},
]
}
}
                                cl.postTemplate(to, data)
                                cl.leaveGroup(to)

                        elif text.lower() == "leaveall":
                            if msg._from in admin:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Pamit semua group")

                        elif text.lower() == "rejectall":
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    sendTextTemplate1(msg.to, "Done cancell {} Grup".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate1(msg.to, "Nothing Invited")

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔽ʙᴏᴛ ʀᴜɴ : " +waktu(eltime)
                               sendTextTemplate1(msg.to,bot)

                        elif cmd == "listpending":
                          if wait["selfbot"] == True:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return cl.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    #cl.sendReplyMessage(msg_id, to, str(ret_))
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(str(ret_)),
                                        "sentBy": {
                                            "label": " 🔰D'pro selfbot🔰",
                                            "iconUrl": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
                                            "linkUrl": "line://nv/profilePopup/mid=ucf0807d4c4242518499c92a02413a112"
                                        }
                                    }
                                    cl.postTemplate(to, data)

                        elif cmd == "delfriend on":
                            if msg._from in admin:                          
                                if wait["delFriend"] == True:
                                    sendTextTemplate1(to, "Send Contact !!!!")
                                else:
                                    wait["delFriend"] = True
                                    sendTextTemplate1(to, "Send Contact :)")

                        elif cmd == "delfriend off":
                            if msg._from in admin:                          
                                if wait["delFriend"] == False:
                                    sendTextTemplate1(to, "Udah Ga aktif !!!")
                                else:
                                    wait["delFriend"] = False
                                    sendTextTemplate1(to, "Berhasil off delete friend")

                        elif cmd.startswith("delfriend "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.deleteContact(ls)
                                        sendTextTemplate1(to, "Udah Boss Ku")

                        elif cmd == "listmember":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                sendTextTemplate2(to, ret_)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate23(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                sendTextTemplate2(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate23(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(danil.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔══「 Info Group 」"
                                ret_ += "\n┣[]► Nama Group : {}".format(G.name)
                                ret_ += "\n┣[]► ID Group : {}".format(G.id)
                                ret_ += "\n┣[]► Pembuat : {}".format(gCreator)
                                ret_ += "\n┣[]► Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┣[]► Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┣[]► Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣[]► Group Qr : {}".format(gQr)
                                ret_ += "\n┣[]► Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══「 Info Finish 」"
                                sendTextTemplate23(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = denal.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n┣[]► "+ str(no) + ". " + mem.displayName
                                sendTextTemplate23(to,"╔══「 Group Info 」\n┣[]► Group Name : " + str(G.name) + "\n┣══「Member List」" + ret_ + "\n╚══「Total %i Members」" % len(G.members))
                            except:
                                pass
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠[]► " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
#invite for mention

                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "●" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate23(msg.to,"    ● GROUP LIST ●\n●\n"+ma+"\n    ●Total "+str(len(gid))+" Groups ●")

                        elif cmd == "gurl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   if X.preventedJoinByTicket == True:
                                       X.preventedJoinByTicket = False
                                       cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to, "Nama : "+str(X.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate1(msg.to, "Url Closed")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  sendTextTemplate1(to, "ᴛᴏᴛᴀʟ {} ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate1(to, "ʙᴇʀsɪʜ")
#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate1(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")

                        elif cmd == "myfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate1(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                         
                        elif cmd.startswith("status: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.statusMessage = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to, "✔sᴜᴋsᴇs " + string + "")
                    
                        elif cmd == "!khilaf" or text.lower()== "!ciak":
                          #if settings["kick"] == True:
                            if msg._from in admin:
                               # projoin.append(msg.to)
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in cl.profile.mid:targk.append(x)
                                imnoob = 'dual.js gid={} token={}'.format(to, cl.authToken)
                                for x in targp:imnoob += ' uid={}'.format(x)
                                for x in targk:imnoob += ' uik={}'.format(x)
                                execute_js(imnoob) 

                        if cmd.startswith('pass '):
                          #if settings["kick"] == True:
                            if msg._from in admin:
                                text = text.split(" ")
                                number =msg.text.replace(text[0] + " ","")
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)-1]
                                        try:
                                            #projoin.append(groupid)
                                            x = cl.getGroup(groupid)
                                            anu = x.id
                                            if x.invitee == None:nama = []
                                            else:nama = [contact.mid for contact in x.invitee]
                                            targets = []
                                            for a in nama:
                                                if a not in admin:
                                                    targets.append(a)
                                            nami = [contact.mid for contact in x.members]
                                            targetk = []
                                            cms = 'dual.js gid={} token={}'.format(anu,cl.authToken)
                                            for a in nami:
                                                if a not in admin:
                                                    targetk.append(a)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            for y in targetk:
                                                cms += ' uik={}'.format(y)
                     #                       print(cms)
                                            success = execute_js(cms)
                                            if success:
                                                cl.sendMessage(to,"Succes Baypass \n " + str(x.name))
                                            else:
                                                cl.sendMessage(to,"Limit Bose")
                                        except:
                                            pass
                        elif cmd == "!hancurkan" or text.lower() == "🐜":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                           #     projoin.append(msg.to)
                                xyz = cl.getGroup(to)
                                mem = [c.mid for c in xyz.members]
                                targets = []
                                for x in mem:
                                  if x not in admin and x not in cl.profile.mid:targets.append(x)
                                imnoob = 'dual.js gid={} token={}'.format(to, cl.authToken)
                                for x in targets:imnoob += ' uik={}'.format(x)
                                execute_js(imnoob)

                        elif cmd == "!cl" or text.lower() == "!cancelall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                           #     projoin.append(msg.to)
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in cl.profile.mid:targp.append(x)
                                imnoob = 'cancel.js gid={} token={}'.format(to, cl.authToken)
                                for x in targp:imnoob += ' uid={}'.format(x)
                                execute_js(imnoob)
                        if cmd.startswith('cancelgc: '):
                       #   if settings["kick"] == True:
                            if msg._from in admin:
                                text = text.split(" ")
                                number =msg.text.replace(text[0] + " ","")
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)-1]
                                        try:
                                            #projoin.append(groupid)
                                            x = cl.getGroup(groupid)
                                            anu = x.id
                                            if x.invitee == None:nama = []
                                            else:nama = [contact.mid for contact in x.invitee]
                                            targets = []
                                            for a in nama:
                                                if a not in admin:
                                                    targets.append(a)
                                            nami = [contact.mid for contact in x.members]
                                            targetk = []
                                            cms = 'dual.js gid={} token={}'.format(anu,cl.authToken)
                                            for a in nami:
                                                if a not in admin:
                                                    targetk.append(a)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            success = execute_js(cms)
                                            if success:

                                                cl.sendMessage(msg.to,"Succes Baypass \n " + str(x.name))
                                            else:
                                                cl.sendMessage(msg.to,"Limit Bose")
                                        except:pass
                                
                        elif cmd == "!ancel" or text.lower() == '.goo':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Kosong.....")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Bots:
                                       klist=[mid]
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.00001)
                                       print (msg.to, [x])
                          if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for a in admin:
                                    if a in targets:
                                        try:
                                            targets.remove(a)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist=[mid]
                                        cl.kickoutFromGroup(msg.to,[target])
                                        time.sleep(0.00001)
                                        print (msg.to,[g.mid])
                                    except:
                                        pass
                                        
                      #
                        if cmd.startswith("join to "):
                                text = cmd.split(" ")
                                number = text[2]
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)]
                                        try:
                                            cl.findAndAddContactsByMid(sender)
                                            cl.inviteIntoGroup(groupid,[sender])
                                            groupname = cl.getGroup(groupid).name
                                            cl.sendMessage(msg.to,"Successfully invite %s"%groupname)
                                        except:
                                            cl.sendMessage(msg.to," Invite banned Bro " + cl.getContact(sender).displayName)
                        elif cmd.startswith("openqr "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ","")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = cl.getGroup(group)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    try:
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                  #      xpesan = 'Sukses Open Qr \n Creator :  '
                                        xpesan = ''
                                        diaa = str(dia.displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@a\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket == True:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "http://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                              #      ret_ += xpesan+zxc
                                    ret_ += zxc
                                    ret_ += "{}".format(gTicket)
                                    ret_ += ""
                                    cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    pass                     
                        if text.startswith('Qr '):
                            if msg._from in admin:
                	            separate = text.split(" ")
                	            number = text.replace(separate[0] + " ","")
                	            groups = cl.getGroupIdsJoined()
                	            ret_ = ""
                	            try:
                	                group = groups[int(number)-1]
                	                G = cl.getGroup(group)
                	                G.preventedJoinByTicket = False
                	                cl.updateGroup(G)
                	                try:
                	                    gCreator = G.creator.mid
                	                    dia = cl.getContact(gCreator)
                	                    zx = ""
                	                    zxc = ""
                	                    zx2 = []
                	                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                	                    diaa = str(dia.displayName)
                	                    pesan = ''
                	                    pesan2 = pesan+"@a\n"
                	                    xlen = str(len(zxc)+len(xpesan))
                	                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                	                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                	                    zx2.append(zx)
                	                    zxc += pesan2
                	                except:
                	                    gCreator = "Tidak ditemukan"
                	                if G.invitee is None:
                	                    gPending = "0"
                	                else:
                	                    gPending = str(len(G.invitee))
                	                if G.preventedJoinByTicket == True:
                	                    gQr = "Tertutup"
                	                    gTicket = "Tidak ada"
                	                else:
                	                    gQr = "Terbuka"
                	                    gTicket = "http://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                	                timeCreated = []
                	                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                	                #ret_ += xpesan+zxc
                	                ret_ += "• Nama : {}".format(G.name)
                	                ret_ += "\n• Group Qr : {}".format(gQr)
                	                ret_ += "\n• Pendingan : {}".format(gPending)
                	                ret_ += "\n• Group Ticket : {}".format(gTicket)
                	                ret_ += ""
                	                cl.sendMessage(msg.to,ret_)
                	            except:pass
                     

#=============={{{{{BATAS}}}}}}}=========
                        elif cmd == "!sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "sɪᴅᴇʀ ᴅɪʜɪᴅᴜᴘᴋᴀɴ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "!sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "sɪᴅᴇʀ ᴅɪᴍᴀᴛɪᴋᴀɴ")
                              else:
                                  sendTextTemplate(msg.to, "sɪᴅᴇʀ ᴅɪ ᴏғғ")
#=========== [ Hiburan] ============#
                        elif cmd.startswith("cctv metro"):
                          if msg._from in admin:
                            ret_ = "Daftar Cctv Pantura\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\nUntuk melihat cctv,\nKetik Lihat (Nomer)"                            
                            sendTextTemplate2(to, ret_)

                        elif cmd.startswith("lihat"):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "LIPUTAN CCTV TERKINI \nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Ketik Lihat nomer cctv selanjutnya"
                                    sendTextTemplate1(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                except:
                                    sendTextTemplate1(to, "🚦Data cctv tidak ditemukan!")

#============Comen Tag=========
                        if text.lower() == "tagnote":
                            if msg._from in admin:
                                NoteCreate(to,cmd,msg)
                        elif msg.text.lower().startswith("tagremot: "):
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//19
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*19 : (a+1)*19]:
                            			b.append(i.mid)
                            		RmentionMembers(gid, b)                            
                    		        sendTextTemplate(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))
                        elif cmd in (wait["tagall"]):
                              if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭━━━╦════╦━━━╮\n│╭━━━━━━━━━━━╮\n╠➢ᴅ'ᴘʀᴏ ʙᴏᴛ\n│╰━━━━━━━━━━━╯\n│╭━━━━━━━━━━━╮"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━╯\n│╭━━━━━━━━━━━╮\n╠❂࿇➢ ᴛᴏᴛᴀʟ: {} ʙᴜᴛɪʀ\n│╰━━━━━━━━━━━╯\n╰━━━╩════╩━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━╮\n╠❂࿇➢ᴛᴏᴛᴀʟ: {} ʙᴜᴛɪʀ\n│╰━━━━━━━━━━━╯\n╰━━━╩════╩━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                        elif cmd == "meh" or text.lower() == 'cipok':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               start = time.time()
                               sendTextTemplate1("u1baf174ebb65fb22d2b133499e445485", '.')
                               elapsed_time = time.time() - start
                               sendTextTemplate1(msg.to, "%s s" % (elapsed_time))

                        elif cmd.startswith("joox"):
                                try:
                                    proses = text.split(" ")
                                    urutan = text.replace(proses[0] + " ","")
                                    r = requests.get("http://mnazria.herokuapp.com/api/joox?search={}".format(str(urllib.parse.quote(urutan))))
                                    data = r.text
                                    data = json.loads(data)
                                    babi = ""
                                    if data["picture"] == babi:
                                        cl.sendMessage(to,"Data Gambar Kosong")
                                    else:
                                        cl.sendImageWithURL(to,data["picture"])
                                    if data["mp3"] == babi:
                                        cl.sendMessage(to,"Data Lagu Kosong")
                                    else:
                                        cl.sendAudioWithURL(to,data["mp3"])
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("mp3: "):
                        #  if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                sendTextTemplate10(msg.to, "📀ᴍᴜsɪᴋ ᴀᴜᴅɪᴏ")
                                cl.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  clProfile.displayName = str(myProfile["displayName"])
                                  clProfile.statusMessage = str(myProfile["statusMessage"])
                                  clProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                  cl.updateProfile(clProfile)
                                  cl.sendMessage(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("smule "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split(" ")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "     ■✯ ʟɪsᴛsᴍᴜʟᴇ ✯■ "
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n■" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n     ■✯ʟɪsᴛsᴍᴜʟᴇ✯■"
                                ret_ += "\nᴋᴇᴛɪᴋ: sᴍᴜʟᴇ{}ɴᴏᴍᴏʀ".format(str(search))
                                sendTextTemplate23(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "\n╠•➣ᴊᴜᴅᴜʟ ʟᴀɢᴜ: "+str(b["title"])
                                    c += "\n╠•➣ᴄʀᴇᴀᴛᴏʀ: "+str(b["owner"]["handle"])
                                    c += "\n╠•➣ʟɪᴋᴇ: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\n╠•➣ᴄᴏᴍᴍᴇɴᴛ: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\n╠•➣sᴛᴀᴛᴜs ᴏᴄ: "+str(b["message"])
                                    c += "\n╠•➣ᴅɪ ᴅᴇɴɢᴀʀᴋᴀɴ: {}".format(b["stats"]["total_listens"])+" orang"
                                    c += "\n╚══[ ✯ᴡᴀɪᴛ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ✯ ]"
                                    hasil = "╔══[ ✯ ᴅᴇᴛᴀɪʟsᴍᴜʟᴇ ✯ ]"+str(c)
                                    dl = str(b["cover_url"])
                                    data = {
                                        "type": "flex",
                                        "altText": "Audio Smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#0000ff" #2f2f4f" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
          },{
            "contents": [
              {
            "text": " D'PRO SELFBOT",
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
 },
{
"type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQtKJ9DZZjfaSZtDWapDmdO1bVccjThrGsrLARUW0ZVu2SqHTTI",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dprikiller88",        
           }, 
            "flex": 1   
            },
            {
     "type": "separator",
           "color": "#33ffff"
           },
           {
            "contents": [
            {           
           "type": "separator",
           "color": "#33ffff"
           },
           {
            "type": "image",
            "url": dl, #"https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___n__",
            },         
            "flex": 1
}
],
   "type": "box",
   "spacing": "xs",
   "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
"contents": [{"type":"separator","color": "#33ffff"},{"contents": [{"text": "🎙️ᴊᴇᴍᴘᴏʟ: "+str(b["stats"]["total_loves"])+" like","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ɴʏɪᴍᴀᴋ: {}".format(b["stats"]["total_listens"])+" orang","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ᴠᴏᴄᴀʟ: "+str(b["owner"]["handle"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️"+str(b["title"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "xs","layout": "vertical"    
},{"type": "separator","color": "#33ffff"}],"type": "box","spacing": "xs","layout": "horizontal"   },{"type": "separator","color": "#33ffff"},{
"contents": [         
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dprokiller88",
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/1his_nurch",
            },        
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                    cl.postTemplate(to, data)

                                    with requests.session() as s:

                                        s.headers['user-agent'] = 'Mozilla/5.0'

                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))

                                        data = BeautifulSoup(r.content, 'html5lib')

                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]

                                        title = data.findAll('h2')[0].text

                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]

                                        if 'Smule.m4a' in get['download']:

                                            cl.sendAudioWithURL(msg.to, get['href'])

                                        else:

                                            cl.sendVideoWithURL(msg.to, get['href'])

                                except Exception as e:

                                    cl.sendReplyMessage(msg.id,msg.to,"Result Error:\n"+str(e))

                        elif "https://www.smule.com" in msg.text.lower():

                            if wait["responsmule"] == True:

                                Ancok = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

                                AbiS69k = re.findall(Ancok, text)

                                Pokeh = []

                                for Nyaman in AbiS69k:

                                    if Nyaman not in Pokeh:

                                        Pokeh.append(Nyaman)

                                for Lottok in Pokeh:

                                    PokenahRengmadureh = Lottok

                                    Apikey = "cinta1234" ## kalau smule udah tidak respon ganti api ini.ini sebagai contoh aku bagi buat kalian

                                    headers = {

                                            "Apikey":Apikey,

                                            }

                                    Squad69KR = json.loads(requests.get("https://beapi.me/smule/post?url="+Lottok,headers=headers).text)
                                    six9="╭──「°❐➣ Notif Smule °❐➣」─────"
                                    six9+="\n├°❐➣   Song : " +Squad69KR["result"]["performance"]["artist"]
                                    six9+="\n├°❐➣   Judul : " +Squad69KR["result"]["performance"]["title"]
                                    six9+="\n├°❐➣   ID Smule : "+Squad69KR["result"]["performance"]["owner"]["handle"]
                                  #  SusuNona+="\n├°❐➣   Status :  " +Nenen["result"]["message"]
                                    six9+="\n╰──「ᴄʀᴇᴀᴛᴏʀ: d'pro killer」─────"
                                    data = {
                                        "type": "flex",
                                        "altText": "➥ daychosal》》》",
                                        "contents": {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/Xtsc29G/20210218-175607.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "66px",
        "height": "66px",
        "borderWidth": "1px",
        "borderColor": "#0034f2",
        "cornerRadius": "100px",
        "offsetTop": "6px",
        "offsetStart": "8px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "width": "66px",
        "height": "66px",
        "borderWidth": "1px",
        "borderColor": "#0034f2",
        "cornerRadius": "100px",
        "position": "absolute",
        "offsetTop": "177px",
        "offsetStart": "178px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
         "text": " " +Squad69KR["result"]["performance"]["artist"],
            "size": "Md",
            "color": "#20f739",
            "offsetTop": "70px",
            "offsetStart": "120px",
            "wrap": True,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": " " +Squad69KR["result"]["performance"]["title"],
            "size": "Md",
            "color": "#20f739",
            "weight": "bold",
            "wrap": True,
            "offsetTop": "100px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": " "+Squad69KR["result"]["performance"]["owner"]["handle"],
            "size": "Md",
            "color": "#20f739",
            "weight": "bold",
            "wrap": True,
            "offsetTop": "155px",
            "offsetStart": "6px"
          }
        ],
        "position": "absolute",
        "width": "250px",
        "height": "250px",
        "borderWidth": "1px",
        "cornerRadius": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "4px",
    "borderColor": "#f72020",
    "cornerRadius": "15px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://linecorp.com/"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000cc"
    }
  }
}
}

                                    cl.sendVideoWithURL(msg.to, Squad69KR["result"]["performance"]["video_media_mp4_url"])

                                    cl.postTemplate(msg.to, data)

                                 #   cl.sendMessage(msg.to, SusuNona)

                                  #  cl.sendAudioWithURL(msg.to, Squad69KR["result"]["performance"]["download_link"])

                                #    cl.sendVideoWithURL(msg.to, Squad69KR["result"]["performance"]["download_link"])

                        if "https://vt.tiktok.com/" in msg.text.lower():

                            if wait["tiktok"] == True:

                                try:

                                    AbiKoplak = msg.text.split(" ")

                                    MatanaJiah = msg.text.replace(AbiKoplak[0] + " ","")

                                    AbiBinOlengKiller = urllib.parse.quote(MatanaJiah)

                                    MuhazirAlwiOleng = "cinta1234"

                                    headers = {

                                        "apiKey":MuhazirAlwiOleng,

                                        }

                                    AbiSangeCok = json.loads(requests.get("https://beapi.me/tiktok?url="+AbiBinOlengKiller,headers=headers).text)

                                    AbiOlengKiller1="╭─「 NOTIF TIKTOK 」─────"

                                    AbiOlengKiller1+="\n├ Sabar Sayang Sedang Didownload"

                                    AbiOlengKiller1+="\n╰─ 「    daychosal     」 ─────"

                                    AbiOlengKiller.sendMessage(msg.to, AbiOlengKiller1)

                                    BocorLu = (MatanaJiah)

                                    KakePatek = BocorLu.replace("watch?v=", "")

                                    AbiGanteng = pafy.new(KakePatek)

                                    CokAnCok = AbiGanteng.streams

                                    AbiCokAnCok = AbiGanteng.getbestaudio()

                                    AbiCokAnCok.bitrate

                                    AbiMuhazir = AbiGanteng.getbest()

                                    AbiMuhazir.resolution, AbiMuhazir.extension

                                    for AbiMuhazirAlwi in CokAnCok:

                                        JalurOleng = AbiCokAnCok.url

                                        JalurOleng1 = AbiMuhazir.url

                                        JalurOleng2 = AbiMuhazirAlwi.url

                                    AbiOlengKiller.sendAudioWithURL(msg.to, JalurOleng)

                                    AbiOlengKiller.sendVideoWithURL(msg.to, JalurOleng1)

                                except:

                                    pass



                        elif "https://youtu.be" in msg.text.lower():

                            if wait["ytube"] == True:

                                try:

                                    proses = cmd.split(" ")

                                    urutan = cmd.replace(proses[0] + " ","")

                                    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={}&type=video&key=AIzaSyDHmqIL8F--G-FM7df9JPH67PDfGF9d0Kk".format(urutan))

                                    data = r.json()

                                    fareel = data["items"][0]

                                    video = pafy.new(fareel['id']['videoId'])

                                    farel = "Tunggu Lagi Sedang proses downlod yang sabar sayang"

                                    cl.sendMessage(msg.to, farel)

                                    streams = video.streams

                                    for s in streams:

                                        cl.sendVideoWithURL(to,str(s.url))

                                except Exception as error:

                                    cl.sendReplyMessage(msg.id, to, str(error))

                                except:

                                    pass        
#===========COMEN PANGGILAN======
                        elif cmd.startswith("stag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("call: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        sendTextTemplate1(msg.to,"Jumlah melebihi 1000")
                        elif msg.text.lower().startswith("naik "):
                          if msg._from in admin:
                           if 'MENTION' in msg.contentMetadata.keys()!= None:
                               names = re.findall(r'@(\w+)', text)
                               mention = eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               lists = []
                               for mention in mentionees:
                                   if mention["M"] not in lists:
                                       lists.append(mention["M"])
                               for ls in lists:
                                   contact = cl.getContact(ls)                          
                                   jmlh = int(wait["limit"])
                                   sendTextTemplate1(msg.to, "Succes {} Call Grup".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                     for x in range(jmlh):
                                         try:
                                             mids = [contact.mid]
                                             cl.acquireGroupCallRoute(msg.to)
                                             cl.inviteIntoGroupCall(msg.to,mids)
                                         except Exception as e:
                                             cl.sendMessage(msg.to,str(e))
                                     else:
                                         sendTextTemplate1(msg.to,"")
                        elif cmd == "call":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate1(msg.to, "Sukses call {} digrup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate1(msg.to,"Jumlah melebihi batas")

#==========Comen Spam==={{{
#
                        elif cmd.startswith("unsend "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            args = text.replace(sep[0] + " ","")
                            ttl = "「UNSEND」"
                            mes = int(sep[1])
                            M = cl.getRecentMessageV2(to, 1001)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == cl.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                cl.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.daemon = True
                                thread1.start()
                                thread1.join()
                        elif cmd =="tagpm":
                          if settings["selfbot"] == True:
                              if msg._from in admin:
                                  if msg.toType != 2:
                                      for num in range(10):
                                          cl.send_mention(to, to, "READ ME!")

                        elif cmd.startswith('tagpm: '):
                          if msg._from in admin: 
                              if msg.toType != 2:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                jumlah = int(strnum)
                                if jumlah <= 500:
                                   for x in range(jumlah):
                                   	try:
                                           cl.send_mention(to, to, "READ ME!")
                                   	except Exception as e:
                                          cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(to, "KEBANYAKAN WOII..!!!")
                        elif cmd.startswith("pmcat: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bctxt = msg.text.replace("Pmcat: ", "")
                                a = cl.getAllContactIds()
                                cl.sendMessage(to, "Sukses broadcast ke "+str(len(a))+" teman")
                                for manusia in a:
                                    try:
                                        C = cl.getContact(mid)
                                        mids = [C.mid]
                                        text = "FRIEND:\n{}\nBROADCASTED BY: @!".format(str(bctxt))
                                        sendMentionV2(manusia, text, mids)
                                    except:
                                        pass
#===========Protection============#
#==
                        elif cmd == "notif on" or text.lower() == '!notifcall on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = True                          
                                sendTextTemplate(msg.to, "Detectcall on")

                        elif cmd == "notif off" or text.lower() == '!notifcall off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = False
                                sendTextTemplate(msg.to,"Detectcall off")
                                #==
                        elif cmd == "smule on" or text.lower() == 'Smule on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responsmule"] = True                          
                                sendTextTemplate(msg.to, "notif mule on")

                        elif cmd == "smule off" or text.lower() == '!smule off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responsmule"] = False
                                sendTextTemplate(msg.to,"Smule off")
                        elif cmd == "youtube on" or text.lower() == 'ytb on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["ytube"] = True                          
                                sendTextTemplate(msg.to, "notif youtube on")

                        elif cmd == "youtube off" or text.lower() == 'ytb off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["ytube"] = False
                                sendTextTemplate(msg.to,"Youtube off") 
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate1(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate1(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif ("Kick" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                       	cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           sendTextTemplate1(msg.to,"Sorry kaki saya struk..")

                        elif "Gkick " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                        elif "Cancelall" in msg.text:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _dn in gMembMids:
                                  if _dn not in admin:
                                    sw.cancelGroupInvitation(msg.to,[_dn])

#=========COMEN RESPON======#
                        elif msg.text in ["Jepit"]:
                            if msg._from in admin:
                                wait["Invi"] = True
                                sendTextTemplate(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                wait["detectMention2"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏɴ")
                        elif cmd == "respon2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = True
                                wait["detectMention"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏғғ")
                        elif cmd == "respon2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏɴ")
                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏғғ")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏn")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                sendTextTemplate(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "post on" or text.lower() == 'post on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "post off" or text.lower() == 'Post off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "like on" or text.lower() == 'like on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = True
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "like off" or text.lower() == 'like off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = False
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplate1(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplate1(msg.to,"ɪɴᴠɪᴛᴇ ᴠɪᴀ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["Unsend"] = True
                                sendTextTemplate1(msg.to, "Unsend message mode on")
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["Unsend"] = False
                                sendTextTemplate1(msg.to, "Unsend message mode off")
                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                wait['autoReject'] = False
                                sendTextTemplate1(msg.to,"❎Auto Reject already Off")
                            elif xres == "on":
                                wait['autoReject'] = True
                                sendTextTemplate1(msg.to,"✅Auto Reject already On")
                        elif cmd == "autoread on":
                            if msg._from in admin:
                                if settings["autoRead"] == True:
                                    sendTextTemplate1(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate1(to, "Berhasil mengaktifkan auto read")

                        elif cmd == "autoread off":
                            if msg._from in admin:
                                if settings["autoRead"] == False:
                                    sendTextTemplate1(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate1(to, "Berhasil menonaktifkan auto read")
                        elif cmd.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    wait["comment"] = txt
                                    sendTextTemplate2(to, "❂Done Mengubah Pesan\n❂CommentTL:\n❂ {}".format(txt))
                                except:
                                    sendTextTemplate1(to, "❂Failed")
                        elif cmd.startswith("eng:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=en&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("ko:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ko&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("th:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("ar:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("in:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error) 

#==================================#
                        elif cmd == "refresh" or text.lower() == 'seger':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                          #      sendTextTemplate1(msg.to,"Clean..")
                                sendTextTemplate(msg.to,"Refresh done 💯")
#===========ADMIN ADD============#
                        elif ("Admin " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"✅ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                                       except:
                                           pass
                        elif ("Staff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                                       except:
                                           pass
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ʜᴀᴘᴜs ᴀᴅᴍɪɴ")
                                       except:
                                           pass
                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ʜᴀᴘᴜs sᴛᴀғғ")
                                       except:
                                           pass
#===========COMMAND BLACKLIST============#

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate1(msg.to,"✅Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate1(msg.to,"✅Berhasil menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "wanted" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate1(msg.to,"Tak ada daftar buronan")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate2(msg.to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   sendTextTemplate1(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "cban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」Bersih" % len(ragets)
                              sendTextTemplate1(msg.to,"Biang kerok " +mc)
#==========Setting bot========
                        elif 'Set hapus: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set hapus: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan clear")
                              else:
                                  wait["clear"] = spl
                                  sendTextTemplate1(msg.to, "「clear」\clearl diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set tagall: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set tagall: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Tagall")
                              else:
                                  wait["tagall"] = spl
                                  sendTextTemplate1(msg.to, "「tagall」\nTagall diganti jadi :\n\n「{}」".format(str(spl))) 
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set autoleave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autoleave: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Autoleave Msg")
                              else:
                                  wait["autoLave"] = spl
                                  sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg mu :\n\n「 " + str(wait["autoleave"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek respon2":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag2"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                        elif cmd == "me" or text.lower() == 'gw':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)                             
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(sender)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "D'PRO SELFBOT",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "1px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
      }
  ]
}
                                cl.postFlex(to, data)

                        
                        elif cmd == "mempict":
                              if msg._from in admin:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~dprokiller"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{} membagikan janda".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)


#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate2(msg.to, "Masuk : %s" % str(group.name))
                                   #  group1 = ka.findGroupByTicket(ticket_id)
#===========add img============#                                                                                
                        elif text.lower() == "!cek":
                            if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["ub52696beffd79277a44e6c6133a5723d"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["ub52696beffd79277a44e6c6133a5723d"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰Cidera ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰Cidera ❎"
                               sendTextTemplate1(to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))
    
#===============HIBURAN============================#
                        elif cmd.startswith("addmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to,"Silahkan kirim mp3 nya...") 
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to, "Done hapus mp3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Music ❳════\n"
                                for audio in audios:
                                    ret_ += "┣[]◇  " + audio.title() + "\n"
                                ret_ += "╚═══❲ {} Record  ❳════".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("addsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("Sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim stickernya...") 
                                else:
                                    sendTextTemplate1(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(to, "Sticker ada di list") 
                                                   
                        elif cmd == "liststicker":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Sticker ❳════\n"
                                for sticker in stickers:
                                    ret_ += "┣[]◇  " + sticker.title() + "\n"
                                ret_ += "╚═══❲  {} Stickers  ❳════".format(str(len(stickers)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("addimg "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim fotonya")
                                else:
                                    sendTextTemplate1(to, "Foto Udah dalam list")

                        elif cmd.startswith("dellimg "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "Foto ada dalam list")

                        elif cmd == "listimage":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Image 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Image 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim video nya...")
                                else:
                                    sendTextTemplate1(to, "video sudah ada")
                        elif cmd.startswith("dellvideo "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "video tidak ada")

                        elif cmd == "listvideo":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Video 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Video 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
    	logError(e)                      
                                     
                               
