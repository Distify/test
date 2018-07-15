import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix='-',case_insensitive=True)
bot.remove_command('help')

print(discord.__version__)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")
    print(f"ID: {bot.user.id}")
    print(f"Discriminator: {bot.user.discriminator}")
    await bot.change_presence(game=discord.Game(type=0,name='DM to message staff'))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.id == '465739177502310400':
        return
    if message.channel.is_private:
        report = f"""
**Report From:** `{message.author.name}#{message.author.discriminator}`
```{message.content}```
**Reply ID:** `{message.author.id}`"""
        await bot.send_message(discord.Object(id='468168421343756319'), embed = discord.Embed(title=' ',description=report,color=0xff7777))
        await bot.send_message(message.author, "Thank you for your message! Our mod team will reply to you as soon as possible.")

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
	fullname = f'{user.name}#{user.discriminator}'
	userinfo = """**Â» User Information**
ID: {0}
Profile: {1}
Created: {2}

**Â» Member information**
Joined: {3}
Rank: {4}

**Â» Status**
Current status: {5}""".format(user.id, user.mention, user.created_at, user.joined_at, user.top_role, user.status)
	embed = discord.Embed(title=' ',description=userinfo, color=0xff7777)
	embed.set_author(name=fullname, icon_url=user.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)

@userinfo.error
async def kickHandler(error, ctx):
    if isinstance(error,commands.UserInputError):
        usage = """
**Usage:** `-userinfo <user>`
**Cooldown:** `1 second`
**Example:** `-userinfo @scarab`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Userinfo',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def uid(ctx):
    embed = discord.Embed(title=' ',description=f'{ctx.message.author.mention}, your ID is `{ctx.message.author.id}`')
    embed.set_author(name=f'{ctx.message.author.name}#{ctx.message.author.discriminator}', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=['russian','roulette'])
async def russianroulette(ctx):
    lists = ["You pulled the trigger and nothing happened :gun:","You pulled the trigger and nothing happened :gun:","You pulled the trigger and nothing happened :gun:","You pulled the trigger and nothing happened :gun:","You pulled the trigger and nothing happened :gun:","You pull the trigger and get a bullet shot into your head :boom::gun:"]
    await bot.say(random.choice(lists))

@bot.command(pass_context=True)
async def subscribe(ctx):
    try:
        role = discord.utils.get(ctx.message.server.roles,name='Subscribers')
        await bot.add_roles(ctx.message.author, role)
        await bot.add_reaction(ctx.message, 'âœ…')
    except:
        await bot.add_reaction(ctx.message, 'âŒ')

@bot.command(pass_context=True)
async def unsubscribe(ctx):
    try:
        role = discord.utils.get(ctx.message.server.roles, name='Subscribers')
        await bot.remove_roles(ctx.message.author, role)
        await bot.add_reaction(ctx.message, 'âœ…')
    except:
        await bot.add_reaction(ctx.message, 'âŒ')

@bot.command(pass_context=True)
async def help(ctx):
    helpmessage1 = """
`Here is a list of commands available to non moderators`
**userinfo** - Sends info about a user
**uid** - Sends your user ID
**subscribe** - Gives you the subscribers role
**unsubscribe** - Removes the subscribers role
**help** - Sends this message
**add** - Adds two numbers
**russianroulette** - You have a 1 in 6 chance of dying. Will you take that chance?
âš  **Note: these are the commands available to non staff. Staff members have more commands.**"""
    helpmessage2 = """
`Here is a list of commands available to moderators and members`
**userinfo** - Sends info about a user
**uid** - Sends your user ID
**subscribe** - Gives you the subscribers role
**unsubscribe** - Removes the subscribers role
**help** - Sends this message
**add** - Adds two numbers
**russianroulette** - You have a 1 in 6 chance of dying. Will you take that chance?
**ban** - Bans a user
**kick** - Kicks a user
**unban** - unbans a user
**say** - sends a string
**embed** - embeds a string
**mute** - Mutes a member
**setnick** - Changes a users nickname
**modmail** - Responds to someones mod mail
**addrole** - Gives a user a role (Head Admin and Developer only)
**warn** - Gives a user a warning
âš  **Note: these are the commands available to staff and members. Developers have more commands**"""
    helpmessage3 = """
