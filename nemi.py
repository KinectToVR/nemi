import time
from subprocess import Popen
import os
import discord
from discord.ext import commands
import json
import Levenshtein as lev
import re
# with open('./chatbot/chat_tags.json') as f:
#     nemi = json.load(f)
# print(nemi)

# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import requests
# import re
# nemi = ChatBot('Nemi',database="database.db",trainer='chatterbot.trainers.ListTrainer')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('nemi ', 'Nemi ', 'NEMI '), case_insensitive=True)

token =  open("token", "r").read()

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return
    if message.channel.id == 738958686818533499:
        await message.channel.send(nemi.get_response(message.content))
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in!')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='https://k2vr.tech'))

@bot.command(brief='Instructions for NUI_INSUFFICIENTBANDWIDTH')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def insufficientbandwidth(ctx):
    await ctx.send("https://k2vr.tech/docs/insufficientbandwidth")

@bot.command(brief='Instructions for NUI_NOTREADY')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def notready(ctx):
    await ctx.send("https://k2vr.tech/docs/notready")

@bot.command(brief='yes its just noready')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def nukedrivers(ctx):
    await ctx.send("""
*When in doubt, nuke drivers.*

Yes, the page claims to be for NUI_NOTREADY, but these instructions just explain how to completely purge the Kinect drivers and reinstall them.
https://k2vr.tech/docs/notready
""")

@bot.command(brief='Instructions for NUI_NOTGENUINE')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def notgenuine(ctx):
    await ctx.send("https://k2vr.tech/docs/notgenuine")

@bot.command(brief='You cant use lens adapters')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def lens(ctx):
    await ctx.send("""
Lens adapters for the Xbox 360 Kinect like the Nyko Zoom are incompatible with K2EX. The Kinect SDK expects the lens of the Kinect to have a specific distortion and is calibrated for that.

Because the lens adapter causes the dot grid that the Kinect projects, and the IR camera to be distorted, the depth data is inflated like a balloon, making the tracking unuseable.
""")

@bot.command(brief='Fix autocalib')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def autocalib(ctx):
    await ctx.send("""
**If automatic calibration is broken (trackers end up at a weird offset instead of lining up):**
**1.** Simply try calibrating again, for best results, there should be ample distance between each position you stand in, and you should change height, crouch or squat.
**2.** Try increasing the number of calibration points from the default of 3. Calibration will take longer but has a better chance of succeeding that way.
**3.** Delete the configuration files from the button in the options tab then try calibrating again.
**4.** If none of the above works, resort to manual calibration. Don't forget to click out of the SteamVR Dashboard! You won't be able to send inputs to K2EX otherwise.
""")

@bot.command(brief='Hahaha ping pong')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def ping(ctx):
    await ctx.send('pong')

@bot.command(brief='Link to the K2VR website')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def site(ctx):
    await ctx.send('https://k2vr.tech')

@bot.command(brief='K.P. Glue')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def vrchat(ctx):
    await ctx.send("""
**My avatar is in a T-pose, how do I calibrate?**
• Open your Quick Menu then go to settings and change your "User Real Height" until it matches your height. ```If doing that makes the avatar float or sink into the ground, that means either your VR headset height is set incorrectly or the avatar you're using doesn't have a good rig for full-body tracking.```• Click Calibrate, so that the spheres show up again.
• Line up to the avatar. __YOU DON'T NEED TO LINE UP YOUR HANDS TO YOUR SIDE,__ only the white spheres representing your trackers matter. Your hands will be mapped based on wingspan, and your head will attach to the avatar's viewpoint.
• Press BOTH triggers together.
Video Version: <https://streamable.com/psg13e> (YouTube Version: <https://youtu.be/gvIJOUTCMGA>)

**My avatar is crumpled into a ball on the ground! I don't have any full-body tracking at all!**
First, make sure to turn off any mods if you have them. MelonLoader has the option to launch the game clean without removing any of your mods using the `--no-mods` launch argument.

IKTweaks will almost never break, but it's better to try without. The real culprit for these types of issues is FBTSaver and the similar functionality in Emm.

If you're still having issues without mods, try with a default avatar from the "Public" row. Not all avatars work for full-body, and if it's not your own, and you can't contact the creator, you're screwed.
""")

@bot.command(brief='Link to the calibration video')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def video(ctx):
    await ctx.send('https://youtu.be/cz6X3HrHaVE')

@bot.command(brief='Permanent invite for this server')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def invite(ctx):
    await ctx.send('https://discord.gg/YBQCRDG')

@bot.command(brief='Alias of previous command')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def drivers(ctx):
    await ctx.send('<:kinect360:811234304809893918> Driver for Xbox 360 Kinect: https://download.microsoft.com/download/E/1/D/E1DEC243-0389-4A23-87BF-F47DE869FC1A/KinectSDK-v1.8-Setup.exe\n\n<:kinectone:811234236430286878> Driver for Xbox One Kinect: https://download.microsoft.com/download/F/2/D/F2D1012E-3BC6-49C5-B8B3-5ACFF58AF7B8/KinectSDK-v2.0_1409-Setup.exe')

@bot.command(brief='Driver links for both Kinect models')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def driver(ctx):
    await ctx.send('<:kinect360:811234304809893918> Driver for Xbox 360 Kinect: https://download.microsoft.com/download/E/1/D/E1DEC243-0389-4A23-87BF-F47DE869FC1A/KinectSDK-v1.8-Setup.exe\n\n<:kinectone:811234236430286878> Driver for Xbox One Kinect: https://download.microsoft.com/download/F/2/D/F2D1012E-3BC6-49C5-B8B3-5ACFF58AF7B8/KinectSDK-v2.0_1409-Setup.exe')

@bot.command(brief='Instructions for use with Beat Saber')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def beatsaber(ctx):
    await ctx.send("""
**BeatSaberCustomAvatars can be downloaded from <https://github.com/nicoco007/BeatSaberCustomAvatars/releases>** or using ModAssistant.

When calibrating in Beat Saber, it's best to try the Full-Body Template avatar first.
Turn off "Floor Height Adjust" and "Move Floor with Height Adjust". If the calibrate button is grayed out on an avatar, that means it's not compatible with this version.
""")

# @bot.command(brief='Steps to replace the Kinect Runtime with the SDK')
# async def reinstallsdk(ctx):
#     await ctx.send("""
# Leave your Kinect plugged in the whole time
# Press `Win` + `I` to go to Settings
# Go to Apps
# Search 'Kinect' in the list (it might lag if you have a lot of programs)
# Uninstall EVERYTHING you see
# Restart your computer
# Install the Kinect __SDK__ 1.8
# Restart again.
# It should work.
# """)

