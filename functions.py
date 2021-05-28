from replit import db
import discord

defaultColor = 0xB00B69
embedAuthor = {
  "name": "Jäger Bot",
  "icon_url": "https://cdn.discordapp.com/avatars/816636186323189780/019dbb41d6f5b301c1fce6980d487f23.webp?size=128"
}

rulesChannel = 769589794300362762
donatingChannel = 813383990194077716
partnerChannel = 812059541414871060

staffID = 820297954618769409
sotwRoleID = 771887695654944799
formerSotwRoleID = 772257145018122293
donatorTierVID = 823005150281072650

async def updateListDB(key, value):
  key = str(key)
  if key in db.keys():
    values = db[key]
    values.append(value)
    db[key] = values
    print(f"Updated database as list | key: {key} | value: {value}")

  else:
    db[key] = value
    print(f"Created database as list | key: {key} | value: {value}")

async def updateDictDB(key, name, value):
  key = str(key)
  if key in db.keys():
    values = db[key]
    values[name] = value
    db[key] = values
    print(f"Updated database as dict | key: {key} | name: {name} | value: {value}")

  else:
    db[key] = {name: value}
    print(f"Created database as dict | key: {key} | name: {name} | value: {value}")

async def checkFor(value, key):
  if key in db.keys():
    key_list = db[key]

    if value in key_list:
      return True

    else:
      return False

  else:
    return False

async def checkFloat(value):
  try:
    float(value)
    return True
  
  except ValueError:
    return False

def TTTCheck(author):
  def inner_check(message): 
    if message.author != author:
      return False

    try: 
      str(message.content) 
      return True 

    except ValueError: 
      return False

  return inner_check

def convertToMember(user: discord.Member):
  return user

def convertToRole(role: discord.Role):
  return role

async def lockChannel(guild, channel: discord.TextChannel):
  perms = channel.overwrites_for(guild.default_role)
  perms.send_messages = False
  await channel.set_permissions(guild.default_role, overwrite=perms, reason=f"Locked the channel")

async def unlockChannel(guild, channel: discord.TextChannel):
  perms = channel.overwrites_for(guild.default_role)
  perms.send_messages = True
  await channel.set_permissions(guild.default_role, overwrite=perms, reason=f"Unlocked the channel")
  
def getColor(user: discord.Member):
  return [role.color for role in reversed(user.roles) if str(role.color) != "#000000"][0]

operatorList = ["sledge", "thatcher", "ash", "thermite", "twitch", "montagne", "glaz", "fuze", "blitz", "iq", "buck", "blackbeard", "capitao", "hibana", "jackal", "ying", "zofia", "dokkaebi", "lion", "finka", "maverick", "nomad", "gridlock", "nokk", "amaru", "kali", "iana", "ace", "zero", "flores", "smoke", "mute", "castle", "pulse", "doc", "rook", "kapkan", "tachanka", "jager", "bandit", "frost", "valkyrie", "caveira", "echo", "mira", "lesion", "ela", "vigil", "maestro", "alibi", "clash", "kaid", "mozzie", "warden", "goyo", "wamai", "oryx", "melusi", "aruni"]

