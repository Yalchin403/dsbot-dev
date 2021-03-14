import discord
from discord.ext import commands
class RulesCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["obey"])
    async def rules(self, ctx):
	    title = """Hello, dear user, you won't be able to send a message unless and until you accept the rules. To accept the rules, click on the check icon below and get verified_member role. Here are our rules:"""
	    description = """1) You can look for partner here only if you need partner for learning, otherwise you are not in the right place.
	2)Users that use hate speech and or fighting words will be disqualified.
	3) If the thing you want to learn is not listed here, please go to the general channel and look for the partner there.
	4) Advertising or any kind of promotion is not allowed, and user committing it will be disqualified.
	5) Please stick to the topic, for example, if you would like to find partner for learning English, please look for the partner in the channel dedicated for English learning.
	6) Racism towards any race is not allowed.
	7) Users have to use only English if they are looking for partner, however they are free to use specific language for specific channel given in "Languages" category for practicing purpose.
	8) We recommend not to share your contact credentials in the server, and instead share it via dm if you want to. In case you share, we are not responsible for any additional risk that you are taking.
	9) If you are looking for a partner to learn something together, please briefly describe your level in this specific field.
	10) You can find partners to get ready for exam, interview etc. together, however, you cannot ask users to help you to pass the exam, interview etc. here. Users not obeying this rules will be banned from the server.
	11) Do not offer your paid courses, tutoring here. Users not obeying this rules will be banned from the server.
	"""
	    embed = discord.Embed(title=title, description=description, color=discord.Color.purple())
	    await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(RulesCog(client))