@bot.command(brief='Posts the EXE for USBTreeView in chat')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def usbtreeview(ctx):
    await ctx.send("""
USBTreeView (https://k2vr.tech/UsbTreeView.exe) shows you what physical USB controller each device on your computer is connected to.

Controllers have a limited amount of bandwidth. If you connect devices into them that go over the amount of bandwidth they have. Something will go down, be it the Kinect or your VR headset.

You can imagine it like this:
USB controllers are circuit breakers.
USB ports are outlets.
USB hubs are power strips.

Not all outlets are connected to the same circuit breaker. If you put too much on one breaker, it trips. If you plug in a power strip, it doesn't add more capacity to the circuit breaker.

You should send us a screenshot so we can take a look at it for you.
""")

@bot.command(brief='just usbtreeview')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def utvsmall(ctx):
    await ctx.send("""
USBTreeView (https://k2vr.tech/UsbTreeView.exe) shows you what physical USB controller each device on your computer is connected to.

You should send us a screenshot of the window so we can take a look at it and help you.
""")

@bot.command(brief='alvr driver instructions')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def alvr(ctx):
    await ctx.send("""
When using ALVR, by default it will hide every other SteamVR driver from the list and only register it's own.
https://k2vr.tech/docs/alvr
""")

@bot.command(brief='mirror of xbonefix')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbone_loop5(ctx):
    await ctx.send("https://k2vr.tech/docs/kinectv2-troubleshooting")

@bot.command(brief='mirror of xbonefix')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbone_loop15(ctx):
    await ctx.send("https://k2vr.tech/docs/kinectv2-troubleshooting")

# @bot.command(brief='kinect one bootlooping every 2-5 seconds')
# @commands.cooldown(1, 6, commands.BucketType.channel)
# async def xbone_loop5(ctx):
#     await ctx.send("""
# If your Kinect is disconnecting every 2-5 seconds:
# 1️⃣ **Is the microphone muted or disabled?**
# As unintuitive as it may seem, removing access to the Kinect's audio will cause the SDK to restart the device indefinitely because it needs it to track you faster from the directional sound of your footsteps.
# • Open the run dialog by pressing <:windowskey:845064227633889290> + R and typing/pasting `control mmsys.cpl,,1` to open the recording devices control panel.
# • Look for the Kinect audio device, you shouldright-click the list and show disabled and disconnected devices.
# • If the device is disabled, enable it.
# • Open it's properties window, in the Levels tab, ensure that the microphone is NOT muted. You can set it to 0% if you're getting feedback loops.
# """)
#     await ctx.send("""
# 2️⃣ **Is the Kinect lacking bandwidth?**
# Xbox One Kinect is a bandwidth-heavy device that needs to transmit a lot of data. Your computer's chipset might not be up to the task, and you'll need to divy up devices onto separate controllers.
# More info about this can be found by running the `@Nemi controller` command
# • Download and run https://k2vr.tech/UsbTreeView.exe to see what devices are connected to which controllers. You should send a screenshot of the window in chat so we can help you make sense of it.
# """)
#     await ctx.send("""
# 3️⃣ **Check your adapter or cables.**
# It's possible that a bad connection somehwere between the Kinect and the PC could cause it to disconnect repeatedly. As well, a bad or broken adapter may cause similar issues. (Bad adapters have only come from Amazon so far. Anecdotal evidence would show that if it was bought elsewhere, it would be working.)
# • Ensure that every connection on the Kinect and adapter is firmly plugged in. The cable at the back of the Kinect is removeable!
# • If possible, try the Kinect on an Xbox One console. If possible without the adapter on a launch model to help pinpoint the issue.
# • Are you using any sort of USB extension? Try without even if they're needed for your room setup.
# """)
#     await ctx.send("""
# 4️⃣ **Are you having driver issues?**
# It's possible that your Kinect drivers might be broken due to various factors like Windows updates or changing PC hardware.
# • Try removing the Kinect drivers entirely from your system first.
# • Open the Windows settings app by pressing <:windowskey:845064227633889290> + Ɪ and look for the `Apps` section.
# • In the search box on the right, type "Kinect" and remove everything that isn't KinectToVR.
# • Restart your PC
# • Download the Kinect driver https://download.microsoft.com/download/F/2/D/F2D1012E-3BC6-49C5-B8B3-5ACFF58AF7B8/KinectSDK-v2.0_1409-Setup.exe and install it again.
# • If this doesn't work, you can also try redoing these steps, but instead of installing the 2.0 (1409) driver you can let Windows 10 install the 2.2 (1905) driver.
# """)

# @bot.command(brief='kinect one bootlooping every 10-15 seconds')
# @commands.cooldown(1, 6, commands.BucketType.channel)
# async def xbone_loop15(ctx):
#     await ctx.send("""
# If your Kinect is disconnecting every 10-15 seconds:
# 1️⃣ **Is the Kinect's temperature sensor going bad?**
# The Kinect contains a temperatur sensor to monitor it's own state. If it gets too hot, it will shut down the device. Which the SDK will try to bring back up right after.
# After a few years, this sensor has a tendency to go bad. If it does, it will always think the Kinect is boiling hot no matter what!
# Luckily, there's a solution, we can simply cut two wires, and defuse the Kinect bomb.
# • Open this YouTube video <https://www.youtube.com/watch?v=BoRK3jJVMLM> and follow the instructions.
# • You will need a Torx T2 screwdriver or scrwedriver bit.
# """)



@bot.command(brief='alias of usbtreeview')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def utv(ctx):
    await ctx.send("""
USBTreeView (https://k2vr.tech/UsbTreeView.exe) shows you what physical USB controller each device on your computer is connected to.

Controllers have a limited amount of bandwidth. If you connect devices into them that go over the amount of bandwidth they have. Something will go down, be it the Kinect or your VR headset.

You can imagine it like this:
USB controllers are circuit breakers.
USB ports are outlets.
USB hubs are power strips.

Not all outlets are connected to the same circuit breaker. If you put too much on one breaker, it trips. If you plug in a power strip, it doesn't add more capacity to the circuit breaker.

You should send us a screenshot so we can take a look at it for you.
""")

@bot.command(brief='how to setup owotrack')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def owotrack(ctx):
    await ctx.send("""
OwoTrack is another opensource app for using an Android phone or iPhone's compass, accelerometer and gyroscope to emulate the functionality of a waist tracker.
It can be used in conjunction with KinectToVR to give you more responsive hip movement.```Some caveats:
- Sitting down isn't that great unless you strap the phone to your chest instead of your waist.
- Not all phones are compatible! Check your phone model on GSMArena and look in the "Sensors" section, you need at least a gyroscope and accelerometer. (Cheap budget tier phones have a tendency to forego these for a baked in screen rotation sensor.)
- The iOS version isn't on the App Store, you must get it from a TestFlight beta testing link. (Not hard but important to mention)```
You can get the app over on the Discord here <https://discord.gg/HPuth34e5E>

Once you have that set up and working, you can disable KinectToVR's waist tracker by going to the Trackers tab and clicking "Disable Waist Tracker". You will be asked to restart SteamVR.`
""")

