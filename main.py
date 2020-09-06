import discord
import random


token = os.environ["DISCORD_TOKEN"]

client = discord.Client()

lm_key = None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """This method will deal with all messages in the server"""

    global lm_key

    if message.content.find("!landmark") != -1 and not message.author.bot:
        #await message.channel.send(gen_landmk(random.randint(0,2)))
        place_val = random.randint(0,9)
        if (place_val == lm_key): #Generate again random to reduce likehood of same image being shown twice
            place_val = random.randint(0,9)
        if (place_val == lm_key): #Generate again random to reduce likehood of same image being shown twice
            place_val = random.randint(0,9)
        lm_key = 0
        if place_val == 0: #Bush Library
            await message.channel.send('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/George_Bush_Presidential_Library.jpg/1200px-George_Bush_Presidential_Library.jpg')
            lm_key = 0
        elif place_val == 1: #Evans Library
            await message.channel.send('https://bloximages.chicago2.vip.townnews.com/myaggienation.com/content/tncms/assets/v3/editorial/3/ed/3ed2c6a8-11ca-11e3-a54c-0019bb2963f4/5221280042426.image.jpg')
            lm_key = 1
        elif place_val == 2: #MSC
            await message.channel.send('https://newsarchive.arch.tamu.edu/media/photologue/phlogphoto/cache/memory%20cloud4_galleria_large.jpg')
            lm_key = 2
        elif place_val == 3: #Zachry
            await message.channel.send('https://zachry.tamu.edu/wp-content/uploads/2018/08/zach-building-july-progress-photo.jpg')
            lm_key = 3
        elif place_val == 4: #Quadrangle
            await message.channel.send('https://leadbyexample.tamu.edu/images/story-newquad5.jpg')
            lm_key = 4
        elif place_val == 5: #ETB
            await message.channel.send('https://th.bing.com/th/id/OIP.0rhyAu2ziSKwhix5NVL7OwHaDV?pid=Api&rs=1')
            lm_key = 5
        elif place_val == 6: #Bright
            await message.channel.send('https://engineering.tamu.edu/_files/_images/_content-images/bright-building-08Jan2019.jpg')
            lm_key = 6
        elif place_val == 7: #Sbisa
            await message.channel.send('https://upload.wikimedia.org/wikipedia/commons/9/9c/Sbisa.jpg')
            lm_key = 7
        elif place_val == 8: #Dixie Chicken
            await message.channel.send('https://i.pinimg.com/736x/1c/25/5d/1c255d279c6cd6a06ec87d1cc2c51b08--aggie-game-college-station-texas.jpg')
            lm_key = 8
        elif place_val == 9: #Academic Building
            await message.channel.send('https://www.thoughtco.com/thmb/oS9b0mb0EbtMbyrAnRpiz7_vfhw=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/texas-a-and-m-flickr-5a4853a4b39d0300372455a9.jpg')
            lm_key = 9

    elif message.content.find("!Bush Library") != -1 and not message.author.bot:
        if (lm_key == 0):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Evans Library") != -1 and not message.author.bot:
        if (lm_key == 1):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!MSC") != -1 and not message.author.bot:
        if (lm_key == 2):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Zachry") != -1 and not message.author.bot:
        if (lm_key == 3):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Quadrangle") != -1 and not message.author.bot:
        if (lm_key == 4):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!ETB") != -1 and not message.author.bot:
        if (lm_key == 5):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Bright") != -1 and not message.author.bot:
        if (lm_key == 6):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Sbisa") != -1 and not message.author.bot:
        if (lm_key == 7):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Dixie Chicken") != -1 and not message.author.bot:
        if (lm_key == 8):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!Academic Building") != -1 and not message.author.bot:
        if (lm_key == 9):
            await message.channel.send(f"{message.author.name} is Correct!")

    elif message.content.find("!key") != -1 and not message.author.bot:
        await message.channel.send("Here are the current landmarks in the AggieSpy 1.0 (Enter exactly for game):\n"
                                   "Bush Library\n"
                                   "Evans Library\n"
                                   "MSC\n"
                                   "Zachry\n"
                                   "Quadrangle\n"
                                   "ETB\n"
                                   "Bright\n"
                                   "Sbisa\n"
                                   "Dixie Chicken\n"
                                   "Academic Building\n")

    elif message.content.find("!help") != -1 and not message.author.bot:
        # To see the commands to control the bot
        await message.channel.send("Here are the commands to control SpyGameBot:\n"
                                   "!landmark - Generates a Aggie landmark to identify\n"
                                   "!key - Shows the possible landmark names\n"
                                   "!help - See the commands to control SpyGameBot\n")

client.run(token)
