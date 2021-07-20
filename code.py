import discord
from discord.ext  import commands
import pandas as pd

bott = discord.Client()
intents = discord.Intents.default()
intents.members = True
bott = discord.Client(intents=intents)
bott = commands.Bot(command_prefix='-', intents=intents)


#begin
data = pd.read_csv("Employee.csv", encoding = 'unicode_escape') #read csv file

@bott.command()
async def find(ctx, salarynumber : str.upper):  #command name: "find" takes salary number as an arguement for further search column  
  
   sal=(data.loc[data['Salary'].isin([salarynumber])]) #matches arguement(salary number) taken from the user with salary column of every employee
   eid = sal.loc[sal['Salary'] == salarynumber]    #gets employee ids of matched rows  
  
   name = eid['Name'].iloc[0].lower()   #get name 
   gender = eid['Gender'].iloc[0]       #get gender
   
   #create embed
   embed = discord.Embed(
            title = f'Employee data with salary: {salarynumber}',
            description = f'Employee Details',
            color = 0xDC143C #crimson
            ) 
   embed.set_footer(text=f'Info requested by {ctx.author.display_name} | ID-{ctx.author.id}  ') #optional
   embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)                       #optional
    
   embed.add_field(name=f'Name: {name}', value= f'**Gender:** {gender}', inline=True)           #set certain data to embed fields
    
   await ctx.send(embed=embed)
   return
  
#To run this command, you should type: -find 2000$
#Syntax of command: "prefix[commandname] salarynumber" (user input)
