import pygame
import json
import os
from pygame.mixer import Channel
from cookie import Cookie, cookieSound
from gui import GUI
from score import Score
from buttons import Button
from upgradeIcon import Image, Text
from titleScreen import Title
from playtime import PlaytimeDisplay


def main():
    global started, clickedBlocked, TwoXMoney2min, TwoXMoney5min, abiliti2xMoneyIcon, FiftyOff, shop_window_open, levelTreeScreen, nextLvlScreen
    running = True
    ckClicked = False
    nextLvlScreen = False
    levelTreeScreen = False
    clickedBlocked = False

    shop_window_open = False
    TwoXMoney2min = False
    TwoXMoney5min = False
    FiftyOff = False

    stats = {
        "Ck_s": 0,
        "cookies": 0,
        "fingers": 1,
        "gAmount": 0,
        "oAmount": 0,
        "farmAmount": 0,
        "fAmount": 0,
        "bAmount": 0,
        "aAmount": 0,
        "tAmount": 0,
        "rAmount": 0,
        "eAmount": 0,
        "batteryAmount": 0,
        "roboArmAmount": 0,
        "botAmount": 0,
        "aiAmount": 0,
        "solarAmount": 0,
        "gigaAmount": 0,
        "ciberAmount": 0,
        "twitterAmount": 0,
        "gaming": 0,
        "mysteryAmount": 0,
        "mouse": 0,
        "controller": 0,
        "playstation": 0,
        "chair": 0,
        "pc": 0,
        "arcade": 0,
        "gamerGirl": 0,
        "gamingStore": 0,
        "nvidea": 0,
        "brain": 0,
        "event": 0,
        "nextLvL": 0,
        "playtime": 0,
    }

    pygame.init()
    window = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Cookie Clicker")

    GREEN = 0, 255, 0
    LIGHTBLUE = 0, 255, 255
    BROWN = 139, 69, 19
    PINK = 255, 105, 180
    LIGHTPURPLE = 255, 0, 255

    if os.path.exists("statsDic.json"):
        with open("statsDic.json", "r") as file:
            stats = json.load(file)
    else:
        with open("statsDic.json", "w") as file:
            json.dump(stats, file)

    saved_playtime = stats.get("playtime", 0)
    start_ticks = pygame.time.get_ticks() - saved_playtime
    
    def wood(): 
        global cookie, gui, score, titleScreen
        cookie = Cookie(
            window, pygame.image.load(r"assets/images/cookie3.png"), 330, 330
        )
        gui = GUI(
            window,
            pygame.image.load(r"assets\images\backgoundWood.png"),
            pygame.image.load(r"assets/images/frame.png"),
            (400, 600),
            pygame.image.load(r"assets/images/shop.png"),
            (300, 100),
            pygame.image.load(r"assets/images/frame2.png"),
            pygame.image.load(r"assets/images/upgradesFrame.png"),
            (300, 100)
        )
        score = Score(window, pygame.image.load(r"assets/images/cookieCount.png"), 300, 100)

    def stone():
        global cookie, gui, score, titleScreen
        cookie = Cookie(
            window, pygame.image.load(r"assets\images\lvlTwo\batery.png"), 270, 310
        )
        gui = GUI(
            window,
            pygame.image.load(r"assets\images\lvlTwo\backgoundStone.png"),
            pygame.image.load(r"assets\images\lvlTwo\shop2_stone.png"),
            (320, 530),
            pygame.image.load(r"assets\images\lvlTwo\shop_stone.png"),
            (300, 100),
            pygame.image.load(r"assets\images\lvlTwo\frame2.png"),
            pygame.image.load(r"assets\images\lvlTwo\upgrade_stone.png"),
            (315, 90)
        )
        score = Score(window, pygame.image.load(r"assets\images\lvlTwo\batteryFrame.png"), 300, 100)

    def lava():
        global cookie, gui, score, titleScreen
        cookie = Cookie(
            window, pygame.image.load(r"assets\images\lvlThree\pig.png"), 270, 310
        )
        gui = GUI(
            window,
            pygame.image.load(r"assets\images\lvlThree\b3.png"),
            pygame.image.load(r"assets\images\lvlThree\goldShop2.png"),
            (330, 530),
            pygame.image.load(r"assets\images\lvlThree\goldShopFrame.png"),
            (330, 110),
            pygame.image.load(r"assets\images\lvlThree\frame3.png"),
            pygame.image.load(r"assets\images\lvlThree\goldUpgradeFrame.png"),
            (315, 90)
        )
        score = Score(window, pygame.image.load(r"assets\images\lvlThree\goldFrame.png"), 250, 95)

    if stats["nextLvL"] == 0:
        wood()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1150, 570, 30, 30))
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(870, 570, 30, 30))
        print("wood")

    if stats["nextLvL"] == 1:
        stone()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(870, 570, 30, 30))
        print("stone")

    if stats["nextLvL"] >= 2:
        lava()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1110, 570, 30, 30))
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(870, 570, 30, 30))
        print("lava")

    if stats["nextLvL"] == 0 or stats["nextLvL"] == 1 or stats["nextLvL"] >= 2:
        shopScreen = Title(window)

    started = False

    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1
    eventUserInactive = pygame.USEREVENT + 2
    eventBlockClick = pygame.USEREVENT + 3
    event2xMoney2min = pygame.USEREVENT + 4
    event2xMoney5min = pygame.USEREVENT + 5

    clickSoundCookie = r"assets/sounds/cookieS.mp3"
    clickSoundBattery = r"assets/sounds/batteryS.mp3"
    clickSoundPig = r"assets/sounds/pigS.wav"

    InfoFrameImage = pygame.image.load(r"assets/images/info-Frame.png")
    infoFrame = pygame.transform.scale(InfoFrameImage, (600, 600))

    InfoFrameImage2 = pygame.image.load(r"assets\images\lvlTwo\info-Frame2.0.png")
    infoFrame2 = pygame.transform.scale(InfoFrameImage2, (900, 600))

    InfoFrameImage3 = pygame.image.load(r"assets\images\lvlThree\lavaInfo.png")
    infoFrame3 = pygame.transform.scale(InfoFrameImage3, (950, 550))

    pauseMusic = Button(window, r"assets/images/mute.png", 255, 30, 30, 40, 40, pygame.Rect(10, 600, 30, 30))

    abiliti2xMoneyIcon = Image(window, r"assets\buttons\abilities\twoXMoney.png", 60, 60)
    abiliti5min2xMoneyIcon = Image(window, r"assets\buttons\abilities\TwoxMoneyTwo.png", 60, 60)
    abiliti50offIcon = Image(window, r"assets\buttons\abilities\fiftyoff.png", 60, 60)
    redLine = Image(window, r"assets\images\redLine.png", 80, 100)

    granny = Image(window, r"assets/upgrades/granny.png", 80, 80)
    oven = Image(window, r"assets/upgrades/oven.png", 80, 80)
    farm = Image(window, r"assets/upgrades/farm.png", 95, 80)
    factory = Image(window, r"assets/upgrades/factory.png", 80, 80)
    bank = Image(window, r"assets/upgrades/bank.png", 65, 65)
    alien = Image(window, r"assets/upgrades/alien.png", 80, 80)
    tesla = Image(window, r"assets/upgrades/tesla.png", 80, 80)
    rocket = Image(window, r"assets/upgrades/rocket.png", 65, 65)

    battey = Image(window, r"assets\upgrades\lvl2\battery.png", 60, 60)
    roboArm = Image(window, r"assets\upgrades\lvl2\roboArm.png", 70, 70)
    bot = Image(window, r"assets\upgrades\lvl2\bot.png", 85, 70)
    ai = Image(window, r"assets\upgrades\lvl2\ai.png", 80, 80)
    solar = Image(window, r"assets\upgrades\lvl2\solar.png", 65, 65)
    giga = Image(window, r"assets\upgrades\lvl2\giga.png", 70, 70)
    ciber = Image(window, r"assets\upgrades\lvl2\ciber.png", 80, 80)
    twitter = Image(window, r"assets\upgrades\lvl2\twitter.png", 55, 55)

    controller = Image(window, r"assets\upgrades\lvl3\controller.png", 65, 65)
    playstation = Image(window, r"assets\upgrades\lvl3\playstation.png", 60, 60)
    chair = Image(window, r"assets\upgrades\lvl3\chair.png", 80, 80)
    pc = Image(window, r"assets\upgrades\lvl3\pc.png", 80, 80)
    arcade = Image(window, r"assets\upgrades\lvl3\arcade.png", 60, 60)
    gamerGirl = Image(window, r"assets\upgrades\lvl3\gamerGirl.png", 70, 70)
    gamingStore = Image(window, r"assets\upgrades\lvl3\game-store.png", 60, 60)
    nvidia = Image(window, r"assets\upgrades\lvl3\nvidia.png", 80, 80)

    grannyAmount = Text(window, 50, GREEN)
    ovenAmount = Text(window, 50, GREEN)
    farmAmount = Text(window, 50, GREEN)
    factoryAmount = Text(window, 50, GREEN)
    bankAmount = Text(window, 50, GREEN)
    aliensAmount = Text(window, 50, GREEN)
    teslaAmount = Text(window, 50, GREEN)
    rocketAmount = Text(window, 50, GREEN)

    batteryAmount = Text(window, 50, LIGHTBLUE)
    roboArmAmount = Text(window, 50, LIGHTBLUE)
    botAmount = Text(window, 50, LIGHTBLUE)
    aiAmount = Text(window, 50, LIGHTBLUE)
    solarAmount = Text(window, 50, LIGHTBLUE)
    gigaAmount = Text(window, 50, LIGHTBLUE)
    ciberAmount = Text(window, 50, LIGHTBLUE)
    twitterAmount = Text(window, 50, LIGHTBLUE)

    controllerAmount = Text(window, 50, PINK)
    playstationAmount = Text(window, 50, PINK)
    chairAmount = Text(window, 50, PINK)
    pcAmount = Text(window, 50, PINK)
    arcadeAmount = Text(window, 50, PINK)
    gamerGirlAmount = Text(window, 50, PINK)
    gamingStoreAmount = Text(window, 50, PINK)
    nvideaAmount = Text(window, 50, PINK)

    def music():
        backgroundMusic = r"assets/sounds/beat.mp3"
        # mixer.music.load(backgroundMusic)
        # mixer.music.set_volume(0.05)
        # pygame.mixer.music.play(loops=100)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(backgroundMusic), loops=-1)
        Channel(1).set_volume(0.1)
        # mixer.music.play()

    def musicLvl2():
        backgroundMusic = r"assets/sounds/beat2.mp3"
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(backgroundMusic), loops=-1)
        Channel(2).set_volume(0.1)

    def musicLvl3():
        backgroundMusic = r"assets/sounds/beat3.wav"
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(backgroundMusic), loops=-1)
        Channel(3).set_volume(0.3)
    
    def playElonMa():
        emonMa = r"assets\sounds\elonma.mp3"
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(emonMa), loops=0)
        Channel(4).set_volume(0.5)
    
    def playGamingSound():
        gaming = r"assets\sounds\gaming.wav"
        pygame.mixer.Channel(5).play(pygame.mixer.Sound(gaming), loops=0)
        Channel(5).set_volume(0.5)

    def reset():
        global started, cookie, gui, score
        started = True
        stats["Ck_s"] = 0
        stats["cookies"] = 0
        stats["fingers"] = 1
        stats["gAmount"] = 0
        stats["oAmount"] = 0
        stats["farmAmount"] = 0
        stats["fAmount"] = 0
        stats["bAmount"] = 0
        stats["aAmount"] = 0
        stats["tAmount"] = 0
        stats["rAmount"] = 0
        stats["eAmount"] = 0
        stats["batteryAmount"] = 0
        stats["roboArmAmount"] = 0
        stats["botAmount"] = 0
        stats["aiAmount"] = 0
        stats["solarAmount"] = 0
        stats["gigaAmount"] = 0
        stats["ciberAmount"] = 0
        stats["twitterAmount"] = 0
        stats["gaming"] = 0
        stats["mysteryAmount"] = 0
        stats["mouseAmount"] = 0
        stats["controllerAmount"] = 0
        stats["playstationAmount"] = 0
        stats["chairAmount"] = 0
        stats["pcAmount"] = 0
        stats["arcadeAmount"] = 0
        stats["gamerGirlAmount"] = 0
        stats["gamingStoreAmount"] = 0
        stats["nvideaAmount"] = 0
        stats["brainAmount"] = 0
        stats["rebirthAmount"] = 0
        stats["event"] = 0
        stats["nextLvL"] = 0
        stats["playtime"] = 0

        Channel(2).stop()

        #* abilities
    def onAbility2xMoneyClick():
        global TwoXMoney2min
        stats["cookies"] -= 10000000000
        TwoXMoney2min = True
        pygame.time.set_timer(event2xMoney2min, 120000)
    
    def onAbiliti5min2xMoneyClick():
        global TwoXMoney5min
        stats["rebirthAmount"] -= 1
        TwoXMoney5min = True
        pygame.time.set_timer(event2xMoney5min, 300000)

    def onRebirthClick():
        # +10% more cookie production
        stats["rebirthAmount"] += 1

    def onAbility50OffClick():
        global FiftyOff
        # stats["rebirth"] -= 2
        FiftyOff = True
        # 50% off all upgrades for 30 seconds
    
        #* lvl1
    def onButtonFingerClick():
        stats["cookies"] -= 25 if FiftyOff else 50
        stats["fingers"] += 1
        # cookie.increaseS = stats["fingers"]

    def onButtonGrannyClick():
        stats["cookies"] -= 250 if FiftyOff else 500
        pygame.time.set_timer(timer_event, 1000)
        stats["gAmount"] += 1
        stats["Ck_s"] += 5
        stats["event"] = 1

    def onButtonOvenClick():
        stats["cookies"] -= 1000 if FiftyOff else 2000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 20
        stats["oAmount"] += 1

    def onButtonFarmClick():
        stats["cookies"] -= 2500 if FiftyOff else 5000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 50
        stats["farmAmount"] += 1

    def onButtonFactoryClick():
        stats["cookies"] -= 15000 if FiftyOff else 30000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 300
        stats["fAmount"] += 1

    def onButtonBankClick():
        stats["cookies"] -= 125000 if FiftyOff else 250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 3000
        stats["bAmount"] += 1

    def onButtonAliensClick():
        stats["cookies"] -= 625000 if FiftyOff else 1250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 5000
        stats["aAmount"] += 1

    def onButtonTeslaClick():
        stats["cookies"] -= 3125000 if FiftyOff else 6250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 30000
        stats["tAmount"] += 1

    def onButtonRocketClick():
        stats["cookies"] -= 15500000 if FiftyOff else 31000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 150000
        stats["rAmount"] += 1

    def onButtonElonClick():
        global nextLvlScreen
        nextLvlScreen = True
        stats["cookies"] -= 5000000000 if FiftyOff else 10000000000
        stats["eAmount"] += 1
        Channel(1).stop()
        playElonMa()

        #* lvl2
    def onButtonBatteryClick():
        stats["cookies"] -= 75 if FiftyOff else 150
        stats["fingers"] += 3
        stats["batteryAmount"] += 1

    def onButtonRoboArmClick():
        stats["cookies"] -= 750 if FiftyOff else 1500
        pygame.time.set_timer(timer_event, 1000)
        stats["event"] = 1
        stats["Ck_s"] += 15
        stats["roboArmAmount"] += 1

    def onButtonBotClick():
        stats["cookies"] -= 3000 if FiftyOff else 6000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 60
        stats["botAmount"] += 1

    def onButtonAiClick():
        stats["cookies"] -= 7500 if FiftyOff else 15000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 150
        stats["aiAmount"] += 1

    def onButtonSolarClick():
        stats["cookies"] -= 45000 if FiftyOff else 90000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 900
        stats["solarAmount"] += 1

    def onButtonGigaClick():
        stats["cookies"] -= 375000 if FiftyOff else 750000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 9000
        stats["gigaAmount"] += 1

    def onButtonCiberClick():
        stats["cookies"] -= 46500000 if FiftyOff else 93000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 180000
        stats["ciberAmount"] += 1

    def onButtonTwitterClick():
        stats["cookies"] -= 1500000000 if FiftyOff else 3000000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 15000000
        stats["twitterAmount"] += 1

    def onButtonGamingClick():
        global levelTreeScreen
        levelTreeScreen = True
        stats["cookies"] -= 450000000000 if FiftyOff else 900000000000
        stats["gaming"] += 1
        stats["eAmount"] += 1
        playGamingSound()
        Channel(2).stop()

    def onButtonMysteryClick():
        # titleScreen.drawMysteryScreen()
        # stats["mysteryAmount"] += 1
        pass

        #* lvl3
    def onButtonMouseClick():
        stats["cookies"] -= 450 if FiftyOff else 900
        stats["fingers"] += 8

    def onButtonControllerClick():
        stats["cookies"] -= 5250 if FiftyOff else 10500
        stats["Ck_s"] += 105
        pygame.time.set_timer(timer_event, 1000)
        stats["controllerAmount"] += 1

    def onButtonPlaystationClick():
        stats["cookies"] -= 26250 if FiftyOff else 52500
        stats["Ck_s"] += 525
        pygame.time.set_timer(timer_event, 1000)
        stats["playstationAmount"] += 1
    
    def onButtonChairClick():
        stats["cookies"] -= 52500 if FiftyOff else 105000
        stats["Ck_s"] += 2625
        pygame.time.set_timer(timer_event, 1000)
        stats["chairAmount"] += 1

    def onButtonPcClick():
        stats["cookies"] -= 656250 if FiftyOff else 1312500
        stats["Ck_s"] += 13125
        pygame.time.set_timer(timer_event, 1000)
        stats["pcAmount"] += 1

    def onButtonArcadeClick():
        stats["cookies"] -= 3281250 if FiftyOff else 6562500
        stats["Ck_s"] += 65625
        pygame.time.set_timer(timer_event, 1000)
        stats["arcadeAmount"] += 1

    def onButtonGamerGirlClick():
        stats["cookies"] -= 16406250 if FiftyOff else 32812500
        stats["Ck_s"] += 328125
        pygame.time.set_timer(timer_event, 1000)
        stats["gamerGirlAmount"] += 1

    def onButtonGamingStoreClick():
        stats["cookies"] -= 82031250 if FiftyOff else 164062500
        stats["Ck_s"] += 1640625
        pygame.time.set_timer(timer_event, 1000)
        stats["gamingStoreAmount"] += 1

    def onButtonNvideaClick():
        stats["cookies"] -= 4551562500 if FiftyOff else 9103125000
        stats["Ck_s"] += 91031250
        pygame.time.set_timer(timer_event, 1000)
        stats["nvideaAmount"] += 1

    def onButtonBrainClick():
        pass


    def setOpacity(cookie_value, rebirth_value, opacityValue):
        required_cookies = cookie_value / 2 if FiftyOff else cookie_value
        return 255 if stats["cookies"] >= required_cookies and stats["rebirthAmount"] >= rebirth_value else opacityValue
    
    def allowBuy(cookie_value):
        return cookie_value / 2 if FiftyOff else cookie_value

    def onInfoClick():
        infoButton.num_clickedInfo += 1

    def onShopClick():
        shopButton.num_clickedShop += 1

    def onMuteClick():
        pauseMusic.num_clickedMute += 1

    def checkIfMaxAmount(whatAmount, statsAmount, x, y):
        if stats[statsAmount] == 200 and stats["nextLvL"] == 0:
            whatAmount.drawText("max", x, y)
        elif stats[statsAmount] == 500 and stats["nextLvL"] == 1:
            whatAmount.drawText("max", x, y)
        elif stats[statsAmount] == 1500 and stats["nextLvL"] >= 2:
            whatAmount.drawText("max", x, y)
        else:
            whatAmount.drawText(": %d" % stats[statsAmount], x, y)

    def checkIfAllMaxLvlOne():
        if all(value == 200 for value in [stats["gAmount"], stats["oAmount"], stats["farmAmount"], stats["fAmount"], stats["bAmount"], stats["aAmount"], stats["tAmount"], stats["rAmount"]]):
            return True
        else:
            return False
        
    def checkIfAllMaxLvlTwo():
        if all(value == 500 for value in [stats["batteryAmount"], stats["roboArmAmount"], stats["botAmount"], stats["aiAmount"], stats["solarAmount"], stats["gigaAmount"], stats["ciberAmount"]]):
            return True
        else:
            return False
    
    def checkIfAllMaxLvlThree():
        if all(value == 1500 for value in [stats["controllerAmount"], stats["playstationAmount"], stats["chairAmount"], stats["pcAmount"], stats["arcadeAmount"], stats["gamerGirlAmount"], stats["gamingStoreAmount"], stats["nvideaAmount"]]):
            return True
        else:
            return False


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("statsDic.json", "w") as file:
                    json.dump(stats, file)
                running = False

            if event.type == timer_event:
                if not TwoXMoney2min or not TwoXMoney5min:
                    stats["cookies"] += stats["Ck_s"]
                if TwoXMoney2min:
                    stats["cookies"] += stats["Ck_s"] * 1
                if TwoXMoney5min:
                    stats["cookies"] += stats["Ck_s"] * 1
                if stats["rebirthAmount"] > 0:
                    multiplier = stats["rebirthAmount"] / 10
                    stats["Ck_s"] += stats["Ck_s"] * multiplier

                if stats["nextLvL"] == 0 and stats["gAmount"] > 0:
                    cookie.clickCookie(clickSoundCookie, "on", 0.2)
                if stats["nextLvL"] == 1 and stats["roboArmAmount"] > 0:
                    cookie.clickCookie(clickSoundBattery, "on", 0.2)
                if stats["nextLvL"] >= 2 and stats["controllerAmount"] > 0:
                    cookie.clickCookie(clickSoundPig, "on", 0.5)

            if event.type == event2xMoney2min:
                TwoXMoney2min = False

            if event.type == event2xMoney5min:
                TwoXMoney5min = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    started = True
                    if stats["nextLvL"] == 0:
                        music()
                    if stats["nextLvL"] == 1:
                        musicLvl2()
                    if stats["nextLvL"] >= 2:
                        musicLvl3()

                    if stats["event"] == 1:
                        pygame.time.set_timer(timer_event, 1000)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                    music()
                    wood()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)
                    saved_playtime = stats.get("playtime", 0)
                    start_ticks = pygame.time.get_ticks() - saved_playtime

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and stats["eAmount"] != 0:
                    # nextLvlScreen = False
                    # levelTreeScreen = False
                    savedPlaytime = stats["playtime"]
                    reset()
                    stats["playtime"] += savedPlaytime
                    stats["eAmount"] += 2
                    stats["gaming"] += 2
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                    if nextLvlScreen and stats["eAmount"]  >= 2:
                        nextLvlScreen = False
                        stats["nextLvL"] += 1
                        musicLvl2()
                        stone()
                    if levelTreeScreen and stats["gaming"] >= 2:
                        levelTreeScreen = False
                        stats["nextLvL"] += 2
                        musicLvl3()
                        lava()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if stats["nextLvL"] == 0:
                        nextLvlScreen = False
                        levelTreeScreen = False
                    # else:
                    #     stats["mysteryAmount"] -= 1
                    stats["cookies"] += 1
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)

            if event.type == pygame.MOUSEMOTION:
                pygame.time.set_timer(eventUserInactive, 300000)

            if event.type == eventUserInactive:
                quit()
                                                    
            if event.type == pygame.MOUSEBUTTONUP:
                if cookie.is_mouse_on_coockie():
                    ckClicked = True
                if not clickedBlocked and cookie.is_mouse_on_coockie():
                    stats["cookies"] += stats["fingers"]
                    if stats["nextLvL"] == 0:
                        cookie.clickCookie(clickSoundCookie, "on", 0.2)
                    if stats["nextLvL"] == 1:
                        cookie.clickCookie(clickSoundBattery, "on", 0.2)
                    if stats["nextLvL"] >= 2:
                        cookie.clickCookie(clickSoundPig, "on", 0.5)
                    
                    clickedBlocked = True
                    pygame.time.set_timer(eventBlockClick, 100)

            if event.type == pygame.MOUSEBUTTONDOWN:
                ckClicked = False
                if not clickedBlocked:
                        #* abilities
                    if shop_window_open:
                        if stats["cookies"] >= 10000000000:
                            abiliti2xMoney_btn.buttonClick(onAbility2xMoneyClick)
                        if stats["rebirthAmount"] >= 1:
                            abiliti5min2xMoney_btn.buttonClick(onAbiliti5min2xMoneyClick)
                        if stats["cookies"] >= 1:
                            abiliti50off_btn.buttonClick(onAbility50OffClick)
                        if checkIfAllMaxLvlThree():
                            abilitiRebirth_btn.buttonClick(onRebirthClick)

                        #* lvl1
                    if not shop_window_open:
                        if stats["nextLvL"] == 0:
                            if stats["cookies"] >= allowBuy(50) and stats["fingers"] <= 199:
                                f_btn.buttonClick(onButtonFingerClick, 1)
                            if stats["cookies"] >= allowBuy(500) and stats["gAmount"] <= 199:
                                g_btn.buttonClick(onButtonGrannyClick, 1)
                            if stats["cookies"] >= allowBuy(2000) and stats["oAmount"] <= 199:
                                o_btn.buttonClick(onButtonOvenClick, 1)
                            if stats["cookies"] >= allowBuy(5000) and stats["farmAmount"] <= 199:
                                farm_btn.buttonClick(onButtonFarmClick, 1)
                            if stats["cookies"] >= allowBuy(30000) and stats["fAmount"] <= 199:
                                fa_btn.buttonClick(onButtonFactoryClick, 1)
                            if stats["cookies"] >= allowBuy(250000) and stats["bAmount"] <= 199:
                                b_btn.buttonClick(onButtonBankClick, 1)
                            if stats["cookies"] >= allowBuy(1250000) and stats["aAmount"] <= 199:
                                a_btn.buttonClick(onButtonAliensClick, 1)
                            if stats["cookies"] >= allowBuy(6250000) and stats["tAmount"] <= 199:
                                t_btn.buttonClick(onButtonTeslaClick, 1)
                            if stats["cookies"] >= allowBuy(31000000) and stats["rAmount"] <= 199:
                                r_btn.buttonClick(onButtonRocketClick, 1)
                            if stats["cookies"] >= allowBuy(10000000000) and checkIfAllMaxLvlOne():
                                e_btn.buttonClick(onButtonElonClick, 1)

                            #* lvl2
                        if stats["nextLvL"] == 1:
                            if stats["cookies"] >= allowBuy(150) and stats["batteryAmount"] <= 499:
                                battery_btn.buttonClick(onButtonBatteryClick, 1)
                            if stats["cookies"] >= allowBuy(1500) and stats["roboArmAmount"] <= 499:
                                roboArm_btn.buttonClick(onButtonRoboArmClick, 1)
                            if stats["cookies"] >= allowBuy(6000) and stats["botAmount"] <= 499:
                                bot_btn.buttonClick(onButtonBotClick, 1)
                            if stats["cookies"] >= allowBuy(15000) and stats["aiAmount"] <= 499:
                                ai_btn.buttonClick(onButtonAiClick, 1)
                            if stats["cookies"] >= allowBuy(90000) and stats["solarAmount"] <= 499:
                                solar_btn.buttonClick(onButtonSolarClick, 1)
                            if stats["cookies"] >= allowBuy(750000) and stats["gigaAmount"] <= 499:
                                giga_btn.buttonClick(onButtonGigaClick, 1)
                            if stats["cookies"] >= allowBuy(93000000) and stats["ciberAmount"] <= 499:
                                ciber_btn.buttonClick(onButtonCiberClick, 1)
                            if stats["cookies"] >= allowBuy(3000000000):
                                twitter_btn.buttonClick(onButtonTwitterClick, 1)  
                            if stats["cookies"] >= allowBuy(900000000000) and checkIfAllMaxLvlTwo():
                                gaming_btn.buttonClick(onButtonGamingClick, 1)

                            #* lvl3
                        if stats["nextLvL"] >= 2:
                            if stats["cookies"] >= allowBuy(900) and stats["mouseAmount"] <= 1499:
                                mouse_btn.buttonClick(onButtonMouseClick, 1)
                            if stats["cookies"] >= allowBuy(10500) and stats["controllerAmount"] <= 1499:
                                controller_btn.buttonClick(onButtonControllerClick, 1)
                            if stats["cookies"] >= allowBuy(52500) and stats["playstationAmount"] <= 1499:
                                playstation_btn.buttonClick(onButtonPlaystationClick, 1)
                            if stats["cookies"] >= allowBuy(105000) and stats["chairAmount"] <= 1499:
                                chair_btn.buttonClick(onButtonChairClick, 1)
                            if stats["cookies"] >= allowBuy(1312500) and stats["pcAmount"] <= 1499:
                                pc_btn.buttonClick(onButtonPcClick, 1)
                            if stats["cookies"] >= allowBuy(6562500) and stats["arcadeAmount"] <= 1499:
                                arcade_btn.buttonClick(onButtonArcadeClick, 1)
                            if stats["cookies"] >= allowBuy(32812500) and stats["gamerGirlAmount"] <= 1499:
                                gamerGirl_btn.buttonClick(onButtonGamerGirlClick, 1)
                            if stats["cookies"] >= allowBuy(164062500) and stats["gamingStoreAmount"] <= 1499:
                                gamingStore_btn.buttonClick(onButtonGamingStoreClick, 1)
                            if stats["cookies"] >= allowBuy(9103125000) and stats["nvideaAmount"] <= 1499:
                                nvidia_btn.buttonClick(onButtonNvideaClick, 1)
                            if stats["cookies"] >= allowBuy(4551562500) and checkIfAllMaxLvlThree():
                                brain_btn.buttonClick(onButtonBrainClick, 1)

                        # if checkIfAllMaxLvlTwo():
                        #     mystery_btn.buttonClick(onButtonMysteryClick)
                        #     nextLvlScreen = True

                    infoButton.buttonClick(onInfoClick, 0)
                    pauseMusic.buttonClick(onMuteClick, 0)
                    shopButton.buttonClick(onShopClick, 0)

            if event.type == eventBlockClick:
                clickedBlocked = False
                pygame.time.set_timer(eventBlockClick, 0)

        if not started:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
            titleScreen.drawScreen()

        if started:
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            window.blit(window, (0, 0))
            # stats["playtime"] += playtime.ticks / 3
            gui.drawBackG()
            # Update playtime
            elapsed_ticks = pygame.time.get_ticks() - start_ticks
            stats["playtime"] = elapsed_ticks
            playtime.run(stats["playtime"])

            if stats["nextLvL"] == 0:
                gui.drawFrame((815, 57), (442, 0), (850, 10))
                score.drawScore(stats["cookies"], (60, 6), GREEN)
                if not ckClicked:
                    cookie.drawCookie((36, 190))
                else:
                    cookie.drawBigCookies()

            if stats["nextLvL"] == 1:
                gui.drawFrame((842, 100), (442, 0), (850, 10))
                score.drawScore(stats["cookies"], (50, 4), LIGHTBLUE)
                if not ckClicked:
                    cookie.drawCookie((40, 160))
                else:
                    cookie.drawBigCookies()

            if stats["nextLvL"] >= 2:
                gui.drawFrame((842, 100), (442, 8), (830, 0))
                score.drawScore(stats["cookies"], (60, 10), PINK)
                if not ckClicked:
                    cookie.drawCookie((45, 190))
                else:
                    cookie.drawBigCookies()

            #* abilities
            opacity2xMoney = setOpacity(10000000000, 0, 175)
            opacity5min2xMoney = setOpacity(0, 1, 175)
            opacityRebirth = setOpacity(0, int(checkIfAllMaxLvlThree()), 175)
            opacity50Off = setOpacity(0, 2, 175)

            #* lvl1
            opacityF = setOpacity(50, 0, 175)
            opacityG = setOpacity(500, 0, 175)
            opacityO = setOpacity(2000, 0, 175)
            opacityFarm = setOpacity(5000, 0, 175)
            opacityFa = setOpacity(30000, 0, 175)
            opacityB = setOpacity(250000, 0, 175)
            opacityA = setOpacity(1250000, 0, 175)
            opacityT = setOpacity(6200000, 0, 175)
            opacityR = setOpacity(31000000, 0, 175)
            opacityE = 175
            if checkIfAllMaxLvlOne() and stats["cookies"] >= 10000000000:
                opacityE = 255

            #* lvl2
            opacityBattery = setOpacity(150, 0, 175)
            opacityRoboArm = setOpacity(1500, 0, 175)
            opacityBot = setOpacity(6000, 0, 175)
            opacityAi = setOpacity(15000, 0, 175)
            opacitySolar = setOpacity(90000, 0, 175)
            opacityGiga = setOpacity(750000, 0, 175)
            opacityCiber = setOpacity(31000000, 0, 175)
            opacityTwitter = setOpacity(3000000000, 0, 175)
            opacityGaming = 175
            if checkIfAllMaxLvlTwo() and stats["cookies"] >= 900000000000:
                opacityGaming = 255

            #* lvl3
            opacityMouse = setOpacity(900, 0, 190)
            opacityController = setOpacity(10500, 0, 190)
            opacityPlaystation = setOpacity(52500, 0, 190)
            opacityChair = setOpacity(105000, 0, 190)
            opacityPc = setOpacity(1312500, 0, 190)
            opacityArcade = setOpacity(6562500, 0, 190)
            opacityGamerGirl = setOpacity(32812500, 0, 190)
            opacityGamingStore = setOpacity(164062500, 0, 190)
            opacityNvidea = setOpacity(9103125000, 0, 190)
            opacityBrain = 175
            if checkIfAllMaxLvlThree():
                opacityBrain = 255
            
            if stats["nextLvL"] == 0:
                granny.drawImage(430, 117)
                checkIfMaxAmount(grannyAmount, "gAmount", 520, 140)
                # grannyAmount.drawText(": %d" % stats["gAmount"], 520, 140)
                oven.drawImage(600, 117)
                checkIfMaxAmount(ovenAmount, "oAmount", 680, 140)
                # ovenAmount.drawText(": %d" % stats["oAmount"], 680, 140)
                farm.drawImage(425, 245)
                checkIfMaxAmount(farmAmount, "farmAmount", 520, 270)
                # farmAmount.drawText(": %d" % stats["farmAmount"], 520, 270)
                factory.drawImage(600, 245)
                checkIfMaxAmount(factoryAmount, "fAmount", 680, 270)
                # factoryAmount.drawText(": %d" % stats["fAmount"], 680, 270)
                bank.drawImage(435, 385)
                checkIfMaxAmount(bankAmount, "bAmount", 520, 400)
                # bankAmount.drawText(": %d" % stats["bAmount"], 520, 400)
                alien.drawImage(600, 375)
                checkIfMaxAmount(aliensAmount, "aAmount", 680, 400)
                # aliensAmount.drawText(": %d" % stats["aAmount"], 680, 400)
                tesla.drawImage(430, 515)
                checkIfMaxAmount(teslaAmount, "tAmount", 520, 530)
                # teslaAmount.drawText(": %d" % stats["tAmount"], 520, 530)
                rocket.drawImage(600, 515)
                checkIfMaxAmount(rocketAmount, "rAmount", 680, 530)
                # rocketAmount.drawText(": %d" % stats["rAmount"], 680, 530)

            if stats["nextLvL"] == 1:
                battey.drawImage(440, 127)
                checkIfMaxAmount(batteryAmount, "batteryAmount", 520, 140)

                roboArm.drawImage(600, 117)
                checkIfMaxAmount(roboArmAmount, "roboArmAmount", 680, 140)

                bot.drawImage(425, 250)
                checkIfMaxAmount(botAmount, "botAmount", 520, 270)

                ai.drawImage(600, 245)
                checkIfMaxAmount(aiAmount, "aiAmount", 680, 270)

                solar.drawImage(435, 385)
                checkIfMaxAmount(solarAmount, "solarAmount", 520, 400)

                giga.drawImage(600, 375)
                checkIfMaxAmount(gigaAmount, "gigaAmount", 680, 400)

                ciber.drawImage(430, 505)
                checkIfMaxAmount(ciberAmount, "ciberAmount", 520, 530)

                twitter.drawImage(600, 520)
                checkIfMaxAmount(twitterAmount, "twitterAmount", 680, 530)

            if stats["nextLvL"] >= 2:
                controller.drawImage(440, 118)
                checkIfMaxAmount(controllerAmount, "controllerAmount", 520, 140)

                playstation.drawImage(600, 127)
                checkIfMaxAmount(playstationAmount, "playstationAmount", 680, 140)

                chair.drawImage(435, 250)
                checkIfMaxAmount(chairAmount, "chairAmount", 520, 270)

                pc.drawImage(590, 245)
                checkIfMaxAmount(pcAmount, "pcAmount", 680, 270)

                arcade.drawImage(435, 385)
                checkIfMaxAmount(arcadeAmount, "arcadeAmount", 520, 400)

                gamerGirl.drawImage(600, 385)
                checkIfMaxAmount(gamerGirlAmount, "gamerGirlAmount", 680, 400)

                gamingStore.drawImage(435, 520)
                checkIfMaxAmount(gamingStoreAmount, "gamingStoreAmount", 520, 530)

                nvidia.drawImage(600, 510)
                checkIfMaxAmount(nvideaAmount, "nvideaAmount", 680, 530)

            if infoButton.num_clickedInfo % 2 and stats["nextLvL"] == 0:
                window.blit(infoFrame, (270, 0))
            if infoButton.num_clickedInfo % 2 and stats["nextLvL"] == 1:
                window.blit(infoFrame2, (145, 43))
            if infoButton.num_clickedInfo % 2 and stats["nextLvL"] >= 2:
                window.blit(infoFrame3, (120, 70))

            channel_id = 1 if stats["nextLvL"] == 0 else 2 if stats["nextLvL"] == 1 else 3
            if pauseMusic.num_clickedMute % 2:
                Channel(channel_id).pause()
            else:
                Channel(channel_id).unpause()


            abiliti2xMoney_btn = Button(window, r"assets\buttons\abilities\bba1.png", opacity2xMoney, 125, 70, 140, 80, pygame.Rect(945, 440, 140, 70))
            abiliti5min2xMoney_btn = Button(window, r"assets\buttons\abilities\bba3.png", opacity5min2xMoney, 125, 70, 140, 80, pygame.Rect(695, 440, 140, 70))
            abiliti50off_btn = Button(window, r"assets\buttons\abilities\bba2.png", opacity50Off, 125, 70, 140, 80, pygame.Rect(105, 440, 140, 70))
            abilitiRebirth_btn = Button(window, r"assets\buttons\abilities\bba4.png", opacityRebirth, 125, 70, 140, 80, pygame.Rect(380, 440, 140, 70))

            f_btn = Button(window, r"assets/buttons/Finger-buttons.png", opacityF, 125, 70, 140, 80, pygame.Rect(870, 145, 140, 70))
            g_btn = Button(window, r"assets/buttons/Granny-buttons.png", opacityG, 125, 70, 140, 80, pygame.Rect(1005, 145, 140, 70))
            o_btn = Button(window, r"assets/buttons/Oven-buttons.png", opacityO, 125, 70, 140, 80, pygame.Rect(870, 230, 140, 70))
            farm_btn = Button(window, r"assets/buttons/Farm-buttons.png", opacityFarm, 125, 70, 140, 80, pygame.Rect(1005, 230, 140, 70))
            fa_btn = Button(window, r"assets/buttons/Factory-buttons.png", opacityFa, 125, 70, 140, 80, pygame.Rect(870, 315, 140, 70))
            b_btn = Button(window, r"assets/buttons/Bank-buttons.png", opacityB, 125, 70, 140, 80, pygame.Rect(1005, 315, 140, 70))
            a_btn = Button(window, r"assets/buttons/Aliens-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(870, 400, 140, 70))
            t_btn = Button(window, r"assets/buttons/Tesla-buttons.png", opacityT, 125, 70, 140, 80, pygame.Rect(1005, 400, 140, 70))
            r_btn = Button(window, r"assets/buttons/Rocket-buttons.png", opacityR, 125, 70, 140, 80, pygame.Rect(870, 485, 140, 70))
            e_btn = Button(window, r"assets/buttons/Elon-buttons.png", opacityE, 125, 70, 140, 80, pygame.Rect(1005, 485, 140, 70))

            battery_btn = Button(window, r"assets\buttons\lvl2\buttonsBattery.png", opacityBattery, 125, 70, 140, 80, pygame.Rect(867, 165, 140, 70))
            roboArm_btn = Button(window, r"assets\buttons\lvl2\buttonsRoboArm.png", opacityRoboArm, 125, 70, 140, 80, pygame.Rect(1002, 165, 140, 70))
            bot_btn = Button(window, r"assets\buttons\lvl2\buttonsBot.png", opacityBot, 125, 70, 140, 80, pygame.Rect(867, 250, 140, 70))
            ai_btn = Button(window, r"assets\buttons\lvl2\buttonsAi.png", opacityAi, 125, 70, 140, 80, pygame.Rect(1002, 250, 140, 70))
            solar_btn = Button(window, r"assets\buttons\lvl2\buttonsSolar.png", opacitySolar, 125, 70, 140, 80, pygame.Rect(867, 335, 140, 70))
            giga_btn = Button(window, r"assets\buttons\lvl2\buttonsGigafactory.png", opacityGiga, 125, 70, 140, 80, pygame.Rect(1002, 335, 140, 70))
            ciber_btn = Button(window, r"assets\buttons\lvl2\buttonsCiber.png", opacityCiber, 125, 70, 140, 80, pygame.Rect(867, 420, 140, 70))
            twitter_btn = Button(window, r"assets\buttons\lvl2\buttonsTwitter.png", opacityTwitter, 125, 70, 140, 80, pygame.Rect(1002, 420, 140, 70))
            gaming_btn = Button(window, r"assets\buttons\lvl2\buttonsGaming.png", opacityGaming, 145, 70, 160, 80, pygame.Rect(935, 505, 140, 70))
            # mystery_btn = Button(window, r"assets\buttons\lvl2\buttonsMystery.png", opacityGaming, 125*2.2, 100, 140*2.1, 110, pygame.Rect(935, 505, 140, 70))

            mouse_btn = Button(window, r"assets\buttons\lvl3\buttonMouse.png", opacityMouse, 125, 70, 140, 80, pygame.Rect(870, 145, 140, 70))
            controller_btn = Button(window, r"assets\buttons\lvl3\buttonController.png", opacityController, 125, 70, 140, 80, pygame.Rect(1005, 145, 140, 70))
            playstation_btn = Button(window, r"assets\buttons\lvl3\buttonPlaystation.png", opacityPlaystation, 125, 70, 140, 80, pygame.Rect(870, 230, 140, 70))
            chair_btn = Button(window, r"assets\buttons\lvl3\buttonChair.png", opacityChair, 125, 70, 140, 80, pygame.Rect(1005, 230, 140, 70))
            pc_btn = Button(window, r"assets\buttons\lvl3\buttonPc.png", opacityPc, 125, 70, 140, 80, pygame.Rect(870, 315, 140, 70))
            arcade_btn = Button(window, r"assets\buttons\lvl3\buttonArcade.png", opacityArcade, 125, 70, 140, 80, pygame.Rect(1005, 315, 140, 70))
            gamerGirl_btn = Button(window, r"assets\buttons\lvl3\buttonGamerGirl.png", opacityGamerGirl, 125, 70, 140, 80, pygame.Rect(870, 400, 140, 70))
            gamingStore_btn = Button(window, r"assets\buttons\lvl3\buttonGStore.png", opacityGamingStore, 125, 70, 140, 80, pygame.Rect(1005, 400, 140, 70))
            nvidia_btn = Button(window, r"assets\buttons\lvl3\buttonNvidia.png", opacityNvidea, 125, 70, 140, 80, pygame.Rect(870, 485, 140, 70))
            brain_btn = Button(window, r"assets\buttons\lvl3\buttonBrainrot.png", opacityBrain, 125, 70, 140, 80, pygame.Rect(1005, 485, 140, 70))

            if shopButton.num_clickedShop % 2:
                shop_window_open = True
                shopScreen.drawShopScreen()
                abiliti2xMoney_btn.drawButton()
                abiliti5min2xMoney_btn.drawButton()
                abiliti50off_btn.drawButton()
                abilitiRebirth_btn.drawButton()

            if shopButton.num_clickedShop % 2 != 1:
                shop_window_open = False

            if stats["nextLvL"] == 0 and shopButton.num_clickedShop % 2 != 1:
                f_btn.drawButton()
                g_btn.drawButton()
                o_btn.drawButton()
                farm_btn.drawButton()
                fa_btn.drawButton()
                b_btn.drawButton()
                a_btn.drawButton()
                t_btn.drawButton()
                r_btn.drawButton()
                e_btn.drawButton()

            if stats["nextLvL"] == 1 and shopButton.num_clickedShop % 2 != 1:
                battery_btn.drawButton()
                roboArm_btn.drawButton()
                bot_btn.drawButton()
                ai_btn.drawButton()
                solar_btn.drawButton()
                giga_btn.drawButton()
                ciber_btn.drawButton()
                twitter_btn.drawButton()
                gaming_btn.drawButton()
                # mystery_btn.drawButton()

            if stats["nextLvL"] >= 2 and shopButton.num_clickedShop % 2 != 1:
                mouse_btn.drawButton()
                controller_btn.drawButton()
                playstation_btn.drawButton()
                chair_btn.drawButton()
                pc_btn.drawButton()
                arcade_btn.drawButton()
                gamerGirl_btn.drawButton()
                gamingStore_btn.drawButton()
                nvidia_btn.drawButton()
                brain_btn.drawButton()

            infoButton.drawButton()
            shopButton.drawButton()
            pauseMusic.drawButton()

            if nextLvlScreen and stats["eAmount"] == 1:
                titleScreen.drawNextLvlScreen()
                cookie.clickCookie(clickSoundCookie, "off", 0)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

            if levelTreeScreen and stats["gamingAmount"] >= 2:
                titleScreen.drawLvLThreeScreen()
                cookie.clickCookie(clickSoundBattery, "off", 0)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                
        if TwoXMoney2min and shopButton.num_clickedShop % 2 != 1:
            abiliti2xMoneyIcon.drawImage(5, 20)

        if TwoXMoney5min and shopButton.num_clickedShop % 2 != 1:
            abiliti5min2xMoneyIcon.drawImage(5, 90)

        if FiftyOff and shopButton.num_clickedShop % 2 != 1:
            abiliti50offIcon.drawImage(5, 160)
            #*left side
            redLine.drawImage(915, 140)
            redLine.drawImage(915, 225)
            redLine.drawImage(915, 310)
            redLine.drawImage(915, 395)
            redLine.drawImage(915, 480)
            #*right side
            redLine.drawImage(1050, 140)
            redLine.drawImage(1050, 225)
            redLine.drawImage(1050, 310)
            redLine.drawImage(1050, 395)
            redLine.drawImage(1050, 480)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
