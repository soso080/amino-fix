import time
import aminofix
import requests
from os import system
import urllib
import json
from json import dumps, load
import argparse
from gtts import gTTS
import random
import datetime
from uuid import uuid4
import threading
from threading import Thread
import subprocess
from io import BytesIO
from getpass import getpass
import os
os.system("clear")

listuid=[]
listname=[]

print("\t\033[1;32m pino 𓂅  \033[1;36m Connection du bot\n\n")

client=aminofix.Client()
email="banesifu@gmail.com"
password="020862waza"

client.login(email=email,password=password)


cid="93307693"
cidy=93307693

path_utilities = "utilities"
path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"
path_download = "audio"
path_lock = f"{path_utilities}/locked"
path_amino = 'utilities/amino_list'
path_picture = 'pictures'
path_sound = 'sound'
path_download = 'download'

adm = []

admx = ["http://aminoapps.com/p/rxuf85", "http://aminoapps.com/p/fv8c06", "http://aminoapps.com/p/7why4y"]

for i in admx:
    try:
        w = client.get_from_code(i).objectId
        adm.append(w)
    except:
        print("lien de profil invalide/format")
subclient = aminofix.SubClient(comId=cid, profile=client.profile)

reloadTime = time.time() + 197
time.sleep(1)
ban = 0
tim = 1
hm = [0]
av = []
nom = 0

@client.event("on_avatar_chat_start")
def on_avatar_start_chat_start(data):
	if data.comId==cidy:
		if subclient.get_chat_thread(data.message.chatId).title!=None:
			try:
				subclient.send_message(chatId=data.message.chatId,message=f"Message fantôme de <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
				subclient.kick(userId=data.message.author.userId,chatId=data.message.chatId,allowRejoin=True)
				print(f"Quelqu'un a envoyé du spam dans le chat")
			except Exception as e:
				print(e)

l=[]
@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		#print(c)
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		#m=data.message.messageType
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=False)
								#subclient.kick(chatId=data.message.chatId,userId=data.message.author.userId,allowRejoin=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user-profile/{data.message.author.userId} faisait de la publicité dans{s}")
								
								subclient.send_message(chatId=data.message.chatId,message="[c]Pas de publicité ici !!")
								print("annonceur repéré")
							except Exception as e:
								print(e)
								
			if x.lower()=="-help" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Voici mes commandes:\n\n[c]-membres\n[c]-fin | -twerk | -cid\n[c]-discord | -omg | -gemir\n[c]-tappe | -blague | -hugme\n[c]-go | -time | -inviteall\n[c]-grrr | -flirter | -acm\n[c]-import | -amino | -pv\n[c]-lol | -play\n\n[c]•────────────•\n\n[c]-code (lien profil)\n[c]-join (lien chat)\n[c]-vc (texte)""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
					
			if x.lower()=="-code":
				try:
					for i in c:
						d=client.get_from_code(i).objectId
					subclient.send_message(chatId=data.message.chatId,message=f"""[bcu]Code d'immatriculation :\n\n[c]ndc://g/user-profile/{d}""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-join":
				if c==[]:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, vous devez coller le lien après la jointure, baka !")
					except:
						pass
				else:
					try:
						for i in c:
							try:
								d=client.get_from_code(i).objectId
								subclient.join_chat(chatId=d)
								subclient.send_message(chatId=data.message.chatId,message="Inscrit(e) !!")
							except Exception as e:
								print(e)
						print(f"Informations demandée par {data.message.author.nickname}")
					except Exception as e:
						print(e)

			if x.lower()=="-vc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"invitez {data.message.author.nickname} à rejoindre le voc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]Je n'ai pas d'identifiant de co-hôte/hôte/personnel pour vous inviter à rejoindre, <$@{data.message.author.nickname}$>")

			if x.lower()=="-inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_online_users(start=0,size=1000)
						for u in h.profile.userId:
							try:
								subclient.invite_to_vc(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Invitez tous les membres de la communauté.")
						print(f"Invitez {data.message.author.nickname} à rejoindre le voc.")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Je n'ai pas d'identifiant de co-hôte/hôte/personnel pour vous inviter à rejoindre le voc, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="La commande Inviteall est verrouillée")
					except:
						pass

			if x.lower()=="-pv" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="Hey, Vous m'avez demander ? ^-^)")
						subclient.send_message(chatId=data.message.chatId,message=f"Regardez vos privés <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
						print(f"invite {data.message.author.nickname} à rejoindre le privé")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"La commande pv est verrouillée<${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			
			if x.lower()=="-lol":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					hx=random.choice(os.listdir("sound"))
					if x.lower() not in l:
						sounds=f"sound/{hx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="sound")
								print(f"Informations demandées par {data.message.author.nickname}")
							except Exception as e:
								print(e)
								
			if x.lower()=="-go" and c==[]:
				if x.lower() not in l:
					try:
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						subclient.send_message(chatId=data.message.chatId,message=f"Live vocal démarré.")
						print(f"Live vocal lancé.")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"[ic]Je n'ai pas d'identifiant de co-hôte/hôte pour exécuter cette commande, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"La commande Start est verrouillée <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			
			if x.lower()=="-membres" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=f"""[cbu]Les membres en lignes :
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
						print("[✓]")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="La commande membres est verrouillée")
					except:
						pass

			if x.lower()=="-amino" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cbu]Qu'est-ce que amino.fix ?\n\n[c]amino.fix est une API Python permettant de communiquer avec les serveurs Amino tout en prétendant que vous êtes un utilisateur de l'application. Ceci est principalement accompli en usurpant les en-têtes de configuration de périphérique. Il sert également à objectiver et à organiser les données de réponse aux acides aminés, de sorte que tout soit plus facile..