# @bot.command(brief='How to copy the right driver folder')
# async def copydrivers(ctx):
#     await ctx.send("https://bad-me.me/BuXasdy.mp4")
#     await ctx.send("If it doesn't work after doing this, check your SteamVR addons and ensure you copied the folder correctly.")

@bot.command(brief='How to enable the SteamVR driver')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def enabledriver(ctx):
    await ctx.send("https://k2vr.tech/img/steamvr_enable_driver.mp4")

@bot.command(brief='How to fix the Kinect thermistor by fucking cutting it off')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def thermistor(ctx):
    await ctx.send("https://www.youtube.com/watch?v=BoRK3jJVMLM")

@bot.command(brief='So you want psmove huh')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def psmove(ctx):
    await ctx.send("""
**Using PlayStation Move controllers and cameras with KinectToVR:**
This setup only works with PS Eyes and PSMoveService, you can't track the Move controllers with the Kinect.

For the setup, you'll want 2 or 3 PS Move controllers (if 2, you need to use OwoTrack for your waist), and at least 3 PS Eye cameras.

For general setup, we recommend this video by Cai VR: <https://www.youtube.com/watch?v=HQSeSZWSZ58>

Ignore the part about downloading the old version of PSMoveService, and the part about using PSMoveAPI to pair controllers. **You should download the newer fork: PSMoveServiceEX, by Externet, instead.**

Here's a link to that: <https://github.com/Timocop/PSMoveServiceEx>
""")

@bot.command(brief='Possibly confusing terms')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def glossary(ctx):
    await ctx.send("""
**K2VR:** KinectToVR (The main project)
**K2EX:** KinectToVR EX (The actual program)
**V1/V2:** Xbox 360 Kinect (V1) and Xbox One Kinect (V2)
**VCRedist:** Visual C++ Redistributable
**Flip:** Skeleton Flip (The feature that lets you turn around)
**OpenVR:** Open-source VR platform created by Valve that SteamVR is built upon. The name is borrowed by third-party utilities like OpenVR Advanced Settings and OpenVR Space-Calibrator. They shouldn't be referred to as "OpenVR" as it can cause confusion.
**OVRAS:** OpenVR Advanced Settings
**OVRIE:** OpenVR-InputEmulator
**ORVSC:** OpenVR-SpaceCalibrator
""")

@bot.command(brief='funny k2ex white screen crash')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def whitescreen(ctx):
    await ctx.send("""
**K2EX shows a white window then crashes, what do I do?**
You need to have your headset plugged in/connected and SteamVR needs to be running, as in, __rendering to the headset, you should see the dashboard and the mountains in the distance__ before starting KinectToVR.
If you've done all that and K2EX still crashes on startup, first try rebooting your computer. We'll go over additional troubleshooting if it's not fixed then.
""")

@bot.command(brief='changing kinect angle')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def angle(ctx):
    await ctx.send("""
You can change the angle of the Kinect just by pushing it. The Xbox 360 Kinect does have a motor, but it's not used by K2EX. The gears are solid enough that you can snap it by hand without fear of breaking it.

If you must insist on using the motor, Install the developer toolkit (http://download.microsoft.com/download/D/0/6/D061A21C-3AF3-4571-8560-4010E96F0BC8/KinectDeveloperToolkit-v1.8.0-Setup.exe) then run `Kinect Developer Toolkit Browser` from the start menu, in the `tools tab`, __run__ `Kinect Explorer D2D`
""")

@bot.command(brief='Jeffy B. aint got nothin on deez')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def amazon(ctx):
    await ctx.send("""
You can change the angle of the Kinect just by pushing it. The Xbox 360 Kinect does have a motor, but it's not used by K2EX. The gears are solid enough that you can snap it by hand without fear of breaking it.

If you must insist on using the motor, Install the developer toolkit (http://download.microsoft.com/download/D/0/6/D061A21C-3AF3-4571-8560-4010E96F0BC8/KinectDeveloperToolkit-v1.8.0-Setup.exe) then run `Kinect Developer Toolkit Browser` from the start menu, in the `tools tab`, __run__ `Kinect Explorer D2D`
""")

# @bot.command(brief='How to disable USB Selective Suspend')
# async def selectivesuspend(ctx):
#     await ctx.send("https://k2vr.tech/assets/selective-suspend.png")

# @bot.command(brief='How to disable USB Power Management')
# async def powermanagement(ctx):
#     await ctx.send("https://k2vr.tech/assets/power-management.png")

@bot.command(brief='trackers in status window')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def trackers(ctx):
    await ctx.send("""
This is what the trackers should look like in the SteamVR window if spawned successfully.
(Headset and controllers may vary obviously)
https://raytracing-benchmarks.are-really.cool/8n1aprf.png
""")

@bot.command(brief='most likely a frayed cable or ded adapter')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbone_cable(ctx):
    await ctx.send("""
If connecting the Kinect makes Windows say the USB device is not recognized. This means the descriptor event failed.
This is caused by a bad USB connection. Check every connector on your adapter (The cable at the back of the Kinect can also be disconnected.)
Try a different USB 3.0 cable to go from the adapter to your PC if you have one.

If a working cable and checking every connection doesn't fix it. Your adapter is most likely broken.
Most online retailers will allow you to get a refund or return the item.

You should avoid buying adapters from Amazon, as we've seen an alarming number of adapters ordered there actually arrive dead.
""")

@bot.command(brief='info about Xbox One VS Xbox 360 Kinect')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbone(ctx):
    await ctx.send("https://k2vr.tech/docs/why-avoid-kinectv2")

@bot.command(brief='info about Xbox One VS Xbox 360 Kinect')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbonefix(ctx):
    await ctx.send("https://k2vr.tech/docs/kinectv2-troubleshooting")

# @bot.command(brief='Xbox One Kinect and USB controllers')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def xbone_usb(ctx):
#     await ctx.send("""
# **Xbox One Kinect is very demanding when it comes to USB bandwidth:**
# Your computer's chipset has a number of USB controllers. Each with a limited amount of bandwidth to share between connected devices. If you try to connect two devices that together require more bandwidth than the one controller can provide, like a VR headset and an Xbox One Kinect, one of them will crash.

# You can check out your USB controllers using this tool: https://k2vr.tech/UsbTreeView.exe
# For it to work, you need at least two controllers capable of USB 3.0 or better.
# Also, ASMedia controllers are incompatible with the Kinect.
# """)

# @bot.command(brief='Diet Coke Xbox 360 Kinect more like')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def xbone_tracking(ctx):
#     await ctx.send("""
# **Xbox 360 Kinect is cheaper and gives the same tracking:**
# Both Kinect models use very different tracking technology, Yet still allow you to accomplish the same movements. The Xbox 360 Kinect only lacks in FOV and how close it can track but is otherwise equal to the Xbox One.
# """)

