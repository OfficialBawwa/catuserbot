"""
inspired from @Deonnn @Mayur_Karaniya
Quotes credits: Being Biblical Channel : @BeingBiblical
AlenPaulVarghese(@STARKTM1)[hp]
Sing credits :By @PhycoNinja13b
No Logic Pligon for @PepeBot
\nCoding by Legend @NeoMatrix90
\nType .logic to see many logical fact
"""

import random
from asyncio import sleep


@bot.on(admin_cmd(pattern=r"sing$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sing$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Singing...")
    await sleep(2)
    x = random.randrange(1, 33)
    if x == 1:
        await event.edit(
            "🎶 I'm in love with the shape of you \n We push and pull like a magnet do\n Although my heart is falling too \n I'm in love with your body \n And last night you were in my room \n And now my bedsheets smell like you \n Every day discovering something brand new 🎶  \n 🎶  I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body 🎶 \n **-Shape of You**"
        )
    if x == 2:
        await event.edit(
            "🎶 I've been reading books of old \n The legends and the myths \n Achilles and his gold \n Hercules and his gifts \n Spiderman's control \n And Batman with his fists \n And clearly I don't see myself upon that list 🎶 \n **-Something Just Like This **"
        )
    if x == 3:
        await event.edit(
            "🎶 I don't wanna live forever \n 'Cause I know I'll be livin' in vain \n And I don't wanna fit wherever \n I just wanna keep callin' your name \n Until you come back home \n I just wanna keep callin' your name \n Until you come back home \n I just wanna keep callin' your name \n Until you come back home 🎶 \n **-I don't Wanna Live Forever **"
        )
    if x == 4:
        await event.edit(
            "🎶 Oh, hush, my dear, it's been a difficult year \n And terrors don't prey on \n Innocent victims \n Trust me, darling, trust me darling \n It's been a loveless year \n I'm a man of three fears \n Integrity, faith and \n Crocodile tears \n Trust me, darling, trust me, darling 🎶 \n **-Bad Lier"
        )
    if x == 5:
        await event.edit(
            "🎶 Walking down 29th and Park \n I saw you in another's arms \n Only a month we've been apart \n **You look happier** \n \n Saw you walk inside a bar \n He said something to make you laugh \n I saw that both your smiles were twice as wide as ours \n Yeah, you look happier, you do 🎶 \n **-Happier **"
        )
    if x == 6:
        await event.edit(
            "🎶 I took the supermarket flowers from the windowsill \n I threw the day old tea from the cup \n Packed up the photo album Matthew had made \n Memories of a life that's been loved \n Took the get well soon cards and stuffed animals \n Poured the old ginger beer down the sink \n Dad always told me, 'don't you cry when you're down' \n But mum, there's a tear every time that I blink 🎶 \n **-Supermarket Flowers**"
        )
    if x == 7:
        await event.edit(
            "🎶 And you and I we're flying on an aeroplane tonight \n We're going somewhere where the sun is shining bright \n Just close your eyes \n And let's pretend we're dancing in the street \n In Barcelona \n Barcelona \n Barcelona \n Barcelona 🎶 \n **-Barcelona **"
        )
    if x == 8:
        await event.edit(
            "🎶 Maybe I came on too strong \n Maybe I waited too long \n Maybe I played my cards wrong \n Oh, just a little bit wrong \n Baby I apologize for it \n \n I could fall, or I could fly \n Here in your aeroplane \n And I could live, I could die \n Hanging on the words you say \n And I've been known to give my all \n And jumping in harder than \n Ten thousand rocks on the lake 🎶 \n **-Dive**"
        )
    if x == 9:
        await event.edit(
            "🎶 I found a love for me \n Darling just dive right in \n And follow my lead \n Well I found a girl beautiful and sweet \n I never knew you were the someone waiting for me \n 'Cause we were just kids when we fell in love \n Not knowing what it was \n \n I will not give you up this time \n But darling, just kiss me slow, your heart is all I own \n And in your eyes you're holding mine 🎶 \n **-Perfect**"
        )
    if x == 10:
        await event.edit(
            "🎶 I was born inside a small town, I lost that state of mind \n Learned to sing inside the Lord's house, but stopped at the age of nine \n I forget when I get awards now the wave I had to ride \n The paving stones I played upon, they kept me on the grind \n So blame it on the pain that blessed me with the life 🎶 \n **-Eraser**"
        )
    if x == 11:
        await event.edit(
            "🎶 Say, go through the darkest of days \n Heaven's a heartbreak away \n Never let you go, never let me down \n Oh, it's been a hell of a ride \n Driving the edge of a knife. \n Never let you go, never let me down \n \n Don't you give up, nah-nah-nah \n I won't give up, nah-nah-nah \n Let me love you \n Let me love you 🎶 \n **-Let me Love You**"
        )
    if x == 12:
        await event.edit(
            "🎶 I'll stop time for you \n The second you say you'd like me to \n I just wanna give you the loving that you're missing \n Baby, just to wake up with you \n Would be everything I need and this could be so different \n Tell me what you want to do \n \n 'Cause I know I can treat you better \n Than he can \n And any girl like you deserves a gentleman 🎶 **-Treat You Better**"
        )
    if x == 13:
        await event.edit(
            "🎶 You're the light, you're the night \n You're the color of my blood \n You're the cure, you're the pain \n You're the only thing I wanna touch \n Never knew that it could mean so much, so much \n You're the fear, I don't care \n 'Cause I've never been so high \n Follow me through the dark \n Let me take you past our satellites \n You can see the world you brought to life, to life \n \n So love me like you do, lo-lo-love me like you do \n Love me like you do, lo-lo-love me like you do 🎶 \n **-Love me Like you Do**"
        )
    if x == 14:
        await event.edit(
            "🎶 Spent 24 hours \n I need more hours with you \n You spent the weekend \n Getting even, ooh ooh \n We spent the late nights \n Making things right, between us \n But now it's all good baby \n Roll that Backwood baby \n And play me close \n \n 'Cause girls like you \n Run around with guys like me \n 'Til sundown, when I come through \n I need a girl like you, yeah yeah 🎶 \n **-Girls Like You**"
        )
    if x == 15:
        await event.edit(
            "🎶 Oh, angel sent from up above \n You know you make my world light up \n When I was down, when I was hurt \n You came to lift me up \n Life is a drink and love's a drug \n Oh, now I think I must be miles up \n When I was a river dried up \n You came to rain a flood 🎶**-Hymn for the Weekend ** "
        )
    if x == 16:
        await event.edit(
            "🎶 I've known it for a long time \n Daddy wakes up to a drink at nine \n Disappearing all night \n I don’t wanna know where he's been lying \n I know what I wanna do \n Wanna run away, run away with you \n Gonna grab clothes, six in the morning, go 🎶 \n **-Runaway **"
        )
    if x == 17:
        await event.edit(
            "🎶 You were the shadow to my light \n Did you feel us \n Another start \n You fade away \n Afraid our aim is out of sight \n Wanna see us \n Alive 🎶 \n **-Faded**"
        )
    if x == 18:
        await event.edit(
            "🎶 It's been a long day without you, my friend \n And I'll tell you all about it when I see you again \n We've come a long way from where we began \n Oh I'll tell you all about it when I see you again \n When I see you again 🎶 \n **-See you Again**"
        )
    if x == 19:
        await event.edit(
            "🎶 I can swallow a bottle of alcohol and I'll feel like Godzilla \n Better hit the deck like the card dealer \n My whole squad's in here, walking around the party \n A cross between a zombie apocalypse and big Bobby 'The \n Brain' Heenan which is probably the \n Same reason I wrestle with mania 🎶 \n **-Godzilla**"
        )
    if x == 20:
        await event.edit(
            "🎶 Yeah, I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more \n I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more (Kio, Kio) 🎶 \n **-Old Town Road**"
        )
    if x == 21:
        await event.edit(
            "🎶 Oh-oh, ooh \n You've been runnin' round, runnin' round, runnin' round throwin' that dirt all on my name \n 'Cause you knew that I, knew that I, knew that I'd call you up \n You've been going round, going round, going round every party in L.A. \n 'Cause you knew that I, knew that I, knew that I'd be at one, oh 🎶 \n **-Attention **"
        )
    if x == 22:
        await event.edit(
            "🎶 This hit, that ice cold \n Michelle Pfeiffer, that white gold \n This one for them hood girls \n Them good girls straight masterpieces \n Stylin', wilin', livin' it up in the city \n Got Chucks on with Saint Laurent \n Gotta kiss myself, I'm so pretty \n \n I'm too hot (hot damn) \n Called a police and a fireman \n I'm too hot (hot damn) \n Make a dragon wanna retire man \n I'm too hot (hot damn) \n Say my name you know who I am \n I'm too hot (hot damn) \n And my band 'bout that money, break it down 🎶 \n **-Uptown Funk**"
        )
    if x == 23:
        await event.edit(
            "🎶 Just a young gun with the quick fuse \n I was uptight, wanna let loose \n I was dreaming of bigger things \n And wanna leave my own life behind \n Not a yes sir, not a follower \n Fit the box, fit the mold \n Have a seat in the foyer, take a number \n I was lightning before the thunder \n \n Thunder, feel the thunder \n Lightning then the thunder \n Thunder, feel the thunder \n Lightning then the thunder \n Thunder, thunder 🎶 \n **-Thunder**"
        )
    if x == 24:
        await event.edit(
            "🎶 Oh, love \n How I miss you every single day \n When I see you on those streets \n Oh, love \n Tell me there's a river I can swim that will bring you back to me \n 'Cause I don't know how to love someone else \n I don't know how to forget your face \n No, love \n God, I miss you every single day and now you're so far away \n So far away 🎶 \n **-So Far Away**"
        )
    if x == 25:
        await event.edit(
            "🎶 And if you feel you're sinking, I will jump right over \n Into cold, cold water for you \n And although time may take us into different places \n I will still be patient with you \n And I hope you know 🎶 \n **-Cold Water**"
        )
    if x == 26:
        await event.edit(
            "🎶 When you feel my heat \n Look into my eyes \n It's where my demons hide \n It's where my demons hide \n Don't get too close \n It's dark inside \n It's where my demons hide \n It's where my demons hide 🎶 \n **-Demons**"
        )
    if x == 27:
        await event.edit(
            "🎶 Who do you love, do you love now? \n I wanna know the truth (whoa) \n Who do you love, do you love now? \n I know it's someone new \n You ain't gotta make it easy, where you been sleepin'? 🎶 \n **-Who do  Love? **"
        )
    if x == 28:
        await event.edit(
            "🎶 Your touch is magnetic \n 'Cause I can't forget it \n (There's a power pulling me back to you) \n And baby I'll let it \n 'Cause you're so magnetic I get it \n (When I'm waking up with you, oh) 🎶 \n **-Magnetic**"
        )
    if x == 29:
        await event.edit(
            "🎶 Girl my body don't lie, I'm outta my mind \n Let it rain over me, I'm rising so high \n Out of my mind, so let it rain over me \n \n Ay ay ay, ay ay ay let it rain over me \n Ay ay ay, ay ay ay let it rain over me 🎶 \n **-Rain over Me**"
        )
    if x == 30:
        await event.edit(
            "🎶 I miss the taste of a sweeter life \n I miss the conversation \n I'm searching for a song tonight \n I'm changing all of the stations \n I like to think that we had it all \n We drew a map to a better place \n But on that road I took a fall \n Oh baby why did you run away? \n \n I was there for you \n In your darkest times \n I was there for you \n In your darkest night 🎶 \n **-Maps**"
        )
    if x == 31:
        await event.edit(
            "🎶 I wish—I wish that I was bulletproof, bulletproof \n I wish—I wish that I was bulletproof, bulletproof \n (Bullet-bulletproof, bullet-bullet-bulletproof) \n I'm trippin' on my words and my patience \n Writing every verse in a cadence \n To tell you how I feel, how I feel, how I feel (Yeah) \n This is how I deal, how I deal, how I deal (Yeah) \n With who I once was, now an acquaintance \n Think my confidence (My confidence) is in the basement \n Tryin' to keep it real, keep it real, keep it real (Yeah) \n 'Cause I'm not made of steel, made of steel 🎶 \n **-Bulletproof**"
        )
    if x == 32:
        await event.edit(
            "🎶 You won't find him down on Sunset \n Or at a party in the hills \n At the bottom of the bottle \n Or when you're tripping on some pills \n When they sold you the dream you were just 16 \n Packed a bag and ran away \n And it's a crying shame you came all this way \n 'Cause you won't find Jesus in LA \n And it's a crying shame you came all this way \n 'Cause you won't find Jesus in LA 🎶 \n **-Jesus in LA**"
        )
    if x == 33:
        await event.edit("Not in a mood to sing. Sorry!")


@bot.on(admin_cmd(pattern=f"hps$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hps$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "__.....__")
    await sleep(2)
    x = random.randrange(1, 40)
    if x == 1:
        await event.edit("**Aberto**")
    if x == 2:
        await event.edit("**Accio**")
    if x == 3:
        await event.edit("**Aguamenti**")
    if x == 4:
        await event.edit("**Alohomora**")
    if x == 5:
        await event.edit("**Avada Kedavra**")
    if x == 6:
        await event.edit("**Colloportus**")
    if x == 7:
        await event.edit("**Confringo**")
    if x == 8:
        await event.edit("**Confundo**")
    if x == 9:
        await event.edit("**Crucio**")
    if x == 10:
        await event.edit("**Descendo**")
    if x == 11:
        await event.edit("**Diffindo**")
    if x == 12:
        await event.edit("**Engorgio**")
    if x == 13:
        await event.edit("**Episkey**")
    if x == 14:
        await event.edit("**Evanesco**")
    if x == 15:
        await event.edit("**Expecto Patronum**")
    if x == 16:
        await event.edit("**Expelliarmus**")
    if x == 17:
        await event.edit("**Finestra**")
    if x == 18:
        await event.edit("**Homenum Revelio**")
    if x == 19:
        await event.edit("**Impedimenta**")
    if x == 20:
        await event.edit("**Imperio**")
    if x == 21:
        await event.edit("**Impervius**")
    if x == 22:
        await event.edit("**Incendio**")
    if x == 23:
        await event.edit("**Levicorpus**")
    if x == 24:
        await event.edit("**Lumos**")
    if x == 25:
        await event.edit("**Muffliato**")
    if x == 26:
        await event.edit("**Obliviate**")
    if x == 27:
        await event.edit("**Petrificus Totalus**")
    if x == 28:
        await event.edit("**Priori Incantato**")
    if x == 29:
        await event.edit("**Protego**")
    if x == 30:
        await event.edit("**Reducto**")
    if x == 31:
        await event.edit("**Rennervate**")
    if x == 32:
        await event.edit("**Revelio**")
    if x == 33:
        await event.edit("**Rictusempra**")
    if x == 34:
        await event.edit("**Riddikulus**")
    if x == 35:
        await event.edit("**Scourgify**")
    if x == 36:
        await event.edit("**Sectumsempra**")
    if x == 37:
        await event.edit("**Silencio**")
    if x == 37:
        await event.edit("**Stupefy**")
    if x == 38:
        await event.edit("**Tergeo**")
    if x == 39:
        await event.edit("**Wingardium Leviosa**")


@bot.on(admin_cmd(pattern=f"gott$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gott$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Typing...")
    await sleep(2)
    x = random.randrange(1, 40)
    if x == 1:
        await event.edit('__"The man who passes the sentence should swing the sword."__')
    if x == 2:
        await event.edit(
            '__"When the snows fall and the white winds blow, the lone wolf dies but the pack survives!"__'
        )
    if x == 3:
        await event.edit('__"The things I do for love!"__')
    if x == 4:
        await event.edit(
            '__"I have a tender spot in my heart for cripples, bastards and broken things."__'
        )
    if x == 5:
        await event.edit(
            '__"Death is so terribly final, while life is full of possibilities."__'
        )
    if x == 6:
        await event.edit(
            '__"Once you’ve accepted your flaws, no one can use them against you."__'
        )
    if x == 7:
        await event.edit('__"If I look back I am lost."__')
    if x == 8:
        await event.edit('__"When you play the game of thrones, you win or you die."__')
    if x == 9:
        await event.edit(
            '__"I grew up with soldiers. I learned how to die a long time ago."__'
        )
    if x == 10:
        await event.edit('__"What do we say to the Lord of Death?\nNot Today!"__')
    if x == 11:
        await event.edit('__"Every flight begins with a fall."__')
    if x == 12:
        await event.edit('__"Different roads sometimes lead to the same castle."__')
    if x == 13:
        await event.edit(
            '__"Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you."__'
        )
    if x == 14:
        await event.edit(
            '__"The day will come when you think you are safe and happy, and your joy will turn to ashes in your mouth."__'
        )
    if x == 15:
        await event.edit('__"The night is dark and full of terrors."__')
    if x == 16:
        await event.edit('__"You know nothing, Jon Snow."__')
    if x == 17:
        await event.edit('__"Night gathers, and now my watch begins!"__')
    if x == 18:
        await event.edit('__"A Lannister always pays his debts."__')
    if x == 19:
        await event.edit('__"Burn them all!"__')
    if x == 20:
        await event.edit('__"What do we say to the God of death?"__')
    if x == 21:
        await event.edit('__"There\'s no cure for being a c*nt."__')
    if x == 22:
        await event.edit('__"Winter is coming!"__')
    if x == 23:
        await event.edit('__"That\'s what I do: I drink and I know things."__')
    if x == 24:
        await event.edit(
            '__"I am the dragon\'s daughter, and I swear to you that those who would harm you will die screaming."__'
        )
    if x == 25:
        await event.edit(
            '__"A lion does not concern himself with the opinion of sheep."__'
        )
    if x == 26:
        await event.edit('__"Chaos isn\'t a pit. Chaos is a ladder."__')
    if x == 27:
        await event.edit(
            '__"I understand that if any more words come pouring out your c*nt mouth, I\'m gonna have to eat every f*cking chicken in this room."__'
        )
    if x == 28:
        await event.edit(
            '__"If you think this has a happy ending, you haven\'t been paying attention."__'
        )
    if x == 29:
        await event.edit(
            '__"If you ever call me sister again, I\'ll have you strangled in your sleep."__'
        )
    if x == 30:
        await event.edit('__"A girl is Arya Stark of Winterfell. And I\'m going home."__')
    if x == 31:
        await event.edit("__\"Any man who must say 'I am the King' is no true King.\"__")
    if x == 32:
        await event.edit('__"If I fall, don\'t bring me back."__')
    if x == 33:
        await event.edit(
            "__\"Lannister, Targaryen, Baratheon, Stark, Tyrell... they're all just spokes on a wheel. This one's on top, then that one's on top, and on and on it spins, crushing those on the ground.\"__"
        )
    if x == 34:
        await event.edit('__"Hold the door!__')
    if x == 35:
        await event.edit(
            '__"When people ask you what happened here, tell them the North remembers. Tell them winter came for House Frey."__'
        )
    if x == 36:
        await event.edit('__"Nothing f*cks you harder than time."__')
    if x == 37:
        await event.edit(
            '__"There is only one war that matters. The Great War. And it is here."__'
        )
    if x == 38:
        await event.edit('__"Power is power!"__')
    if x == 39:
        await event.edit('__"I demand a trial by combat!"__')
    if x == 40:
        await event.edit('__"I wish I was the monster you think I am!"__')
    if x == 41:
        await event.edit(
            "Never forget what you are. The rest of the world will not.Wear it like armor,\n and it can never be used to hurt you."
        )
    if x == 42:
        await event.edit("There is only one thing we say to death: **Not today.**")
    if x == 43:
        await event.edit(
            "If you think this has a happy ending, you haven’t been **paying attention**."
        )
    if x == 44:
        await event.edit("Chaos isn’t a pit. Chaos is a ladder.")
    if x == 45:
        await event.edit("You know nothing, **Jon Snow**")
    if x == 46:
        await event.edit("**Winter** is coming.")
    if x == 47:
        await event.edit("When you play the **game of thrones**, you win or you die.")
    if x == 48:
        await event.edit(
            "I'm not going to **stop** the wheel, I'm going to **break** the wheel."
        )
    if x == 49:
        await event.edit(
            "When people ask you what happened here, tell them the **North remembers**. Tell them winter came for **House Frey**."
        )
    if x == 50:
        await event.edit(
            "When the snows fall and the white winds blow,\n the lone wolf dies, but the pack **survives**."
        )


@bot.on(admin_cmd(pattern=f"gotm$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gotm$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Thinking... 🤔")
    await sleep(2)
    x = random.randrange(1, 30)
    if x == 1:
        await event.edit(
            "[To your teachers on failing you in all your papers confidently, every time...](https://telegra.ph/file/431d178780f9bff353047.jpg)",
            link_preview=True,
        )
    if x == 2:
        await event.edit(
            "[A shift from the mainstream darling, sweetheart, jaanu, and what not...](https://telegra.ph/file/6bbb86a6c7d2c4a61e102.jpg)",
            link_preview=True,
        )
    if x == 3:
        await event.edit(
            "[To the guy who's friendzone-ing you...](https://telegra.ph/file/8930b05e9535e9b9b8229.jpg)",
            link_preview=True,
        )
    if x == 4:
        await event.edit(
            "[When your friend asks for his money back...](https://telegra.ph/file/2df575ab38df5ce9dbf5e.jpg)",
            link_preview=True,
        )
    if x == 5:
        await event.edit(
            "[A bad-ass reply to who do you think you are?](https://telegra.ph/file/3a35a0c37f4418da9f702.jpg)",
            link_preview=True,
        )
    if x == 6:
        await event.edit(
            "[When the traffic police stops your car and asks for documents...](https://telegra.ph/file/52612d58d6a61315a4c3a.jpg)",
            link_preview=True,
        )
    if x == 7:
        await event.edit(
            "[ When your friend asks about the food he/she just cooked and you don't want to break his/her heart...](https://telegra.ph/file/702df36088f5c26fef931.jpg)",
            link_preview=True,
        )
    if x == 8:
        await event.edit(
            "[When you're out of words...](https://telegra.ph/file/ba748a74bcab4a1135d2a.jpg)",
            link_preview=True,
        )
    if x == 9:
        await event.edit(
            "[When you realize your wallet is empty...](https://telegra.ph/file/a4508324b496d3d4580df.jpg)",
            link_preview=True,
        )
    if x == 10:
        await event.edit(
            "[When shit is about to happen...](https://telegra.ph/file/e15d9d64f9f25e8d05f19.jpg)",
            link_preview=True,
        )
    if x == 11:
        await event.edit(
            "[When that oversmart classmate shouts a wrong answer in class...](https://telegra.ph/file/1a225a2e4b7bfd7f7a809.jpg)",
            link_preview=True,
        )
    if x == 12:
        await event.edit(
            "[When things go wrong in a big fat Indian wedding...](https://telegra.ph/file/db69e17e85bb444caca32.jpg)",
            link_preview=True,
        )
    if x == 13:
        await event.edit(
            "[A perfect justification for breaking a promise...](https://telegra.ph/file/0b8fb8fb729d157844ac9.jpg)",
            link_preview=True,
        )
    if x == 14:
        await event.edit(
            "[When your friend just won't stop LOL-ing on something silly you said...](https://telegra.ph/file/247fa54106c32318797ae.jpg)",
            link_preview=True,
        )
    if x == 15:
        await event.edit(
            "[When someone makes a joke on you...](https://telegra.ph/file/2ee216651443524eaafcf.jpg)",
            link_preview=True,
        )
    if x == 16:
        await event.edit(
            "[When your professor insults you in front of the class...](https://telegra.ph/file/a2dc7317627e514a8e180.jpg)",
            link_preview=True,
        )
    if x == 17:
        await event.edit(
            "[When your job interviewer asks if you're nervous...](https://telegra.ph/file/9cc147d0bf8adbebf164b.jpg)",
            link_preview=True,
        )
    if x == 18:
        await event.edit(
            "[When you're sick of someone complaining about the heat outside...](https://telegra.ph/file/9248635263c52b968f968.jpg)",
            link_preview=True,
        )
    if x == 19:
        await event.edit(
            "[When your adda is occupied by outsiders...](https://telegra.ph/file/ef537007ba6d9d4cbd384.jpg)",
            link_preview=True,
        )
    if x == 20:
        await event.edit(
            "[When you don't have the right words to motivate somebody...](https://telegra.ph/file/2c932d769ae4c5fbed368.jpg)",
            link_preview=True,
        )
    if x == 21:
        await event.edit(
            "[When the bouncer won't let you and your group of friends in because you're all under-aged...](https://telegra.ph/file/6c8ca79f1e20ebd04391c.jpg)",
            link_preview=True,
        )
    if x == 22:
        await event.edit(
            "[To the friend who wants you to take the fall for his actions...](https://telegra.ph/file/d4171b9bc9104b5d972d9.jpg)",
            link_preview=True,
        )
    if x == 23:
        await event.edit(
            "[When that prick of a bully wouldn't take your words seriously...](https://telegra.ph/file/188d73bd24cf866d8d8d0.jpg)",
            link_preview=True,
        )
    if x == 24:
        await event.edit(
            "[ When you're forced to go shopping/watch a football match with your partner...](https://telegra.ph/file/6e129f138c99c1886cb2b.jpg)",
            link_preview=True,
        )
    if x == 25:
        await event.edit(
            "[To the large queue behind you after you get the last concert/movie ticket...](https://telegra.ph/file/2423f213dd4e4282a31ea.jpg)",
            link_preview=True,
        )
    if x == 26:
        await event.edit(
            "[When your parents thought you'd fail but you prove them wrong...](https://telegra.ph/file/39cc5098466f622bf21e3.jpg)",
            link_preview=True,
        )
    if x == 27:
        await event.edit(
            "[A justification for not voting!](https://telegra.ph/file/87d475a8f9a8350d2450e.jpg)",
            link_preview=True,
        )
    if x == 28:
        await event.edit(
            "[When your partner expects you to do too many things...](https://telegra.ph/file/68bc768d36e08862bf94e.jpg)",
            link_preview=True,
        )
    if x == 29:
        await event.edit(
            "[When your friends cancel on the plan you made at the last minute...](https://telegra.ph/file/960b58c8f625b17613307.jpg)",
            link_preview=True,
        )
    if x == 30:
        await event.edit(
            "[For that friend of yours who does not like loud music and head banging...](https://telegra.ph/file/acbce070d3c52b921b2bd.jpg)",
            link_preview=True,
        )


@bot.on(admin_cmd(pattern="bello$", outgoing=True))
@bot.on(sudo_cmd(pattern="bello$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Typing....")
    await sleep(2)
    x = random.randrange(1, 101)
    if x == 1:
        await event.edit(
            '__"Underwater bubbles and raindrops are total opposites of each other."__'
        )
    if x == 2:
        await event.edit(
            '__"If you buy an eraser you are literally paying for your mistakes."__'
        )
    if x == 3:
        await event.edit(
            '__"The Person you care for most has the potential to destroy you the most."__'
        )
    if x == 4:
        await event.edit(
            '__"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."__'
        )
    if x == 5:
        await event.edit(
            '__"Any video with “wait for it” in the title is simply too long."__'
        )
    if x == 6:
        await event.edit(
            '__"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you."__'
        )
    if x == 7:
        await event.edit(
            '__"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."__'
        )
    if x == 8:
        await event.edit(
            '__"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."__'
        )
    if x == 9:
        await event.edit(
            '__"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back."__'
        )
    if x == 10:
        await event.edit(
            '__"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."__'
        )
    if x == 11:
        await event.edit('__"A folder is for things that you don\'t want to fold."__')
    if x == 12:
        await event.edit(
            '__"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."__'
        )
    if x == 13:
        await event.edit(
            '__"If everything goes smoothly, you probably won\'t remember today."__'
        )
    if x == 14:
        await event.edit(
            '__"When you meet new people in real life, you unlock more characters for your dream world."__'
        )
    if x == 15:
        await event.edit(
            '__"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it."__'
        )
    if x == 16:
        await event.edit(
            '__"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."__'
        )
    if x == 17:
        await event.edit(
            '__"Parents worry about what their sons download and worry about what their daughters upload."__'
        )
    if x == 18:
        await event.edit(
            '__"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."__'
        )
    if x == 19:
        await event.edit(
            "__\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"__"
        )
    if x == 20:
        await event.edit('__"Technically, no one has ever been in an empty room."__')
    if x == 21:
        await event.edit(
            '__"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there."__'
        )
    if x == 22:
        await event.edit(
            "__\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"__"
        )
    if x == 23:
        await event.edit(
            '__"Every single decision you ever made has brought you to read this sentence."__'
        )
    if x == 24:
        await event.edit("__\"The word 'quiet' is often said very loud.\"__")
    if x == 25:
        await event.edit(
            '__"Everybody wants you to work hard, but nobody wants to hear about how hard you work."__'
        )
    if x == 26:
        await event.edit(
            '__"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."__'
        )
    if x == 27:
        await event.edit(
            '__"No one remembers your awkward moments but they’re too busy remembering their own."__'
        )
    if x == 28:
        await event.edit(
            '__"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."__'
        )
    if x == 29:
        await event.edit(
            "__\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"__"
        )
    if x == 30:
        await event.edit(
            '__"The biggest irony is that computers & mobiles were invented to save out time!"__'
        )
    if x == 31:
        await event.edit(
            '__"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."__'
        )
    if x == 32:
        await event.edit(
            '__"You know you’re getting old when your parents start disappointing you, instead of you disappointing them."__'
        )
    if x == 33:
        await event.edit(
            '__"Humans are designed to learn through experience yet the education system has made it so we get no experience."__'
        )
    if x == 34:
        await event.edit(
            '__"By focusing on blinking, you blink slower... Same for breathing."__'
        )
    if x == 35:
        await event.edit(
            '__"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."__'
        )
    if x == 36:
        await event.edit(
            '__"Characters that get married in fiction were literally made for each other."__'
        )
    if x == 37:
        await event.edit(
            '__"Babies are a clean hard drive that can be programmed with any language."__'
        )
    if x == 38:
        await event.edit(
            "__\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"__"
        )
    if x == 39:
        await event.edit(
            "__\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"__"
        )
    if x == 40:
        await event.edit(
            '__"Maybe we don\'t find time travelers because we all die in 25-50 years."__'
        )
    if x == 41:
        await event.edit(
            '__"Sleep is the trial version of death, It even comes with ads based on your activity."__'
        )
    if x == 42:
        await event.edit(
            '__"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"__'
        )
    if x == 43:
        await event.edit(
            '__"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."__'
        )
    if x == 44:
        await event.edit(
            '__"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."__'
        )
    if x == 45:
        await event.edit('__"If Greenland actually turns green, we\'re all screwed."__')
    if x == 46:
        await event.edit(
            '__"If someone says clever things in your dream, it actually shows your own cleverness."__'
        )
    if x == 47:
        await event.edit(
            '__"Famous movie quotes are credited to the actor and not the actual writer who wrote them."__'
        )
    if x == 48:
        await event.edit(
            '__"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."__'
        )
    if x == 49:
        await event.edit('__"Ask yourself why the the brain ignores the second the."__')
    if x == 50:
        await event.edit(
            '__"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."__'
        )
    if x == 51:
        await event.edit(
            '__"It will be a lot harder for kids to win against their parents in video games in the future."__'
        )
    if x == 52:
        await event.edit(
            '__"Everyone has flaws, if you don\'t recognize yours, you have a new one."__'
        )
    if x == 53:
        await event.edit('__"Raising a child is training your replacement."__')
    if x == 54:
        await event.edit(
            "__\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"__"
        )
    if x == 55:
        await event.edit(
            '__"There\'s always someone who hated you for no reason, and still does."__'
        )
    if x == 56:
        await event.edit(
            '__"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."__'
        )
    if x == 57:
        await event.edit(
            '__"The more important a good night\'s sleep is, the harder it is to fall asleep."__'
        )
    if x == 58:
        await event.edit(
            '__"Blessed are those that can properly describe the type of haircut they want to a new stylist."__'
        )
    if x == 59:
        await event.edit(
            "__\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"__"
        )
    if x == 60:
        await event.edit(
            '__"Theme park employees must be good at telling the difference between screams of horror and excitement."__'
        )
    if x == 61:
        await event.edit('__"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"__')
    if x == 62:
        await event.edit(
            '__"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."__'
        )
    if x == 63:
        await event.edit(
            '__"Listening to podcasts before bed is the adult version of story-time."__'
        )
    if x == 64:
        await event.edit(
            '__"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."__'
        )
    if x == 65:
        await event.edit('__"A ton of whales is really only like half a whale."__')
    if x == 66:
        await event.edit(
            '__"When you get old, the old you is technically the new you, and your young self is the old you."__'
        )
    if x == 67:
        await event.edit(
            '__"You probably won\'t find many negative reviews of parachutes on the Internet."__'
        )
    if x == 68:
        await event.edit(
            '__"We show the most love and admiration for people when they\'re no longer around to appreciate it."__'
        )
    if x == 69:
        await event.edit(
            "__\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"__"
        )
    if x == 70:
        await event.edit(
            '__"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."__'
        )
    if x == 71:
        await event.edit(
            "__\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"__"
        )
    if x == 72:
        await event.edit('__"The most effective alarm clock is a full bladder."__')
    if x == 73:
        await event.edit(
            '__"You probably just synchronized blinks with millions of people."__'
        )
    if x == 74:
        await event.edit(
            '__"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."__'
        )
    if x == 75:
        await event.edit(
            '__"Night before a day off is more satisfying than the actual day off."__'
        )
    if x == 76:
        await event.edit('__"We put paper in a folder to keep it from folding."__')
    if x == 77:
        await event.edit(
            '__"Somewhere, two best friends are meeting for the first time."__'
        )
    if x == 78:
        await event.edit(
            '__"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."__'
        )
    if x == 79:
        await event.edit(
            '__"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."__'
        )
    if x == 80:
        await event.edit(
            '__"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."__'
        )
    if x == 81:
        await event.edit('__"Wikipedia is what the internet was meant to be."__')
    if x == 82:
        await event.edit(
            '__"A theme park is the only place that you can hear screams in the distance and not be concerned."__'
        )
    if x == 83:
        await event.edit(
            '__"A wireless phone charger offers less freedom of movement than a wired one."__'
        )
    if x == 84:
        await event.edit(
            "__\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"__"
        )
    if x == 85:
        await event.edit(
            '__"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."__'
        )
    if x == 86:
        await event.edit(
            '__"If someday human teleportation becomes real, people will still be late for work."__'
        )
    if x == 87:
        await event.edit(
            '__"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"__'
        )
    if x == 88:
        await event.edit(
            '__"Doing something alone is kind of sad, but doing it solo is cool af."__'
        )
    if x == 89:
        await event.edit(
            '__"Your brain suddenly becomes perfect at proofreading after you post something."__'
        )
    if x == 90:
        await event.edit(
            '__"There\'s always that one song in your playlist that you always skip but never remove."__'
        )
    if x == 91:
        await event.edit(
            '__"Kids next century will probably hate us for taking all the good usernames."__'
        )
    if x == 92:
        await event.edit('__"Bubbles are to fish what rain is to humans."__')
    if x == 93:
        await event.edit(
            '__"The more people you meet, the more you realise and appreciate how well your parents raised you."__'
        )
    if x == 94:
        await event.edit('__"A comma is a short pause, a coma is a long pause."__')
    if x == 95:
        await event.edit('__"Someday you will either not wake up or not go to sleep."__')
    if x == 96:
        await event.edit(
            '__"Bermuda Triangle might be the exit portal of this simulation."__'
        )
    if x == 97:
        await event.edit(
            '__"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."__'
        )
    if x == 98:
        await event.edit(
            '__"By faith Abraham, when he was called to go out into a place which he should after receive for an inheritance, obeyed; and he went out, not knowing whither he went.  <Hebrews 11:8>."__'
        )
    if x == 99:
        await event.edit(
            '__"By faith Noah, being warned of God of things not seen as yet, moved with fear, prepared an ark to the saving of his house; by the which he condemned the world, and became heir of the righteousness which is by faith.  <Hebrews 11:7>."__'
        )
    if x == 100:
        await event.edit(
            '__"These words spake Jesus, and lifted up his eyes to heaven, and said, Father, the hour is come; glorify thy Son, that thy Son also may glorify thee:  <John 17:1>."__'
        )
    if x == 101:
        await event.edit(
            '__"As thou hast given him power over all flesh, that he should give eternal life to as many as thou hast given him.  <John 17:2>."__'
        )


@bot.on(admin_cmd(pattern=r"tip$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"tip$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Well, let me give you a life-pro tip... 😉")
    await sleep(2)
    x = random.randrange(1, 87)
    if x == 1:
        await event.edit(
            "__\"Before telling your landlord you're moving, ask them to fix anything broken that you're worried you might get charged for. They often will, and then when you move out they won't be able to take it out of your security deposit.\"__"
        )
    if x == 2:
        await event.edit(
            '__"Walking before solving a problem improves your creativity by an average of 60%."__'
        )
    if x == 3:
        await event.edit(
            '__"Wake up a little earlier than your alarm? Don’t go back to bed and wait for your alarm. Waking up naturally instead of to some sort of stimuli will help you get off to a better and healthier start to your day."__'
        )
    if x == 4:
        await event.edit(
            '__"Act like your future self is a real person. So when you see a chore that needs to be done, you can say "I\'ll do this now to be nice to my future self". Helps motivate to get things done because you\'re doing work for someone you want to help."__'
        )
    if x == 5:
        await event.edit(
            '__"Think of purchases as a percentage of your budget/account balance rather than their actual cost."__'
        )
    if x == 6:
        await event.edit(
            '__"Counting on fingers is a vital part of learning math, and children that do it from an early age develop much better math skills than those who have been told not to."__'
        )
    if x == 7:
        await event.edit(
            '__"There are just some things in life you can’t control or you’ll never know the real reason why. The only thing you can do is accept it and move on. Part of happiness is accepting the past happened or being proud of it."__'
        )
    if x == 8:
        await event.edit(
            '__"Make a recording of your voice with a sweet message or telling a story. If anything happens to you, your loved ones will greatly appreciate being able to listen to your voice again."__'
        )
    if x == 9:
        await event.edit(
            "__\"If someone is treating you to a meal and you're wondering how much you should spend, ask them what they're ordering to get a better idea of the range.\"__"
        )
    if x == 10:
        await event.edit(
            '__"Never leave water bottles, reading glasses, or anything else that can focus light in a spot that could get direct sunlight. A significant number of house/vehicle fires happen every year because of this."__'
        )
    if x == 11:
        await event.edit(
            '__"If you reach out to someone for help on a technical issue and they spend their valuable time helping you but are unable to resolve it, always try and let them know how it got resolved so they can help the next person with the same issue."__'
        )
    if x == 12:
        await event.edit(
            '__"If you find information on the internet that you may need again in the future, print the page to a PDF digital file. There is no guarantee that the page will be available again in the future, and now you will have a digital copy for future reference."__'
        )
    if x == 13:
        await event.edit(
            '__"If you want to learn another language, watch children’s shows in that language to pick up on it quicker."__'
        )
    if x == 14:
        await event.edit(
            '__"If you want to separate some pdf pages without using any new software. you can open the pdf file in chrome then click on print then select custom pages option, and finally choose to save as pdf."__'
        )
    if x == 15:
        await event.edit(
            '__"If you’re ever in the heat of an argument, always act like you’re being recorded. This helps you from saying things you don’t mean and could regret later."__'
        )
    if x == 16:
        await event.edit(
            '__"Make music playlists during times in your life when good things are happening and you are experiencing good feelings. Then when you\'re down later in life listen to those playlists to instantly feel better, and feel those good emotions again."__'
        )
    if x == 17:
        await event.edit(
            '__"When going on a first date, think in terms of "will I like them?" instead of "will they like me?""__'
        )
    if x == 18:
        await event.edit(
            r"__\"When researching things to do for your next leisure travel. Include \<location\> tourism scam into your search. All tourist heavy areas will have their own scams. This should not dampen your excitement but heighten your knowledge so your vacation will be more enjoyable.\"__"
        )
    if x == 19:
        await event.edit(
            '__"Just because you’ve know that person for years doesn’t mean you should stay friends with them. A toxic friend need to be cut out of your life."__'
        )
    if x == 20:
        await event.edit(
            '__"Tired of all the ads in one of the free (offline) game apps you’re playing? Go to your settings and turn off the apps access to cellular data. Enjoy the ad free game play!"__'
        )
    if x == 21:
        await event.edit(
            r"__\"Treat your monthly savings goal like a bill. At the end of the month, hold yourself accountable to \“pay it off\” like you would your rent or your utilities. This will keep you on track for your savings goals.\"__"
        )
    if x == 22:
        await event.edit(
            '__"If you need to wait until your boss is in a good mood to ask for something as simple as time off, you\'re in a toxic work environment and you need to take steps to exit sooner than later."__'
        )
    if x == 23:
        await event.edit(
            '__"When debating someone on a heated issue, start by looking for something to agree with them on. The rest of the conversation will be a lot less hostile if you establish common ground."__'
        )
    if x == 24:
        await event.edit(
            '__"Record random conversations with your parents and grandparents. Someday hearing their voice may be priceless to you."__'
        )
    if x == 25:
        await event.edit(
            "__\"If you're a student planning on your career, look up postings of your dream job, find the skills and qualifications you'll need, then work backwards from there.\"__"
        )
    if x == 26:
        await event.edit(
            "__\"If someone asks how your weekend was, assume they're really wanting to tell you about theirs. Keep your answer short and enthusiastically ask about theirs. It'll make their day.\"__"
        )
    if x == 27:
        await event.edit(
            '__"When traveling with a friend or family member, don’t be afraid to suggest breaking off to each do your own things for a day. Going solo can be enjoyable (eat/go wherever want at your own pace), plus it reduces you being sick of each other by the end of the trip."__'
        )
    if x == 28:
        await event.edit(
            '__"If you’ve got some free time and you’re planning on spending it watching tv/playing video games, etc. make yourself go on a short walk or do some brief exercise beforehand. You’ll probably end up going longer than you planned and you’ll feel better about relaxing after."__'
        )
    if x == 29:
        await event.edit(
            '__"When you get a new notebook, leave the first page blank. When you finish using the notebook, you can number the pages and use the first page as a table of contents."__'
        )
    if x == 30:
        await event.edit(
            '__"Don’t delete old playlists if you can prevent it; years later you can listen and not only rediscover music you were into but also experience whatever emotion you had associated with your tunes at the time."__'
        )
    if x == 31:
        await event.edit(
            '__"No matter how small the job is, wear correct masks/respirators/eye or ear protection. Your future self will thank you."__'
        )
    if x == 32:
        await event.edit(
            '__"Getting angry with people for making mistakes doesn\'t teach them not to make mistakes, it just teaches them to hide them."__'
        )
    if x == 33:
        await event.edit(
            "__\"When making conversation with someone you've just met, ask them what they've been listening to lately, rather than what their favorite kind of music is - it's fresh in their mind and they won't have to pick favorites on the spot.\"__"
        )
    if x == 34:
        await event.edit(
            '__"Learn to do -- and enjoy -- things by yourself. You\'re going to miss out on a lot of fun if you keep waiting for someone else to accompany you."__'
        )
    if x == 35:
        await event.edit(
            '__"If you want someone to really listen to you, then start the conversation with "I shouldn\'t be telling you this, but...""__'
        )
    if x == 36:
        await event.edit(
            '__"Do you not like having bitter coffee but don\'t want to add sugar for dietary or other reasons? Add a pinch of salt instead, it removes the bitter taste while not making your coffee taste salty."__'
        )
    if x == 37:
        await event.edit(
            '__"Don\'t choose a common sound for your alarm clock to wake up. If you hear your alarm clock sound any other time, you will get anxiety."__'
        )
    if x == 38:
        await event.edit(
            '__"Keep your water bottle near you and your alarm far from you in the morning for a great start to the day!"__'
        )
    if x == 39:
        await event.edit(
            '__"If you borrow money from someone, don’t let it get to the point that he/she has to ask for it back. It sucks for both. If you can’t repay now, show intent by paying what you can and keeping the other person posted often"__'
        )
    if x == 40:
        await event.edit(
            '__"Don\'t brag about knowledge you just acquired, simply explain it. You will learn humility, plus people often like to learn new things."__'
        )
    if x == 41:
        await event.edit(
            '__"If you have a favorite movie you’ve seen several (or hundreds) of times, try watching it with subtitles/closed captioning on. You might be surprised just how many lines you heard wrong or missed entirely."__'
        )
    if x == 42:
        await event.edit(
            '__"Write down great ideas when you get them; do that right away. You think you will never forget them, but you almost always will."__'
        )
    if x == 43:
        await event.edit(
            '__"If you’re not sure whether someone is waving at you or someone behind you, just smile at them. \n(It’ll save you the very awkward feeling of receiving a greeting meant for someone else.)"__'
        )
    if x == 44:
        await event.edit(
            '__"If you want to offer a deep and memorable compliment, ask someone how they did something. It gives them the opportunity to tell their story, and shows your genuine interest."__'
        )
    if x == 45:
        await event.edit(
            '__"Don’t hide the things that make you unique. If you smile a certain way or have any thing about you that is not normal, be confident with it. People will find it cute or attractive because it makes you special."__'
        )
    if x == 46:
        await event.edit(
            '__"When someone only remove one ear pod to talk to you, they most probably don\'t want a lengthy conversation."__'
        )
    if x == 47:
        await event.edit(
            "__\"If you haven't used your voice in a while (sleeping, lonely, etc) and suddenly need to take a phone call, hum for a few seconds prior. Your vocal cords won't let you down.\"__"
        )
    if x == 48:
        await event.edit(
            '__"Open chip bags upside down. They\'ve been sitting upright most of their lives which makes the seasoning settle to the bottom of the bag."__'
        )
    if x == 49:
        await event.edit(
            '__"If you tell people there is an invisible man in the sky that created the entire universe, most will believe you; if you tell them the paint is wet, most will touch it to be sure."__'
        )
    if x == 50:
        await event.edit(
            '__"When asked online to confirm "I am not a robot", if you long press on the tick box and release, you will not be asked to complete the "click all store front" etc tests."__'
        )
    if x == 51:
        await event.edit(
            '__"Buy yourself a good pillow. You use it every night and the difference between a good pillow and a stack of cheap ones is almost immediately noticeable."__'
        )
    if x == 52:
        await event.edit(
            '__"If you want your man to win in this world, treat him as a king at home, the world by itself call you a queen!"__'
        )
    if x == 53:
        await event.edit(
            '__"Be mindful of poorer friends when suggesting splitting the bill equally in a restaurant. Some people will choose cheaper options because they\'re on a budget."__'
        )
    if x == 54:
        await event.edit(
            r"__\"When you are trying to resolve an issue where someone else made an error, put the focus on the error and not the person. Example of this: Instead of saying, \“You didn’t send the attachment,\” I say, \“The attachment didn’t come through, please try sending it again.\”\"__"
        )
    if x == 55:
        await event.edit(
            '__"Buy a small bottle of perfume you have never tried on before going for a vacation and use it for while you\'re there. At any point after your vacation, you get a sniff of it, it brings back those memories instantly. Because scents are among the most powerful memory triggers."__'
        )
    if x == 56:
        await event.edit(
            "__\"If someone wishes you Merry Christmas and you don't celebrate Christmas, just say thank you. There's no need to tell them you don't celebrate. It just makes things awkward.\"__"
        )
    if x == 57:
        await event.edit(
            '__"When trying to focus on something (writing, revising, reading) listen to music with no words. This allows you to block out unwanted sound and having no lyrics can stop you from being distracted."__'
        )
    if x == 58:
        await event.edit(
            '__"If you are quitting a vice (smoking, drinking, etc.) treat yourself with the money you are saving. It makes quitting easier."__'
        )
    if x == 59:
        await event.edit(
            '__"Someone who likes you will often automatically look at you when they laugh or find something funny."__'
        )
    if x == 60:
        await event.edit(
            '__"Never shake spices over a hot pan. The steam will enter the bottle causing the spice to go hard."__'
        )
    if x == 61:
        await event.edit(
            '__"When starting a new change in your life such as going to the gym or quitting smoking, avoid telling friends or family. Their positive feedback can give you a false feeling of accomplishment tricking you into thinking you have already succeeded which can hinder your efforts to change."__'
        )
    if x == 62:
        await event.edit(
            '__"If you are composing an important message, do not enter the recipient until you have finished composing it so that you do not accidentally send an incomplete message."__'
        )
    if x == 63:
        await event.edit(
            '__"If you are nervous walking into a new place with a group of people, make sure you are the first to the building. You can hold the door for everyone else making yourself look kind, yet you will be the last one in and can follow everyone elses lead."__'
        )
    if x == 2:
        await event.edit(
            '__"If you\'re double checking a number or a sequence, read it backwards to avoid making the same mistake twice."__'
        )
    if x == 64:
        await event.edit(
            '__"Take photos of your parents doing things they do every day. When you get older, they will bring back memories more than any posed pic ever could."__'
        )
    if x == 65:
        await event.edit(
            "__\"If you're in a job interview and you're offered a glass of water, always accept. If you're asked a tough question, you can take a sip and get yourself some extra seconds to think of a response.\"__"
        )
    if x == 66:
        await event.edit(
            "__\"If you make a mistake, admit to the mistake, apologize, and explain what steps you'll take to prevent it from happening again in the future. It's very hard for people to yell at you if you've done that.\"__"
        )
    if x == 67:
        await event.edit(
            '__"Universities like MIT offer free online courses for subjects like Computer Science, Engineering, Psychology and more that include full lectures and exams."__'
        )
    if x == 68:
        await event.edit(
            "__\"Treat another persons phone or computer like you would their diary. Don't even touch it unless they allow you to. It's always for the best.\"__"
        )
    if x == 69:
        await event.edit(
            "__\"Don't undervalue yourself when deciding whether or not to apply for a new job. It's up to the person doing the hiring to determine if you are what they're looking for, and the only way to guarantee that you won't get the job is if you don't apply for it.\"__"
        )
    if x == 70:
        await event.edit(
            '__"When drying clothes in the sun, turn them inside out so the colours don’t fade in the sunlight."__'
        )
    if x == 71:
        await event.edit(
            '__"To listen to music on your phone via YouTube in the background, use the Chrome browser, go to the video, and request desktop site. This will allow you to listen anywhere on the phone."__'
        )
    if x == 72:
        await event.edit(
            '__"Whenever your smoke alarm goes off, give your dog a treat. They\'ll associate the alarm with the treat; so when the alarm goes off for real, your dog will come right to you."__'
        )
    if x == 73:
        await event.edit(
            '__"You never know what is taking place in a stranger\'s life. Try to be patient and passive if some seems to be "overreacting"."__'
        )
    if x == 74:
        await event.edit(
            '__"Everybody is genious of its own. But if you judge a fish by its ability to climb a tree rather than swimming, she will felt whole life like dumb. So master your field and recognise it very well rather than going after the blind suspections."__'
        )
    if x == 75:
        await event.edit(
            '__"Search a beautiful heart, not a beautiful face. Beautiful things are not always good, but good things are always beautiful."__'
        )
    if x == 76:
        await event.edit(
            '__"It\'s better to cross the line and suffer the consequences than to just stare at the line for the rest of your life."__'
        )
    if x == 77:
        await event.edit(
            '__"Rather than shushing someone who’s speaking too loudly, try just talking to them in a much quieter voice. They often pick up on the contrast in volume, and self-correct without feeling attacked."__'
        )
    if x == 78:
        await event.edit(
            '__"If there are no chances for job growth or improvement - it\'s time to move on. You are worth more the more you learn. Otherwise you are getting paid less the more you know."__'
        )
    if x == 79:
        await event.edit(
            '__"If you burn food to the bottom of a pot and can\'t scrub it out, put the pot back on the stove and boil water in it. It will loosen the burnt food and make it easier to clean."__'
        )
    if x == 80:
        await event.edit(
            '__"When filling out applications online, make sure you copy responses which typically take a long time to write, and paste them to a text file. You never know when you could get a server timeout."__'
        )
    if x == 81:
        await event.edit(
            '__"Being positive doesn’t mean we don’t get negative thoughts. It just means that we don’t allow those thoughts to control our life."__'
        )
    if x == 82:
        await event.edit(
            "__\"If you share an 'inside joke' with a friend around other people, just let them know what it is even if they won't get it. People don't appreciate being excluded.\"__"
        )
    if x == 83:
        await event.edit(
            '__"Never make fun of someone if they mispronounce a word. It means they learned it by reading."__'
        )
    if x == 84:
        await event.edit(
            '__"If a service dog without a person approaches you, it means that the person is in need of help."__'
        )
    if x == 85:
        await event.edit(
            '__"When taking a taxi ALWAYS get a receipt even if you don\'t need one. That way if you happen to accidentally leave a personal belonging behind you will have the company name and taxi number."__'
        )
    if x == 86:
        await event.edit(
            "__\"If you're buying a home printer for occasional use, get a laser printer; they're more expensive up front but way more economical in the long run.\"__"
        )
    if x == 87:
        await event.edit(
            '__"Go for that run, no one is looking at you, don\'t overthink it, do it!"__'
        )


@bot.on(admin_cmd(pattern=r"qt$"))
@bot.on(sudo_cmd(pattern=r"qt$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "selecting question...")
    await sleep(2)
    x = random.randrange(1, 60)
    if x == 1:
        await event.edit(
            '__"Arrange them in descending order of importance – MONEY, LOVE, FAMILY, CAREER, FRIENDS."__'
        )
    if x == 2:
        await event.edit(
            '__"If you had to change your name, what would your new name be, and why would you choose that name?"__'
        )
    if x == 3:
        await event.edit(
            '__"What’s the most interesting thing you’ve read or seen this week?"__'
        )
    if x == 4:
        await event.edit('__"What scene from a TV show will you never forget?"__')
    if x == 5:
        await event.edit(
            '__"If you could become a master in one skill, what skill would you choose?"__'
        )
    if x == 6:
        await event.edit('__"What three words can describe you?"__')
    if x == 7:
        await event.edit(
            '__"If you had to delete one app from your phone, what would it be?"__'
        )
    if x == 8:
        await event.edit(
            '__"Would you go out with me if I was the last person on earth?"__'
        )
    if x == 9:
        await event.edit('__"If you switched genders for the day, what would you do?"__')
    if x == 10:
        await event.edit(
            '__"If you could eat lunch with someone here. Who would you choose?"__'
        )
    if x == 11:
        await event.edit(
            '__"If you were told you only had one week left to live, what would you do?"__'
        )
    if x == 12:
        await event.edit(
            '__"What\'s number one item you would save from your burning house?"__'
        )
    if x == 13:
        await event.edit(
            '__"If you could only text one person for the rest of your life, but you could never talk to that person face to face, who would that be?"__'
        )
    if x == 14:
        await event.edit('__"How many kids do you want to have in the future?"__')
    if x == 15:
        await event.edit(
            '__"Who in this group would be the worst person to date? Why?"__'
        )
    if x == 16:
        await event.edit('__"What does your dream boy or girl look like?"__')
    if x == 17:
        await event.edit(
            '__"What would be in your web history that you’d be embarrassed if someone saw?"__'
        )
    if x == 18:
        await event.edit('__"Do you sing in the shower?"__')
    if x == 19:
        await event.edit('__"What’s the right age to get married?"__')
    if x == 20:
        await event.edit('__"What are your top 5 rules for life?"__')
    if x == 21:
        await event.edit(
            '__"If given an option, would you choose a holiday at the beach or in the mountains?"__'
        )
    if x == 22:
        await event.edit(
            '__"If you are made the president of your country, what would be the first thing that you will do?"__'
        )
    if x == 23:
        await event.edit(
            '__"If given a chance to meet 3 most famous people on the earth, who would it be, answer in order of preference."__'
        )
    if x == 24:
        await event.edit(
            '__"Have you ever wished to have a superpower, if so, what superpower you would like to have?"__'
        )
    if x == 25:
        await event.edit(
            '__"Can you spend an entire day without phone and internet? If yes, what would you do?"__'
        )
    if x == 26:
        await event.edit('__"Live-in relation or marriage, what do you prefer?"__')
    if x == 27:
        await event.edit('__"What is your favorite cuisine or type of food?"__')
    if x == 28:
        await event.edit(
            '__"What are some good and bad things about the education system in your country?"__'
        )
    if x == 29:
        await event.edit('__"What do you think of online education?"__')
    if x == 30:
        await event.edit('__"What are some goals you have failed to accomplish?"__')
    if x == 31:
        await event.edit('__"Will technology save the human race or destroy it?"__')
    if x == 32:
        await event.edit('__"What was the best invention of the last 50 years?"__')
    if x == 33:
        await event.edit(
            '__"Have you travelled to any different countries? Which ones?"__'
        )
    if x == 34:
        await event.edit(
            '__"Which sport is the most exciting to watch? Which is the most boring to watch?"__'
        )
    if x == 35:
        await event.edit('__"What’s the most addictive mobile game you have played?"__')
    if x == 36:
        await event.edit('__"How many apps do you have on your phone?"__')
    if x == 37:
        await event.edit('__"What was the last song you listened to?"__')
    if x == 38:
        await event.edit(
            '__"Do you prefer to watch movies in the theater or in the comfort of your own home?"__'
        )
    if x == 39:
        await event.edit('__"Do you like horror movies? Why or why not?"__')
    if x == 40:
        await event.edit(
            '__"How often do you help others? Who do you help? How do you help?"__'
        )
    if x == 41:
        await event.edit('__"What song do you play most often?"__')
    if x == 42:
        await event.edit('__"Suggest a new rule that should be added in this group!"__')
    if x == 43:
        await event.edit('__"What app on your phone do you think I should get?"__')
    if x == 44:
        await event.edit(
            '__"What website or app has completely changed your life for better or for worse?"__'
        )
    if x == 45:
        await event.edit('__"What isn’t real but you desperately wish it was?"__')
    if x == 46:
        await event.edit('__"What thing do you really wish you could buy right now?"__')
    if x == 47:
        await event.edit(
            '__"If you could ban an admin from this group. Who would you prefer ?"__'
        )
    if x == 48:
        await event.edit(
            '__"What would you do if someone left a duffle bag filled with $2,000,000 on your back porch?"__'
        )
    if x == 49:
        await event.edit('__"Who is the luckiest person you know?"__')
    if x == 50:
        await event.edit(
            '__"If you could visit someone\'s house in this group, who would it be ?"__'
        )
    if x == 51:
        await event.edit('__"What are you tired of hearing about?"__')
    if x == 52:
        await event.edit(
            '__"If you died today, what would your greatest achievement be?"__'
        )
    if x == 53:
        await event.edit('__"What method will you choose to kill yourself?"__')
    if x == 54:
        await event.edit('__"What’s the best news you\'ve heard in the last 24 hours?"__')
    if x == 55:
        await event.edit(
            '__"What is the most important change that should be made to your country’s education system?"__'
        )
    if x == 56:
        await event.edit('__"Send your favourite sticker pack."__')
    if x == 57:
        await event.edit('__"Send your favourite animated sticker pack."__')
    if x == 58:
        await event.edit('__"Send your favourite video or gif."__')
    if x == 59:
        await event.edit('__"Send your favourite emojies"__')
    if x == 60:
        await event.edit(
            '__"What’s something you misunderstood as a child and only realized much later was wrong?"__'
        )


@bot.on(admin_cmd(pattern=f"logic$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"logic$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    x = random.randrange(1, 104)
    event = await edit_or_reply(event, "__Wait me getting a logic for you__")
    await sleep(2)
    if x == 1:
        await event.edit(
            '__"Underwater bubbles and raindrops are total opposites of each other."__'
        )
    if x == 2:
        await event.edit(
            '__"If you buy an eraser you are literally paying for your mistakes."__'
        )
    if x == 3:
        await event.edit(
            '__"The Person you care for most has the potential to destroy you the most."__'
        )
    if x == 4:
        await event.edit(
            '__"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."__'
        )
    if x == 5:
        await event.edit(
            '__"Any video with ?wait for it? in the title is simply too long."__'
        )
    if x == 6:
        await event.edit(
            '__"Your age in years is how many times you?ve circled the Sun, but your age in months is how many times the Moon has circled you."__'
        )
    if x == 7:
        await event.edit(
            '__"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."__'
        )
    if x == 8:
        await event.edit(
            '__"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."__'
        )
    if x == 9:
        await event.edit(
            '__"The most crushing feeling is when someone smiles at you on the street and you don?t react fast enough to smile back."__'
        )
    if x == 10:
        await event.edit(
            '__"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."__'
        )
    if x == 11:
        await event.edit('__"A folder is for things that you don\'t want to fold."__')
    if x == 12:
        await event.edit(
            '__"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."__'
        )
    if x == 13:
        await event.edit(
            '__"If everything goes smoothly, you probably won\'t remember today."__'
        )
    if x == 14:
        await event.edit(
            '__"When you meet new people in real life, you unlock more characters for your dream world."__'
        )
    if x == 15:
        await event.edit(
            '__"Maybe if they renamed sunscreen to ?anti-cancer cream? more people would wear it."__'
        )
    if x == 16:
        await event.edit(
            '__"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."__'
        )
    if x == 17:
        await event.edit(
            '__"Parents worry about what their sons download and worry about what their daughters upload."__'
        )
    if x == 18:
        await event.edit(
            '__"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."__'
        )
    if x == 19:
        await event.edit(
            "__\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"__"
        )
    if x == 20:
        await event.edit('__"Technically, no one has ever been in an empty room."__')
    if x == 21:
        await event.edit(
            '__"An onion is the bass player of food. You would probably not enjoy it solo, but you?d miss it if it wasn?t there."__'
        )
    if x == 22:
        await event.edit(
            "__\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"__"
        )
    if x == 23:
        await event.edit(
            '__"Every single decision you ever made has brought you to read this sentence."__'
        )
    if x == 24:
        await event.edit("__\"The word 'quiet' is often said very loud.\"__")
    if x == 25:
        await event.edit(
            '__"Everybody wants you to work hard, but nobody wants to hear about how hard you work."__'
        )
    if x == 26:
        await event.edit(
            '__"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."__'
        )
    if x == 27:
        await event.edit(
            '__"No one remembers your awkward moments but they?re too busy remembering their own."__'
        )
    if x == 28:
        await event.edit(
            '__"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."__'
        )
    if x == 29:
        await event.edit(
            "__\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"__"
        )
    if x == 30:
        await event.edit(
            '__"The biggest irony is that computers & mobiles were invented to save out time!"__'
        )
    if x == 31:
        await event.edit(
            '__"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."__'
        )
    if x == 32:
        await event.edit(
            '__"You know you?re getting old when your parents start disappointing you, instead of you disappointing them."__'
        )
    if x == 33:
        await event.edit(
            '__"Humans are designed to learn through experience yet the education system has made it so we get no experience."__'
        )
    if x == 34:
        await event.edit(
            '__"By focusing on blinking, you blink slower... Same for breathing."__'
        )
    if x == 35:
        await event.edit(
            '__"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."__'
        )
    if x == 36:
        await event.edit(
            '__"Characters that get married in fiction were literally made for each other."__'
        )
    if x == 37:
        await event.edit(
            '__"Babies are a clean hard drive that can be programmed with any language."__'
        )
    if x == 38:
        await event.edit(
            "__\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"__"
        )
    if x == 39:
        await event.edit(
            "__\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"__"
        )
    if x == 40:
        await event.edit(
            '__"Maybe we don\'t find time travelers because we all die in 25-50 years."__'
        )
    if x == 41:
        await event.edit(
            '__"Sleep is the trial version of death, It even comes with ads based on your activity."__'
        )
    if x == 42:
        await event.edit(
            '__"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"__'
        )
    if x == 43:
        await event.edit(
            '__"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."__'
        )
    if x == 44:
        await event.edit(
            '__"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."__'
        )
    if x == 45:
        await event.edit('__"If Greenland actually turns green, we\'re all screwed."__')
    if x == 46:
        await event.edit(
            '__"If someone says clever things in your dream, it actually shows your own cleverness."__'
        )
    if x == 47:
        await event.edit(
            '__"Famous movie quotes are credited to the actor and not the actual writer who wrote them."__'
        )
    if x == 48:
        await event.edit(
            '__"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."__'
        )
    if x == 49:
        await event.edit('__"Ask yourself why the the brain ignores the second the."__')
    if x == 50:
        await event.edit(
            '__"You?ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."__'
        )
    if x == 51:
        await event.edit(
            '__"It will be a lot harder for kids to win against their parents in video games in the future."__'
        )
    if x == 52:
        await event.edit(
            '__"Everyone has flaws, if you don\'t recognize yours, you have a new one."__'
        )
    if x == 53:
        await event.edit('__"Raising a child is training your replacement."__')
    if x == 54:
        await event.edit(
            "__\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"__"
        )
    if x == 55:
        await event.edit(
            '__"There\'s always someone who hated you for no reason, and still does."__'
        )
    if x == 56:
        await event.edit(
            '__"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."__'
        )
    if x == 57:
        await event.edit(
            '__"The more important a good night\'s sleep is, the harder it is to fall asleep."__'
        )
    if x == 58:
        await event.edit(
            '__"Blessed are those that can properly describe the type of haircut they want to a new stylist."__'
        )
    if x == 59:
        await event.edit(
            "__\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"__"
        )
    if x == 60:
        await event.edit(
            '__"Theme park employees must be good at telling the difference between screams of horror and excitement."__'
        )
    if x == 61:
        await event.edit('__"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"__')
    if x == 62:
        await event.edit(
            '__"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."__'
        )
    if x == 63:
        await event.edit(
            '__"Listening to podcasts before bed is the adult version of story-time."__'
        )
    if x == 64:
        await event.edit(
            '__"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."__'
        )
    if x == 65:
        await event.edit('__"A ton of whales is really only like half a whale."__')
    if x == 66:
        await event.edit(
            '__"When you get old, the old you is technically the new you, and your young self is the old you."__'
        )
    if x == 67:
        await event.edit(
            '__"You probably won\'t find many negative reviews of parachutes on the Internet."__'
        )
    if x == 68:
        await event.edit(
            '__"We show the most love and admiration for people when they\'re no longer around to appreciate it."__'
        )
    if x == 69:
        await event.edit(
            "__\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"__"
        )
    if x == 70:
        await event.edit(
            '__"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."__'
        )
    if x == 71:
        await event.edit(
            "__\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"__"
        )
    if x == 72:
        await event.edit('__"The most effective alarm clock is a full bladder."__')
    if x == 73:
        await event.edit(
            '__"You probably just synchronized blinks with millions of people."__'
        )
    if x == 74:
        await event.edit(
            '__"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."__'
        )
    if x == 75:
        await event.edit(
            '__"Night before a day off is more satisfying than the actual day off."__'
        )
    if x == 76:
        await event.edit('__"We put paper in a folder to keep it from folding."__')
    if x == 77:
        await event.edit(
            '__"Somewhere, two best friends are meeting for the first time."__'
        )
    if x == 78:
        await event.edit(
            '__"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."__'
        )
    if x == 79:
        await event.edit(
            '__"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."__'
        )
    if x == 80:
        await event.edit(
            '__"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."__'
        )
    if x == 81:
        await event.edit('__"Wikipedia is what the internet was meant to be."__')
    if x == 82:
        await event.edit(
            '__"A theme park is the only place that you can hear screams in the distance and not be concerned."__'
        )
    if x == 83:
        await event.edit(
            '__"A wireless phone charger offers less freedom of movement than a wired one."__'
        )
    if x == 84:
        await event.edit(
            "__\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"__"
        )
    if x == 85:
        await event.edit(
            '__"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."__'
        )
    if x == 86:
        await event.edit(
            '__"If someday human teleportation becomes real, people will still be late for work."__'
        )
    if x == 87:
        await event.edit(
            '__"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"__'
        )
    if x == 88:
        await event.edit(
            '__"Doing something alone is kind of sad, but doing it solo is cool af."__'
        )
    if x == 89:
        await event.edit(
            '__"Your brain suddenly becomes perfect at proofreading after you post something."__'
        )
    if x == 90:
        await event.edit(
            '__"There\'s always that one song in your playlist that you always skip but never remove."__'
        )
    if x == 91:
        await event.edit(
            '__"Kids next century will probably hate us for taking all the good usernames."__'
        )
    if x == 92:
        await event.edit('__"Bubbles are to fish what rain is to humans."__')
    if x == 93:
        await event.edit(
            '__"The more people you meet, the more you realise and appreciate how well your parents raised you."__'
        )
    if x == 94:
        await event.edit('__"A comma is a short pause, a coma is a long pause."__')
    if x == 95:
        await event.edit('__"Someday you will either not wake up or not go to sleep."__')
    if x == 96:
        await event.edit(
            '__"Bermuda Triangle might be the exit portal of this simulation."__'
        )
    if x == 97:
        await event.edit(
            '__"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."__'
        )
    if x == 98:
        await event.edit(
            "__Do You Know, Some Mosquitos Became Ghosts, When you *Killed* Them...__"
        )
    if x == 99:
        await event.edit("__Do You Know, Mosquitoes has Teleportation Power...__")
    if x == 100:
        await event.edit(
            "__Do You Know, When you see a bearded Goat, that means you juat saw a *Smarter Goat* than YOU....__"
        )
    if x == 101:
        await event.edit(
            "__Do You Know, when You give some ruppess to a Bus Conductor, He will give You a Piece of Paper, *Called Ticket*...__"
        )
    if x == 102:
        await event.edit("__Do You Know, Bus are called Bus, Because they are Bus....__")
    if x == 103:
        await event.edit(
            "__Do You Know, There's a Huge Difference between *Cartoon amd Anime*...__"
        )
    if x == 104:
        await event.edit("__Do You Know, We can't see Ghosts But Ghosts Can see Us...__")


CMD_HELP.update(
    {
        "randomtext": """**Plugin : **__randomtext__

**Commands : **
  •  __.sing__
  •  __.hps__
  •  __.gott__
  •  __.gotm__
  •  __.bello__
  •  __.tip__
  •  __.qt__
  •  __.logic__  

**Function : **__Random text strings are shown__"""
    }
)
