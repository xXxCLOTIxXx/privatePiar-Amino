from os import system as s
try:from colored import fore
except:s('pip install colored');from colored import fore
try:import AminoXZ
except:s('pip install AminoXZ');import AminoXZ
from threading import Thread

error_color = fore.RED
successful_color = fore.GREEN
regular_color = fore.GREY_63  
input_color = fore.DEEP_SKY_BLUE_2
antiban="_(.a={}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{},=_(template-default.blog1.content,_locale=ar)_)_"

client = AminoXZ.Client()
s('cls')
print(fore.DARK_CYAN,"""

██████╗░██████╗░██╗██╗░░░██╗░█████╗░████████╗███████╗  ██████╗░██╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║██║░░░██║██╔══██╗╚══██╔══╝██╔════╝  ██╔══██╗██║██╔══██╗██╔══██╗
██████╔╝██████╔╝██║╚██╗░██╔╝███████║░░░██║░░░█████╗░░  ██████╔╝██║███████║██████╔╝
██╔═══╝░██╔══██╗██║░╚████╔╝░██╔══██║░░░██║░░░██╔══╝░░  ██╔═══╝░██║██╔══██║██╔══██╗
██║░░░░░██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░███████╗  ██║░░░░░██║██║░░██║██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
		

	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q
	Discord server: https://discord.gg/GtpUnsHHT4
	""",regular_color)


while True:
	try:client.login(email=input(f'{input_color}Email>> {regular_color}'), password=input(f'{input_color}Password>> {regular_color}'));print(successful_color,"Successful login", regular_color);break
	except Exception as error:print(error_color,'Fail login:\n',error,f'\n{regular_color}')

while True:
	print('\n1)In console\n2)Advertising message will be taken from the file "message.txt"\n')
	select = input(f'{input_color}How do you want to write a message>> {regular_color}')
	if select == '1':
		message = input(f'{input_color}Advertising message>> {regular_color}')
		if message == '':print(error_color,"\nYou didn't write a message\n",f'\n{regular_color}')
		else:break
	elif select == '2':
		try:message = open("message.txt", encoding='utf-8').read()
		except FileNotFoundError:print(error_color,'\n"message.txt" file not found, please create it and enter ad text there\n',f'\n{regular_color}');continue
		if message =='':print(error_color,'\n"message.txt" file is empty\n',f'\n{regular_color}')
		else:break
	else:print(error_color,"\nChoose one of the options\n",f'\n{regular_color}')

while True:
	try:comId = client.get_from_link(input(f"{input_color}Input community link>> "))['extensions']['community']['ndcId'];break
	except Exception as error:print(error_color, f"Fail:\n{error}\n", regular_color)

try:client.join_community(comId=comId)
except Exception as error:print(fore.RED, f"Fail join community:\n{error}\n", fore.GREY_63)
try:client.change_profile(comId=comId, name='Free scripts -> @DXsarz | Бесплатные скрипты -> @DXsarz', content=antiban); print(successful_color,'Profile changed successfully.\n',regular_color)
except Exception as error:print(error_color, f"Fail:\n{error}\n", regular_color)
try:
	userIds = list()
	while True:
		print("\n1)Online users\n2)All users\n")
		user_type = input(f"{input_color}Select user type>> {regular_color}")
		if user_type == '1':users = client.get_community_members(comId=comId, type="online", size=100)["userProfileList"]; break
		elif user_type == '2':users = client.get_community_members(comId=comId, type="recent", size=100)["userProfileList"]; break
		else:print(error_color, f"\nChoose one of the options\n", regular_color)
	leaders = client.get_community_members(comId=comId, type="leaders", size=100)["userProfileList"]
	curators = client.get_community_members(comId=comId, type="curators", size=100)["userProfileList"]
	admins = leaders+curators
	for i in users:
		userIds.append(i["uid"])
	for i in admins:
		i = i["uid"]
		if i in userIds:
			userIds.remove(i)
	print(successful_color,"Users Saved Successfully", regular_color)
except Exception as error:print(error_color, f"Fail:\n{error}\n", regular_color)

def start_piar():
	try:
		chatId = client.start_chat(userId=userIds, message=None, comId=comId, content=message)["threadId"]
		try:client.send_message_web(chatId=chatId, comId=comId, message=message);print(successful_color,'Ad sent successfully.\n',regular_color)
		except Exception as error:print(error_color, f"Failed to send message:\n{error}\n", regular_color)
	except Exception as error:print(error_color, f"Chat creation error:\n{error}\n", regular_color)


for _ in range(6):
	Thread(target=start_piar).start()

input()