@bot.command(brief='Xbox One Kinect and base stations')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def xbone_lighthouse(ctx):
    await ctx.send("""
**Xbox One Kinect is incompatible with base stations:**
The Xbox One Kinect uses a time-of-flight sensor that sends out quick pulses of infrared light. Vive and Index base stations do the same, but the Kinect works on different timings, screwing up the headset and controller tracking with no easy way of fixing it.

With enough patience (multiple hours) you can get it semi-working. But you'll always have dead spots where your headset or controllers won't track.
""")

@bot.command(brief='Redoing your Oculus guardian')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def guardian(ctx):
    await ctx.send("http://www.emuvr.net/download/GuardianBoundaryEditor.zip\nhttps://raytracing-benchmarks.are-really.cool/6s3Lm92.png")

# @bot.command(brief='Installer 2.0 link')
# async def installer(ctx):
#     await ctx.send("""
# Download for K2EX Installer 2.1.2 (Installs K2EX 0.8.0):
# https://github.com/KinectToVR/k2vr-installer-gui/releases/download/2.1.2/k2ex-installer-2.1.2.exe
# """)

@bot.command(brief='How to reset playspace orientation on Rift CV1')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def playspace_rift(ctx):
    await ctx.send("""
**How to reset your playspace orientation on Oculus Rift:**```In most cases you can just do "Change Floor Height" in the "Rift and Touch" menu, and it will prompt you to set the playspace direction without resetting your entire guardian.```

• Open the Oculus desktop app, go to Devices > Oculus Rift and Touch > Reset Sensor Tracking
**• When instructed to point the controller towards your monitor, point it at the Kinect instead.**
• You will need to redraw your guardian after doing this.

You can confirm the direction of your playspace in SteamVR by looking for the arrow on the floor.
K2EX must be restarted after doing this for changes to take effect.
You will need to recalibrate K2EX.
https://raytracing-benchmarks.are-really.cool/5HyuYg8.png
""")

@bot.command(brief='How to reset playspace orientation on Rift S/Quest/Quest 2')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def playspace_laguna(ctx):
    await ctx.send("""
**How to reset your playspace orientation on Oculus Rift S/Quest/Quest 2:**
• For Rift S: Open the Oculus desktop app, go to Devices > Rift S and Touch > Guardian Setup
• For Quest/Quest 2: If inside an app, open the Universal Menu by pressing the Oculus button, go to Settings > Guardian
• Choose Roomscale Boundary.
• **During each step make sure to face the edge of your playspace where the Kinect is**
• Click "Confirm" to keep your current guardian boundary.
`The "laguna" headsets can only put your playspace at 90degree angles, so you can't put your Kinect in the corner of the room.`

You can confirm the direction of your playspace in SteamVR by looking for the arrow on the floor.
K2EX must be restarted after doing this for changes to take effect.
You will need to recalibrate K2EX.
https://raytracing-benchmarks.are-really.cool/5HyuYg8.png
""")

@bot.command(brief='How to reset playspace orientation on SteamVR headsets')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def playspace_lighthouse(ctx):
    await ctx.send("""
**How to reset your playspace orientation on HTC Vive/Valve Index:**
• Click on the SteamVR version on the status window and in the contextual menu, choose Run Room Setup.
• Choose Room Scale.
• When asked to point your headset towards your monitor for centering, **point it at the Kinect instead.**
• Continue with room setup as instructed.

You can confirm the direction of your playspace in SteamVR by looking for the arrow on the floor.
K2EX must be restarted after doing this for changes to take effect.
You will need to recalibrate K2EX.
https://raytracing-benchmarks.are-really.cool/5HyuYg8.png
""")

@bot.command(brief='How to reset playspace orientation on Mixed Reality headsets')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def playspace_wmr(ctx):
    await ctx.send("""
**How to reset your playspace orientation on Windows Mixed Reality:**
• Bring up the Mixed Reality Portal and expand the sidebar.
• Click on Set up room boundary.
• Choose Set me up for all experiences (Recommended).
• When asked to center the headset. Place it facing the Kinect, and **position it at the edge of your play area where the Kinect is.**
• Continue with setup dra-wing your boundary.

You can confirm the direction of your playspace in SteamVR by looking for the arrow on the floor.
K2EX must be restarted after doing this for changes to take effect.
You will need to recalibrate K2EX.
https://raytracing-benchmarks.are-really.cool/5HyuYg8.png
""")

# @bot.command(brief='One day it will be fixed')
# async def rotation(ctx):
#     await ctx.send("""
# Foot rotation for Xbox One Kinect is broken in K2EX 0.7.1
# Please update to K2EX 0.8.0 at https://k2vr.tech
# """)

# @bot.command(brief='KinectToVR calibration controls')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def controls(ctx):
#     await ctx.send("https://k2vr.tech/assets/controls.png")

@bot.command(brief='how to improve tracking')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def bettertracking(ctx):
    await ctx.send("https://k2vr.tech/docs/bettertracking")

@bot.command(brief='autostart and tracker autospawn')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def autostart(ctx):
    await ctx.send("https://k2vr.tech/docs/autostart")

@bot.command(brief='OVR Advanced Settings')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def ovras(ctx):
    await ctx.send("https://store.steampowered.com/app/1009850")

@bot.command(brief='Kinect FOV Explorer')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def fov(ctx):
    await ctx.send("https://www.smeenk.com/webgl/kinectfovexplorer.html")

@bot.command(brief='calibrate fbt at incredible hgih speed')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def tupper(ctx):
    await ctx.send("https://www.youtube.com/watch?v=hBBdFKITdJM")

@bot.command(brief='STOP BUYING THE XBOX ONE KINECT')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def rant(ctx):
    await ctx.send("https://www.youtube.com/watch?v=UiZKgHJHLT4")

@bot.command(brief='How to position the Kinect.')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def position(ctx):
    await ctx.send("https://k2vr.tech/docs/onboarding")

@bot.command(brief='its just the onboarding page morty')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def instructions(ctx):
    await ctx.send("https://k2vr.tech/docs/onboarding")

# @bot.command(brief='beta reddit chungus moment')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def beta(ctx):
#     await ctx.send("""
# **NO SUPPORT WILL BE PROVIDED FOR THE BETA. WE REFER TO IT AS 0.9 BUT THE BRANCH IS CALLED 0.8.1-TESTING AND THE WINDOW STILL SAYS 0.8.1**

# - You must have an existing 0.8.1 installation from K2EX Installer.
# - Go to <https://github.com/KinectToVR/KinectToVR/releases/tag/a0.8.1-testing> scroll down and download both the ZIPs for the app and the driver.
# - Extract the files to `C:\K2EX` or wherever you installed KinectToVR. Say yes to overwrite all.
# - Optionally, rename `main_theme.theme` to just `.theme` so that the black see-through theme works.

# Visual Instructions: https://streamable.com/w3wlna
# """)

