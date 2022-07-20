import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import os

client = discord.Client()
bot = commands.Bot(command_prefix = '고려야 ', help_command = None) 

status = cycle(["고려봇에 오신 것을 환영합니다", "고려봇 Ver.β 1.1", "반갑습니다!"])    # 본인이 원하는 만큼 추가 가능

@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중\n")    # 참여 중인 서버 수

    change_status.start()    # 봇이 on_ready 상태라면, change_message 함수 실행

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@bot.command(aliases=['도움말','사용법','설명'])
async def 도움(ctx) :
    embed=discord.Embed(title="도움말 및 커맨드", description="접두사는 '고려야' 입니다 커맨드 사용시 꼭 붙여주셔야 합니다", color=0xfedc89)
    embed.set_author(name="고려봇")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/987391627955941426/Royal_flag_of_Goryeo_Bong-gi_Fringeless.png")
    embed.add_field(name="정당-고려야 '정당 이름'", value="원내정당에 대한 정보를 제공합니다", inline=False)
    embed.add_field(name="도•광역시-고려야 '도•또는 광역시 이름'", value="북한•미수복지역 포함 전국 도•광역시의 정보를 제공합니다", inline=False)   
    embed.set_footer(text="고려봇 ver.β 1.1")
    await ctx.send(embed = embed)