`Here is a list of commands available to AppBot Developers`
**userinfo** - Sends info about a user
**uid** - Sends your user ID
**subscribe** - Gives you the subscribers role
**unsubscribe** - Removes the subscribers role
**help** - Sends this message
**add** - Adds two numbers
**russianroulette** - You have a 1 in 6 chance of dying. Will you take that chance?
**ban** - Bans a user
**kick** - Kicks a user
**unban** - unbans a user
**say** - sends a string
**embed** - embeds a string
**mute** - Mutes a member
**setnick** - Changes a users nickname
**modmail** - Responds to someones mod mail
**addrole** - Gives a user a role (Head Admin and Developer only)
**warn** - Gives a user a warning
**changeuser** - Changes the bots username
**changestatus** - Changes the bots status
**vote** - Sends a poll embed
**table** - Secret c;
**shutdown** - Shuts the bot down
**eval** - This is self explanatory, unstable, and temporarily disabled"""
    if ctx.message.author.id == '370777160216215553' or ctx.message.author.id == '394402252498010113':
        embed = discord.Embed(title=' ',description=helpmessage3,color=0xff7777)
        embed.set_author(name='Dave Developer Commands',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    elif ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title=' ',description=helpmessage2,color=0xff7777)
        embed.set_author(name='Dave Staff Commands',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title=' ',description=helpmessage1,color=0xff7777)
        embed.set_author(name='Dave Commands',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member, *, reason):
    if user.id == '370777160216215553' or user.id =='394402252498010113':
        await bot.reply("why are you even trying to ban a developer?")
    elif user.server_permissions.manage_messages:
        await bot.say(f"<:DaveNo:466458146966339585> I can't ban **{user.name}#{user.discriminator}** because they are a server mod/admin")
    elif ctx.message.author.server_permissions.manage_messages:
        infraction = f"""
**BANNED**
**User:** <@{user.id}>
**User ID:** {user.id}
**Reason:** {reason}"""
        await bot.ban(user)
        await bot.say(f"**{ctx.message.author.name}** :hammer: banned **{user.name}#{user.discriminator}** for `{reason}`")
        embed = discord.Embed(title=' ',description=infraction,color=0x9e0d0d)
        embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}#{ctx.message.author.discriminator} (STAFF)',icon_url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='468168300325502996'), embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `ban` command.")

@ban.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-ban <user> [reason]`
**Cooldown:** `3 seconds`
**Example:** `-ban @scarab annoying`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Ban',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `ban` command.")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member, *, reason):
    if user.server_permissions.manage_messages:
        await bot.say(f"<:DaveNo:466458146966339585> I can't kick **{user.name}#{user.discriminator}** because they are a server mod/admin")
    elif ctx.message.author.server_permissions.manage_messages:
        infraction = f"""
**KICKED**
**User:** <@{user.id}>
**User ID:** {user.id}
**Reason:** {reason}"""
        await bot.kick(user)
        await bot.say(f"**{ctx.message.author.name}** :hammer: kicked **{user.name}#{user.discriminator}** for `{reason}`")
        embed = discord.Embed(title=' ',description=infraction,color=0xff7a00)
        embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}#{ctx.message.author.discriminator} (STAFF)',icon_url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='468168300325502996'), embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `kick` command.")

@kick.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-kick <user> [reason]`
**Cooldown:** `3 seconds`
**Example:** `-kick @scarab annoying`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Kick',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `kick` command.")

@bot.command(pass_context=True)
async def mute(ctx, user: discord.Member, *, reason):
    if user.server_permissions.manage_messages:
        await bot.say(f"<:DaveNo:466458146966339585> I can't mute **{user.name}#{user.discriminator}** because they are a server mod/admin")
    elif ctx.message.author.server_permissions.manage_messages:
        infraction = f"""
**MUTED**
**User:** <@{user.id}>
**User ID:** {user.id}
**Reason:** {reason}"""
        role = discord.utils.get(user.server.roles, name='Muted')
        await bot.add_roles(user, role)
        await bot.say(f"**{ctx.message.author.name}** :hammer: muted **{user.name}#{user.discriminator}** for `{reason}`")
        embed = discord.Embed(title=' ',description=infraction,color=0x60cdff)
        embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}#{ctx.message.author.discriminator} (STAFF)',icon_url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='468168300325502996'), embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `mute` command.")

@mute.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-mute <user> [reason]`
**Cooldown:** `3 seconds`
**Example:** `-mute @scarab annoying`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Mute',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `mute` command.")

@bot.command(pass_context=True)
async def unmute(ctx, user: discord.Member, *, reason):
    if user.server_permissions.manage_messages:
        await bot.say(f"<:DaveNo:466458146966339585> I can't unmute **{user.name}#{user.discriminator}** because they are a server mod/admin")
    elif ctx.message.author.server_permissions.manage_messages:
        infraction = f"""