# @bot.command(brief='OVRIE DLL Fix removal setps')
# async def ovrie(ctx):
#     await ctx.send("K2VR Installer installs both the release 1.3 of OpenVR-InputEmulator (<https://github.com/matzman666/OpenVR-InputEmulator/releases/tag/v1.3>) as well as a custom built DLL driver for SteamVR that replaces the existing one installed by OpenVR-InputEmulator's installer.  That DLL implements these two fixes (<https://github.com/matzman666/OpenVR-InputEmulator/pull/125> and <https://github.com/matzman666/OpenVR-InputEmulator/pull/130>)\n\nIn some cases, that dll will actually break SteamVR for some reason.  To replace it, find the folder where you downloaded the K2VR Installer, and next to it you should find a `temp` folder which contains the files it downloaded including `ovrie-1.3.exe`.  That's the OpenVR-InputEmulator installer. Run it and say yes to upgrade the existing installation. and it will reinstall the original DLL.")

@bot.command(brief='How to reset SteamVR to factory defaults')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def vrsettings(ctx):
    await ctx.send("SteamVR's main configuration file is located in `C:\Program Files (x86)\Steam\config\steamvr.vrsettings`\n\n")

# @bot.command(brief='Index/Vive Camera disable.')
# async def camera(ctx):
#     await ctx.send("""
# The HTC Vive (Including Pro and Pro Eye) and the Valve Index have their cameras handled by SteamVR unlike Oculus and WMR headsets which have their own drivers and dashboard handling passthrough.
#
# OpenVR-InputEmulator will cause SteamVR to crash when the camera is activated.  To fix it, go to Settings > Camera and turn it off. Then you can re-enable OpenVR-InputEmulator.
# """)

@bot.command(brief='CPU Reducing for Virgin Wizards')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def cpu(ctx):
    await ctx.send("""
__CPU REDUCING 101__
In Windows Settings:
- **Disable Game Mode** under Gaming (screws with Oculus processes)
- Under Privacy, go to background apps and **uncheck Allow apps to run in the background** to disable background processes from "modern apps"
- Open Start, search "Services" and open that, **find the "SysMain" service. Set the startup type to disabled and stop it in the properties window.** (SysMain is predictive application/DLL loading and is garbage)
- If you haven't done so already, **launch VRChat from Steam or Oculus, and then immediately hold Shift before the game shows up.** In the settings window change the graphics to DesktopLow, (This works in VR despite the stupid name, it disables antialiasing and caps mirror resolution, quite a dramatic performance improvement)

Otherwise, uhhh, stop running WallpaperEngine and your 844 tabs of chrome, VRChat and VR itself needs lots of RAM. especially in highly populated worlds.
""")

@bot.command(brief='thanks microsoft!!')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def redistfix(ctx):
    await ctx.send("""
In the same folder where you downloaded K2EX Installer there should be a folder named `k2vr-installer`
Download this file: https://aka.ms/vs/16/release/vc_redist.x64.exe
And copy it to the `k2vr-installer` folder and say yes to overwrite.
Run the installer again.
""")

@bot.command(brief='blazepose who?')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def posenet(ctx):
    await ctx.send("""
Webcam body tracking is glitchy and jittery because of its very nature. There's nothing you can do about that.

MediaPipe is based on TensorFlow, which has no way to run it on your GPU (graphics card) on Windows.  The CPU (processor) performance for machine learning is so bad, it can saturate a high-end 8-12 core chip and yet output less than 20fps.

If you've got nothing more than a webcam, you've got a much better chance using markers (Use the AprilTags driver, not D4VR.). It is still CPU-bound, but it will actually let you play VR and won't randomly jump around.
""")

@bot.command(brief='asmedia be like')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def usb(ctx):
    await ctx.send("""
USB ports and generations (2.0, 3.0, e.t.c.) aren't the whole story.

When connecting a USB device to your computer, each USB port is connected to a controller chip, which may be part of your motherboard, or integrated in your CPU.

There are various brands and revisions of these controllers. Generally, all USB 2.0 controllers are pretty mature and will work well for any task. But with USB 3.0/3.1/3.2, the situation gets more complicated, generally you want to:

Avoid: ASMedia, VIA, AMD pre-Ryzen and Fresco Logic controllers
Look for: Renesas/NEC, AMD Ryzen and Intel 3.1 controllers

Various brands will have better or worse handling and compatibility of USB devices, and will tolerate less or more bandwidth.
""")

@bot.command(brief='skeleton closet something idk')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def skeletonscale(ctx):
    await ctx.send("""
***DISCLAIMER!***
The Kinect SDK skeleton does not scale it's proportions to your body. No matter how short or tall you are, the waist and feet trackers will always be the same distance apart.

This is because Kinect was designed for gesture control for natural user interfaces (Hence the acronym NUI you may see across parts of the driver and SDK). And the goal was to allow the same gesture detection code to work for anyone.

I implore that you try using the resulting calibration from K2EX in VRChat before saying it's "wrong" or "the legs are too short".

As an extra important addendum to this, the offsets tab in K2EX is NOT there to fix this. If you touch anything there you will break your tracking. That tab is meant to make fine-tuning adjustments to the trackers for games that require it like Blade & Sorcery.

While we could scale the skeleton in software to match it to the user's height, as it stands, the un-scaled skeleton already provides more than adequate tracking when setup correctly. So there are no plans to do this.
""")

# @bot.command(brief='antialiasing bad!!')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def desktoplow(ctx):
#     await ctx.send("https://raytracing-benchmarks.are-really.cool/8fgJn9m.png")

# @bot.command(brief='this assumes the kinect works fine')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def calibration(ctx):
#     await ctx.send("""
# __Manual Calibration:__
# • Spawn trackers
# • Click `Show/Hide Skeleton Tracking` to make sure the Kinect can see you.
# ```Standing about 3 meters (9 feet) away will help with tracking.```
# • Turn off the preview once you've ensured it's working.
# • Click the checkbox labelled `Enable Manual Calibration` under the Begin Calibration button.
# • Click on `Begin Calibration`
# • Close out of the SteamVR dashboard by clicking outside of it.
# ```Don't open Oculus Dash, Virtual Desktop or anything that could take control away from SteamVR. You should be in the empty void!```
# • Use the trackpads/thumbsticks on your VR controllers to move and rotate the trackers around.
# • Press the grip on your right controller to switch back and forth between position and rotation modes.
# **You can hold the left controller's grip to make more fine-tuned adjustments.**
# ```If trackers aren't following you; E.g. walking forward makes the trackers walk to the left, use the left trackpad/thumbstick to rotate the trackers until they line up to your movements. Try taking a few steps to make sure.```
# • Hold triggers on **both controllers** to save and confirm.
# """)

# WEB COMMANDS WOOOO DOCS

# @bot.command(brief='(Web) How to fix Code -10')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def wminus10(ctx):
#     await ctx.send("https://k2vr.tech/docs/minus10")

# @bot.command(brief='(Web) nui_notgenuine fix')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def wnotgenuine(ctx):
#     await ctx.send("https://k2vr.tech/docs/notgenuine")
    