quotesList = [
{"title": "A really big fucking hole coming right up!", "description": "Jordan 'Thermite' Trace"},
{"title": "Pass those plates around!", "description":"Julien 'Rook' Nizan"},
{"title": "You can stop worrying about grenades now!", "description": "Marius 'Jäger' Streicher"},
{"title": "if it runs on batteries, I'll see it!", "description": "Monica 'IQ' Weiss"},
{"title": "Fookin' laser sights!", "description": "Mike 'Thatcher' Baker"},
{"title": "Toxic babes are in position!", "description": "James 'Smoke' Porter"},
{"title": "Jammah in position!", "description": "Mark 'Mute' R. Chandar"},
{"title": "EDD primed, let them come!", "description": "Maxim 'Kapkan' Basuda"},
{"title": "Mine flying out!", "description": "Elżbieta 'Ela' Bosak"},
{"title": "You're mine bloody asshole!", "description": "Taina 'Caveira' Pereira"},
{"title": "Malbodan haengdong-iji (말보단 행동이지)", "description": "Chul 'Vigil' Kyung Hwa"},
{"title": "Launching override!", "description": "Grace 'Dokkaebi' Nam"},
{"title": "Camera in position!", "description": "Meghan 'Valkyrie' J. Castellano"},
{"title": "As my friend would say: A really big fucking hole coming right up.", "description": "Yumiko 'Hibana' Imagawa"},
{"title": "Big brother coming in for overwatch!", "description": "Olivier 'Lion' Flament"},
{"title": "Time for a wakeup call", "description": "Grace 'Dokkaebi' Nam"},
{"title": "No runnin' in the halls!", "description": "Morowa 'Clash' Evans"},
{"title": "LMG mounted and loaded!", "description": "Alexsandr 'Tachanka' Senaviev, RIP old tachanka"},
{"title": "Rtila active!", "description": "Jalal 'Kaid' El Fassi"},
{"title": "Now you see me, now you don't!", "description": "Elena 'Mira' María Álvarez"},
{"title": "Why do it yourself when robots do it better?", "description": "Masaru 'Echo' Enatsu"},
{"title": "Bullseye, got us a drone", "description": "Max 'Mozzie' Goose"},
]

racistWords = [
    "nigga",
    "niggas",
    "nigger",
    "niggers",
    "/Vigga",
    "/Viggas",
    "/Vigger",
    "/Viggers",
    "niga",
    "Niga",
    "nega",
    "negga",
    "nibba",
    "/vigga",
    "/viggas",
    "/vigger",
    "/viggers",
]

dababyReactions = [
  "LESSS GOOOOOO",
  "Yeah Yeah",
  "I will turn a fella into a convertible"
]

gunsList = [
  "MP5",
  "M4",
  "AK-47",
  "MP7",
  "SCAR-L",
  "Desert Eagle",
  "MP5K",
  "AUG A2",
  "M249",
  "AR15"
]

titleList = [
  "Elimination",
  "Homicide",
  "Assasination",
  "Drive-by",
  "Sniped",
  "Popped",
  "Capped",
  "No-scoped",
]

categoryRoles = [808514745614467102, 820087344953819197, 820086843709325322, 820087010525315092, 820086674712428584, 820086008421810186, 820085362457444393, 820084892884664391, 820085510386221086]

scrambleWords = [
"jager",
"rainbow",
"discord",
"snake",
"wolf",
"google",
"windows",
"anime",
"electricity",
"internet",
"frog",
"police",
"door",
"monitor",
]

emojis = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯"]

regionalIndicators = [
":regional_indicator_a:",
":regional_indicator_b:",
":regional_indicator_c:",
":regional_indicator_d:",
":regional_indicator_e:",
":regional_indicator_f:",
":regional_indicator_g:",
":regional_indicator_h:",
":regional_indicator_i:",
":regional_indicator_j:"
]

staffRoles = [
  769577772652691486,
  834184731193114714,
  810585594638893096,
  769577839313551360,
  810586176515080223,
  769579500752863243,
  839209488727932969,
  839209591887364126
]

staffRolesDict = {
  "Owner": 769577772652691486,
  "Co Owner": 834184731193114714,
  "Admin": 810585594638893096,
  "Trial Admin": 769577839313551360,
  "Mod": 810586176515080223,
  "Trial Mod": 769579500752863243,
  "Helper": 839209488727932969,
  "Trial Helper": 839209591887364126
}

levelRoles = {
0: 835901251714678836,
5: 769579510902947861,
10: 769579510181658664,
15: 769579509363376168,
20: 769579506766708816,
30: 769579505295032351,
40: 769579505646829593,
50: 769579504237674547,
60: 769579503675506698,
70: 769579502606090250,
80: 833369830186811392,
90: 833369823957614612,
100: 833369826709471282
}

NoPermErrorMessages = [
  "Nah bro",
  "Not feeling like it today",
  "Im busy",
  "Make me",
  "No lol"
]