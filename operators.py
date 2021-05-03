import discord


#operator profiles
embeds = {}
#sledge
embeds["sledge"] = discord.Embed(
title="Sledge",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Sledge",
color=0x916F7A
)
embeds["sledge"].add_field(name="Name", value="Seamus Cowden", inline=False)
embeds["sledge"].add_field(name="Organization", value="SAS", inline=False)
embeds["sledge"].add_field(name="Age", value="35", inline=True)
embeds["sledge"].add_field(name="Height", value="1.92m / 6'4\"", inline=True)
embeds["sledge"].add_field(name="Weight", value="95kg / 209 lbs", inline=True)
embeds["sledge"].add_field(name="Date of birth", value="April 2", inline=True)
embeds["sledge"].add_field(name="Birthplace", value="John o' Groats, Scotland", inline=True)
embeds["sledge"].add_field(name="Voice Actor", value="Ryan Nicolls", inline=False)
embeds["sledge"].add_field(name="Primary Weapons", value="M590A1 / L85A2", inline=True)
embeds["sledge"].add_field(name="Secondary Weapons", value="P226 MK25 / SMG-11", inline=True)
embeds["sledge"].add_field(name="Gadget", value="Frag Grenade / Stun Grenade", inline=False)
embeds["sledge"].add_field(name="Ability", value="Tactical Breaching Hammer 'The Caber, Brucie'", inline=True)
embeds["sledge"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["sledge"].set_author(name="Operator profile")
embeds["sledge"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/7/76/Sledge_Icon_-_Standard.png/revision/latest/scale-to-width-down/125?cb=20151222045526")

#thatcher
embeds["thatcher"] = discord.Embed(
title="Thatcher",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Thatcher",
color=0x916F7A
)
embeds["thatcher"].add_field(name="Name", value="Mike Baker", inline=False)
embeds["thatcher"].add_field(name="Organization", value="SAS", inline=False)
embeds["thatcher"].add_field(name="Age", value="56", inline=True)
embeds["thatcher"].add_field(name="Height", value="1.8m / 5'11\"", inline=True)
embeds["thatcher"].add_field(name="Weight", value="72kg / 158.4 lbs", inline=True)
embeds["thatcher"].add_field(name="Date of birth", value="June 22", inline=True)
embeds["thatcher"].add_field(name="Birthplace", value="Bideford, England", inline=True)
embeds["thatcher"].add_field(name="Voice Actor", value="Jamie Muffett", inline=False)
embeds["thatcher"].add_field(name="Primary Weapons", value="M590A1 / AR33 / L85A2", inline=True)
embeds["thatcher"].add_field(name="Secondary Weapons", value="P226 MK25", inline=True)
embeds["thatcher"].add_field(name="Gadget", value="Claymore / Breach Charge", inline=False)
embeds["thatcher"].add_field(name="Ability", value="EMP Grenade 'EG MKO-EMP Grenade'", inline=True)
embeds["thatcher"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["thatcher"].set_author(name="Operator profile")
embeds["thatcher"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/6/6d/Thatcher_Icon_-_Standard.png/revision/latest/scale-to-width-down/125?cb=20151222045527")

#smoke
embeds["smoke"] = discord.Embed(
title="Smoke",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Smoke",
color=0x916F7A
)
embeds["smoke"].add_field(name="Name", value="James Porter", inline=False)
embeds["smoke"].add_field(name="Organization", value="SAS", inline=False)
embeds["smoke"].add_field(name="Age", value="36", inline=True)
embeds["smoke"].add_field(name="Height", value="1.73m / 5'8\"", inline=True)
embeds["smoke"].add_field(name="Weight", value="70kg / 154 lbs", inline=True)
embeds["smoke"].add_field(name="Date of birth", value="May 14", inline=True)
embeds["smoke"].add_field(name="Birthplace", value="London, England (Kings Cross)", inline=True)
embeds["smoke"].add_field(name="Voice Actor", value="Martin Sims", inline=False)
embeds["smoke"].add_field(name="Primary Weapons", value="FMG-9 / M590A1", inline=True)
embeds["smoke"].add_field(name="Secondary Weapons", value="P226 MK25 / SMG-11", inline=True)
embeds["smoke"].add_field(name="Gadget", value="Deployable Shield / Barbed Wire", inline=False)
embeds["smoke"].add_field(name="Ability", value="Remote Gas Grenade 'Compound Z8 Grenade' ", inline=True)
embeds["smoke"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["smoke"].set_author(name="Operator profile")
embeds["smoke"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/ae/Smoke_Icon_-_Standard.png/revision/latest/scale-to-width-down/125?cb=20151222045526")

#mute
embeds["mute"] = discord.Embed(
title="Mute",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Mute",
color=0x916F7A
)
embeds["mute"].add_field(name="Name", value="Mark R. Chandar", inline=False)
embeds["mute"].add_field(name="Organization", value="SAS", inline=False)
embeds["mute"].add_field(name="Age", value="25", inline=True)
embeds["mute"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["mute"].add_field(name="Weight", value="74kg / 163 lbs", inline=True)
embeds["mute"].add_field(name="Date of birth", value="October 11", inline=True)
embeds["mute"].add_field(name="Birthplace", value="York, England", inline=True)
embeds["mute"].add_field(name="Voice Actor", value="Gary Milner", inline=False)
embeds["mute"].add_field(name="Primary Weapons", value="MP5K / M590A1", inline=True)
embeds["mute"].add_field(name="Secondary Weapons", value="P226 MK25 / SMG-11", inline=True)
embeds["mute"].add_field(name="Gadget", value="Nitro Cell / Bulletproof Camera", inline=False)
embeds["mute"].add_field(name="Ability", value="Signal Disruptor '\"Moni\" GC90 Signal Disruptor' ", inline=True)
embeds["mute"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["mute"].set_author(name="Operator profile")
embeds["mute"].set_footer(text="Mute is cute")
embeds["mute"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/c/c2/Mute_Icon_-_Standard.png/revision/latest/scale-to-width-down/125?cb=20151222045525")

#ash
embeds["ash"] = discord.Embed(
title="Ash",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Ash",
color=0xD55B2C
)
embeds["ash"].add_field(name="Name", value="Eliza Cohen", inline=False)
embeds["ash"].add_field(name="Organization", value="FBI SWAT", inline=False)
embeds["ash"].add_field(name="Age", value="33", inline=True)
embeds["ash"].add_field(name="Height", value="1.7m / 5'7\"", inline=True)
embeds["ash"].add_field(name="Weight", value="63kg / 138 lbs", inline=True)
embeds["ash"].add_field(name="Date of birth", value="December 24", inline=True)
embeds["ash"].add_field(name="Birthplace", value="Jerusalem, Israel", inline=True)
embeds["ash"].add_field(name="Voice Actor", value="Patricia Summersett", inline=False)
embeds["ash"].add_field(name="Primary Weapons", value="R4C / G36C", inline=True)
embeds["ash"].add_field(name="Secondary Weapons", value="M45 MEUSOC / 5.7 USG", inline=True)
embeds["ash"].add_field(name="Gadget", value="Breach Charge / Claymore", inline=False)
embeds["ash"].add_field(name="Ability", value="Breaching Rounds 'M120 Crem'", inline=True)
embeds["ash"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["ash"].set_author(name="Operator profile")
embeds["ash"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/d7/Ash_Icon_-_Standard.png/revision/latest/scale-to-width-down/125?cb=20151222045522")

#thermite
embeds["thermite"] = discord.Embed(
title="Thermite",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Thermite",
color=0xD55B2C
)
embeds["thermite"].add_field(name="Name", value="Jordan Tracen", inline=False)
embeds["thermite"].add_field(name="Organization", value="FBI SWAT", inline=False)
embeds["thermite"].add_field(name="Age", value="35", inline=True)
embeds["thermite"].add_field(name="Height", value="1.78m / 5'10\"", inline=True)
embeds["thermite"].add_field(name="Weight", value="80kg / 179 lbs", inline=True)
embeds["thermite"].add_field(name="Date of birth", value="March 14", inline=True)
embeds["thermite"].add_field(name="Birthplace", value="Plano, Texas", inline=True)
embeds["thermite"].add_field(name="Voice Actor", value="Carlo Mestroni", inline=False)
embeds["thermite"].add_field(name="Primary Weapons", value="556XI / M1014", inline=True)
embeds["thermite"].add_field(name="Secondary Weapons", value="M45 MEUSOC / 5.7 USG", inline=True)
embeds["thermite"].add_field(name="Gadget", value="Stun Grenade / Claymore", inline=False)
embeds["thermite"].add_field(name="Ability", value="Exothermic Charge 'Brimstone BC-3 Exothermic Charge'", inline=True)
embeds["thermite"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["thermite"].set_author(name="Operator profile")
embeds["thermite"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/e/e3/Thermite_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045527")

#castle
embeds["castle"] = discord.Embed(
title="Castle",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Castle",
color=0xD55B2C
)
embeds["castle"].add_field(name="Name", value="Miles Campbell", inline=False)
embeds["castle"].add_field(name="Organization", value="FBI SWAT", inline=False)
embeds["castle"].add_field(name="Age", value="36", inline=True)
embeds["castle"].add_field(name="Height", value="1.85m / 6'1\"", inline=True)
embeds["castle"].add_field(name="Weight", value="70kg / 154 lbs", inline=True)
embeds["castle"].add_field(name="Date of birth", value="September 20", inline=True)
embeds["castle"].add_field(name="Birthplace", value="Sherman Oaks, California", inline=True)
embeds["castle"].add_field(name="Voice Actor", value="Luke Forbes", inline=False)
embeds["castle"].add_field(name="Primary Weapons", value="UMP45 / M1014", inline=True)
embeds["castle"].add_field(name="Secondary Weapons", value="5.7 USG / Super Shorty", inline=True)
embeds["castle"].add_field(name="Gadget", value="Bulletproof Camera / Proximity Alarm", inline=False)
embeds["castle"].add_field(name="Ability", value="Armor Panel 'UTP1 Universal Tactical Panel' ", inline=True)
embeds["castle"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["castle"].set_author(name="Operator profile")
embeds["castle"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/a9/Castle_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045523")

#pulse
embeds["pulse"] = discord.Embed(
title="Pulse",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Pulse",
color=0xD55B2C
)
embeds["pulse"].add_field(name="Name", value="Jack Estrada", inline=False)
embeds["pulse"].add_field(name="Organization", value="FBI SWAT", inline=False)
embeds["pulse"].add_field(name="Age", value="32", inline=True)
embeds["pulse"].add_field(name="Height", value="1.88m / 6'2\"", inline=True)
embeds["pulse"].add_field(name="Weight", value="85kg / 187 lbs", inline=True)
embeds["pulse"].add_field(name="Date of birth", value="October 11", inline=True)
embeds["pulse"].add_field(name="Birthplace", value="Goldsboro, North Carolina", inline=True)
embeds["pulse"].add_field(name="Voice Actor", value="Eric T. Miller", inline=False)
embeds["pulse"].add_field(name="Primary Weapons", value="M1014 / UMP45", inline=True)
embeds["pulse"].add_field(name="Secondary Weapons", value="M45 MEUSOC / 5.7 USG", inline=True)
embeds["pulse"].add_field(name="Gadget", value="Barbed Wire / Nitro Cell", inline=False)
embeds["pulse"].add_field(name="Ability", value="Heartbeat Sensor 'HB-5 Cardiac Sensor' ", inline=True)
embeds["pulse"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["pulse"].set_author(name="Operator profile")
embeds["pulse"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/4/40/Pulse_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045526")

#twitch
embeds["twitch"] = discord.Embed(
title="Twitch",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Twitch",
color=0x396181
)
embeds["twitch"].add_field(name="Name", value="Emmanuelle Pichon", inline=False)
embeds["twitch"].add_field(name="Organization", value="GIGN", inline=False)
embeds["twitch"].add_field(name="Age", value="28", inline=True)
embeds["twitch"].add_field(name="Height", value="1.68m / 5'6\"", inline=True)
embeds["twitch"].add_field(name="Weight", value="58kg / 127 lbs", inline=True)
embeds["twitch"].add_field(name="Date of birth", value="October 12", inline=True)
embeds["twitch"].add_field(name="Birthplace", value="Nancy, Meurthe-et-Moselle, France", inline=True)
embeds["twitch"].add_field(name="Voice Actor", value="Brigitte Bourdeau", inline=False)
embeds["twitch"].add_field(name="Primary Weapons", value="F2 / 417 / SG-CQB", inline=True)
embeds["twitch"].add_field(name="Secondary Weapons", value="P9 / LFP586", inline=True)
embeds["twitch"].add_field(name="Gadget", value="Stun Grenade / Claymore", inline=False)
embeds["twitch"].add_field(name="Ability", value="Shock Drome 'RSD Model 1 Shock Drone'", inline=True)
embeds["twitch"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["twitch"].set_author(name="Operator profile")
embeds["twitch"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/4/47/Twitch_Badge_New_2.png/revision/latest/scale-to-width-down/125?cb=20151222045527")

#montagne
embeds["montagne"] = discord.Embed(
title="Montagne",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Montagne",
color=0x396181
)
embeds["montagne"].add_field(name="Name", value="Gilles Touré", inline=False)
embeds["montagne"].add_field(name="Organization", value="GIGN", inline=False)
embeds["montagne"].add_field(name="Age", value="48", inline=True)
embeds["montagne"].add_field(name="Height", value="1.90m / 6'3\"", inline=True)
embeds["montagne"].add_field(name="Weight", value="90kg / 198 lbs", inline=True)
embeds["montagne"].add_field(name="Date of birth", value="October 11", inline=True)
embeds["montagne"].add_field(name="Birthplace", value="Bordeaux, Gironde, France", inline=True)
embeds["montagne"].add_field(name="Voice Actor", value="Louis Philippe Dandenault", inline=False)
embeds["montagne"].add_field(name="Primary Weapons", value="Extendable Shield", inline=True)
embeds["montagne"].add_field(name="Secondary Weapons", value="P9 / LFP586", inline=True)
embeds["montagne"].add_field(name="Gadget", value="Hard Breach Charge / Smoke Grenade", inline=False)
embeds["montagne"].add_field(name="Ability", value="Extendable Shield '\"Le Roc\" Extendable Shield'", inline=True)
embeds["montagne"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["montagne"].set_author(name="Operator profile")
embeds["montagne"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/b/be/Montagne_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045525")

#doc
embeds["doc"] = discord.Embed(
title="Doc",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Doc",
color=0x396181
)
embeds["doc"].add_field(name="Name", value="Gustave Kateb", inline=False)
embeds["doc"].add_field(name="Organization", value="GIGN", inline=False)
embeds["doc"].add_field(name="Age", value="39", inline=True)
embeds["doc"].add_field(name="Height", value="1.77m / 5'10\"", inline=True)
embeds["doc"].add_field(name="Weight", value="85kg / 187 lbs", inline=True)
embeds["doc"].add_field(name="Date of birth", value="September 16", inline=True)
embeds["doc"].add_field(name="Birthplace", value="Paris, France", inline=True)
embeds["doc"].add_field(name="Voice Actor", value="Alex Ivanovici", inline=False)
embeds["doc"].add_field(name="Primary Weapons", value="SG-CQB / MP5 / P90", inline=True)
embeds["doc"].add_field(name="Secondary Weapons", value="P9 / LFP586", inline=True)
embeds["doc"].add_field(name="Gadget", value="Barbed Wire / Bulletproof Camera", inline=False)
embeds["doc"].add_field(name="Ability", value="Stim Pistol 'MPD-0 Stim Pistol' ", inline=True)
embeds["doc"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["doc"].set_author(name="Operator profile")
embeds["doc"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/8f/Doc_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045524")

#rook
embeds["rook"] = discord.Embed(
title="Rook",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Rook",
color=0x396181
)
embeds["rook"].add_field(name="Name", value="Julien Nizan", inline=False)
embeds["rook"].add_field(name="Organization", value="GIGN", inline=False)
embeds["rook"].add_field(name="Age", value="27", inline=True)
embeds["rook"].add_field(name="Height", value="1.77m / 5'10\"", inline=True)
embeds["rook"].add_field(name="Weight", value="72kg / 158,7 lbs", inline=True)
embeds["rook"].add_field(name="Date of birth", value="January 6", inline=True)
embeds["rook"].add_field(name="Birthplace", value="Tours, Indre-et-Loire, France", inline=True)
embeds["rook"].add_field(name="Voice Actor", value="Marc-André Brunet", inline=False)
embeds["rook"].add_field(name="Primary Weapons", value="P90 / MP5 / SG-CQB", inline=True)
embeds["rook"].add_field(name="Secondary Weapons", value="LFP586 / P9", inline=True)
embeds["rook"].add_field(name="Gadget", value="Proximity Alarm / Impact Grenade", inline=False)
embeds["rook"].add_field(name="Ability", value="Armor Pack 'R1N \"Rhino\" Armor Pack'", inline=True)
embeds["rook"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["rook"].set_author(name="Operator profile")
embeds["rook"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/ab/Rook_Badge_New_2.png/revision/latest/scale-to-width-down/125?cb=20151222045526")

#glaz
embeds["glaz"] = discord.Embed(
title="Glaz",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Glaz",
color=0xa9151a
)
embeds["glaz"].add_field(name="Name", value="Timur Glazkov", inline=False)
embeds["glaz"].add_field(name="Organization", value="Spetsnaz", inline=False)
embeds["glaz"].add_field(name="Age", value="30", inline=True)
embeds["glaz"].add_field(name="Height", value="1.78m / 5'10\"", inline=True)
embeds["glaz"].add_field(name="Weight", value="79kg / 174 lbs", inline=True)
embeds["glaz"].add_field(name="Date of birth", value="July 2", inline=True)
embeds["glaz"].add_field(name="Birthplace", value="Vladivostok, Primorsky Krai, Russia (Russian SFSR, Soviet Union)", inline=True)
embeds["glaz"].add_field(name="Voice Actor", value="Stan Demidoff", inline=False)
embeds["glaz"].add_field(name="Primary Weapons", value="OTs-03", inline=True)
embeds["glaz"].add_field(name="Secondary Weapons", value="GONNE-6 / GSh-18", inline=True)
embeds["glaz"].add_field(name="Gadget", value="Smoke Grenade / Frag Grenade", inline=False)
embeds["glaz"].add_field(name="Ability", value="Flip Sight 'HDS Flip Sight'", inline=True)
embeds["glaz"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["glaz"].set_author(name="Operator profile")
embeds["glaz"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/8d/Glaz_Badge_2.png/revision/latest/scale-to-width-down/250?cb=20151222045524")

#fuze
embeds["fuze"] = discord.Embed(
title="Fuze",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Fuze",
color=0xa9151a
)
embeds["fuze"].add_field(name="Name", value="Shuhrat Kessikbayev", inline=False)
embeds["fuze"].add_field(name="Organization", value="Spetsnaz", inline=False)
embeds["fuze"].add_field(name="Age", value="34", inline=True)
embeds["fuze"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["fuze"].add_field(name="Weight", value="80kg / 177 lbs", inline=True)
embeds["fuze"].add_field(name="Date of birth", value="October 12", inline=True)
embeds["fuze"].add_field(name="Birthplace", value="Samarkand, Uzbekistan (Uzbek SSR, Soviet Union)", inline=True)
embeds["fuze"].add_field(name="Voice Actor", value="Gabriel Furman", inline=False)
embeds["fuze"].add_field(name="Primary Weapons", value="AK-12 / 6P41 / Ballistic Shield", inline=True)
embeds["fuze"].add_field(name="Secondary Weapons", value="PMM / GSh-18", inline=True)
embeds["fuze"].add_field(name="Gadget", value="Breach Charge / Hard Breach Charge", inline=False)
embeds["fuze"].add_field(name="Ability", value="Cluster Charge 'APM-6 \"Matryoshka\"'", inline=True)
embeds["fuze"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["fuze"].set_author(name="Operator profile")
embeds["fuze"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/3/3f/Fuze_Badge_2.png/revision/latest/scale-to-width-down/250?cb=20151222045524")

#kapkan
embeds["kapkan"] = discord.Embed(
title="Kapkan",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Kapkan",
color=0xa9151a
)
embeds["kapkan"].add_field(name="Name", value="Maxim Basuda", inline=False)
embeds["kapkan"].add_field(name="Organization", value="Spetsnaz", inline=False)
embeds["kapkan"].add_field(name="Age", value="38", inline=True)
embeds["kapkan"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["kapkan"].add_field(name="Weight", value="80kg / 176 lbs", inline=True)
embeds["kapkan"].add_field(name="Date of birth", value="May 14", inline=True)
embeds["kapkan"].add_field(name="Birthplace", value="Kovrov, Vladimir Oblast, Russia (Russian SFSR, Soviet Union)", inline=True)
embeds["kapkan"].add_field(name="Voice Actor", value="Victor Bevine", inline=False)
embeds["kapkan"].add_field(name="Primary Weapons", value="9×19VSN / SASG-12", inline=True)
embeds["kapkan"].add_field(name="Secondary Weapons", value="PMM / GSh-18", inline=True)
embeds["kapkan"].add_field(name="Gadget", value="Impact Grenade / Nitro Cell", inline=False)
embeds["kapkan"].add_field(name="Ability", value="Entry Denial Device 'EDD MK II Trip Wire'", inline=True)
embeds["kapkan"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["kapkan"].set_author(name="Operator profile")
embeds["kapkan"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/81/Kapkan_Badge_2.png/revision/latest?cb=20151222045525")

#tachanka
embeds["tachanka"] = discord.Embed(
title="Lord Tachanka",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Tachanka",
color=0xa9151a
)
embeds["tachanka"].add_field(name="Name", value="Alexsandr Senaviev", inline=False)
embeds["tachanka"].add_field(name="Organization", value="Spetsnaz", inline=False)
embeds["tachanka"].add_field(name="Age", value="48", inline=True)
embeds["tachanka"].add_field(name="Height", value="1.83m / 6'0\"", inline=True)
embeds["tachanka"].add_field(name="Weight", value="86kg / 190 lbs", inline=True)
embeds["tachanka"].add_field(name="Date of birth", value="November 3", inline=True)
embeds["tachanka"].add_field(name="Birthplace", value="Saint Petersburg, Russia (Leningrad, Russian SFSR, Soviet Union)", inline=True)
embeds["tachanka"].add_field(name="Voice Actor", value="Vlad Stokanic / Anatoly Zinoviev (Formerly)", inline=False)
embeds["tachanka"].add_field(name="Primary Weapons", value="DP27 / 9×19VSN", inline=True)
embeds["tachanka"].add_field(name="Secondary Weapons", value="GSh-18 / PMM", inline=True)
embeds["tachanka"].add_field(name="Gadget", value="Barbed Wire / Proximity Alarm", inline=False)
embeds["tachanka"].add_field(name="Ability", value="Shumikha Launcher 'Grenade Launcher'", inline=True)
embeds["tachanka"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["tachanka"].set_author(name="Operator profile")
embeds["tachanka"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/8c/Tachanka_Badge_Rework.png/revision/latest/scale-to-width-down/400?cb=20201008005243")

#blitz
embeds["blitz"] = discord.Embed(
title="Blitz",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Blitz",
color=0xF7C334
)
embeds["blitz"].add_field(name="Name", value="Elias Kötz", inline=False)
embeds["blitz"].add_field(name="Organization", value="GSG 9", inline=False)
embeds["blitz"].add_field(name="Age", value="37", inline=True)
embeds["blitz"].add_field(name="Height", value="1.75m / 5'9\"", inline=True)
embeds["blitz"].add_field(name="Weight", value="75kg / 165 lbs", inline=True)
embeds["blitz"].add_field(name="Date of birth", value="April 2", inline=True)
embeds["blitz"].add_field(name="Birthplace", value="Bremen, Germany (West Germany)", inline=True)
embeds["blitz"].add_field(name="Voice Actor", value="Christopher J. Domig", inline=False)
embeds["blitz"].add_field(name="Primary Weapons", value="G52-Tactical Shield", inline=True)
embeds["blitz"].add_field(name="Secondary Weapons", value="P12", inline=True)
embeds["blitz"].add_field(name="Gadget", value="Smoke Grenade / Breach Charge", inline=False)
embeds["blitz"].add_field(name="Ability", value="Flash Shield 'G52-Tactical Shield'", inline=True)
embeds["blitz"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["blitz"].set_author(name="Operator profile")
embeds["blitz"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/6/62/Blitz_Badge_2.png/revision/latest/scale-to-width-down/250?cb=20151222045523")

#IQ
embeds["iq"] = discord.Embed(
title="IQ",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/IQ",
color=0xF7C334
)
embeds["iq"].add_field(name="Name", value="Monica Weiss", inline=False)
embeds["iq"].add_field(name="Organization", value="GSG 9", inline=False)
embeds["iq"].add_field(name="Age", value="38", inline=True)
embeds["iq"].add_field(name="Height", value="1.75m / 5'9\"", inline=True)
embeds["iq"].add_field(name="Weight", value="70kg / 154 lbs", inline=True)
embeds["iq"].add_field(name="Date of birth", value="August 1", inline=True)
embeds["iq"].add_field(name="Birthplace", value="Leipzig, Saxony, Germany (East Germany)", inline=True)
embeds["iq"].add_field(name="Voice Actor", value="Sandra Kawloski", inline=False)
embeds["iq"].add_field(name="Primary Weapons", value="AUG A2 / 552 Commande / G8A1", inline=True)
embeds["iq"].add_field(name="Secondary Weapons", value="P12", inline=True)
embeds["iq"].add_field(name="Gadget", value="Breach Charge / Claymore", inline=False)
embeds["iq"].add_field(name="Ability", value="Electronics Detector 'RED Mk III Spectre'", inline=True)
embeds["iq"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["iq"].set_author(name="Operator profile")
embeds["iq"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/b/b7/IQ_Badge_2.png/revision/latest/scale-to-width-down/250?cb=20151222045524")

#jager
embeds["jager"] = discord.Embed(
title="Lord Jäger",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Jäger",
color=0xF7C334
)
embeds["jager"].add_field(name="Name", value="Marius Streicher", inline=False)
embeds["jager"].add_field(name="Organization", value="GSG 9", inline=False)
embeds["jager"].add_field(name="Age", value="39", inline=True)
embeds["jager"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["jager"].add_field(name="Weight", value="64kg / 141 lbs", inline=True)
embeds["jager"].add_field(name="Date of birth", value="March 9", inline=True)
embeds["jager"].add_field(name="Birthplace", value="Düsseldorf, NRW, Germany (West Germany)", inline=True)
embeds["jager"].add_field(name="Voice Actor", value="Michael Sinterniklaas", inline=False)
embeds["jager"].add_field(name="Primary Weapons", value="M870 / 416-C Carbine", inline=True)
embeds["jager"].add_field(name="Secondary Weapons", value="P12", inline=True)
embeds["jager"].add_field(name="Gadget", value="Bulletproof Camera / Barbed Wire", inline=False)
embeds["jager"].add_field(name="Ability", value="Active Defense System 'ADS-MKIV \"Magpie\"'", inline=True)
embeds["jager"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["jager"].set_author(name="Operator profile")
embeds["jager"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/9/95/Jager_Badge_2.png/revision/latest/scale-to-width-down/125?cb=20151222045525")

#bandit
embeds["bandit"] = discord.Embed(
title="Bandit",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Bandit",
color=0xF7C334
)
embeds["bandit"].add_field(name="Name", value="Dominic Brunsmeier", inline=False)
embeds["bandit"].add_field(name="Organization", value="GSG 9", inline=False)
embeds["bandit"].add_field(name="Age", value="42", inline=True)
embeds["bandit"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["bandit"].add_field(name="Weight", value="68kg / 149 lbs", inline=True)
embeds["bandit"].add_field(name="Date of birth", value="August 13", inline=True)
embeds["bandit"].add_field(name="Birthplace", value="Berlin, Germany (East Germany)", inline=True)
embeds["bandit"].add_field(name="Voice Actor", value="Carl Bishop", inline=False)
embeds["bandit"].add_field(name="Primary Weapons", value="MP7 / M870", inline=True)
embeds["bandit"].add_field(name="Secondary Weapons", value="P12", inline=True)
embeds["bandit"].add_field(name="Gadget", value="Barbed Wire / Nitro Cell", inline=False)
embeds["bandit"].add_field(name="Ability", value="Shock Wire 'CED-1 (Crude Electrical Device)'", inline=True)
embeds["bandit"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["bandit"].set_author(name="Operator profile")
embeds["bandit"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/3/30/Bandit_Badge_2.png/revision/latest?cb=20151222045523")

#buck
embeds["buck"] = discord.Embed(
title="Buck",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Buck",
color=0x2F82A2
)
embeds["buck"].add_field(name="Name", value="Sébastien Côté", inline=False)
embeds["buck"].add_field(name="Organization", value="JTF2", inline=False)
embeds["buck"].add_field(name="Age", value="36", inline=True)
embeds["buck"].add_field(name="Height", value="1.78m / 5'10\"", inline=True)
embeds["buck"].add_field(name="Weight", value="78kg / 185 lbs", inline=True)
embeds["buck"].add_field(name="Date of birth", value="August 20", inline=True)
embeds["buck"].add_field(name="Birthplace", value="Montreal, Quebec", inline=True)
embeds["buck"].add_field(name="Voice Actor", value="Lucien Bergeron", inline=False)
embeds["buck"].add_field(name="Primary Weapons", value="C8-SFW / CAMRS", inline=True)
embeds["buck"].add_field(name="Secondary Weapons", value="Mk1 9mm", inline=True)
embeds["buck"].add_field(name="Gadget", value="Stun Grenade / Hard Breach Charge", inline=False)
embeds["buck"].add_field(name="Ability", value="Skeleton Key 'SK 4-12'", inline=True)
embeds["buck"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["buck"].set_author(name="Operator profile")
embeds["buck"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/3/34/Buck_Badge_New.png/revision/latest/scale-to-width-down/332?cb=20160203040454")


#frost
embeds["frost"] = discord.Embed(
title="Frost",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Frost",
color=0x2F82A2
)
embeds["frost"].add_field(name="Name", value="Tina Lin Tsang", inline=False)
embeds["frost"].add_field(name="Organization", value="JTF2", inline=False)
embeds["frost"].add_field(name="Age", value="32", inline=True)
embeds["frost"].add_field(name="Height", value="1.72m / 5'8\"", inline=True)
embeds["frost"].add_field(name="Weight", value="63kg / 139 lbs", inline=True)
embeds["frost"].add_field(name="Date of birth", value="May 4", inline=True)
embeds["frost"].add_field(name="Birthplace", value="Vancouver, British Colombia", inline=True)
embeds["frost"].add_field(name="Voice Actor", value="Julie Tamiko", inline=False)
embeds["frost"].add_field(name="Primary Weapons", value="Super 90 / 9mm C1", inline=True)
embeds["frost"].add_field(name="Secondary Weapons", value="Mk1 9mm / ITA12S", inline=True)
embeds["frost"].add_field(name="Gadget", value="Bulletproof Camera / Deployable Shield", inline=False)
embeds["frost"].add_field(name="Ability", value="Welcome Mat 'Sterling Mk2 LHT'", inline=True)
embeds["frost"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["frost"].set_author(name="Operator profile")
embeds["frost"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/c/c1/Frost_Badge_New.png/revision/latest?cb=20160203040937")

#blackbeard
embeds["blackbeard"] = discord.Embed(
title="Blackbeard",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Blackbeard",
color=0xC38F00
)
embeds["blackbeard"].add_field(name="Name", value="Craig Jenson", inline=False)
embeds["blackbeard"].add_field(name="Organization", value="Navy SEALs", inline=False)
embeds["blackbeard"].add_field(name="Age", value="32", inline=True)
embeds["blackbeard"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["blackbeard"].add_field(name="Weight", value="84kg / 185 lbs", inline=True)
embeds["blackbeard"].add_field(name="Date of birth", value="March 12", inline=True)
embeds["blackbeard"].add_field(name="Birthplace", value="Bellevue, Washington", inline=True)
embeds["blackbeard"].add_field(name="Voice Actor", value="Christian Jadah", inline=False)
embeds["blackbeard"].add_field(name="Primary Weapons", value="Mk17 CQB / SR-25", inline=True)
embeds["blackbeard"].add_field(name="Secondary Weapons", value="D-50", inline=True)
embeds["blackbeard"].add_field(name="Gadget", value="Breach Charge/ Stun Grenade", inline=False)
embeds["blackbeard"].add_field(name="Ability", value="Rifle-Shield 'TARS Mk 0-Transparent Armored Rifle-Shield'", inline=True)
embeds["blackbeard"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["blackbeard"].set_author(name="Operator profile")
embeds["blackbeard"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/dd/Blackbeard_badge.png/revision/latest/scale-to-width-down/166?cb=20160509214645")

#valkyrie
embeds["valkyrie"] = discord.Embed(
title="Valkyrie",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Valkyrie",
color=0xC38F00
)
embeds["valkyrie"].add_field(name="Name", value="Meghan J. Castellano", inline=False)
embeds["valkyrie"].add_field(name="Organization", value="Navy SEALs", inline=False)
embeds["valkyrie"].add_field(name="Age", value="31", inline=True)
embeds["valkyrie"].add_field(name="Height", value="1.70m / 5'7\"", inline=True)
embeds["valkyrie"].add_field(name="Weight", value="61kg / 134 lbs", inline=True)
embeds["valkyrie"].add_field(name="Date of birth", value="July 21", inline=True)
embeds["valkyrie"].add_field(name="Birthplace", value="Oceanside, California", inline=True)
embeds["valkyrie"].add_field(name="Voice Actor", value="Christine Lakin", inline=False)
embeds["valkyrie"].add_field(name="Primary Weapons", value="MPX / SPAS-12", inline=True)
embeds["valkyrie"].add_field(name="Secondary Weapons", value="D-50", inline=True)
embeds["valkyrie"].add_field(name="Gadget", value="Impact Grenade / Nitro Cell", inline=False)
embeds["valkyrie"].add_field(name="Ability", value="Black Eye 'Gyro Cam Mk2'", inline=True)
embeds["valkyrie"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["valkyrie"].set_author(name="Operator profile")
embeds["valkyrie"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/e/ef/Valkyrie_badge.png/revision/latest?cb=20160509214702")

#capitao
embeds["capitao"] = discord.Embed(
title="Capitão",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Capitão",
color=0x468C40
)
embeds["capitao"].add_field(name="Name", value="Vicente Souza", inline=False)
embeds["capitao"].add_field(name="Organization", value="BOPE", inline=False)
embeds["capitao"].add_field(name="Age", value="49", inline=True)
embeds["capitao"].add_field(name="Height", value="1.83m / 6'0\"", inline=True)
embeds["capitao"].add_field(name="Weight", value="86kg / 190 lbs", inline=True)
embeds["capitao"].add_field(name="Date of birth", value="November 17", inline=True)
embeds["capitao"].add_field(name="Birthplace", value="Nova Iguaçu, Brazil", inline=True)
embeds["capitao"].add_field(name="Voice Actor", value="Jonathan Davis", inline=False)
embeds["capitao"].add_field(name="Primary Weapons", value="PARA-308 / M249", inline=True)
embeds["capitao"].add_field(name="Secondary Weapons", value="PRB92", inline=True)
embeds["capitao"].add_field(name="Gadget", value="Claymore / Hard Breach Charge", inline=False)
embeds["capitao"].add_field(name="Ability", value="Tactical Crossbow 'TAC Mk0'", inline=True)
embeds["capitao"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["capitao"].set_author(name="Operator profile")
embeds["capitao"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/4/4e/R6S-badge-capitao.png/revision/latest/scale-to-width-down/166?cb=20160802150526")

#caveira
embeds["caveira"] = discord.Embed(
title="Caveira",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Caveira",
color=0x468C40
)
embeds["caveira"].add_field(name="Name", value="Taina Pereira", inline=False)
embeds["caveira"].add_field(name="Organization", value="BOPE", inline=False)
embeds["caveira"].add_field(name="Age", value="31", inline=True)
embeds["caveira"].add_field(name="Height", value="1.77m / 5'10\"", inline=True)
embeds["caveira"].add_field(name="Weight", value="72kg / 160 lbs", inline=True)
embeds["caveira"].add_field(name="Date of birth", value="October 15", inline=True)
embeds["caveira"].add_field(name="Birthplace", value="Rinópolis, São Paulo, Brazil", inline=True)
embeds["caveira"].add_field(name="Voice Actor", value="Renata Eastlick", inline=False)
embeds["caveira"].add_field(name="Primary Weapons", value="M12 / SPAS-15", inline=True)
embeds["caveira"].add_field(name="Secondary Weapons", value="Luison", inline=True)
embeds["caveira"].add_field(name="Gadget", value="Impact Grenade / Proximity Alarm", inline=False)
embeds["caveira"].add_field(name="Ability", value="Silent Step", inline=True)
embeds["caveira"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["caveira"].set_author(name="Operator profile")
embeds["caveira"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/e/ef/R6S-badge-caveira.png/revision/latest?cb=20160802150554")

#hibana
embeds["hibana"] = discord.Embed(
title="Hibana",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Hibana",
color=0x8F2842
)
embeds["hibana"].add_field(name="Name", value=" Yumiko Imagawa", inline=False)
embeds["hibana"].add_field(name="Organization", value="SAT", inline=False)
embeds["hibana"].add_field(name="Age", value="34", inline=True)
embeds["hibana"].add_field(name="Height", value="1.73m / 5'8\"", inline=True)
embeds["hibana"].add_field(name="Weight", value="57kg / 125 lbs", inline=True)
embeds["hibana"].add_field(name="Date of birth", value="July 12", inline=True)
embeds["hibana"].add_field(name="Birthplace", value="Nagoya, Japan", inline=True)
embeds["hibana"].add_field(name="Voice Actor", value="Laura Miyata / Jamie Choi (Formerly)", inline=False)
embeds["hibana"].add_field(name="Primary Weapons", value="SuperNova / Type-89", inline=True)
embeds["hibana"].add_field(name="Secondary Weapons", value="P229 / Bearing 9", inline=True)
embeds["hibana"].add_field(name="Gadget", value="Stun Grenade / Breach Charge", inline=False)
embeds["hibana"].add_field(name="Ability", value="X-KAIROS", inline=True)
embeds["hibana"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["hibana"].set_author(name="Operator profile")
embeds["hibana"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/7/79/R6S-hibana.png/revision/latest/scale-to-width-down/150?cb=20161118012747")

#echo
embeds["echo"] = discord.Embed(
title="Echo",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Echo",
color=0x8F2842
)
embeds["echo"].add_field(name="Name", value="Masaru Enatsu", inline=False)
embeds["echo"].add_field(name="Organization", value="SAT", inline=False)
embeds["echo"].add_field(name="Age", value="36", inline=True)
embeds["echo"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["echo"].add_field(name="Weight", value="72kg / 158 lbs", inline=True)
embeds["echo"].add_field(name="Date of birth", value="October 31", inline=True)
embeds["echo"].add_field(name="Birthplace", value="Suginami, Tokyo", inline=True)
embeds["echo"].add_field(name="Voice Actor", value="Shuhei Kinoshita", inline=False)
embeds["echo"].add_field(name="Primary Weapons", value="SuperNova / MP5SD", inline=True)
embeds["echo"].add_field(name="Secondary Weapons", value="P229 / Bearing 9", inline=True)
embeds["echo"].add_field(name="Gadget", value="Impact Grenade / Deployable Shield", inline=False)
embeds["echo"].add_field(name="Ability", value="Yokai", inline=True)
embeds["echo"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["echo"].set_author(name="Operator profile")
embeds["echo"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/b/b4/R6S-echo.png/revision/latest?cb=20161118012816")

#jackal
embeds["jackal"] = discord.Embed(
title="Jackal",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Jackal",
color=0x6D2E8E
)
embeds["jackal"].add_field(name="Name", value="Ryad Ramírez Al-Hassar", inline=False)
embeds["jackal"].add_field(name="Organization", value="GEO", inline=False)
embeds["jackal"].add_field(name="Age", value="49", inline=True)
embeds["jackal"].add_field(name="Height", value="1.90m / 6'3\"", inline=True)
embeds["jackal"].add_field(name="Weight", value="78kg / 172 lbs", inline=True)
embeds["jackal"].add_field(name="Date of birth", value="February 29", inline=True)
embeds["jackal"].add_field(name="Birthplace", value="Ceuta, Spain (Spanish State)", inline=True)
embeds["jackal"].add_field(name="Voice Actor", value="Conrad Pla", inline=False)
embeds["jackal"].add_field(name="Primary Weapons", value="C7E / PDW9 / ITA12L", inline=True)
embeds["jackal"].add_field(name="Secondary Weapons", value="ITA12S / USP40", inline=True)
embeds["jackal"].add_field(name="Gadget", value="Claymore / Smoke Grenade", inline=False)
embeds["jackal"].add_field(name="Ability", value="Eyenox Model III", inline=True)
embeds["jackal"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["jackal"].set_author(name="Operator profile")
embeds["jackal"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/d4/R6S-jackal.png/revision/latest/scale-to-width-down/166?cb=20170206195745")

#mira
embeds["mira"] = discord.Embed(
title="Mira",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Mira",
color=0x6D2E8E
)
embeds["mira"].add_field(name="Name", value="Elena María Álvarez", inline=False)
embeds["mira"].add_field(name="Organization", value="GEO", inline=False)
embeds["mira"].add_field(name="Age", value="39", inline=True)
embeds["mira"].add_field(name="Height", value="1.65m / 5'5\"", inline=True)
embeds["mira"].add_field(name="Weight", value="60kg / 132 lbs", inline=True)
embeds["mira"].add_field(name="Date of birth", value="November 18", inline=True)
embeds["mira"].add_field(name="Birthplace", value="Madrid, Spain", inline=True)
embeds["mira"].add_field(name="Voice Actor", value="Christine Solomon / Anahi Bustillos (Formerly)", inline=False)
embeds["mira"].add_field(name="Primary Weapons", value="Vector .45 ACP / ITA12L", inline=True)
embeds["mira"].add_field(name="Secondary Weapons", value="ITA12S / USP40", inline=True)
embeds["mira"].add_field(name="Gadget", value="Proximity Alarm / Nitro Cell", inline=False)
embeds["mira"].add_field(name="Ability", value="Black Mirror", inline=True)
embeds["mira"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["mira"].set_author(name="Operator profile")
embeds["mira"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/8f/R6S-mira.png/revision/latest?cb=20170206200012")

#ying
embeds["ying"] = discord.Embed(
title="Ying",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Ying",
color=0xAE6142
)
embeds["ying"].add_field(name="Name", value="Siu Mei Lin", inline=False)
embeds["ying"].add_field(name="Organization", value="SDU", inline=False)
embeds["ying"].add_field(name="Age", value="33", inline=True)
embeds["ying"].add_field(name="Height", value="1.60m / 5'3\"", inline=True)
embeds["ying"].add_field(name="Weight", value="52kg / 125 lbs", inline=True)
embeds["ying"].add_field(name="Date of birth", value="May 12", inline=True)
embeds["ying"].add_field(name="Birthplace", value="Central, Hong Kong (British Hong Kong)", inline=True)
embeds["ying"].add_field(name="Voice Actor", value="Jenny Raven", inline=False)
embeds["ying"].add_field(name="Primary Weapons", value="T-95 LSW / SIX12", inline=True)
embeds["ying"].add_field(name="Secondary Weapons", value="Q-929", inline=True)
embeds["ying"].add_field(name="Gadget", value="Hard Breach Charge / Smoke Grenade", inline=False)
embeds["ying"].add_field(name="Ability", value="Candela", inline=True)
embeds["ying"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["ying"].set_author(name="Operator profile")
embeds["ying"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/d7/R6S-Ying.png/revision/latest/scale-to-width-down/158?cb=20170828194010")

#lesion
embeds["lesion"] = discord.Embed(
title="Lesion",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Lesion",
color=0xAE6142
)
embeds["lesion"].add_field(name="Name", value="Liu Tze Long", inline=False)
embeds["lesion"].add_field(name="Organization", value="SDU / CBRN Threat Unit", inline=False)
embeds["lesion"].add_field(name="Age", value="44", inline=True)
embeds["lesion"].add_field(name="Height", value="1.74m / 5'9\"", inline=True)
embeds["lesion"].add_field(name="Weight", value="82kg / 181 lbs", inline=True)
embeds["lesion"].add_field(name="Date of birth", value="July 2", inline=True)
embeds["lesion"].add_field(name="Birthplace", value="Junk Bay (Tseung Kwan O), Hong Kong (British Hong Kong)", inline=True)
embeds["lesion"].add_field(name="Voice Actor", value="Albert Chung", inline=False)
embeds["lesion"].add_field(name="Primary Weapons", value="SIX12 SD / T-5 SMG", inline=True)
embeds["lesion"].add_field(name="Secondary Weapons", value="Q-929", inline=True)
embeds["lesion"].add_field(name="Gadget", value="Impact Grenade / Bulletproof Camera", inline=False)
embeds["lesion"].add_field(name="Ability", value="Gu", inline=True)
embeds["lesion"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["lesion"].set_author(name="Operator profile")
embeds["lesion"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/d2/R6S-Lesion.png/revision/latest/scale-to-width-down/158?cb=20170828194022")

#zofia
embeds["zofia"] = discord.Embed(
title="Zofia",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Zofia",
color=0x489391
)
embeds["zofia"].add_field(name="Name", value="Zofia Bosak", inline=False)
embeds["zofia"].add_field(name="Organization", value="GROM", inline=False)
embeds["zofia"].add_field(name="Age", value="36", inline=True)
embeds["zofia"].add_field(name="Height", value="1.79m / 5'10\"", inline=True)
embeds["zofia"].add_field(name="Weight", value="72kg / 159 lbs", inline=True)
embeds["zofia"].add_field(name="Date of birth", value="January 28", inline=True)
embeds["zofia"].add_field(name="Birthplace", value="Wrocław, Lower Silesia, Poland (Polish People's Republic)", inline=True)
embeds["zofia"].add_field(name="Voice Actor", value="Carolina Bartczak", inline=False)
embeds["zofia"].add_field(name="Primary Weapons", value="LMG-E / M762", inline=True)
embeds["zofia"].add_field(name="Secondary Weapons", value="RG15", inline=True)
embeds["zofia"].add_field(name="Gadget", value="Breach Charge / Claymore", inline=False)
embeds["zofia"].add_field(name="Ability", value="KS79 LIFELINE", inline=True)
embeds["zofia"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["zofia"].set_author(name="Operator profile")
embeds["zofia"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/f/fb/Zofia_icon.png/revision/latest/scale-to-width-down/96?cb=20171115182418")

#ela
embeds["ela"] = discord.Embed(
title="Ela",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Ela",
color=0x489391
)
embeds["ela"].add_field(name="Name", value="Elżbieta Bosak", inline=False)
embeds["ela"].add_field(name="Organization", value="GROM", inline=False)
embeds["ela"].add_field(name="Age", value="31", inline=True)
embeds["ela"].add_field(name="Height", value="1.73m / 5'8\"", inline=True)
embeds["ela"].add_field(name="Weight", value="68kg / 150 lbs", inline=True)
embeds["ela"].add_field(name="Date of birth", value="November 8", inline=True)
embeds["ela"].add_field(name="Birthplace", value="Wrocław, Lower Silesia, Poland (Polish People's Republic)", inline=True)
embeds["ela"].add_field(name="Voice Actor", value="Unkown", inline=False)
embeds["ela"].add_field(name="Primary Weapons", value="Scorpion EVO 3 A1 / FO-12", inline=True)
embeds["ela"].add_field(name="Secondary Weapons", value="RG15", inline=True)
embeds["ela"].add_field(name="Gadget", value="Barbed Wire / Deployable Shield", inline=False)
embeds["ela"].add_field(name="Ability", value="Grzmot Mine", inline=True)
embeds["ela"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["ela"].set_author(name="Operator profile")
embeds["ela"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/3/3f/Ela_icon.png/revision/latest/scale-to-width-down/128?cb=20170913223125")

#dokkaebi
embeds["dokkaebi"] = discord.Embed(
title="Dokkaebi",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Dokkaebi",
color=0xF5FAF8
)
embeds["dokkaebi"].add_field(name="Name", value="Grace Nam", inline=False)
embeds["dokkaebi"].add_field(name="Organization", value="707th SMB", inline=False)
embeds["dokkaebi"].add_field(name="Age", value="29", inline=True)
embeds["dokkaebi"].add_field(name="Height", value="1.69m / 5'2\"", inline=True)
embeds["dokkaebi"].add_field(name="Weight", value="62kg / 137 lbs", inline=True)
embeds["dokkaebi"].add_field(name="Date of birth", value="February 2", inline=True)
embeds["dokkaebi"].add_field(name="Birthplace", value="Seoul, South Korea", inline=True)
embeds["dokkaebi"].add_field(name="Voice Actor", value="Christine Lee", inline=False)
embeds["dokkaebi"].add_field(name="Primary Weapons", value="Mk 14 EBR / BOSG. 12.2", inline=True)
embeds["dokkaebi"].add_field(name="Secondary Weapons", value="GONNE-6 / SMG-12", inline=True)
embeds["dokkaebi"].add_field(name="Gadget", value="Smoke Grenade / Frag Grenade", inline=False)
embeds["dokkaebi"].add_field(name="Ability", value="Logic Bomb", inline=True)
embeds["dokkaebi"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["dokkaebi"].set_author(name="Operator profile")
embeds["dokkaebi"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/0/0c/Dokkaebi_icon.png/revision/latest/scale-to-width-down/160?cb=20171120222956")

#vigil
embeds["vigil"] = discord.Embed(
title="Vigil",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Vigil",
color=0xF5FAF8
)
embeds["vigil"].add_field(name="Name", value="Chul Kyung Hwa", inline=False)
embeds["vigil"].add_field(name="Organization", value="707th SMB / ROKN (Formerly)", inline=False)
embeds["vigil"].add_field(name="Age", value="34", inline=True)
embeds["vigil"].add_field(name="Height", value="1.73m / 5'8\"", inline=True)
embeds["vigil"].add_field(name="Weight", value="73kg / 161 lbs", inline=True)
embeds["vigil"].add_field(name="Date of birth", value="January 17", inline=True)
embeds["vigil"].add_field(name="Birthplace", value="North Korea", inline=True)
embeds["vigil"].add_field(name="Voice Actor", value="Anthony Shim", inline=False)
embeds["vigil"].add_field(name="Primary Weapons", value="K1A / BOSG.12.2", inline=True)
embeds["vigil"].add_field(name="Secondary Weapons", value="C75 Auto / SMG-12", inline=True)
embeds["vigil"].add_field(name="Gadget", value="Bulletproof Camera / Impact Grenade", inline=False)
embeds["vigil"].add_field(name="Ability", value="ERC-7 'Electronic Rendering Cloak'", inline=True)
embeds["vigil"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["vigil"].set_author(name="Operator profile")
embeds["vigil"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/1/1d/Vigil_icon.png/revision/latest/scale-to-width-down/160?cb=20171120223005")

#lion
embeds["lion"] = discord.Embed(
title="Lion",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/lion",
color=0xFEAD1B
)
embeds["lion"].add_field(name="Name", value="Olivier Flament", inline=False)
embeds["lion"].add_field(name="Organization", value="CBRN Threat Unit", inline=False)
embeds["lion"].add_field(name="Age", value="31", inline=True)
embeds["lion"].add_field(name="Height", value="1.85m / 6'1\"", inline=True)
embeds["lion"].add_field(name="Weight", value="87kg / 192 lbs", inline=True)
embeds["lion"].add_field(name="Date of birth", value="August 29", inline=True)
embeds["lion"].add_field(name="Birthplace", value="Toulouse, Occitanie, France", inline=True)
embeds["lion"].add_field(name="Voice Actor", value="Shawn Baichoo", inline=False)
embeds["lion"].add_field(name="Primary Weapons", value="V308 / 417 / SG-CQB", inline=True)
embeds["lion"].add_field(name="Secondary Weapons", value="GONNE-6 / LFP586", inline=True)
embeds["lion"].add_field(name="Gadget", value="Stun Grenade / Claymore", inline=False)
embeds["lion"].add_field(name="Ability", value="EE-ONE-D", inline=True)
embeds["lion"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["lion"].set_author(name="Operator profile")
embeds["lion"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/4/47/Lion.png/revision/latest/scale-to-width-down/160?cb=20180220011251")

#finka
embeds["finka"] = discord.Embed(
title="Finka",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Finka",
color=0xFEAD1B
)
embeds["finka"].add_field(name="Name", value="Lera Melnikova", inline=False)
embeds["finka"].add_field(name="Organization", value="CBRN Threat Unit", inline=False)
embeds["finka"].add_field(name="Age", value="27", inline=True)
embeds["finka"].add_field(name="Height", value="1.71m / 5'7\"", inline=True)
embeds["finka"].add_field(name="Weight", value="68kg / 149 lbs", inline=True)
embeds["finka"].add_field(name="Date of birth", value="June 7", inline=True)
embeds["finka"].add_field(name="Birthplace", value="Gomel, Belarus", inline=True)
embeds["finka"].add_field(name="Voice Actor", value="Becky Grimman", inline=False)
embeds["finka"].add_field(name="Primary Weapons", value="Spear .308 / 6P41 / SASG-12", inline=True)
embeds["finka"].add_field(name="Secondary Weapons", value="PMM / GONNE-6", inline=True)
embeds["finka"].add_field(name="Gadget", value="hard Breach Charge / Frag Grenade", inline=False)
embeds["finka"].add_field(name="Ability", value="Adrenal Surge", inline=True)
embeds["finka"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["finka"].set_author(name="Operator profile")
embeds["finka"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/de/Finka_icon.png/revision/latest/scale-to-width-down/160?cb=20180220011308")

#maestro
embeds["maestro"] = discord.Embed(
title="Maestro",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Maestro",
color=0x6A7332
)
embeds["maestro"].add_field(name="Name", value="Adriano Martello", inline=False)
embeds["maestro"].add_field(name="Organization", value="GIS", inline=False)
embeds["maestro"].add_field(name="Age", value="45", inline=True)
embeds["maestro"].add_field(name="Height", value="1.85m / 6'1\"", inline=True)
embeds["maestro"].add_field(name="Weight", value="87kg / 192 lbs", inline=True)
embeds["maestro"].add_field(name="Date of birth", value="April 13", inline=True)
embeds["maestro"].add_field(name="Birthplace", value="Rome, Italy", inline=True)
embeds["maestro"].add_field(name="Voice Actor", value="Phil Luzi", inline=False)
embeds["maestro"].add_field(name="Primary Weapons", value="ALDA 5.56 / ACS12", inline=True)
embeds["maestro"].add_field(name="Secondary Weapons", value="Bailiff 410 / Keratos .357", inline=True)
embeds["maestro"].add_field(name="Gadget", value="Barbed Wire / impact Grenade", inline=False)
embeds["maestro"].add_field(name="Ability", value="Evil Eye 'Compact Laser Emplacement (CLE-V)'", inline=True)
embeds["maestro"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["maestro"].set_author(name="Operator profile")
embeds["maestro"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/b/b7/Maestro_-_Icon.png/revision/latest/scale-to-width-down/310?cb=20180522220537")

#alibi
embeds["alibi"] = discord.Embed(
title="Alibi",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Alibi",
color=0x6A7332
)
embeds["alibi"].add_field(name="Name", value="Aria de Luca", inline=False)
embeds["alibi"].add_field(name="Organization", value="GIS", inline=False)
embeds["alibi"].add_field(name="Age", value="37", inline=True)
embeds["alibi"].add_field(name="Height", value="1.71m / 5'7\"", inline=True)
embeds["alibi"].add_field(name="Weight", value="63kg / 139 lbs", inline=True)
embeds["alibi"].add_field(name="Date of birth", value="December 15", inline=True)
embeds["alibi"].add_field(name="Birthplace", value="Tripoli, Libya (Libyan Arab Jamahiriya)", inline=True)
embeds["alibi"].add_field(name="Voice Actor", value="Tara Nicodemo", inline=False)
embeds["alibi"].add_field(name="Primary Weapons", value="Mx4 Storm / ACS12", inline=True)
embeds["alibi"].add_field(name="Secondary Weapons", value="Bailiff 410 / Keratos .357", inline=True)
embeds["alibi"].add_field(name="Gadget", value="Deployable Shield / impact Grenade", inline=False)
embeds["alibi"].add_field(name="Ability", value="Prisma", inline=True)
embeds["alibi"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["alibi"].set_author(name="Operator profile")
embeds["alibi"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/d/d7/Alibi_-_Icon.png/revision/latest/scale-to-width-down/310?cb=20180522220413")

#maverick
embeds["maverick"] = discord.Embed(
title="Maverick",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Maverick",
color=0x6F8290
)
embeds["maverick"].add_field(name="Name", value="Erik Thorn", inline=False)
embeds["maverick"].add_field(name="Organization", value="GSUTR", inline=False)
embeds["maverick"].add_field(name="Age", value="36", inline=True)
embeds["maverick"].add_field(name="Height", value="1.80m / 5'11\"", inline=True)
embeds["maverick"].add_field(name="Weight", value="82kg / 181 lbs", inline=True)
embeds["maverick"].add_field(name="Date of birth", value="April 20", inline=True)
embeds["maverick"].add_field(name="Birthplace", value="Boston, Massachusetts", inline=True)
embeds["maverick"].add_field(name="Voice Actor", value="Alden Adair", inline=False)
embeds["maverick"].add_field(name="Primary Weapons", value="AR-15.50 / M4", inline=True)
embeds["maverick"].add_field(name="Secondary Weapons", value="1911 TACOPS", inline=True)
embeds["maverick"].add_field(name="Gadget", value="Claymore / Frag Grenades", inline=False)
embeds["maverick"].add_field(name="Ability", value="Breaching Torch 'Exothermic-S \"Suri\" Torch'", inline=True)
embeds["maverick"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["maverick"].set_author(name="Operator profile")
embeds["maverick"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/c/c8/Maverick_logo_HD.png/revision/latest/scale-to-width-down/310?cb=20190524235156")

#clash
embeds["clash"] = discord.Embed(
title="Clash",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Clash",
color=0x6F8290
)
embeds["clash"].add_field(name="Name", value="Morowa Evans", inline=False)
embeds["clash"].add_field(name="Organization", value="GSUTR", inline=False)
embeds["clash"].add_field(name="Age", value="35", inline=True)
embeds["clash"].add_field(name="Height", value="1.79m / 5'10\"", inline=True)
embeds["clash"].add_field(name="Weight", value="73kg / 160 lbs", inline=True)
embeds["clash"].add_field(name="Date of birth", value="June 7", inline=True)
embeds["clash"].add_field(name="Birthplace", value="London, England", inline=True)
embeds["clash"].add_field(name="Voice Actor", value="Sophia Walker", inline=False)
embeds["clash"].add_field(name="Primary Weapons", value="CCE Shield", inline=True)
embeds["clash"].add_field(name="Secondary Weapons", value="P-10C / SPSMG9", inline=True)
embeds["clash"].add_field(name="Gadget", value="impact Grenades / Barbed Wire", inline=False)
embeds["clash"].add_field(name="Ability", value="CCE Shield 'Crowd Control Electro Shield'", inline=True)
embeds["clash"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["clash"].set_author(name="Operator profile")
embeds["clash"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/5/5c/Clash_logo_HD_-_Copy2.png/revision/latest/scale-to-width-down/310?cb=20190525001600")

#nomad
embeds["nomad"] = discord.Embed(
title="Nomad",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Nomad",
color=0xAE8656
)
embeds["nomad"].add_field(name="Name", value="Sanaa El Maktoub", inline=False)
embeds["nomad"].add_field(name="Organization", value="GIGR", inline=False)
embeds["nomad"].add_field(name="Age", value="39", inline=True)
embeds["nomad"].add_field(name="Height", value="1.71m / 5'7\"", inline=True)
embeds["nomad"].add_field(name="Weight", value="63kg / 139 lbs", inline=True)
embeds["nomad"].add_field(name="Date of birth", value="July 27", inline=True)
embeds["nomad"].add_field(name="Birthplace", value="Marrakesh, Morocco", inline=True)
embeds["nomad"].add_field(name="Voice Actor", value="Rasha Zamamiri", inline=False)
embeds["nomad"].add_field(name="Primary Weapons", value="AK-74M / ARX200", inline=True)
embeds["nomad"].add_field(name="Secondary Weapons", value=".44 Mag Semi-Auto / PRB92", inline=True)
embeds["nomad"].add_field(name="Gadget", value="Breach Charge / Stun Grenade", inline=False)
embeds["nomad"].add_field(name="Ability", value="Airjab Launcher", inline=True)
embeds["nomad"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["nomad"].set_author(name="Operator profile")
embeds["nomad"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/8d/R6S-Nomad.png/revision/latest/scale-to-width-down/154?cb=20181119191959")

#kaid
embeds["kaid"] = discord.Embed(
title="Kaid",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Kaid",
color=0xAE8656
)
embeds["kaid"].add_field(name="Name", value="Jalal El Fassi", inline=False)
embeds["kaid"].add_field(name="Organization", value="GIGR", inline=False)
embeds["kaid"].add_field(name="Age", value="58", inline=True)
embeds["kaid"].add_field(name="Height", value="1.95m / 6'5\"", inline=True)
embeds["kaid"].add_field(name="Weight", value="98kg / 216 lbs", inline=True)
embeds["kaid"].add_field(name="Date of birth", value="June 26", inline=True)
embeds["kaid"].add_field(name="Birthplace", value="Aroumd, Morocco", inline=True)
embeds["kaid"].add_field(name="Voice Actor", value="Peter Ganim", inline=False)
embeds["kaid"].add_field(name="Primary Weapons", value="AUG A3 / TCSG12", inline=True)
embeds["kaid"].add_field(name="Secondary Weapons", value=".44 Mag Semi-Auto / LFP586", inline=True)
embeds["kaid"].add_field(name="Gadget", value="Barbed Wire / Nitro Cell", inline=False)
embeds["kaid"].add_field(name="Ability", value="Electroclaw 'Rtila'", inline=True)
embeds["kaid"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["kaid"].set_author(name="Operator profile")
embeds["kaid"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/0/0b/R6S-Kaid.png/revision/latest/scale-to-width-down/154?cb=20181119192012")

#gridlock
embeds["gridlock"] = discord.Embed(
title="Gridlock",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Gridlock",
color=0xC00753
)
embeds["gridlock"].add_field(name="Name", value="Tori Tallyo Fairous", inline=False)
embeds["gridlock"].add_field(name="Organization", value="SASR", inline=False)
embeds["gridlock"].add_field(name="Age", value="36", inline=True)
embeds["gridlock"].add_field(name="Height", value="1.77m / 5'10\"", inline=True)
embeds["gridlock"].add_field(name="Weight", value="102kg / 225 lbs", inline=True)
embeds["gridlock"].add_field(name="Date of birth", value="August 5", inline=True)
embeds["gridlock"].add_field(name="Birthplace", value="Longreach, Central Queensland, Australia", inline=True)
embeds["gridlock"].add_field(name="Voice Actor", value="Rhona Rees", inline=False)
embeds["gridlock"].add_field(name="Primary Weapons", value="F90 / M249 SAW", inline=True)
embeds["gridlock"].add_field(name="Secondary Weapons", value="Super Shorty / GONNE-6", inline=True)
embeds["gridlock"].add_field(name="Gadget", value="Smoke Grenade / Breach Charge", inline=False)
embeds["gridlock"].add_field(name="Ability", value="Trax Stingers", inline=True)
embeds["gridlock"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["gridlock"].set_author(name="Operator profile")
embeds["gridlock"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/6/61/R6S-Gridlock.png/revision/latest/scale-to-width-down/154?cb=20190218194313")

#jagersmom
embeds["jagersmom"] = discord.Embed(
title="Gridlock",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Gridlock",
color=0xC00753
)
embeds["jagersmom"].add_field(name="Name", value="Tori Tallyo Fairous", inline=False)
embeds["jagersmom"].add_field(name="Organization", value="SASR", inline=False)
embeds["jagersmom"].add_field(name="Age", value="36", inline=True)
embeds["jagersmom"].add_field(name="Height", value="1.77m / 5'10\"", inline=True)
embeds["jagersmom"].add_field(name="Weight", value="102kg / 225 lbs", inline=True)
embeds["jagersmom"].add_field(name="Date of birth", value="August 5", inline=True)
embeds["jagersmom"].add_field(name="Birthplace", value="Longreach, Central Queensland, Australia", inline=True)
embeds["jagersmom"].add_field(name="Voice Actor", value="Rhona Rees", inline=False)
embeds["jagersmom"].add_field(name="Primary Weapons", value="F90 / M249 SAW", inline=True)
embeds["jagersmom"].add_field(name="Secondary Weapons", value="Super Shorty / GONNE-6", inline=True)
embeds["jagersmom"].add_field(name="Gadget", value="Smoke Grenade / Breach Charge", inline=False)
embeds["jagersmom"].add_field(name="Ability", value="Trax Stingers", inline=True)
embeds["jagersmom"].add_field(name="Armor / Speed", value="●●● / ●○○", inline=False)
embeds["jagersmom"].set_author(name="Operator profile")
embeds["jagersmom"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/6/61/R6S-Gridlock.png/revision/latest/scale-to-width-down/154?cb=20190218194313")

#mozzie
embeds["mozzie"] = discord.Embed(
title="Mozzie",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Mozzie",
color=0xC00753
)
embeds["mozzie"].add_field(name="Name", value="Max Goose", inline=False)
embeds["mozzie"].add_field(name="Organization", value="SASR", inline=False)
embeds["mozzie"].add_field(name="Age", value="35", inline=True)
embeds["mozzie"].add_field(name="Height", value="1.62m / 5'4\"", inline=True)
embeds["mozzie"].add_field(name="Weight", value="64kg / 141 lbs", inline=True)
embeds["mozzie"].add_field(name="Date of birth", value="February 15", inline=True)
embeds["mozzie"].add_field(name="Birthplace", value="Portland, Victoria, Australia", inline=True)
embeds["mozzie"].add_field(name="Voice Actor", value="Martin Copping", inline=False)
embeds["mozzie"].add_field(name="Primary Weapons", value="Commando 9 / P10 RONI", inline=True)
embeds["mozzie"].add_field(name="Secondary Weapons", value="SDP 9mm", inline=True)
embeds["mozzie"].add_field(name="Gadget", value="Barbed Wire / Nitro Cell", inline=False)
embeds["mozzie"].add_field(name="Ability", value="Pest Launcher", inline=True)
embeds["mozzie"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["mozzie"].set_author(name="Operator profile")
embeds["mozzie"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/3/3a/R6S-Mozzie.png/revision/latest/scale-to-width-down/154?cb=20190218194326")

#nokk
embeds["nokk"] = discord.Embed(
title="Nokk",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Nokk",
color=0x2C3D8E
)
embeds["nokk"].add_field(name="Name", value="`[REDACTED]`", inline=False)
embeds["nokk"].add_field(name="Organization", value="Jaeger Corps", inline=False)
embeds["nokk"].add_field(name="Age", value="`[REDACTED]`", inline=True)
embeds["nokk"].add_field(name="Height", value="`[REDACTED]`", inline=True)
embeds["nokk"].add_field(name="Weight", value="`[REDACTED]`", inline=True)
embeds["nokk"].add_field(name="Date of birth", value="`[REDACTED]`", inline=True)
embeds["nokk"].add_field(name="Birthplace", value="`[REDACTED]`", inline=True)
embeds["nokk"].add_field(name="Voice Actor", value="Julie Lynn Mortensen", inline=False)
embeds["nokk"].add_field(name="Primary Weapons", value="FMG-9 / SIX12 SD", inline=True)
embeds["nokk"].add_field(name="Secondary Weapons", value="5.7 USG / D-50", inline=True)
embeds["nokk"].add_field(name="Gadget", value="Frag Grenade / Hard Breach Charge", inline=False)
embeds["nokk"].add_field(name="Ability", value="HEL Presence Reduction", inline=True)
embeds["nokk"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["nokk"].set_author(name="Operator profile")
embeds["nokk"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/2/2e/Nokk.png/revision/latest/scale-to-width-down/125?cb=20190523003359")

#warden
embeds["warden"] = discord.Embed(
title="Warden",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Warden",
color=0x2C3D8E
)
embeds["warden"].add_field(name="Name", value="Collinn McKinley", inline=False)
embeds["warden"].add_field(name="Organization", value="Secret Service", inline=False)
embeds["warden"].add_field(name="Age", value="48", inline=True)
embeds["warden"].add_field(name="Height", value="1.83m / 6'0\"", inline=True)
embeds["warden"].add_field(name="Weight", value="80kg / 176 lbs", inline=True)
embeds["warden"].add_field(name="Date of birth", value="March 18", inline=True)
embeds["warden"].add_field(name="Birthplace", value="Louisville, Kentucky", inline=True)
embeds["warden"].add_field(name="Voice Actor", value="Mark Deklin", inline=False)
embeds["warden"].add_field(name="Primary Weapons", value="M590A1 / MPX", inline=True)
embeds["warden"].add_field(name="Secondary Weapons", value="P10-C / SMG-12", inline=True)
embeds["warden"].add_field(name="Gadget", value="Nitro Cell / Deployable Shield", inline=False)
embeds["warden"].add_field(name="Ability", value="Glance Smart Glasses", inline=True)
embeds["warden"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["warden"].set_author(name="Operator profile")
embeds["warden"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/a5/Warden.png/revision/latest/scale-to-width-down/100?cb=20190701101127")

#amaru
embeds["amaru"] = discord.Embed(
title="Amaru",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Amaru",
color=0x13590B
)
embeds["amaru"].add_field(name="Name", value="Azucena Rocío Quispe", inline=False)
embeds["amaru"].add_field(name="Organization", value="APCA", inline=False)
embeds["amaru"].add_field(name="Age", value="48", inline=True)
embeds["amaru"].add_field(name="Height", value="1.89m / 6'2\"", inline=True)
embeds["amaru"].add_field(name="Weight", value="84kg / 185 lbs", inline=True)
embeds["amaru"].add_field(name="Date of birth", value="May 6", inline=True)
embeds["amaru"].add_field(name="Birthplace", value="Cojata, Puno, Peru", inline=True)
embeds["amaru"].add_field(name="Voice Actor", value="Presciliana Esparolini", inline=False)
embeds["amaru"].add_field(name="Primary Weapons", value="G8A1 / SuperNova", inline=True)
embeds["amaru"].add_field(name="Secondary Weapons", value="ITA12S / GONNE-6", inline=True)
embeds["amaru"].add_field(name="Gadget", value="Hard Breach Charge / Stun Grenade", inline=False)
embeds["amaru"].add_field(name="Ability", value="Garra Hook", inline=True)
embeds["amaru"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["amaru"].set_author(name="Operator profile")
embeds["amaru"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/9/94/Amaru_Icon.png/revision/latest/scale-to-width-down/190?cb=20190820020748")

#goyo
embeds["goyo"] = discord.Embed(
title="Goyo",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Goyo",
color=0x13590B
)
embeds["goyo"].add_field(name="Name", value="César Ruiz Hernández", inline=False)
embeds["goyo"].add_field(name="Organization", value="FES", inline=False)
embeds["goyo"].add_field(name="Age", value="31", inline=True)
embeds["goyo"].add_field(name="Height", value="1.71m / 5'7\"", inline=True)
embeds["goyo"].add_field(name="Weight", value="83kg / 183 lbs", inline=True)
embeds["goyo"].add_field(name="Date of birth", value="June 10", inline=True)
embeds["goyo"].add_field(name="Birthplace", value="Culiacán Rosales, Sinaloa, Mexico", inline=True)
embeds["goyo"].add_field(name="Voice Actor", value="Victor Andres Turgeon-Trelles", inline=False)
embeds["goyo"].add_field(name="Primary Weapons", value="Vector .45 ACP / TCSG12", inline=True)
embeds["goyo"].add_field(name="Secondary Weapons", value="P229", inline=True)
embeds["goyo"].add_field(name="Gadget", value="Nitro Cell / Proximity Alarm", inline=False)
embeds["goyo"].add_field(name="Ability", value="Volcán Shield", inline=True)
embeds["goyo"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["goyo"].set_author(name="Operator profile")
embeds["goyo"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/9/9f/Goyo_Icon.png/revision/latest/scale-to-width-down/190?cb=20190820020749")

#kali
embeds["kali"] = discord.Embed(
title="Kali",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/kali",
color=0x23C2CE
)
embeds["kali"].add_field(name="Name", value="Jaimini Kalimohan Shah", inline=False)
embeds["kali"].add_field(name="Organization", value="NIGHTHAVEN", inline=False)
embeds["kali"].add_field(name="Age", value="34", inline=True)
embeds["kali"].add_field(name="Height", value="1.70m / 5'7\"", inline=True)
embeds["kali"].add_field(name="Weight", value="67kg / 148 lbs", inline=True)
embeds["kali"].add_field(name="Date of birth", value="August 21", inline=True)
embeds["kali"].add_field(name="Birthplace", value="Amreli, Gujarat, India", inline=True)
embeds["kali"].add_field(name="Voice Actor", value="Yasmine Aker", inline=False)
embeds["kali"].add_field(name="Primary Weapons", value="CSRX 300", inline=True)
embeds["kali"].add_field(name="Secondary Weapons", value="C75 Auto / SPSMG9", inline=True)
embeds["kali"].add_field(name="Gadget", value="Breach Charge / Claymore", inline=False)
embeds["kali"].add_field(name="Ability", value="LV Explosive Lance", inline=True)
embeds["kali"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["kali"].set_author(name="Operator profile")
embeds["kali"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/0/06/Kali_Icon_2.png/revision/latest/scale-to-width-down/100?cb=20191111224152")

#wamai
embeds["wamai"] = discord.Embed(
title="Wamai",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Wamai",
color=0x23C2CE
)
embeds["wamai"].add_field(name="Name", value="Ngũgĩ Muchoki Furaha", inline=False)
embeds["wamai"].add_field(name="Organization", value="NIGHTHAVEN", inline=False)
embeds["wamai"].add_field(name="Age", value="28", inline=True)
embeds["wamai"].add_field(name="Height", value="1.87m / 6'2\"", inline=True)
embeds["wamai"].add_field(name="Weight", value="83kg / 183 lbs", inline=True)
embeds["wamai"].add_field(name="Date of birth", value="June 1", inline=True)
embeds["wamai"].add_field(name="Birthplace", value="Lamu, Kenya", inline=True)
embeds["wamai"].add_field(name="Voice Actor", value="Ike Amadi", inline=False)
embeds["wamai"].add_field(name="Primary Weapons", value="AUG A2 / MP5K", inline=True)
embeds["wamai"].add_field(name="Secondary Weapons", value="Keratos .357 / P12", inline=True)
embeds["wamai"].add_field(name="Gadget", value="Proximity Alarm / Impact Grenade", inline=False)
embeds["wamai"].add_field(name="Ability", value="Mag-NET", inline=True)
embeds["wamai"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["wamai"].set_author(name="Operator profile")
embeds["wamai"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/c/cc/Wamai_Icon_2.png/revision/latest/scale-to-width-down/100?cb=20191111223721")

#iana
embeds["iana"] = discord.Embed(
title="Iana",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Iana",
color=0x926996
)
embeds["iana"].add_field(name="Name", value="Nienke Meijer", inline=False)
embeds["iana"].add_field(name="Organization", value="REU", inline=False)
embeds["iana"].add_field(name="Age", value="35", inline=True)
embeds["iana"].add_field(name="Height", value="1.75m / 5'2\"", inline=True)
embeds["iana"].add_field(name="Weight", value="56kg / 124 lbs", inline=True)
embeds["iana"].add_field(name="Date of birth", value="August 27", inline=True)
embeds["iana"].add_field(name="Birthplace", value="Katwijk, the Netherlands", inline=True)
embeds["iana"].add_field(name="Voice Actor", value="Clare McConnell", inline=False)
embeds["iana"].add_field(name="Primary Weapons", value="G36C / ARX200", inline=True)
embeds["iana"].add_field(name="Secondary Weapons", value="Mk1 9mm / GONNE-6", inline=True)
embeds["iana"].add_field(name="Gadget", value="Frag Grenade / Stun Grenade", inline=False)
embeds["iana"].add_field(name="Ability", value="Gemini Replicator", inline=True)
embeds["iana"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["iana"].set_author(name="Operator profile")
embeds["iana"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/e/e1/Iana_Icon.png/revision/latest/scale-to-width-down/100?cb=20200311062422")

#oryx
embeds["oryx"] = discord.Embed(
title="Oryx",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Oryx",
color=0x926996
)
embeds["oryx"].add_field(name="Name", value="Saif Al Hadid", inline=False)
embeds["oryx"].add_field(name="Organization", value="GIGR", inline=False)
embeds["oryx"].add_field(name="Age", value="45", inline=True)
embeds["oryx"].add_field(name="Height", value="1.95m / 6'5\"", inline=True)
embeds["oryx"].add_field(name="Weight", value="130kg / 287 lbs", inline=True)
embeds["oryx"].add_field(name="Date of birth", value="July 3", inline=True)
embeds["oryx"].add_field(name="Birthplace", value="Azraq, Zarqa, Jordan", inline=True)
embeds["oryx"].add_field(name="Voice Actor", value="JB Blanc", inline=False)
embeds["oryx"].add_field(name="Primary Weapons", value="T-5 SMG / SPAS-15", inline=True)
embeds["oryx"].add_field(name="Secondary Weapons", value="Bailiff 410 / USP40", inline=True)
embeds["oryx"].add_field(name="Gadget", value="Proximity Alarm / Barbed Wire", inline=False)
embeds["oryx"].add_field(name="Ability", value="Remah Dash", inline=True)
embeds["oryx"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["oryx"].set_author(name="Operator profile")
embeds["oryx"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/8/89/Oryx_Icon.png/revision/latest/scale-to-width-down/100?cb=20200311062523")

#ace
embeds["ace"] = discord.Embed(
title="Ace",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Ace",
color=0x317F8B
)
embeds["ace"].add_field(name="Name", value="Håvard Haugland", inline=False)
embeds["ace"].add_field(name="Organization", value="NIGHTHAVEN", inline=False)
embeds["ace"].add_field(name="Age", value="33", inline=True)
embeds["ace"].add_field(name="Height", value="1.87m / 6'1\"", inline=True)
embeds["ace"].add_field(name="Weight", value="75kg / 156 lbs", inline=True)
embeds["ace"].add_field(name="Date of birth", value="March 15", inline=True)
embeds["ace"].add_field(name="Birthplace", value="Lærdalsøyri, Vestland, Norway", inline=True)
embeds["ace"].add_field(name="Voice Actor", value="Kyle Gatehouse", inline=False)
embeds["ace"].add_field(name="Primary Weapons", value="AK-12 / M1014", inline=True)
embeds["ace"].add_field(name="Secondary Weapons", value="P9", inline=True)
embeds["ace"].add_field(name="Gadget", value="Breach Charge / Smoke Grenade", inline=False)
embeds["ace"].add_field(name="Ability", value="S.E.L.M.A. AQUA BREACHER", inline=True)
embeds["ace"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["ace"].set_author(name="Operator profile")
embeds["ace"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/a0/Ace_Icon_2.png/revision/latest/scale-to-width-down/96?cb=20200519202822")

#melusi
embeds["melusi"] = discord.Embed(
title="Melusi",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Melusi",
color=0x317F8B
)
embeds["melusi"].add_field(name="Name", value="Thandiwe Ndlovu", inline=False)
embeds["melusi"].add_field(name="Organization", value="Inkaba Task Force", inline=False)
embeds["melusi"].add_field(name="Age", value="32", inline=True)
embeds["melusi"].add_field(name="Height", value="1.72m / 5'8\"", inline=True)
embeds["melusi"].add_field(name="Weight", value="68kg / 150 lbs", inline=True)
embeds["melusi"].add_field(name="Date of birth", value="June 16", inline=True)
embeds["melusi"].add_field(name="Birthplace", value="Louwsburg, KwaZulu-Natal, South Africa", inline=True)
embeds["melusi"].add_field(name="Voice Actor", value="Sibongile Mlambo", inline=False)
embeds["melusi"].add_field(name="Primary Weapons", value="MP5 / Super 90", inline=True)
embeds["melusi"].add_field(name="Secondary Weapons", value="RG15", inline=True)
embeds["melusi"].add_field(name="Gadget", value="Impact Grenade / Nitro Cell", inline=False)
embeds["melusi"].add_field(name="Ability", value="Banshee Sonic Defense", inline=True)
embeds["melusi"].add_field(name="Armor / Speed", value="●○○ / ●●●", inline=False)
embeds["melusi"].set_author(name="Operator profile")
embeds["melusi"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/b/b2/Melusi_Icon_2.png/revision/latest/scale-to-width-down/96?cb=20200519202939")

#zero
embeds["zero"] = discord.Embed(
title="Zero",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Zero",
color=0x6DA344
)
embeds["zero"].add_field(name="Name", value="Samuel Leo Fisher", inline=False)
embeds["zero"].add_field(name="Organization", value="ROS", inline=False)
embeds["zero"].add_field(name="Age", value="63", inline=True)
embeds["zero"].add_field(name="Height", value="1.78m / 5'10\"", inline=True)
embeds["zero"].add_field(name="Weight", value="77kg / 170 lbs", inline=True)
embeds["zero"].add_field(name="Date of birth", value="August 8", inline=True)
embeds["zero"].add_field(name="Birthplace", value="Baltimore, Maryland", inline=True)
embeds["zero"].add_field(name="Voice Actor", value="Jeff Teravainen", inline=False)
embeds["zero"].add_field(name="Primary Weapons", value="SC3000K / MP7", inline=True)
embeds["zero"].add_field(name="Secondary Weapons", value="5.7 USG / GONNE-6", inline=True)
embeds["zero"].add_field(name="Gadget", value="Claymore / Hard Breach Charge", inline=False)
embeds["zero"].add_field(name="Ability", value="ARGUS LAUNCHER", inline=True)
embeds["zero"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["zero"].set_author(name="Operator profile")
embeds["zero"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/7/7b/Zero_Icon.png/revision/latest/scale-to-width-down/200?cb=20200822022315")

#aruni
embeds["aruni"] = discord.Embed(
title="Aruni",
description="Defender",
url="https://rainbowsix.fandom.com/wiki/Aruni",
color=0x8D2B03
)
embeds["aruni"].add_field(name="Name", value="Apha Tawanroong", inline=False)
embeds["aruni"].add_field(name="Organization", value="NIGHTHAVEN", inline=False)
embeds["aruni"].add_field(name="Age", value="42", inline=True)
embeds["aruni"].add_field(name="Height", value="1.60m / 5'3\"", inline=True)
embeds["aruni"].add_field(name="Weight", value="58kg / 127 lbs", inline=True)
embeds["aruni"].add_field(name="Date of birth", value="August 9", inline=True)
embeds["aruni"].add_field(name="Birthplace", value="Ta Phyraya, Sa Kaeo, Thailand", inline=True)
embeds["aruni"].add_field(name="Voice Actor", value="Sumalee Montano", inline=False)
embeds["aruni"].add_field(name="Primary Weapons", value="P10 RONI / Mk14 EBR", inline=True)
embeds["aruni"].add_field(name="Secondary Weapons", value="PRB92", inline=True)
embeds["aruni"].add_field(name="Gadget", value="Barbed Wire / BulletProof Camera", inline=False)
embeds["aruni"].add_field(name="Ability", value="SURYA LASER GATE", inline=True)
embeds["aruni"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["aruni"].set_author(name="Operator profile")
embeds["aruni"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/e/ed/Aruni_Badge.png/revision/latest/scale-to-width-down/310?cb=20201111190010")

#flores
embeds["flores"] = discord.Embed(
title="Flores",
description="Attacker",
url="https://rainbowsix.fandom.com/wiki/Flores",
color=0x7B090B
)
embeds["flores"].add_field(name="Name", value="Santiago Lucero", inline=False)
embeds["flores"].add_field(name="Organization", value="FBI", inline=False)
embeds["flores"].add_field(name="Age", value="38", inline=True)
embeds["flores"].add_field(name="Height", value="1.81m / 5'11\"", inline=True)
embeds["flores"].add_field(name="Weight", value="72kg / 158 lbs", inline=True)
embeds["flores"].add_field(name="Date of birth", value="October 2", inline=True)
embeds["flores"].add_field(name="Birthplace", value="Buenos Aires, Argentina (El Proceso)", inline=True)
embeds["flores"].add_field(name="Voice Actor", value="Jason Canela", inline=False)
embeds["flores"].add_field(name="Primary Weapons", value="AR33 / SR-25", inline=True)
embeds["flores"].add_field(name="Secondary Weapons", value="GSh-18", inline=True)
embeds["flores"].add_field(name="Gadget", value="Stun Grenade / Claymore", inline=False)
embeds["flores"].add_field(name="Ability", value="RCE-Ratero Charge", inline=True)
embeds["flores"].add_field(name="Armor / Speed", value="●●○ / ●●○", inline=False)
embeds["flores"].set_author(name="Operator profile")
embeds["flores"].set_thumbnail(url="https://static.wikia.nocookie.net/rainbowsix/images/a/a9/Flores_icon.png/revision/latest/scale-to-width-down/200?cb=20210222210203")