# @bot.command(brief='(Web) nui_notpowered fix')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def wnotpowered(ctx):
#     await ctx.send("https://k2vr.tech/docs/notpowered")

# @bot.command(brief='(Web) Calibration instructions')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def wcalibration(ctx):
#     await ctx.send("https://k2vr.tech/docs/calibration")

@bot.command(brief='(Web) Calibration instructions but without w')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def calibration(ctx):
    await ctx.send("https://k2vr.tech/docs/calibration")

# @bot.command(brief='How to fix Code -10')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def minus10(ctx):
#     await ctx.send("""
# __Fixing Code -10:__
# Check in SteamVR settings > Startup/Shutdown > Manage Add-ons if KinectToVR is there and enabled, if it's blocked or disabled, enable it then restart SteamVR. (*SteamVR settings can be accessed by clicking the label in the top-left of the small status window.*)

# **If it's not listed in Manage Add-ons,** __close SteamVR__ and open the file `%localappdata%\openvr\openvrpaths.vrpath` in Notepad or your text editor of choice.

# In the section labelled `"external_drivers"` you want to make sure you have a line that links to the KinectToVR driver folder, in the default installation folder, that would be `"C:\\\\K2EX\\\\KinectToVR"`.

# If you have other lines in your drivers list, make sure to add a comma to the last one that was there. And don't add a comma after your new line as it's the last item.

# ` "one", "two", "three"  ` :white_check_mark: 
# `                        `
# ` "one", "two" "three"   ` :x:
# `             ^          `
# ` "one", "two", "three", ` :x:
# `                      ^ `

# Here's what my vrpaths file looks like for example: <https://pastebin.com/raw/dkw5rnWB>

# After doing that, go back to the first step and make sure the driver is actually there when you launch SteamVR again.
# """)

@bot.command(brief='how to fix error -10')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def minus10(ctx):
    await ctx.send("https://k2vr.tech/docs/minus10")

@bot.command(brief='alias of vcredist')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def vcredists(ctx):
    await ctx.send("""
__Downloads for Visual C++ Redistributables (x64):__
**This is probably the one you need! -->** 2015-2019: https://aka.ms/vs/16/release/vc_redist.x64.exe
2013: https://aka.ms/highdpimfc2013x64enu
2012: https://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe
2010: https://download.microsoft.com/download/3/2/2/3224B87F-CFA0-4E70-BDA3-3DE650EFEBA5/vcredist_x64.exe
""")

@bot.command(brief='how tu oonninstallle konenect to vr')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def uninstall(ctx):
    await ctx.send("""
You can uninstall KinectToVR from the Windows add/remove programs list.
Press <:windowskey:845064227633889290> + I then go to Apps and find KinectToVR. Then click on it and click Uninstall.
Follow the directions.

**If the uninstaller fails:**
Delete the folder `C:\K2EX`
Click the shortcut in the start menu, Windows will prompt you to remove the shortcut. Click yes.
Click the uninstall button in Add/Remove Programs, Windows will prompt you to remove it. Click yes.

**If you wish to reinstall K2EX, you must remove the registry entry:**
Press <:windowskey:845064227633889290> + R and type `regedit`
Find `HKEY_LOCAL_MACHINE` > `Software` > `KinectToVR` and delete that registry folder.
You can now reinstall K2EX.
If you don't want to reinstall, this step is not needed.
""")

@bot.command(brief='runtime/sdk/toolkit explanation')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def sdkruntime(ctx):
    await ctx.send("""
<:Devices_KinectV1:798503278346371073> __The Xbox 360 Kinect (Kinect for Windows V1) has three versions of the driver:__
**• Kinect for Windows Runtime v1.8:** Bare minimum including drivers to run the Kinect device. Does not support Xbox Kinect.
**• Kinect for Windows SDK v1.8:** Includes runtime, adds support for Xbox Kinect and header files for development. This is required for using KinectToVR.
**• Kinect for Windows Developer Toolkit v1.8:** Includes SDK and runtime, also adds about 200MB of developer sample programs so that you can make stuff with the SDK. Completely optional.

<:Devices_KinectV2:798503291959902208> __The Xbox One Kinect (Kinect for Windows V2) has two versions:__
**• Kinect for Windows Runtime v2.0:** These drivers are enough to run both Xbox Kinect and Windows Kinect.
**• Kinect for Windows SDK v2.0:** Includes Kinect Studio, and developer samples including Kinect Configuration Verifier.
""")

@bot.command(brief='openvrpaths funny')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def vrpath(ctx):
    await ctx.send("""
**If your PC has only one user account:**
• Shutdown SteamVR if it's running.
• Using the Windows run dialog or a file explorer, go to the `%localappdata%\openvr` folder
• Delete the file `openvrpaths.vrpath` in the folder, it's the only file.```
You should make a copy or simply rename the file if you have other SteamVR drivers/add-ons you want to easily restore aftwards.```• Launch SteamVR with your headset working so it generates an updated copy of the file.
• Close SteamVR again and relaunch K2EX Installer.
**If your PC has multiple accounts (Especially if you aren't administrator):**
• Log into the administrator account, and run K2EX Installer.
(The installation is global for all user accounts so it doesn't matter who uses it.)
• Lob back into your main account and follow through the calibration instructions on the website.
""")

@bot.command(brief='usb controller explanation')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def controller(ctx):
    await ctx.send("""
USB controllers have a limited amount of bandwidth. If you connect devices into them that go over the amount of bandwidth they have. Something will go down, be it the Kinect or your VR headset.

You can imagine it like this:
USB controllers are circuit breakers.
USB ports are outlets.
USB hubs are power strips.

Not all outlets are connected to the same circuit breaker. If you put too much on one breaker, it trips. If you plug in a power strip, it doesn't add more capacity to the circuit breaker.
""")

@bot.command(brief='[JP] autocalibration instructions')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def jp_calibration(ctx):
    await ctx.send("""
**キャリブレーション:**
- SteamVRを開くと、何もない部屋が出迎えてくれます。 これがSteamVR Compositorです。ゲームが起動していないときに表示されます。
- ダッシュボードを開き、「デスクトップ」をクリックします。
- スタートメニューからKinectToVRを見つけて起動し、起動するのを待ちます。
- 「Show/Hide Skeleton Tracking」をクリック。Kinectで体が見えることを確認します。
`3メートル離れた場所に立つ必要があります。そうでなければスケルトン追跡は機能しません。`
- プレビューをオフにすることができます。
- 「Spawn Trackers」をクリック。トラッカーが近くに表示されるはずです。
`トラッカーがかなり離れている可能性があります。`
`SteamVRのステータスウィンドウに表示されていれば問題ありません。`
- 「Begin Calibration」をクリック。画面の指示に従ってください。*英語だけなのは知っています。*
- 3秒間、所定の位置に立ちます。
- 別の場所に移動します。
- これを2回繰り返します。
- 最後にKinectの方を3秒間見ます。
""")