**UNMUTED**
**User:** <@{user.id}>
**User ID:** {user.id}
**Reason:** {reason}"""
        role = discord.utils.get(user.server.roles, name='Muted')
        await bot.remove_roles(user, role)
        await bot.say(f"**{ctx.message.author.name}** :hammer: unmuted **{user.name}#{user.discriminator}** for `{reason}`")
        embed = discord.Embed(title=' ',description=infraction,color=0x136b20)
        embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}#{ctx.message.author.discriminator} (STAFF)',icon_url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='468168300325502996'), embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `unmute` command.")

@unmute.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-unmute <user> [reason]`
**Cooldown:** `3 seconds`
**Example:** `-unmute @scarab cool`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Mute',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `unmute` command.")

@bot.command(pass_context=True)
async def say(ctx, *, message):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say(f"""{message}""")
        await bot.delete_message(ctx.message)
    else:
        await bot.reply(":lock: you do not have permission to execute the `say` command")

@bot.command(pass_context=True)
async def embed(ctx, *, message):
    if ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title=' ',description=message)
        embed.set_author(name=f'{ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    else:
        await bot.reply(":lock: you do not have permission to execute the `embed` command")

@bot.command(pass_context=True)
async def setnick(ctx, user: discord.Member, *, name):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.change_nickname(user, nickname=name)
        await bot.say(f"**{ctx.message.author.name}** changed **{user.name}#{user.discriminator}**'s nickname to `{name}`")
    else:
        await bot.say(":lock: you do not have permission to execute the `setnick` command")

@setnick.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-setnick <user> [name]`
**Cooldown:** `3 seconds`
**Example:** `-set @scarab cool`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Setnick',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `setnick` command.")

@bot.command(pass_context=True)
async def modmail(ctx, user: discord.Member, *, message):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.send_message(user, f"**{ctx.message.author.name}:** {message}")
        await bot.add_reaction(ctx.message, "âœ…")
    else:
        await bot.reply(":lock: you do not have permission to execute the `modmail` command")

@modmail.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-modmail <reply ID> [message]`
**Cooldown:** `3 seconds`
**Example:** `-modmail 370777160216215553 I got your report`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Modmail',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `modmail` command.")

@bot.command(pass_context=True)
async def warn(ctx, user: discord.Member, *, reason):
    if user.server_permissions.manage_messages:
        await bot.say(f"<:DaveNo:466458146966339585> I can't warn **{user.name}#{user.discriminator}** because they are a server mod/admin")
    elif ctx.message.author.server_permissions.manage_messages:
        infraction = f"""
**WARNED**
**User:** <@{user.id}>
**User ID:** {user.id}
**Reason:** {reason}"""
        await bot.say(f"**{ctx.message.author.name}** :hammer: warned **{user.name}#{user.discriminator}** for `{reason}`")
        embed = discord.Embed(title=' ',description=infraction,color=0xffd941)
        embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}#{ctx.message.author.discriminator} (STAFF)',icon_url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='YOUR MODLOG CHANNEL ID'), embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `warn` command.")

@warn.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.manage_messages:
        usage = """
**Usage:** `-warn <user> [reason]`
**Cooldown:** `3 seconds`
**Example:** `-warn @scarab annoying`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Warn',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `warn` command.")

#deev 