@bot.command()
async def 더불어민주당(ctx) :
    embed=discord.Embed(title="원내정당-제1야당", description="민주당계 정당", color=0x0062cb)
    embed.set_author(name="더불어민주당")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/987409082849841202/c16525411109e43f.png")
    embed.add_field(name="국회 의석 수", value="170석-56.86%", inline=True)
    embed.add_field(name="광역단체장", value="5석-29.41%", inline=True)
    embed.add_field(name="기초단체장", value="63석-27.87%", inline=True)
    embed.add_field(name="광역의원", value="322석-36.92%", inline=True)
    embed.add_field(name="기초의원", value="1384석-46.31%", inline=True)
    embed.add_field(name="비상대책위원장", value="우상호", inline=True)
    embed.add_field(name="원내대표", value="박홍근", inline=True)
    embed.add_field(name="사무총장", value="김민기", inline=True)
    embed.add_field(name="정책위의장", value="김성환", inline=True)
    embed.add_field(name="정책연구소", value="민주연구원", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/987408101357527051/355319036775601b.png")
    await ctx.send(embed = embed)

@bot.command()
async def 국민의힘(ctx) :
    embed=discord.Embed(title="원내정당-여당", description="보수 정당", color=0xe60024)
    embed.set_author(name="국민의힘")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/987413467793350706/09175f886ef56ecd.png")
    embed.add_field(name="국회 의석 수", value="115석-38.46%", inline=True)
    embed.add_field(name="광역단체장", value="12석-70.58%", inline=True)
    embed.add_field(name="기초단체장", value="145석-64.15%", inline=True)
    embed.add_field(name="광역의원", value="540석-61.92%", inline=True)
    embed.add_field(name="기초의원", value="1435석-48.02%", inline=True)
    embed.add_field(name="대표", value="이준석-직무정지", inline=True)
    embed.add_field(name="원내대표", value="권성동", inline=True)
    embed.add_field(name="사무총장", value="한기호", inline=True)
    embed.add_field(name="정책위의장", value="성일종", inline=True)
    embed.add_field(name="정책연구소", value="여의도연구원", inline=True)
    embed.add_field(name="대통령", value="윤석열-20대", inline=True)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/987413468112097340/5b7b4911c8bf1b13.png")
    await ctx.send(embed = embed)

@bot.command()
async def 정의당(ctx) :
    embed=discord.Embed(title="원내정당-제2야당", description="진보 정당", color=0xffcc00)
    embed.set_author(name="정의당")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/987416887128383598/8908697419ec5497.png")
    embed.add_field(name="국회 의석 수", value="6석-2.01%", inline=True)
    embed.add_field(name="광역단체장", value="0석-0%", inline=True)
    embed.add_field(name="기초단체장", value="0석-0%", inline=True)
    embed.add_field(name="광역의원", value="2석-0.22%", inline=True)
    embed.add_field(name="기초의원", value="7석-0.23%", inline=True)
    embed.add_field(name="비상대책위원장", value="이은주", inline=True)
    embed.add_field(name="원내대표", value="이은주", inline=True)
    embed.add_field(name="사무총장", value="신언직", inline=True)
    embed.add_field(name="정책위의장", value="장혜영", inline=True)
    embed.add_field(name="정책연구소", value="정의정책연구소", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/987416887405203556/32d2a37831039b47.png")
    await ctx.send(embed = embed)

@bot.command()
async def 기본소득당(ctx) :
    embed=discord.Embed(title="원내정당-제3야당", description="단일쟁점 정당", color=0x00b1a0)
    embed.set_author(name="기본소득당")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/989213461257011231/30b3d7e0958f2f11.png")
    embed.add_field(name="국회 의석 수", value="1석-0.33%", inline=True)
    embed.add_field(name="광역단체장", value="0석-0%", inline=True)
    embed.add_field(name="기초단체장", value="0석-0%", inline=True)
    embed.add_field(name="광역의원", value="0석-0%", inline=True)
    embed.add_field(name="기초의원", value="0석-0%", inline=True)
    embed.add_field(name="상임대표", value="김영길", inline=True)
    embed.add_field(name="원내대표", value="용혜인", inline=True)
    embed.add_field(name="사무총장", value="김영길", inline=True)
    embed.add_field(name="정책위의장", value="공석", inline=True)
    embed.add_field(name="정책연구소", value="기본소득정책연구소", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/989213461579956264/ba1b19d756675c2d.png")
    await ctx.send(embed = embed)

@bot.command()
async def 시대전환(ctx) :
    embed=discord.Embed(title="원내정당-제3야당", description="실용주의 정당", color=0x5b157f)
    embed.set_author(name="시대전환")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/989215600503050240/6184ce7dd29cdb74.png")
    embed.add_field(name="국회 의석 수", value="1석-0.33%", inline=True)
    embed.add_field(name="광역단체장", value="0석-0%", inline=True)
    embed.add_field(name="기초단체장", value="0석-0%", inline=True)
    embed.add_field(name="광역의원", value="0석-0%", inline=True)
    embed.add_field(name="기초의원", value="0석-0%", inline=True)
    embed.add_field(name="대표", value="조정훈", inline=True)
    embed.add_field(name="원내대표", value="조정훈", inline=True)
    embed.add_field(name="사무총장", value="이재후", inline=True)
    embed.add_field(name="정책위의장", value="박숙현", inline=True)
    embed.add_field(name="정책연구소", value="시대전환LAB", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/989215600914087936/9cd78c7d4d6b54c6.png")
    await ctx.send(embed = embed)

@bot.command()
async def 서울특별시(ctx) :
    embed=discord.Embed(title="서울특별시 🇰🇷", description="다시 뛰는 공정 도시 서울", color=0xae1932)
    embed.set_author(name="대한민국 도•광역시")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/989225317484859512/fd29cecbade48ad2.png")
    embed.add_field(name="시장", value="오세훈 <:ppp:996806277600641054>", inline=False)
    embed.add_field(name="교육감", value="조희연 <:prg:996811071962763284>", inline=False)
    embed.add_field(name="시청", value="중구 세종대로 110", inline=False)
    embed.add_field(name="행정구역", value="25구", inline=False)
    embed.add_field(name="인구", value="9,496,887명", inline=False)
    embed.add_field(name="인구밀도", value="15,692.15명/㎢", inline=False)
    embed.add_field(name="면적", value="605.2㎢", inline=False)
    embed.add_field(name="GDP", value="4053억$", inline=False)
    embed.add_field(name="1인당GDP", value="42215$", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/989224273652629564/unknown.png")
    await ctx.send(embed = embed)

@bot.command()
async def 경기도(ctx) :
    embed=discord.Embed(title="경기도 🇰🇷", description="새로운 경기 공정한 세상", color=0x004097)
    embed.set_author(name="대한민국 도•광역시")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/989233342811603004/2e853beccb00c956.png")
    embed.add_field(name="도지사", value="김동연 <:dpk:996806299218100265>", inline=False)
    embed.add_field(name="교육감", value="임태희 <:rht:996811088974844004>", inline=False)
    embed.add_field(name="도청", value="수원시 영통구 도청로 30", inline=False)
    embed.add_field(name="행정구역", value="28시 3군", inline=False)
    embed.add_field(name="인구", value="13,581,496명", inline=False)
    embed.add_field(name="인구밀도", value="1,331.95명/㎢", inline=False)
    embed.add_field(name="면적", value="10,196.7㎢", inline=False)
    embed.add_field(name="GDP", value="4480억$", inline=False)
    embed.add_field(name="1인당GDP", value="33420$", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/989233306144997436/unknown.png")
    await ctx.send(embed = embed)

@bot.command()
async def 강원도(ctx) :
    embed=discord.Embed(title="강원도 🇰🇷", description="새로운 강원도! 특별자치시대!", color=0x00ab84)
    embed.set_author(name="대한민국 도•광역시")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/996813829436620871/e08933fb5857e247.png")
    embed.add_field(name="도지사", value="김진태 <:ppp:996806277600641054>", inline=False)
    embed.add_field(name="교육감", value="신경호 <:rht:996811088974844004>", inline=False)
    embed.add_field(name="도청", value="춘천시 중앙로 1", inline=False)
    embed.add_field(name="행정구역", value="7시 11군", inline=False)
    embed.add_field(name="인구", value="1,539,064명", inline=False)
    embed.add_field(name="인구밀도", value="91.31명/㎢", inline=False)
    embed.add_field(name="면적", value="16,829.7㎢", inline=False)
    embed.add_field(name="GDP", value="449억$", inline=False)
    embed.add_field(name="1인당GDP", value="32,235$", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/996816528286683176/unknown.png")
    await ctx.send(embed = embed)

@bot.command()
async def 충청북도(ctx) :
    embed=discord.Embed(title="충청북도 🇰🇷", description="충북을 새롭게, 도민을 신나게", color=0x009a44)
    embed.set_author(name="대한민국 도•광역시")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/996818066983899206/5006a97114bb4088.png")
    embed.add_field(name="도지사", value="김영환 <:ppp:996806277600641054>", inline=False)
    embed.add_field(name="교육감", value="윤건영 <:rht:996811088974844004>", inline=False)
    embed.add_field(name="도청", value="청주시 상당구 상당로 82 (문화동)", inline=False)
    embed.add_field(name="행정구역", value="3시 8군", inline=False)
    embed.add_field(name="인구", value="1,597,118명", inline=False)
    embed.add_field(name="인구밀도", value="215.51명/㎢", inline=False)
    embed.add_field(name="면적", value="7,407.0㎢", inline=False)
    embed.add_field(name="GDP", value="656억$", inline=False)
    embed.add_field(name="1인당GDP", value="40,228$", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/996818359725338674/unknown.png")
    await ctx.send(embed = embed)

@bot.command()
async def 충청남도(ctx) :
    embed=discord.Embed(title="충청남도 🇰🇷", description="힘쎈충남, 대한민국의 힘", color=0x8c8c70)
    embed.set_author(name="대한민국 도•광역시")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/597758831631532032/996820670480646205/ff25e96b55e3c157.png")
    embed.add_field(name="도지사", value="김태흠 <:ppp:996806277600641054>", inline=False)
    embed.add_field(name="교육감", value="김지철 <:prg:996811071962763284>", inline=False)
    embed.add_field(name="도청", value="홍성군 홍북읍 충남대로 21", inline=False)
    embed.add_field(name="행정구역", value="8시 7군", inline=False)
    embed.add_field(name="인구", value="2,120,201명", inline=False)
    embed.add_field(name="인구밀도", value="256.86명/㎢", inline=False)
    embed.add_field(name="면적", value="8,246.2㎢", inline=False)
    embed.add_field(name="GDP", value="1,049억$", inline=False)
    embed.add_field(name="1인당GDP", value="51,711$", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/597758831631532032/996820624284581969/unknown.png")
    await ctx.send(embed = embed)

bot.run(os.environ['token'])