@bot.command(brief='vc redist downloads')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def vcredist(ctx):
    await ctx.send("""
__Downloads for Visual C++ Redistributables (x64):__
**This is probably the one you need! -->** 2015-2019: https://aka.ms/vs/16/release/vc_redist.x64.exe
2013: https://aka.ms/highdpimfc2013x64enu
2012: https://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe
2010: https://download.microsoft.com/download/3/2/2/3224B87F-CFA0-4E70-BDA3-3DE650EFEBA5/vcredist_x64.exe
""")

@bot.command(brief='how shit works')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def howitworks(ctx):
    await ctx.send("""
**How KinectToVR works:**
The Kinect captures it's depth data (here's a paper about it http://pages.cs.wisc.edu/~dyer/cs534/slides/17_kinect.pdf)
It's then sent to the PC over USB, and read by the Kinect driver.
KinectToVR queries the Kinect SDK to do skeleton tracking from the depth data (here's another paper about it https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Microsoft20Kinect20Sensor20and20Its20Effect20-20IEEE20MM202012.pdf)
It uses the generated skeleton data and sends the position and rotation data of the two ankles and the waist to a SteamVR driver that creates virtual Vive trackers.
SteamVR games see these trackers the same as real ones.
""")

# @bot.command(brief='how 2 delet old drivur')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def deletedriver(ctx):
#     await ctx.send("""
# **This only matters if you followed the instructions from the old "copydrivers" command**
# In the eventuality that K2EX Installer didn't delete a previous version of the KinectToVR driver, here's how.
# Open Steam, go to the library, find SteamVR.
# Right-click it in the list, go to Manage then Browse local files.
# Double-click on drivers, and delete the folder named "KinectToVR"
# """)

@bot.command(brief='I dont trust that norton guy')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def antivirus(ctx):
    await ctx.send("""
**Antivirus software sucks.** Firewall software sucks. Fuck Driver Booster, PC Optimizer and Norton.
**None of them actually do anything useful or that Windows Defender can't do better, for free, and using less system resources.**

The best protection against viruses is to **leave Windows Defender on**, have an ad-blocker, keep your web browser and operating system updated and **using COMMON SENSE.**

Mutahar a.k.a. SomeOrdinaryGamers has a video about this
https://www.youtube.com/watch?v=osqF50XhJEg
""")

@bot.command(brief='NO YOUR KINECT IS NOT BROKEN')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def notpowered(ctx):
    await ctx.send("https://k2vr.tech/docs/notpowered")

#     await ctx.send("""
# • Unplug the Kinect from your computer
# • Press <:windowskey:845064227633889290> + X
# • Click on "Apps and Features"
# *You may have to wait up to 30 seconds while the list loads*
# • Click the search box on the right labelled "Search this list"
# • Type "Kinect"
# • For each item that appears, click on it then click "Uninstall"
# • Restart your computer
# • Plug the Kinect back into your computer
# • Reinstall the Kinect SDK, here's the link: <https://download.microsoft.com/download/E/1/D/E1DEC243-0389-4A23-87BF-F47DE869FC1A/KinectSDK-v1.8-Setup.exe>
# • Open Device Manager
# • Ensure that "Kinect for Windows" contains the following
#   • Kinect for Windows Audio Array Control
#   • Kinect for Windows Camera
#   • Kinect for Windows Device
#   • Kinect for Windows Security Control
# **This is the magic fixing part**
# • If any of these show up under the "Other Devices" category, right-click each of them and click "Uninstall device"
# (They may have different names such as "Xbox NUI Camera" or "Audios")
# • Unplug and replug your Kinect for changes to take effect.
# They should re-appear in the "Kinect for Windows" category and your Kinect should be working.
# """)

@bot.command(brief='you dont need it to spin around.')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def multikinect(ctx):
    await ctx.send("""
__About using multiple Kinect sensors:__

There are multiple practical and technical factors at play that make implementing multi-kinect non-viable.

• In the Kinect for Windows documentation, it is said here (<https://docs.microsoft.com/en-us/previous-versions/windows/kinect-1.8/dn188677(v=ieb.10)>) that while it's fully possible to do skeleton tracking from multiple Kinect sensors at once, pointing two of them at the same play area would cause infrared interference, and the tracking SDK does not provide an easy solution for merging the skeletons together.
• The USB bandwidth requirement for a single device is already often a limiting factor and causes random disconnects for some users. Attempting to run two at once would be very difficult.
• The minimum distance required for tracking gets doubled in two directions of your room. (Most of us are in small apartments or college dorms)
• Combining the data from both sensors without making a mess is about as hard as rewriting the tracking code from scratch. At that point, you could create a much better and modern tracking tech based on the kinect depth map.

TL;DR
Support for multiple Kinect sensors will never happen.
""")

@bot.command(brief='Buying links for Renesas cards')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def renesas(ctx):
    await ctx.send("""
Renesas chipset USB controller PCI Express add-in card:
Amazon UK: <https://www.amazon.co.uk/SEDNA-Express-Adapter-Profile-uPD720201/dp/B0183G6696>
Amazon US: <https://www.amazon.com/SEDNA-Express-Adapter-Renesas-720201/dp/B00VV6YJKE>
Similar cards can be found elsewhere, but make sure they have an NEC/Renesas controller on them.
""")

# @bot.command(brief='How to fix Kinect One FINALLY')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def tracking(ctx):
#     await ctx.send("""
# __How to fix your god damn Kinect One tracking (why did you buy it?):__
# **• Open Kinect Studio v2.0** it can be found in the <:windowskey:845064227633889290> Start Menu by searching for it. Then click Connect in the top-left. Then if needed, Monitor view.
# You'll notice a "fog" on the floor where your feet stop being tracked. This is what we're trying to fix.
# **• Cover your play area floor in __black__ rugs.** This will reduce the amount of infrared light that bounces back to the Kinect sensor.```Be careful! If the entire floor becomes IR absorbing, the Kinect might not be able to detect the floor anymore, and won't be able to calibrate properly!```**• Put a piece of cardboard or sheet on top of the Kinect.** You want to create sort of a cap like this
# """)
#     await ctx.send("https://i.imgur.com/UiX5giS.png")
#     await ctx.send("""
# over the sensor to reduce the overall light that goes into it, so your rugs appear completely invisible to the Kinect. Refer to Kinect Studio's preview to help you.
# **• Enjoy your tracking** and __discourage anyone else from buying Kinect One over the 360 and send them to our server instead.__
# """)

# @bot.command(brief='How to set tracker roles')
# async def roles(ctx):
#     await ctx.send("""
# **Setting up Vive tracker roles in SteamVR:**
# Go to SteamVR settings > Controllers > Manage Vive Trackers, then find the three trackers lit in green and set them as:
# LHR-CB11ABEC: **Waist**
# LHR-CB1441A7: **Right Foot**
# LHR-CB9AD1T2: **Left Foot**
# `The order may vary`
# """)

