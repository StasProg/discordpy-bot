import nextcord
from nextcord.ext import commands
from config import *

TESTING_GUILD_ID = 1038802426603520090

class ProhodkaModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            title="Заявка на проходку",
            custom_id="persistent_modal:server",
        )

        self.nickplat = nextcord.ui.TextInput(
            label="Ваш игровой ник Minecraft? и Платформа",
            placeholder="Пример: valera2009 и Java / Bedrock",
            required=True,
            min_length=4,
            max_length=50,
            custom_id="persistent_modal:nickplat",
        )
        self.add_item(self.nickplat)

        self.whyarewe = nextcord.ui.TextInput(
            label="На Какой проект хотите попасть и почему он?",
            placeholder="Откуда вы узнали о нашем проекте?",
            style=nextcord.TextInputStyle.paragraph,
            min_length=100,
            max_length=600,
            required=True,
            custom_id="persistent_modal:whyarewe",
        )
        self.add_item(self.whyarewe)

        self.tellplans = nextcord.ui.TextInput(
            label="Расскажите о ваших планах",
            placeholder="Просьба не писать потипо: Я ХОЧУ НАЙТИ ДРУЗЕЙ - ПОИГРАТЬ",
            style=nextcord.TextInputStyle.paragraph,
            required=True,
            min_length=50,
            max_length=300,
            custom_id="persistent_modal:tellplans",
        )
        self.add_item(self.tellplans)

        self.xpgame = nextcord.ui.TextInput(
            label="Есть ли опыт игры в майнкрафт?",
            placeholder="Расскажите ваш опыт игры в Minecraft, вашу историю.",
            style=nextcord.TextInputStyle.paragraph,
            min_length=50,
            max_length=170,
            required=True,
            custom_id="persistent_modal:xpgame",
        )
        self.add_item(self.xpgame)

        self.yourrez = nextcord.ui.TextInput(
            label="Расскажите о себе",
            placeholder="Расскажите подробно о себе таланты, и успехи",
            required=True,
            style=nextcord.TextInputStyle.paragraph,
            min_length=400,
            max_length=600,
            custom_id="persistent_modal:yourrez",
        )
        self.add_item(self.yourrez)

    async def callback(self, interaction: nextcord.Interaction):
        channel = bot.get_channel(adminchannel)
        emb=nextcord.Embed(color=0x2f3136, title="ГОТОВАЯ ЗАЯВКА ИГРОКА")
        emb.add_field(name="Дискорд игрока", value={interaction.user.mention})
        emb.add_field(name="Minecraft ник и Платформа", value={self.nickplat.value})
        emb.add_field(name="На Какой проект вы хотите попасть и почему он", value={self.whyarewe.value})
        emb.add_field(name="Планы Игрока", value={self.tellplans.value})
        emb.add_field(name="Опыт игры в Minecraft", value={self.xpgame.value})
        emb.add_field(name="О игроке", value={self.yourrez.value})
        await channel.send(embed=emb)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_modals_added = False

    async def on_ready(self):
        if not self.persistent_modals_added:
            self.add_modal(ProhodkaModal())
            self.persistent_modals_added = True

        print(f"Бот был запущен, Информация по запуску: {self.user} (ID: {self.user.id})")

bot = Bot()

@bot.slash_command(
    name="adminsinfo",
    description="Подача заявки на проходку!",
    guild_ids=[TESTING_GUILD_ID],
)
async def server(interaction: nextcord.Interaction):
    await interaction.response.send_modal(ProhodkaModal())

@bot.slash_command(name="accept", description="Данная команда требуется для принятия заявок!")
async def cmd(ctx, user: nextcord.User):
    files = nextcord.File("32.png")
    lcemb=nextcord.Embed(color=0x2f3136, title="")
    lcemb.add_field(name="WAYLER", value="Здравствуйте дорогой приятель! Не будем тянуть котов за хвосты. Вы были приняты на проект .Wayler! Надеемся что мы вас обрадовали.")
    lcemb.add_field(name=" ", value="```・Вам была успешно выданная роль игрока, и открыты специальные чаты.```")
    lcemb.add_field(name="Конкретная инструкция у нас на [ВИКИПЕДИИ] -> (https://fedkovichs-organization.gitbook.io/server-wayler/) в отделении ``Ξ Как начать играть?``", value=" ")
    lcemb.set_image(url="attachment://32.png")
    await user.send(file=files, embed=lcemb)#, view=Button3())
    role = nextcord.utils.get(ctx.guild.roles, id=1038803917103972425)
    await user.add_roles(role)

@bot.slash_command(name="deny", description="Данная команда требуется для отклонения заявок!")
async def cmd(ctx, user: nextcord.User):
    lcemb=nextcord.Embed(color=0x2f3136, title="")
    lcemb.add_field(name="WAYLER", value="К сожалению вашу заявку не одобрили на вход в проект...")
    lcemb.add_field(name=" ", value="```・Но выше нос вы можете приобрести проходку у нас на сайте!```")
    lcemb.add_field(name="Ссылка на сайт -> (https://wayler-shop.easydonate.ru/)", value=" ")
    await user.send(embed=lcemb)

class Button1(nextcord.ui.View):
    def __init__(self): 
        super().__init__()
    @nextcord.ui.button(label="Заявка", style=nextcord.ButtonStyle.green)
    async def button1(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.send_modal(ProhodkaModal())

@bot.slash_command(
    name="textbutton",
    description="Начальная подача заявки",
    guild_ids=[TESTING_GUILD_ID],
)
async def button(ctx):
    channel = bot.get_channel(infochannel)
    file = nextcord.File("32.png")
    embed=nextcord.Embed(color=0x2f3136, title=" ")
    embed.add_field(name=" ", value="**ПРОХОЖДЕНИЕ НА ПРОЕКТ**\n**Wayler** - это приватный ванильный Minecraft проект с **RP** и соответствующими плагинами. И огромной связанной сюжетной историей.", inline=False)
    embed.add_field(name="Для того чтобы попасть на проект вам нужно заполнить заявку в **Discord**.", value="```・Ваша миссия это нажать на кнопочку ниже под названием Заявка!``````\n・После чего вы уже будете на месте, вы должны заполнять бланк, и главное чтобы подходило вам и нам!``````\n・А теперь ждите когда вашу заявку осмотрит вселенный документ.```", inline=True)
    embed.set_footer(text="Чтобы купить проходку зайдите на сайт: https://wayler-shop.easydonate.ru/")
    embed.set_image(url="attachment://32.png")
    await channel.send(file=file, embed=embed, view=Button1())

bot.run(token)