faire -import pour trouver plus
-acm """)
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-import" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]import amino.fix
[c]Cette commande/ligne importe le module amino.fix qui se compose de 5 ensembles de fichiers python, à savoir
-acm
-client
-subclient
-socket
-init""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-acm" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]Attribut acm\n\n[c]Pour utiliser ces commandes Acm, vous devrez d'abord créer un objet de acm Acm=amino.ACM() Vous pouvez utiliser cet objet "Acm" dans les commandes Par exemple : - si vous voulez créer une communauté, la ligne est\n[c]--------------------------------\n\nimport amino\nAcm=amino.ACM()\nAcm.create_community(name: str, tagline: str, icon: BinaryIO, themeColor: str, joinType: int = 0, primaryLanguage: str = 'fr')\n[c]--------------------------------\nPS : - str désigne une chaîne qui signifie du texte en devis Ex : - "L'Univers Perdu !" BinaryIO désigne un fichier binaire... Ce qui signifie que l'icône/l'image doit être au format binaire (nous traiterons des choses binaires plus tard) int désigne un entier qui signifie des nombres... Il existe différents types d'int pour joinType ....comme 1,2,3.... en désignant l'anglais""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-client" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Cette commande n'est pas à jour""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-subclient" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Cette commande n'est pas à jour""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-init" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Cette commande n'est pas à jour""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-flirter" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]Je veux te serrer dans mes bras puis t'embrasser juste pour vérifier si tu es vraiment fait de sucre. Parce que tu es si mim's!""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-grrr" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[ic]Te fais des choses que tu ne peux même pas imaginer -3-""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-hugme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]T'embrasse ce n'est pas juste un câlin normal, un de ces câlins serrés peuvent me couper le souffle. Donnez-moi des papillons et faites-moi sourire comme un fou. (づ｡◕‿‿◕｡)づ 
[i]Je suis là pour toi....""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-blague" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Ta vie.""")

					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
			if x.lower()=="-play1" and c==[]:
				if subclient.get_chat_thread(data.message.chatId).title==None:
						sounds="musique1.mp3"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Informations demandées par {data.message.author.nickname}")
							except Exception as e:
								print(e)
					
			if x.lower()=="-tappe" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]Prend mes gants de boxe et te frappe fort au visage""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
			if x.lower()=="-play" and c==[]:
				if subclient.get_chat_thread(data.message.chatId).title==None:
					if x.lower() not in l:
						sounds="musique.mp3"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Informations demandées par {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="Commande verrouillée")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="La commande fonctionne qu'en pv, tapez -pv pour que le bot rejoigne pv")
					except:
						pass

			if x.lower()=="-omg" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]J'ai répondu à de nombreux membres, mais quand je vous réponds, ça fait ma journée!""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
					
			if x.lower()=="-time" and c==[]:
				if subclient.get_chat_thread(data.message.chatId).title==None:
					if x.lower() not in l:
						sounds="time.mp3"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Informations demandées par {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="Commande verrouillée")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="La commande fonctionne qu'en pv, tapez -pv pour que le bot rejoigne pv")
					except:
						pass

			if x.lower()=="-discord" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""https://discord.gg/FB4daJK6NG""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-cid" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"{cid}")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)

			if x.lower()=="-twerk" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Mon fessier me fait mal en ce moment, peut-être plus tard..""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
					
			if x.lower()=="-help2" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]""")
					print(f"Informations demandées par {data.message.author.nickname}")
				except Exception as e:
					print(e)
					
			if x.lower()=="-gemir" and c==[]:
				if subclient.get_chat_thread(data.message.chatId).title==None:
					if x.lower() not in l:
						sounds="gemir.mp3"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Informations demandées par {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="La commande gémir est verrouillée")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="La commande gémir ne fonctionne qu'en pv, tapez -pv pour que le bot rejoigne pv")
					except:
						pass
					
			if x.lower()=="-fin" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="fin du vocal dans 5 secondes")
					time.sleep(5)
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=2)
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]Je n'ai pas d'identifiant co/hôte/hôte/personnel pour exécuter cette commande, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])

def on_message(data):
	global ban
	global tim
	global nom
	chatId = data.message.chatId
	nickname = data.message.author.nickname
	content = data.message.content
	vrem = data.message.createdTime[17:19]
	id = data.message.messageId
	
	print(f"# Log: {nickname}: {content}: {chatId} : {ban}: {data.message.type}")

	lis2 = ['Je suis aussi désolé.', 'Pardon pour ça, je m excuse aussi', 'svp, ne soyez pas offensé. Je suis désolé...']
	
	gayper = ['🏳‍🌈 Vous êtes gay/lesbienne à: 0%', '🏳‍🌈 Vous êtes gay/lesbienne à: 0.5%', '🏳‍🌈 Vous êtes gay/lesbienne à: 1%', '🏳‍🌈 Vous êtes gay/lesbienne à: 2.56%', '🏳‍🌈 Vous êtes gay/lesbienne à: 3%', '🏳‍🌈 Vous êtes gay/lesbienne à: 5%', '🏳‍🌈 Vous êtes gay/lesbienne à: 13.45%', '🏳‍🌈 Vous êtes gay/lesbienne à: 23.75%', '🏳‍🌈 Vous êtes gay/lesbienne à: 35.93%', '🏳‍🌈 Vous êtes gay/lesbienne à: 41.99%', '🏳‍🌈 Vous êtes gay/lesbienne à: 49%', '🏳‍🌈 Vous êtes gay/lesbienne à: 69.34%', '🏳‍🌈 Vous êtes gay/lesbienne à: 79.33%', '🏳‍🌈 Vous êtes gay/lesbienne à: 95.55%', '🏳‍🌈 Vous êtes gay/lesbienne à: 100%', 'Vous êtes hétéro.', 'Vous êtes hétéro.', 'Vous êtes hétéro.']
	
	randomnumb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
	
	content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "help":
		sub_client.send_message(message="[c]Voici mes commandes :\n\n[c]!kiss (mention) | !hug (mention)\n[c]!mc (texte) | !msg (texte)\n[c]!vc (texte)\n\n[c]•────────────•\n\n[c]!nmb | !on | !sup | !info | !t\n[c]!chatid | !inv | !pino | !déco\n[c]!co | !kick", chatId=chatId, replyTo=id)
		
	if content[0] == "!vc":
		myobj = gTTS(text=data.message.content[4:], lang='fr', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
			
	if content[0] == "!t":
                sub_client.send_message(message="Bot connecté\navec succès [✓]", chatId=chatId, replyTo=id)

	if content[0][0] == "?":
		sub_client.send_message(message=str(random.choice(lis)), chatId=chatId, replyTo=id)

	if content[0] == "!kick":
		sub_client.send_message(message=f"vous avez été kick, {nickname}", chatId=chatId, replyTo=id)
		sub_client.kick(userId=data.message.author.userId, chatId=data.message.chatId, allowRejoin = True)

	if content[0] == "!co":
		sub_client.activity_status('online')
		sub_client.send_message(message="Je suis désormais connecté [✓]", chatId=chatId, replyTo=id)

	if content[0] == "!déco":
		sub_client.activity_status('offline')
		sub_client.send_message(message="Je suis désormais déconnecté [✓]", chatId=chatId, replyTo=id)

	if content[0] == "!msg":
		sub_client.send_message(message=(f"{data.message.content[4:]}"), chatId=chatId,asStaff=True)

	if content[0] == "!pino":
		sub_client.send_message(message=(f"Vous m'avez appelé, {nickname}?"), chatId=chatId, replyTo=id)

	if content[0][1:].lower()=="!inv":
		sub_client.join_chat(chatId=chatInfo.chatId)
		x=client.get_from_code(str(content[1])).objectId
		sub_client.invite_to_chat([x], chatId=chatInfo.chatId)

	if content[0] == "!chatid":
		sub_client.send_message(message=(f"{chatId}"), chatId=chatId, replyTo=id)

	if content[0] == "!mc":
		sub_client.send_message(message=(f"{nickname}: {content}"), chatId=chatId)

	if content[0] == "!info":
		sub_client.send_message(message="[BC][📄]Informations sur le bot\n[C]Créateurs du bot:\n\n[c]Soso/Mikey\n\n[c]pino 𓂅", chatId=chatId, replyTo=id)
		
	if content[0] == "!sup":
	               if data.message.author.role != 0:
	               	for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=100).messageId:
	               		sub_client.delete_message(reason="sup", chatId=data.message.chatId, messageId=msgId,asStaff=True)
	               	
	if content[0][0] == "!" and content[0][1:].lower() == "on":
		tim = -tim

	if content[0][0] == "!" and content[0][1:].lower() == "nmb":
	  	sub_client.send_message(message=str(random.choice(randomnumb)), chatId=chatId, replyTo=id)

	if content[0] == "!hug":
	  	        				author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        				sub_client.send_message(message=f"[cb]{data.message.author.nickname}\n\n[c]Fait son plus gros câlin pour {author2}", chatId=chatId)


	if content[0] == "!kiss":
	  	        							author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        							sub_client.send_message(message=f"[cb]{data.message.author.nickname}\n\n[c]J'embrasse profondément {author2}", chatId=chatId)

	if content[0][0] == "!" and content[0][1:].lower() == "os":
	  	sub_client.send_message(message=str(random.choice(gayper)), chatId=chatId, replyTo=id)

					
#Protection des chats

	global nazvan
	global opisan
	global fonsss
	if content[0][0] == "!":
		if content[0][1:].lower() == "save":

			nazvan = sub_client.get_chat_thread(chatId=data.message.chatId).title
			opisan = sub_client.get_chat_thread(chatId=data.message.chatId).content
			nom = 0
methods = []
for x in client.chat_methods:
	methods.append(client.event(client.chat_methods[x].__name__)(on_message))
subs = client.sub_clients(0, 100)
for x, i in enumerate(subs.name, 1):
    print(f"{x}. {i}")
comId = "93307693"
sub_client = aminofix.SubClient(comId=comId, profile=client.profile) # 144781697
print("Surveillance des chats...")

##################################

################################################commands/команды################################################
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()