# @bot.command(brief='If K2VR crashes with SteamVR open.')
# async def crash(ctx):
#     await ctx.send("""
# __Troubleshooting steps for KinectToVR crashing when launching with SteamVR:__
# - Run KinectToVR as administrator. **IF IT DOESN'T WORK AS ADMIN, RUN NORMALLY THE NEXT TIME**
# - Restart your PC.
# - Reinstall OpenVR-InputEmulator. (The installer for it is in the `temp` folder created by K2VR Installer but you can also download the 1.3 version from Github yourself.)
# - Delete your SteamVR configuration file (custom controller bindings will be reset for any games, but you can re-apply them.) The file is in `C:\Program Files (x86)\Steam\config\steamvr.vrsettings`
# """)

# @bot.command(brief='Youre not getting NN-based FBT')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def nvidia(ctx):
#     await ctx.send("""
# __About NVIDIA's pose estimation:__
# We don't know if it's actually running in real-time. Even if it is and doesn't use too much GPU, you'll still need to buy a really expensive graphics card to use it. (No way this runs without a performance loss on 20 series)
# At that point, just go out and buy trackers.

# All that was shown was a hand-picked 5 second demo with editing.
# NVIDIA makes their AI research findings available to everyone else months before using it in their own tech.  If they had a brand-spanking new optimized NN for high framerate lightweight pose estimation, we would've known about it a long time ago.

# Current pose estimation technology is either imprecise or takes monumental amounts of GPU power to run at like 30fps.  When compared to the tiny CPU footprint of Kinect tracking, the incentive to create a full-body tracking method based on it is very slim.
# """)

@bot.command(brief='skeleton tracker positions')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def skeleton(ctx):
    await ctx.send("https://i.imgur.com/FrE1E9D.png")

@bot.command(brief='dev toolkit 1.8')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def toolkit(ctx):
    await ctx.send("Install the developer toolkit (http://download.microsoft.com/download/D/0/6/D061A21C-3AF3-4571-8560-4010E96F0BC8/KinectDeveloperToolkit-v1.8.0-Setup.exe) then run `Kinect Developer Toolkit Browser` from the start menu, in the `tools tab`, __run__ `Kinect Explorer D2D`")
    await ctx.send("https://i.imgur.com/SLk7Vm4.png")
    await ctx.send("**Make sure to close KinectToVR first if it is running! Only one app can use the Kinect at a time.**")

# @bot.command(brief='InputEmulator be like')
# async def camera(ctx):
#     await ctx.send("The HTC Vive, Vive Pro and Valve Index use SteamVR for their passthrough cameras.  But OpenVR-InputEmulator, which is required by ")

@bot.command(brief='download stats from github')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def downloadcount(ctx):
    installercount = os.popen("curl -s https://api.github.com/repos/kinecttovr/k2vr-installer-gui/releases | egrep 'download_count'  | cut '-d:' -f 2 | sed 's/,/+/' | xargs echo | xargs -I N echo N 0  | bc").read().rstrip("\n")
    appcount = os.popen("curl -s https://api.github.com/repos/kinecttovr/kinecttovr/releases | egrep 'download_count'  | cut '-d:' -f 2 | sed 's/,/+/' | xargs echo | xargs -I N echo N 0  | bc").read().rstrip("\n")
    await ctx.send(f"""
**⬇ Download stats:**
K2EX Installer: {installercount}
KinectToVR: {appcount}
""")

@bot.command(pass_context=True, brief="Opt in to updates.")
@commands.cooldown(1, 3, commands.BucketType.channel)
async def optin(ctx):
    member = ctx.message.author
    role = ctx.message.guild.get_role(718351639940956160)
    await member.add_roles(role)
    await ctx.send("You're now opted in to updates for KinectToVR and K2VR Installer.")

# @bot.command(pass_context=True, brief="K2EX info.")
# async def k2ex(ctx):
#     # member = ctx.message.author
#     # role = ctx.message.guild.get_role(738957357765230673)
#     # await member.add_roles(role)
#     await ctx.send("This command is deprecated. Please read <#741268778674946049> for details.")

@bot.command(pass_context=True, brief="Opt out of updates.")
@commands.cooldown(1, 3, commands.BucketType.channel)
async def optout(ctx):
    member = ctx.message.author
    role = ctx.message.guild.get_role(718351639940956160)
    await member.remove_roles(role)
    await ctx.send("Opted out of updates.")

# @bot.command(brief='Love to hear percussion')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def spin(ctx):
#     await ctx.send("https://imgur.com/TIIiDcS")
#     await ctx.send("This is using Xbox 360 Kinect. The first part has foot rotation set to Use Head Orientation.")

# @bot.command(brief='turn the beat around')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def spin2(ctx):
#     await ctx.send("https://imgur.com/HNDATq8")
#     await ctx.send("This is using Xbox 360 Kinect, you need a big room to do this. Default rotation modes won't turn this smoothly.")

# @bot.command(brief='Love to hear it')
# @commands.cooldown(1, 3, commands.BucketType.channel)
# async def spin3(ctx):
#     await ctx.send("https://imgur.com/ThSjFHD")
#     await ctx.send("This is using Xbox 360 Kinect.")

@bot.command(brief='Love to hear it')
@commands.cooldown(1, 3, commands.BucketType.channel)
async def spin3(ctx):
    await ctx.send("https://imgur.com/NH4ioJR")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.channel)
async def avatar(ctx):
    await ctx.send(ctx.message.author.avatar_url)

@bot.command()
async def nt(ctx, *msg: str):
    if ctx.channel.id == 785573754197508096:
        channel = bot.get_channel(424351941624070146)
        await channel.send(" ".join(msg))
    if ctx.channel.id == 785583685948276758:
        channel = bot.get_channel(738957751450992680)
        await channel.send(" ".join(msg))

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.channel)
async def role(ctx, device: str, mention: str):
    # set funny variables
    device = device.lower()
    mention = re.sub("[^0-9]", "", mention)
    id = int(mention)
    role = 0

    # gatekeeping
    helpers = ctx.guild.get_role(842754493858054204)
    if not (helpers in ctx.author.roles):
        await ctx.send("You are not a helper or moderator!")
        return

    # device parse
    if device == "v1":
        role  = 708579395585048646
    elif device == "v2":
        role = 708579697600102411
    elif device == "psmove":
        role = 708579825283104768
    elif device == "360":
        role = 708579395585048646
    elif device == "one":
        role = 708579697600102411
    else:
        await ctx.send("Invalid or missing role! Valid options are `v1`, `v2`, `360`, `one` or `psmove`.")
        return
    await ctx.send(f"device: {device}\nrole: {role}\nmention: {mention}")

    # get user and give role
    user = ctx.message.guild.get_member(id)
    # if not user:
    #     await ctx.send("User could not be found!")
    #     return
    role_object = ctx.message.guild.get_role(role)
    user.add_roles(role_object)
    await ctx.send(f"Gave `{device}` to {user.display_name}.")

bot.run(token)