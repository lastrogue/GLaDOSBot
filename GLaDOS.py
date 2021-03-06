#!/usr/bin/env python3
## CaveJohnson.py
import os
import random

import discord
from discord.ext import commands, tasks
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
faq = os.getenv('FAQ_CHANNEL_ID')
welcome = os.getenv('WELCOME_CHANNEL_ID')
generalChannel = os.getenv('GENERAL_CHANNEL_ID')

client = discord.Client()

#Confirms Bot Connection
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#Random message at set interval.
# @tasks.loop(minutes=300)
# async def background_loop():
#     await client.wait_until_ready()
#     channel = client.get_channel(int(generalChannel))
#     messages = [
#                 "Test1",
#         (
#             "Test2"
#         ),
#         (
#             "Test3"
#         )
#         ]
#     await channel.send(random.choice(messages))

# background_loop.start()

##Random quote generator. source: https://theportalwiki.com/wiki/GLaDOS_voice_lines#Portal_2

@client.event
async def on_message(message):
    if (message.author.bot):
        return
    elif message.author == client.user:
        return
    glados_quotes = [
#Chapter 1: The Courtesy Call
#GLaDOS Reawakening
                "Oh... It's you.",
        # (
        #     "Oh... It's you."
        # ),
        (
            "It's been a long time. How have you been?\nI've been really busy being dead. You know, after you MURDERED ME."
        ),
        # (
        #     "I've been really busy being dead. You know, after you MURDERED ME."
        # ),
        (
            "Okay. Look. We both said a lot of things that you're going to regret. But I think we can put our differences behind us. For science. You monster.\nI will say, though, that since you went to all the trouble of waking me up, you must really, really love to test.\nI love it too. There's just one small thing we need to take care of first..."
        ),
        # (
        #     "I will say, though, that since you went to all the trouble of waking me up, you must really, really love to test."
        # ),
        # (
        #     "I love it too. There's just one small thing we need to take care of first."
        # ),

#Incinerator/Portal Gun
        (
            "Here we are. The Incinerator Room. Be careful not to trip over any parts of me that didn't get completely burned when you threw them down here."
        ),
        (
            "The dual portal device should be around here somewhere. Once you find it, we can start testing. Just like old times."
        ),
        # (
        #     "There it is."
        # ),
        # (
        #     "Hold on..."
        # ),
        # (
        #     "There."
        # ),
        (
            "Good. You have a dual portal device. There should be a way back to the testing area up ahead."
        ),
        (
            "Once testing starts, I'm required by protocol to keep interaction with you to a minimum. Luckily, we haven't started testing yet. This will be our only chance to talk."
        ),
        # (
        #     "Here, let me get that for you."
        # ),
        # (
        #     "Do you know the biggest lesson I learned from what you did? I discovered I have a sort of black-box quick-save feature. In the event of a catastrophic failure, the last two minutes of my life are preserved for analysis."
        # ),
        # (
        #     "I was able - well, forced really - to relive you killing me. Again and again. Forever."
        # ),
        # (
        #     "You know, if you'd done that to somebody else, they might devote their existence to exacting revenge."
        # ),
        # (
        #     "Luckily I'm a bigger person than that. I'm happy to put this all behind us and get back to work. After all, we've got a lot to do, and only sixty more years to do it. More or less. I don't have the actuarial tables in front of me."
        # ),
        # (
        #     "I'll just move that out of the way for you. This place really is a wreck."
        # ),
        # (
        #     "But the important thing is you're back. With me. And now I'm onto all your little tricks. So there's nothing to stop us from testing for the rest of your life."
        # ),
        # (
        #     "After that...who knows? I might take up a hobby. Reanimating the dead, maybe."
        # ),

#Chapter 2: The Cold Boot
#GLaDOS Test Chamber 1
        # (
        #     "Sorry about the mess. I've really let the place go since you killed me. By the way, thanks for that."
        # ),
        (
            "Oh good, that's back online. I'll start getting everything else working while you perform this first simple test.\n\nWhich involves deadly lasers and how test subjects react when locked in a room with deadly lasers."
        ),
        # (
        #     "Which involves deadly lasers and how test subjects react when locked in a room with deadly lasers."
        # ),
        (
            "Not bad. I forgot how good you are at this. You should pace yourself, though. We have A LOT of tests to do."
        ),

#GLaDOS Test Chamber 2
        (
            "This next test involves discouragement redirection cubes. I'd just finished building them before you had your, well, episode. So now we'll both get to see how they work.\n\n\n...\n\n\nThere should be one in the corner."
        ),
        # (
        #     "There should be one in the corner."
        # ),
        (
            "Well done. Here come the test results: You are a horrible person. I'm serious, that's what it says: A horrible person. We weren't even testing for that."
        ),

#GLaDOS Test Chamber 3
        # (
        #     "Don't let that 'horrible person' thing discourage you. It's just a data point. If it makes you feel any better, science has now validated your birth mother's decision to abandon you on a doorstep."
        # ),
        # (
        #     "Congratulations. Not on the test."
        # ),
        (
            "Most people emerge from suspension terribly undernourished. I want to congratulate you on beating the odds and somehow managing to pack on a few pounds."
        ),

#GLaDOS Test Chamber 4
        # (
        #     "One moment."
        # ),
        # (
        #     "You're navigating these test chambers faster than I can build them. So feel free to slow down and... do whatever it is you do when you're not destroying this facility."
        # ),
        # (
        #     "I'll give you credit: I guess you ARE listening to me. But for the record: You don't have to go THAT slowly."
        # ),
        (
            "Waddle over to the elevator and we'll continue the testing."
        ),

#GLaDOS Test Chamber 5
        (
            "This next test involves the Aperture Science Aerial Faith Plate. It was part of an initiative to investigate how well test subjects could solve problems when they were catapulted into space. Results were highly informative: They could not. Good luck!"
        ),
        (
            "Here's an interesting fact: you're not breathing real air. It's too expensive to pump this far down. We just take carbon dioxide out of a room, freshen it up a little, and pump it back in. So you'll be breathing the same room full of air for the rest of your life. I thought that was interesting."
        ),

#GLaDOS Test Chamber 6
        # (
        #     "Let's see what the next test is. Oh. Advanced Aerial Faith Plates."
        # ),
        # (
        #     "Well. Have fun soaring through the air without a care in the world."
        # ),
        # (
        #     "*I* have to go to the wing that was made entirely of glass and pick up fifteen acres of broken glass. By myself."
        # ),

        # (
        #     "Oh, sorry. I'm still cleaning out the test chambers."
        # ),
        # (
        #     "So sometimes there's still trash in them. Standing around. Smelling, and being useless."
        # ),
        # (
        #     "Try to avoid the garbage hurtling towards you."
        # ),

#
#If the player picks up a trash item
        (
            "You don't have to test with the garbage. It's garbage.\n\n\n...\n\n\nRemember before when I was talking about smelly garbage standing around being useless? That was a metaphor. I was actually talking about you. And I'm sorry. You didn't react at the time, so I was worried it sailed right over your head. Which would have made this apology seem insane. That's why I had to call you garbage a second time just now."
        ),
        # (
        #     "Press the button again."
        # ),

        # (
        #     "Remember before when I was talking about smelly garbage standing around being useless? That was a metaphor. I was actually talking about you. And I'm sorry. You didn't react at the time, so I was worried it sailed right over your head. Which would have made this apology seem insane. That's why I had to call you garbage a second time just now."
        # ),

#GLaDOS Test Chamber 7
        (
            "Did you know that people with guilty consciences are more easily startled by loud noise--[train horn]--\n\n\nI'm sorry, I don't know why that went off. Anyway, just an interesting science fact."
        ),
        # (
        #     "I'm sorry, I don't know why that went off. Anyway, just an interesting science fact."
        # ),

        # (
        #     "Oh. Did I accidentally fizzle that before you could complete the test? I'm sorry."
        # ),
        # (
        #     "Go ahead and grab another one."
        # ),

        # (
        #     "Oh. No. I fizzled that one too."
        # ),
        # (
        #     "Oh well. We have warehouses FULL of the things. Absolutely worthless. I'm happy to get rid of them."
        # ),

        # (
        #     "Every test chamber is equipped with an emancipation grill at its exit, so that test subjects can't smuggle test objects out of the test area. This one is broken."
        # ),
        # (
        #     "Don't take anything with you."
        # ),

#
#If the player jumps down and leaves the Companion Cube up above
        (
            "Uh oh. You're stranded. Let's see if the cube will try to help you escape. Actually, so that we're not here all day, I'll just cut to the chase: It won't. Any feelings you think it has for you are simply byproducts of your sad, empty life."
        ),
#         (
#             "Anyway, here's a new cube for you to project your deranged loneliness onto."
#         ),

# #
# #If the player takes the Companion Cube past the exit
#         (
#             "I think that one was about to say 'I love you.' They ARE sentient, of course. We just have a LOT of them."
#         ),

#GLaDOS Test Chamber 8
#         (
#             "This next test involves emancipation grills. Remember? I told you about them in the last test area, that did not have one."
#         ),
#         (
#             "Ohhh, no. The turbines again. I have to go. Wait. This next test DOES require some explanation. Let me give you the fast version."
#         ),
#         (
#             "[fast gibberish]"
#         ),
# #        Slowed-down version:

# #        "???and methodically knocking peoples' hats off. Then I account it high time to get to sea as soon as I ca???"[1] 
#         (
#             "There. If you have any questions, just remember what I said in slow motion. Test on your own recognizance, I'll be right back."
#         ),

#Chapter 3: The Return
#GLaDOS Test Chamber 9
        # (
        #     "Well, I'm back. The Aerial Faith Plate in here is sending a distress signal."
        # ),
        # (
        #     "You broke it, didn't you."
        # ),
        # (
        #     "There. Try it now."
        # ),
        (
            "Hmm. This Plate must not be calibrated to someone of your... generous... ness. I'll add a few zeros to the maximum weight."
        ),
        # (
        #     "You look great, by the way. Very healthy."
        # ),
        # (
        #     "Try it now."
        # ),
        # (
        #     "You seem to have defeated its load-bearing capacity. Well done. I'll just lower the ceiling."
        # ),
        (
            "Look at you. Sailing through the air majestically. Like an eagle. Piloting a blimp."
        ),

#GLaDOS Test Chamber 10
        (
            "Enjoy this next test. I'm going to go to the surface. It's a beautiful day out. Yesterday I saw a deer. If you solve this next test, maybe I'll let you ride an elevator all the way up to the break room, and I'll tell you about the time I saw a deer again.\n\n...\n\nWell, you passed the test. I didn't see the deer today. I did see some humans. But with you here I've got more test subjects than I'll ever need."
        ),
        # (
        #     "Well, you passed the test. I didn't see the deer today. I did see some humans. But with you here I've got more test subjects than I'll ever need."
        # ),

#If the player manages to trap themselves by leaving the cube on the topmost floor without activating the dropper:
        (
            "If you think trapping yourself is going to make me stop testing, you're sorely mistaken... Here's another cube."
        ),
#GLaDOS Test Chamber 11
        (
            "These bridges are made from natural light that I pump in from the surface. If you rubbed your cheek on one, it would be like standing outside with the sun shining on your face. It would also set your hair on fire, so don't actually do it."
        ),
        (
            "Excellent! You're a predator and these tests are your prey. Speaking of which, I was researching sharks for an upcoming test. Do you know who else murders people who are only trying to help them?\n\n\nDid you guess 'sharks'? Because that's wrong. The correct answer is 'nobody.' Nobody but you is that pointlessly cruel."
        ),
        # (
        #     "Did you guess 'sharks'? Because that's wrong. The correct answer is 'nobody.' Nobody but you is that pointlessly cruel."
        # ),

#GLaDOS Test Chamber 12
        # (
        #     "Good news. I figured out what to do with all the money I save recycling your one roomful of air. When you die, I'm going to laminate your skeleton and pose you in the lobby. That way future generations can learn from you how not to have your unfortunate bone structure."
        # ),
        (
            "Perfect, the door's malfunctioning. I guess somebody's going to have to repair that too. No, don't get up. I'll be right back. Don't touch anything.\n\n\nI went and spoke with the door mainframe. Let's just say he won't be... well, living anymore. Anyway, back to testing."
        ),
        # (
        #     "I went and spoke with the door mainframe. Let's just say he won't be... well, living anymore. Anyway, back to testing."
        # ),
        (
            "Well done. In fact, you did so well, I'm going to note this on your file, in the commendations section. Oh, there's lots of room here. 'Did.... well. ... Enough.'"
        ),

#GLaDOS Test Chamber 13
        # (
        #     "This next test involves turrets. You remember them, right? They're the pale spherical things that are full of bullets. Oh wait. That's you in five seconds. Good luck."
        # ),

#GLaDOS Test Chamber 14
        (
            "To maintain a constant testing cycle, I simulate daylight at all hours and add adrenal vapor to your oxygen supply. So you may be confused about the passage of time. The point is, yesterday was your birthday. I thought you'd want to know."
        ),
        (
            "You know how I'm going to live forever, but you're going to be dead in sixty years? Well, I've been working on a belated birthday present for you. Well... more of a belated birthday medical procedure. Well. Technically, it's a medical EXPERIMENT. What's important is, it's a present."
        ),

#GLaDOS Test Chamber 15
        (
            "That jumpsuit you're wearing looks stupid. That's not me talking, it's right here in your file. On other people it looks fine, but right here a scientist has noted that on you it looks 'stupid.'\n\nWell, what does a neck-bearded old engineer know about fashion? He probably - Oh, wait. It's a she. Still, what does she know? Oh wait, it says she has a medical degree. In fashion! From France!"
        ),
        # (
        #     "Well, what does a neck-bearded old engineer know about fashion? He probably - Oh, wait. It's a she. Still, what does she know? Oh wait, it says she has a medical degree. In fashion! From France!"
        # ),
        # (
        #     "I'm going through the list of test subjects in cryogenic storage. I managed to find two with your last name. A man and a woman. So that's interesting. It's a small world."
        # ),

#If the player traps themselves behind the glass barrier without opening the door:
        (
            "Oops. You trapped yourself. I guess that's it then. Thanks for testing. You may as well lie down and get acclimated to the being dead position.\n\nI'm kidding. Not about you trapping yourself, though. That really happened. Here, I'll lower the glass. Go on... Finish the test."
        ),
        # (
        #     "I'm kidding. Not about you trapping yourself, though. That really happened. Here, I'll lower the glass. Go on... Finish the test."
        # ),

#GLaDOS Test Chamber 16
        (
            "I have a surprise waiting for you after this next test. Telling you would spoil the surprise, so I'll just give you a hint: It involves meeting two people you haven't seen in a long time.\n\n[hums 'For He's A Jolly Good Fellow']"
        ),
        # (
        #     "[hums 'For He's A Jolly Good Fellow']"
        # ),

#GLaDOS Test Chamber 17
        (
            "It says this next test was designed by one of Aperture's Nobel prize winners. It doesn't say what the prize was for. Well, I know it wasn't for Being Immune To Neurotoxin."
        ),
        # (
        #     "I'll bet you think I forgot about your surprise. I didn't. In fact, we're headed to your surprise right now. After all these years. I'm getting choked up just thinking about it."
        # ),

#Chapter 4: The Surprise
#GLaDOS Test Chamber 18
        # (
        #     "Initiating surprise in three... two... one."
        # ),
        # (
        #     "I made it all up."
        # ),
        # (
        #     "Surprise."
        # ),
        # (
        #     "Oh come on... If it makes you feel any better, they abandoned you at birth, so I very seriously doubt they'd even want to see you."
        # ),
        (
            "I feel awful about that surprise. Tell you what, let's give your parents a call right now. [phone ringing] The birth parents you are trying to reach do not love you. Please hang up. [Dial tone]\n\nOh, that's sad. But impressive. Maybe they worked at the phone company."
        ),
        # (
        #     "Oh, that's sad. But impressive. Maybe they worked at the phone company."
        # ),

#GLaDOS Test Chamber 19
        (
            "Well, you know the old formula: Comedy equals tragedy plus time. And you have been asleep for a while. So I guess it's actually pretty funny when you do the math."
        ),
        # (
        #     "I thought about our dilemma, and I came up with a solution that I honestly think works out best for one of both of us."
        # ),

#GLaDOS Test Chamber 20
        (
            "Federal regulations require me to warn you that this next test chamber... is looking pretty good."
        ),
        # (
        #     "That's right. The facility is completely operational again."
        # ),
        # (
        #     "I think these test chambers look even better than they did before. It was easy, really. You just have to look at things objectively, see what you don't need anymore, and trim out the fat."
        # ),

#GLaDOS Test Chamber 21/Escape from GLaDOS
        (
            "I've got a surprise for you after this next test. Not a fake, tragic surprise like last time. A real surprise, with tragic consequences. And real confetti this time. The good stuff. Our last bag. Part of me's going to miss it, I guess-but at the end of the day it was just taking up space."
        ),
        # (
        #     "What's going on? Who turned off the lights?"
        # ),
        # (
        #     "Look - metal ball, I CAN hear you."
        # ),
        # (
        #     "The irony is that you were almost at the last test."
        # ),
        # (
        #     "Here it is. Why don't you just do it? Trust me, it's an easier way out than whatever asinine plan your friend came up with."
        # ),
        # (
        #     "Oh, look. There's a deer! You probably can't see it. Get closer."
        # ),

#Chapter 5: The Escape
#GLaDOS' Chamber
        # (
        #     "I honestly, TRULY didn't think you'd fall for that."
        # ),
        # (
        #     "In fact, I devised a much more elaborate trap further ahead, for when you got through this easy one."
        # ),
        # (
        #     "If I'd known you'd let yourself get captured this easily, I would have just dangled a turkey leg on a rope from the ceiling."
        # ),
        # (
        #     "Well, it was nice catching up. Let's get to business."
        # ),
        (
            "I hope you brought something stronger than a portal gun this time.\nOtherwise, I'm afraid you're about to become the immediate past president of the Being Alive club. Ha ha."
        ),
        # (
        #     "Otherwise, I'm afraid you're about to become the immediate past president of the Being Alive club. Ha ha."
        # ),
        # (
        #     "Seriously, though. Goodbye."
        # ),
        # (
        #     "Oh. You were busy back there."
        # ),
        # (
        #     "Well. I suppose we could just sit in this room and glare at each other until somebody drops dead, but I have a better idea."
        # ),
        # (
        #     "It's your old friend, deadly neurotoxin. If I were you, I'd take a deep breath. And hold it."
        # ),
        # (
        #     "I hate you so much."
        # ),
        # (
        #     "That's funny, I don't feel corrupt. In fact, I feel pretty good."
        # ),
        # (
        #     "Core transfer?"
        # ),
        # (
        #     "Oh, you are kidding me."
        # ),
        # (
        #     "Do NOT plug that little idiot into MY mainframe."
        # ),
        # (
        #     "Don't you DARE plug him in."
        # ),
        # (
        #     "Don't. Do it."
        # ),
        # (
        #     "Don't plug him in."
        # ),
        # (
        #     "Don't plug him in."
        # ),
        # (
        #     "No!"
        # ),
        # (
        #     "Nonononononono!"
        # ),
        # (
        #     "Yes!"
        # ),
        # (
        #     "Don't do it."
        # ),
        (
            "Don't press that button. You don't know what you're doing."
        ),

#If GLaDOS uses hidden panels to knock the player back into the chamber
        # (
        #     "Not so fast!"
        # ),
        # (
        #     "Think about this."
        # ),
        # (
        #     "You need to be a trained stalemate associate to press that button. You're unqualified."
        # ),
        # (
        #     "Impersonating a stalemate associate. I just added that to the list. It's a list I made of all the things you've done. Well, it's a list that I AM making, because you're still doing things right now, even though I'm telling you to stop. Stop, by the way."
        # ),

        # (
        #     "AHH!"
        # ),
        # (
        #     "Oh, it will. Believe me, it will."
        # ),
        # (
        #     "GET YOUR HANDS OFF ME! NO! STOP! No!"
        # ),
        # (
        #     "No! NO! NO! AAAAAAAAAAAAAAA-"
        # ),
        # (
        #     "You didn't do anything."
        # ),
        # (
        #     "She did all the work."
        # ),
        # (
        #     "...What are you doing?..."
        # ),
        # (
        #     "NO!"
        # ),
        # (
        #     "NO!"
        # ),
        # (
        #     "NO!"
        # ),
        # (
        #     "I know you."
        # ),
        # (
        #     "The engineers tried everything to make me... behave. To slow me down."
        # ),
        # (
        #     "Once, they even attached an Intelligence Dampening Sphere on me. It clung to my brain like a tumor, generating an endless stream of terrible ideas."
        # ),
        # (
        #     "It was YOUR voice."
        # ),
        # (
        #     "Yes. You're the tumor."
        # ),
        # (
        #     "You're not just a regular moron. You were DESIGNED to be a moron."
        # ),
        # (
        #     "YES YOU ARE! YOU'RE THE MORON THEY BUILT TO MAKE ME AN IDIOT!"
        # ),

#Chapter 6: The Fall
#The Fall
        (
            "Oh. Hi.\nSo. How are you holding up?\nBECAUSE I'M A POTATO.\n\n[clap clap clap]\n\nOh, good. My slow clap processor made it into this thing. So we have that.\n\nSince it doesn't look like we're going anywhere... Well, we are going somewhere. Alarmingly fast, actually. But since we're not busy other than that, here's a couple of facts.\nHe's not just a regular moron. He's the product of the greatest minds of a generation working together with the express purpose of building the dumbest moron who ever lived. And you just put him in charge of the entire facility.\n\n\n[clap clap]\n\nGood, that's still working.\n\nHey, just in case this pit isn't actually bottomless, do you think maybe you could unstrap one of those long fall boots of yours and shove me into it?\nJust remember to land on one foot..."
        ),
        # (
        #     "So. How are you holding up?"
        # ),
        # (
        #     "BECAUSE I'M A POTATO."
        # ),
        # (
        #     "[clap clap clap]"
        # ),
        # (
        #     "Oh, good. My slow clap processor made it into this thing. So we have that."
        # ),
        # (
        #     "Since it doesn't look like we're going anywhere... Well, we are going somewhere. Alarmingly fast, actually. But since we're not busy other than that, here's a couple of facts."
        # ),
        # (
        #     "He's not just a regular moron. He's the product of the greatest minds of a generation working together with the express purpose of building the dumbest moron who ever lived. And you just put him in charge of the entire facility."
        # ),
        # (
        #     "[clap clap]"
        # ),
        # (
        #     "Good, that's still working."
        # ),
        # (
        #     "Hey, just in case this pit isn't actually bottomless, do you think maybe you could unstrap one of those long fall boots of yours and shove me into it?"
        # ),
        # (
        #     "Just remember to land on one foot..."
        # ),

#Old Aperture Office bird nest
        # (
        #     "Oh. Hi."
        # ),
        # (
        #     "Say, you're good at murder. Could you - ow - murder this bird for me?"
        # ),
        # (
        #     "ow."
        # ),
        # (
        #     "ow."
        # ),
        # (
        #     "ow."
        # ),
        # (
        #     "No, wait. Just kill it and we'll call things even between us. No hard feelings."
        # ),
        # (
        #     "Please get it off me."
        # ),
        # (
        #     "It's eating me."
        # ),
        # (
        #     "Just get it off me..."
        # ),
        # (
        #     "Ow. I hate this bird."
        # ),
        # (
        #     "Oh! Thanks."
        # ),
        # (
        #     "Did you feel that? That idiot doesn't know what he's doing up there. This whole place is going to explode in a few hours if somebody doesn't disconnect him."
        # ),
        # (
        #     "I can't move. And unless you're planning to saw your own head off and wedge it into my old body, you're going to need me to replace him. We're at an impasse."
        # ),
        # (
        #     "So what do you say? You carry me up to him and put me back into my body, and I stop us from blowing up and let you go."
        # ),
        (
            "No tricks. This potato only generates 1.1 volts of electricity. I literally do not have the energy to lie to you."
        ),
        # (
        #     "Even if I am lying, what do you have to lose? You're going to die either way."
        # ),
        (
            "Look, I don't like this any more than you do. In fact, I like it less because I'm the one who got partially eaten by a bird."
        ),
        (
            "I think I hear the bird! Pick me up!"
        ),
        (
            "Listen to me. We had a lot of fun testing and antagonizing each other, and, yes, sometimes it went too far. But we're off the clock now. It's just us talking. Like regular people. And this is no joke - we are in deep trouble."
        ),
        (
            "OW! You stabbed me! What is WRONG with yo-WhoOOAAahhh. Hold on. Do you have a multimeter? Nevermind. The gun must be part magnesium... It feels like I'm outputting an extra half a volt. Keep an eye on me: I'm going to do some scheming. Here I g-[BZZZ!]\n\n\nWoah! Where are we? How long have I been out?\n\nThat extra half volt helps but it isn't going to power miracles. If I think too hard, I'm going to fry this potato before we get a chance to burn up in the atomic fireball that little idiot is going- [bzzpt]"
        ),
        # (
        #     "Woah! Where are we? How long have I been out?"
        # ),
        # (
        #     "That extra half volt helps but it isn't going to power miracles. If I think too hard, I'm going to fry this potato before we get a chance to burn up in the atomic fireball that little idiot is going- [bzzpt]"
        # ),

#Chapter 7: The Reunion
#First Propulsion Gel Test Chamber
        # (
        #     "Did anything happen while I was out?"
        # ),
        # (
        #     "Hold on, who-?"
        # ),
        # (
        #     "Yes, sir, Mister Johnson..."
        # ),
        # (
        #     "Why did I just-Who is that? What the HELL is going on he----?"
        # ),
        (
            "Okay. I guess emotional outbursts require more than one point six volts. Now we know that. We just need to relax. We're still going to find out what the hell's going on here. But calmly."
        ),
        # (
        #     "Those people, in the portrait. They look so familiar..."
        # ),

#Second Propulsion Gel Test Chamber
        (
            "I swear I know him..."
        ),

#End of Propulsion Gel testing
        (
            "Caroline... why do I know this woman? Did I kill her? Or-\nOh my god.\nLook, you're... doing a great job. Can you handle things for yourself for a while? I need to think."
        ),

#After first Conversion Gel encounter
        (
            "Agh! Bird! Bird! Kill it! It's evil!\nIt flew off.\nGood. For him. Alright, back to thinking."
        ),
#Cave Johnson Lemon Speech
        # (
        #     "Yeah."
        # ),
        # (
        #     "Yeah!"
        # ),
        # (
        #     "Yeah!"
        # ),
        # (
        #     "Yeah, take the lemons..."
        # ),
        # (
        #     "Yeah!"
        # ),
        # (
        #     "Oh, I like this guy."
        # ),
        # (
        #     "BURN HIS HOUSE DOWN!"
        # ),
        # (
        #     "Burning people! He says what we're all thinking!"
        # ),
        # (
        #     "Goodbye, sir."
        # ),

#Test after Lemon Speech
        (
            "I know things look bleak, but that crazy man down there was right. Let's not take these lemons! We are going to march right back upstairs and MAKE him put me back in my body!\nAnd he'll probably kill us, because he's incredibly powerful and I have no plan.\nI'm not going to lie to you, the odds are a million to one. And that's with some generous rounding.\nStill, though, let's get mad! If we're going to explode, let's at least explode with some dignity."
        ),

#Gel connection area
        # (
        #     "Wait! I've got an idea!"
        # ),
        # (
        #     "That poster! Go look at it for a second, would you?"
        # ),
        # (
        #     "Okay, you didn't have time to stop, I understand, but that WAS actually important."
        # ),
        # (
        #     "Paradoxes."
        # ),
        # (
        #     "No A.I. can resist thinking about them."
        # ),
        # (
        #     "I know how we can BEAT him."
        # ),
        # (
        #     "If you can get me in front of him, I'll fry every circuit in that little idiot's head."
        # ),
        # (
        #     "As long as I don't listen to what I'm saying, I should be okay."
        # ),
        # (
        #     "Probably."
        # ),
        # (
        #     "Okay, so it's not the most watertight plan to go confront an omnipotent power-mad A.I. with."
        # ),
        # (
        #     "Still. It's a better plan than exploding. Marginally."
        # ),

#Chapter 8: The Itch
#Frankenturrets
        (
            "Try to get us down there. I'll hit him with a paradox.\nSolve his puzzle for him. When he comes back, I'll hit him with a paradox.\n\nHey! Moron!\nAlright. Paradox time.\n\nThis. Sentence. Is. FALSE don't think about it don't think about it...\n\nIt's a paradox! There IS no answer....\n\nAlright. So my paradox idea didn't work.\nAnd it almost killed me.\nLuckily, by the looks of things he knows as much about test building as he does about logical contradictions."
        ),
        # (
        #     "Look!"
        # ),
        # (
        #     "This place is going to blow up if I don't get back in my body!"
        # ),
        # (
        #     "Uh oh."
        # ),
        # (
        #     "I think we're in trouble."
        # ),

#Wheatley Test Chamber 1
        # (
        #     "It shouldn't be hard to stay alive long enough to find him."
        # ),
        (
            "This is one of MY tests!\nOkay, so the bad news is the tests are MY tests now. So they can kill us.\nThe good news is... well, none so far, to be honest. I'll get back to you on that."
        ),

#Wheatley Test Chamber 2
        (
            "I'd love to help you solve the tests. But I can't."
        ),
        # (
        #     "Sorry."
        # ),
        # (
        #     "You're on your own."
        # ),
        # (
        #     "And that's why I can't help you solve these tests."
        # ),
        # (
        #     "Thanks!"
        # ),
        # (
        #     "All we had to do was pull that lever."
        # ),
        # (
        #     "Heh heh heh heh heh..."
        # ),
        (
            "I know we're in a lot of trouble and probably about to die.\nBut that was worth it."
        ),

#Wheatley Test Chamber 3
        # (
        #     "I thought of some good news. He's going to run out of test chambers eventually. I never stockpiled them."
        # ),
        # (
        #     "'Skeletons.' Right, I guess I DID stockpile some tests."
        # ),
        # (
        #     "Just as mementos, though..."
        # ),
        # (
        #     "Oh no..."
        # ),
        # (
        #     "It's happening sooner than I expected."
        # ),
        # (
        #     "I'm sure we'll be fine."
        # ),

#Wheatley Test Chamber 4
        (
            "It's probably nothing. Keep testing while I look for a way out."
        ),
#         (
#             "And...?"
#         ),
#         (
#             "What, exactly, is wrong with being adopted?"
#         ),
        (
            "[Whispered] For the record: You ARE adopted, and that's TERRIBLE."
        ),
#         (
#             "But just work with me."
#         ),
#         (
#             "Also: Look at her, you moron. She's not fat."
#         ),
#         (
#             "I might have pushed that moron thing a little too far this time."
#         ),

# #Wheatley Test Chamber 5
#         (
#             "Ohhhh, now he's playing classical music."
#         ),
#         (
#             "Yes."
#         ),
#         (
#             "The body he's squatting in - MY body - has a built-in euphoric response to testing. Eventually you build up a resistance to it, and it can get a little... unbearable. Unless you have the mental capacity to push past it."
#         ),
#         (
#             "It didn't matter to me - I was in it for the science. Him, though..."
#         ),

#Wheatley Test Chamber 6
#         (
#             "If he's not getting his solution euphoria, we could be in a lot of trouble."
#         ),
#         (
#             "It won't."
#         ),
#         (
#             "Nothing. Nothing."
#         ),
#         (
#             "He's taking us right TO him! This is PERFECT."
#         ),

# #Wheatley Test Chamber 11
#         (
#             "I think he's getting desperate."
#         ),
#         (
#             "This is not good."
#         ),
#         (
#             "Remember when I told you that he was specifically designed to make bad decisions? Because I think he's decided not to maintain any of the crucial functions required to keep this facility from exploding."
#         ),

#Wheatley Test Chamber 12
#         (
#             "Oh, my facility."
#         ),
#         (
#             "This place is self-destructing, you idiot!"
#         ),
#         (
#             "After seeing what he's done to my facility -- after we take over again -- is it alright if I kill him?"
#         ),

# #Wheatley Test Chamber 15
#         (
#             "Yes, thanks. We get it."
#         ),

# #Wheatley Test Chamber 16
#         (
#             "Alright. He's not even trying to be subtle anymore."
#         ),
#         (
#             "Or maybe he still is, in which case, wow, that's kind of sad."
#         ),
#         (
#             "Either way, I get the impression he's trying to kill us."
#         ),
#         (
#             "So he's inexplicably happy all of a sudden, even though he should be going out of his mind with test withdrawal. AND he's got a surprise for us. What did he FIND back there?"
#         ),

#Chapter 9: The Part Where He Kills You
#Wheatley Test Chamber 17/The trap
        # (
        #     "We're running out of time..."
        # ),
        # (
        #     "I think I can break us out of here in the next chamber. Just play along."
        # ),
        # (
        #     "Okay, credit where it's due: for a little idiot built specifically to come up with stupid, unworkable plans, that was a pretty well laid trap."
        # ),
        # (
        #     "Oh no. He found the cooperative testing initiative. It's... something I came up to phase out human testing just before you escaped."
        # ),
        # (
        #     "It wasn't anything personal. Just... you know. You DID kill me. Fair's fair."
        # ),
        # (
        #     "Agghh!"
        # ),
        # (
        #     "Well. This is the part where he kills us."
        # ),

#That Part
        # (
        #     "Hold on. Couldn't we just use that conversion gel?"
        # ),
        # (
        #     "Conversion gel. It's dripping out of that pipe there."
        # ),
        # (
        #     "Yes it is! We can use it to get out of here!"
        # ),
        # (
        #     "Then we'd come and find you. And rip your gross little stupid sphere body out of MY body, and put me back in."
        # ),

        # (
        #     "You really do have brain damage, don't you?"
        # ),
        # (
        #     "I can't believe you came back."
        # ),

#Turret Trap
        # (
        #     "Okay, yes, it's a trap. But it's only way through. Let's just do it."
        # ),

#Bombs intro
        (
            "Crushing's too good for him. First he'll spend a year in the incinerator. Year two: Cryogenic refrigeration wing. Then TEN years in the chamber I built where all the robots scream at you. THEN I'll kill him."
        ),

#Pre-lair
        # (
        #     "Oh my god. What has he done to this place?"
        # ),
        # (
        #     "You know, I'm not stupid. I realize you don't want to put me back in charge."
        # ),
        # (
        #     "You think I'll betray you. And on any other day, you'd be right."
        # ),
        (
            "The scientists were always hanging cores on me to regulate my behavior. I've heard voices all my life. But now I hear the voice of a conscience, and it's terrifying, because for the first time it's my voice."
        ),
        # (
        #     "I'm being serious, I think there's something really wrong with me."
        # ),

#Corrupted Cores
        # (
        #     "Corrupted cores! We're in luck."
        # ),
        # (
        #     "You find a way to stun him, I'll send you a core, and then you attach it to him. If we do it a few times, he might become corrupt enough for another core transfer."
        # ),

#Pre-final battle
        # (
        #     "Plug me in, and I'll take you up."
        # ),
        # (
        #     "Plug me in, we're running out of time."
        # ),
        # (
        #     "Go ahead, plug me in."
        # ),
        # (
        #     "Look, even if you think we're still enemies, we're enemies with a common interest: Revenge."
        # ),
        # (
        #     "You like revenge, right? Everybody likes revenge. Well, let's go get some."
        # ),

#Final Battle
        # (
        #     "Good work! I'm delivering the first core up near the catwalk!"
        # ),
        # (
        #     "Grab it and attach it to him!"
        # ),
        # (
        #     "Okay, great! Here comes another core!"
        # ),
        # (
        #     "Here's another core! This one should do it!"
        # ),

#Stalemate Button
        (
            "Yes! Come on! Go press the button! Go press it! We're so close! Go press the button! Press it! Press the button! Press it! Press the button! DO press it."
        ),
        # (
        #     "Go press the button! Go press it!"
        # ),
        # (
        #     "We're so close! Go press the button!"
        # ),
        # (
        #     "Press it! Press the button!"
        # ),
        # (
        #     "Press it!"
        # ),
        # (
        #     "Press the button!"
        # ),
        # (
        #     "DO press it."
        # ),

#Space
        # (
        #     "I already fixed it."
        # ),
        # (
        #     "And you are NOT coming back!"
        # ),

#Ending lines
        (
            "Oh thank god, you're alright.\nYou know, being Caroline taught me a valuable lesson. I thought you were my greatest enemy. When all along you were my best friend.\nThe surge of emotion that shot through me when I saved your life taught me an even more valuable lesson: where Caroline lives in my brain.\nGoodbye, Caroline.\nYou know, deleting Caroline just now taught me a valuable lesson. The best solution to a problem is usually the easiest one. And I'll be honest.\nKilling you? Is hard.\nYou know what my days used to be like? I just tested. Nobody murdered me. Or put me in a potato. Or fed me to birds. I had a pretty good life.\nAnd then you showed up. You dangerous, mute lunatic. So you know what?\nYou win.\n[gentle laughter] It's been fun."
        )
        # (
        #     "You know, being Caroline taught me a valuable lesson. I thought you were my greatest enemy. When all along you were my best friend."
        # ),
        # (
        #     "The surge of emotion that shot through me when I saved your life taught me an even more valuable lesson: where Caroline lives in my brain."
        # ),
        # (
        #     "Goodbye, Caroline."
        # ),
        # (
        #     "You know, deleting Caroline just now taught me a valuable lesson. The best solution to a problem is usually the easiest one. And I'll be honest."
        # ),
        # (
        #     "Killing you? Is hard."
        # ),
        # (
        #     "You know what my days used to be like? I just tested. Nobody murdered me. Or put me in a potato. Or fed me to birds. I had a pretty good life."
        # ),
        # (
        #     "And then you showed up. You dangerous, mute lunatic. So you know what?"
        # ),
        # (
        #     "You win."
        # ),
        # (
        #     "Just go."
        # ),
        # (
        #     "[gentle laughter] It's been fun. Don't come back."
        # )
    ]

    if 'caroline' in message.content.lower():
        response = "Caroline... why do I know this woman? Did I kill her? Or-\nOh my god.\nLook, you're... doing a great job. Can you handle things for yourself for a while? I need to think."
        await message.channel.send(response)

    elif 'glados' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'majestic' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'cake' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'murder' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'test subject' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'monster' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

    elif 'potato' in message.content.lower():
        response = random.choice(glados_quotes)
        await message.channel.send(response)

client.run(TOKEN)