@bot.command(pass_context=True)
async def vote(ctx, *, ass):
    if ctx.message.author.id == '370777160216215553' or ctx.message.author.id == '394402252498010113':
        emoji1 = discord.utils.get(ctx.message.server.emojis, name='DaveYes')
        emoji2 = discord.utils.get(ctx.message.server.emojis, name='DaveNo')
        embed = discord.Embed(title=' ',description=ass)
        embed.set_author(name='Poll',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Poll started by {ctx.message.author.name}#{ctx.message.author.discriminator}',icon_url=ctx.message.author.avatar_url)
        x = await bot.say(embed=embed)
        await bot.add_reaction(x, emoji1)
        await bot.add_reaction(x, emoji2)
        await bot.delete_message(ctx.message)
    else:
        await bot.reply(":lock: you do not have permission to execute the `vote` command")

@bot.command(pass_context=True)
async def changeuser(ctx, *, name):
    if ctx.message.author.id == '370777160216215553' or ctx.message.author.id == '394402252498010113':
        await bot.edit_profile(username=name)
        embed = discord.Embed(title=' ',description=f'{ctx.message.author.mention} successfully changed the bots username to `{name}`')
        embed.set_author(name='Username Changed',icon_url=bot.user.avatar_url)
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `changeuser` command")

@bot.command(pass_context=True)
async def changestatus(ctx, *, status):
    if ctx.message.author.id == '394402252498010113' or ctx.message.author.id == '370777160216215553':
        await bot.change_presence(game=discord.Game(type=0,name=status))
        embed = discord.Embed(title=' ',description=f'{ctx.message.author.mention} successfully changed the bots status to `Playing {status}`')
        embed.set_author(name='Status Changed',icon_url=bot.user.avatar_url)
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `changestatus` command")

@bot.command(pass_context=True)
async def table2(ctx):
    #-table [{"User":"Joshuliu","Role":"Dumb"},{"User":"Scarab","Role":"Developer"},{"User":"Jared","Role":"Dumb"},{"User":"Shadow","Role":"Dumb"}]
    if ctx.message.author.id == '370777160216215553':
        thing = """```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ User     â”‚ Role      â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Joshuliu â”‚ Dumb      â”‚
â”‚ Scarab   â”‚ Developer â”‚
â”‚ Jared    â”‚ Dumb      â”‚
â”‚ Shadow   â”‚ Dumb      â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜```"""
        await bot.say(thing)
    else:
        await bot.reply(":lock: you do not have permission to use the `table` command")

@bot.command(pass_context=True)
async def table1(ctx):
    #-table [{"User":"Joshuliu","Dicksize":"Small"},{"User":"Shadow","Dicksize":"Small"}]
    if ctx.message.author.id == '370777160216215553':
        thing = """```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ User     â”‚ Dicksize â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Joshuliu â”‚ Small    â”‚
â”‚ Shadow   â”‚ Small    â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜```"""
        await bot.say(thing)
    else:
        await bot.reply("you do not have permission to use the `table` command")

@bot.command(pass_context=True)
async def table(ctx):
    #-table [{"Fags":"Shadow","Sexy people":"scarab"},{"Fags":"Kenny","Sexy people":"Jared"},{"Fags":"Grim","Sexy people":"Incognito"}]
    if ctx.message.author.id == '370777160216215553':
        thing = """```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Fags   â”‚ Sexy people â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Shadow â”‚ scarab      â”‚
â”‚ Kenny  â”‚ Jared       â”‚
â”‚ Grim   â”‚ Incognito   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜```"""
        await bot.say(thing)
    else:
        await bot.reply(":lock: you do not have permission to use the `table` command")

@bot.command(pass_context=True)
async def add(ctx, left: int, right: int):
    await bot.say(left + right)

@bot.command(pass_context=True)
async def smartadd(ctx, *args):
    sum = 0
    for item_in_list in args:
        sum = sum + int(item_in_list)
        await bot.say(sum)

@bot.command(pass_context=True)
async def addrole(ctx, member: discord.Member, *, args):
    if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name=args)
        await bot.add_roles(member, role)
        await bot.say(f"**{ctx.message.author.name}** gave **{member.name}#{member.discriminator}** the `{args}` role")
    else:
        await bot.reply("you do not have permission to use the `addrole` command")

@addrole.error
async def kickHandler(error, ctx):
    if ctx.message.author.server_permissions.administrator:
        usage = """
**Usage:** `-addrole <user> [role]`
**Cooldown:** `3 seconds`
**Example:** `-addrole @scarab Developer`"""
        embed = discord.Embed(title=' ',description=usage)
        embed.set_author(name='Addrole',icon_url=bot.user.avatar_url)
        embed.set_footer(text=f'Command invoked by {ctx.message.author.name}#{ctx.message.author.discriminator}')
        await bot.say(embed=embed)
    else:
        await bot.reply(":lock: you do not have permission to execute the `addrole` command.")

@bot.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id =='370777160216215553':
        embed = discord.Embed(title='<:DaveYes:466458077433036821> Dave has shutdown',description=' ')
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
        await bot.logout()
    else:
        await bot.say("no")

@bot.command(pass_context=True)
async def BanJared(ctx):
    await bot.say("Confirm you would like to ban <@173450781784145921> by typing `CONFIRM`")
    await bot.wait_for_message(author=ctx.message.author, content='CONFIRM')
    await bot.say("do it yourself then retard")

bot.run("NDY4MTcwNDkyOTMxNzM1NTYz.Di1RWQ.AVfwWn3X90HMp8cQCqieyQd6waQ")