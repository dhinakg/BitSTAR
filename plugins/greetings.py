#    Copyright 2017 Starbot Discord Project
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from api import command, message, plugin, database
from api.bot import bot
from api.database.table import table, tableTypes
from api.database.entry import entry

# Command names.
SETWELCOMECMD = "setwelcome"

def onInit(plugin_in):
    setwelcome_command = command.command(plugin_in, SETWELCOMECMD, shortdesc="Set the welcome message for the server.")
    return plugin.plugin(plugin_in, "greetings", [setwelcome_command])

@bot.client.event
async def on_member_join(member):
    # Welcome new user.
    await bot.client.send_message(member.server, content = "Welcome " + member.mention + " to **" + member.server.name + "**!")

@bot.client.event
async def on_member_remove(member):
    # Say goodbye to user.
    await bot.client.send_message(member.server, content = "Goodbye " + member.mention + ", **" + member.server.name + "** will miss you!")

@bot.client.event
async def on_member_ban(member) :
    # Announce ban.
    await bot.client.send_message(member.server, content = displayname.name(member) + " got banned from **" + member.server.name + "**.")

@bot.client.event
async def on_member_unban(server, user):
    # Announce unban.
    await bot.client.send_message(server, content = displayname.name(user) + " got unbanned from **" + server.name + "**.")



async def onCommand(message_in):
    # Initialize database.
    database.init()
    OffsetTable = table("greetings", tableTypes.pServer)

