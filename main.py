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
    global started, clickedBlocked, TwoXMoney2min, TwoXMoney5min
    running = True
    ckClicked = False
    nextLvlScreen = False
    clickedBlocked = False

    TwoXMoney2min = False
    TwoXMoney5min = False

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
            (320, 530),
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
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        print("wood")

    if stats["nextLvL"] == 1:
        stone()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        print("stone")

    if stats["nextLvL"] >= 2:
        lava()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1150, 570, 30, 30))
        shopButton = Button(window, r"assets\buttons\shopping-cart.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        print("lava")

    if stats["nextLvL"] == 0 or stats["nextLvL"] == 1 or stats["nextLvL"] >= 2:
        shopScreen = Title(window)

    # opacityF = 200 #! remove if not needed
    # opacityG = 200
    # opacityO = 200
    # opacityFarm = 200
    # opacityFa = 200
    # opacityB = 200
    # opacityA = 200
    # opacityT = 200
    # opacityR = 200
    # opacityE = 200

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

    pauseMusic = Button(window, r"assets/images/mute.png", 255, 30, 30, 40, 40, pygame.Rect(10, 600, 30, 30))

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
    nvidea = Image(window, r"assets\upgrades\lvl3\nvidia.png", 80, 80)

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
    
    def playEmonMa():
        emonMa = r"assets\sounds\elonma.mp3"
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(emonMa), loops=0)
        Channel(4).set_volume(0.5)

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
        stats["mysteryAmount"] = 0
        stats["mouse"] = 0
        stats["controller"] = 0
        stats["playstation"] = 0
        stats["chair"] = 0
        stats["pc"] = 0
        stats["arcade"] = 0
        stats["gamerGirl"] = 0
        stats["gamingStore"] = 0
        stats["nvidea"] = 0
        stats["brain"] = 0
        stats["rebirth"] = 0
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
        stats["rebirth"] -= 1
        TwoXMoney5min = True
        pygame.time.set_timer(event2xMoney5min, 300000)

    def onRebirthClick():
        # +10% more cookie production
        stats["rebirth"] += 1

    def onAbility50OffClick():
        stats["rebirth"] -= 2
        # 50% off all upgrades for 30 seconds
    
        #* lvl1
    def onButtonFingerClick():
        stats["cookies"] -= 50
        stats["fingers"] += 1
        # cookie.increaseS = stats["fingers"]

    def onButtonGrannyClick():
        stats["cookies"] -= 500
        pygame.time.set_timer(timer_event, 1000)
        stats["gAmount"] += 1
        stats["Ck_s"] += 5
        stats["event"] = 1

    def onButtonOvenClick():
        stats["cookies"] -= 2000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 20
        stats["oAmount"] += 1

    def onButtonFarmClick():
        stats["cookies"] -= 5000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 50
        stats["farmAmount"] += 1

    def onButtonFactoryClick():
        stats["cookies"] -= 30000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 300
        stats["fAmount"] += 1

    def onButtonBankClick():
        stats["cookies"] -= 250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 3000
        stats["bAmount"] += 1

    def onButtonAliensClick():
        stats["cookies"] -= 1250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 5000
        stats["aAmount"] += 1

    def onButtonTeslaClick():
        stats["cookies"] -= 6250000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 30000
        stats["tAmount"] += 1

    def onButtonRocketClick():
        stats["cookies"] -= 31000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 150000
        stats["rAmount"] += 1

    def onButtonElonClick():
        stats["cookies"] -= 10000000000
        stats["eAmount"] += 1
        playEmonMa()
        Channel(1).stop()

        #* lvl2
    def onButtonBatteryClick():
        stats["cookies"] -= 150
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 3
        stats["batteryAmount"] += 1

    def onButtonRoboArmClick():
        stats["cookies"] -= 1500
        pygame.time.set_timer(timer_event, 1000)
        stats["event"] = 1
        stats["Ck_s"] += 15
        stats["roboArmAmount"] += 1

    def onButtonBotClick():
        stats["cookies"] -= 6000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 60
        stats["botAmount"] += 1

    def onButtonAiClick():
        stats["cookies"] -= 15000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 150
        stats["aiAmount"] += 1

    def onButtonSolarClick():
        stats["cookies"] -= 90000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 900
        stats["solarAmount"] += 1

    def onButtonGigaClick():
        stats["cookies"] -= 750000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 9000
        stats["gigaAmount"] += 1

    def onButtonCiberClick():
        stats["cookies"] -= 31000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 180000
        stats["ciberAmount"] += 1

    def onButtonTwitterClick():
        stats["cookies"] -= 3000000000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 15000000
        stats["twitterAmount"] += 1

    def onButtonMysteryClick():
        # titleScreen.drawMysteryScreen()
        stats["mysteryAmount"] += 1

    def setOpacity(cookie_value, rebirth_value):
        if stats["cookies"] >= cookie_value and stats["rebirth"] >= rebirth_value:
            return 255
        # elif stats["rebirth"] >= rebirth_value:
        #     return 255
        else:
            return 175

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
        if all(value == 1500 for value in [stats["controller"], stats["playstation"], stats["chair"], stats["pc"], stats["arcade"], stats["gamerGirl"], stats["gamingStore"], stats["nvidea"]]):
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
                if stats["rebirth"] > 0:
                    multiplier = stats["rebirth"] / 10
                    stats["Ck_s"] += stats["Ck_s"] * multiplier

                if stats["nextLvL"] != 0 and stats["gAmount"] > 0:
                    cookie.clickCookie(clickSoundBattery, "on", 0.2)
                elif stats["nextLvL"] == 0 and stats["gAmount"] > 0:
                    cookie.clickCookie(clickSoundCookie, "on", 0.2)

            if event.type == event2xMoney2min:
                TwoXMoney2min = False

            if event.type == event2xMoney5min:
                TwoXMoney5min = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stats["nextLvL"] = 2
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
                    nextLvlScreen = False
                    savedPlaytime = stats["playtime"]
                    reset()
                    stats["playtime"] += savedPlaytime
                    stats["nextLvL"] += 1
                    stats["eAmount"] += 1
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                    musicLvl2()
                    stone()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if stats["nextLvL"] == 0:
                        nextLvlScreen = False
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
                    if stats["cookies"] >= 10000000000:
                        abiliti2xMoney_btn.buttonClick(onAbility2xMoneyClick)
                    if stats["rebirth"] >= 1:
                        abiliti5min2xMoney_btn.buttonClick(onAbiliti5min2xMoneyClick)
                    if checkIfAllMaxLvlThree():
                        abilitiRebirth_btn.buttonClick(onRebirthClick)

                        #* lvl1
                    if stats["nextLvL"] == 0:
                        if stats["cookies"] >= 50 and stats["fingers"] <= 199:
                            f_btn.buttonClick(onButtonFingerClick)

                        if stats["cookies"] >= 500 and stats["gAmount"] <= 199:
                            g_btn.buttonClick(onButtonGrannyClick)

                        if stats["cookies"] >= 2000 and stats["oAmount"] <= 199:
                            o_btn.buttonClick(onButtonOvenClick)

                        if stats["cookies"] >= 5000 and stats["farmAmount"] <= 199:
                            farm_btn.buttonClick(onButtonFarmClick)

                        if stats["cookies"] >= 30000 and stats["fAmount"] <= 199:
                            fa_btn.buttonClick(onButtonFactoryClick)

                        if stats["cookies"] >= 250000 and stats["bAmount"] <= 199:
                            b_btn.buttonClick(onButtonBankClick)

                        if stats["cookies"] >= 1250000 and stats["aAmount"] <= 199:
                            a_btn.buttonClick(onButtonAliensClick)

                        if stats["cookies"] >= 6250000 and stats["tAmount"] <= 199:
                            t_btn.buttonClick(onButtonTeslaClick)

                        if stats["cookies"] >= 31000000 and stats["rAmount"] <= 199:
                            r_btn.buttonClick(onButtonRocketClick)
                        
                        if stats["cookies"] >= 10000000000 and checkIfAllMaxLvlOne():
                            e_btn.buttonClick(onButtonElonClick)
                            nextLvlScreen = True
                    else:
                        #* lvl2
                        if stats["cookies"] >= 150 and stats["batteryAmount"] <= 499:
                            battery_btn.buttonClick(onButtonBatteryClick)

                        if stats["cookies"] >= 1500 and stats["roboArmAmount"] <= 499:
                            roboArm_btn.buttonClick(onButtonRoboArmClick)

                        if stats["cookies"] >= 6000 and stats["botAmount"] <= 499:
                            bot_btn.buttonClick(onButtonBotClick)

                        if stats["cookies"] >= 15000 and stats["aiAmount"] <= 499:
                            ai_btn.buttonClick(onButtonAiClick)

                        if stats["cookies"] >= 90000 and stats["solarAmount"] <= 499:
                            solar_btn.buttonClick(onButtonSolarClick)

                        if stats["cookies"] >= 750000 and stats["gigaAmount"] <= 499:
                            giga_btn.buttonClick(onButtonGigaClick)

                        if stats["cookies"] >= 93000000 and stats["ciberAmount"] <= 499:
                            ciber_btn.buttonClick(onButtonCiberClick)

                        if stats["cookies"] >= 3000000000:
                            twitter_btn.buttonClick(onButtonTwitterClick)

                        # if checkIfAllMaxLvlTwo():
                        #     mystery_btn.buttonClick(onButtonMysteryClick)
                        #     nextLvlScreen = True

                    # if stats["cookies"] >= 9:
                    #     nextLvlScreen = True

                    infoButton.buttonClick(onInfoClick)
                    pauseMusic.buttonClick(onMuteClick)
                    shopButton.buttonClick(onShopClick)

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
            opacity2xMoney = setOpacity(10000000000, 0)
            opacity5min2xMoney = setOpacity(0, 1)
            opacityRebirth = setOpacity(0, int(checkIfAllMaxLvlThree()))
            opacity50Off = setOpacity(0, 2)

            #* lvl1
            opacityF = setOpacity(50, 0)
            opacityG = setOpacity(500, 0)
            opacityO = setOpacity(2000, 0)
            opacityFarm = setOpacity(5000, 0)
            opacityFa = setOpacity(30000, 0)
            opacityB = setOpacity(250000, 0)
            opacityA = setOpacity(1250000, 0)
            opacityT = setOpacity(6200000, 0)
            opacityR = setOpacity(31000000, 0)
            if checkIfAllMaxLvlOne():
                opacityE = setOpacity(10000000000, 0)
            else:
                opacityE = 175

            #* lvl2
            opacityBattery = setOpacity(150, 0)
            opacityRoboArm = setOpacity(1500, 0)
            opacityBot = setOpacity(6000, 0)
            opacityAi = setOpacity(15000, 0)
            opacitySolar = setOpacity(90000, 0)
            opacityGiga = setOpacity(750000, 0)
            opacityCiber = setOpacity(31000000, 0)
            opacityTwitter = setOpacity(3000000000, 0)
            opacityMystery = 160
            if checkIfAllMaxLvlTwo():
                opacityMystery = 255
            
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
                checkIfMaxAmount(controllerAmount, "controller", 520, 140)

                playstation.drawImage(600, 127)
                checkIfMaxAmount(playstationAmount, "playstation", 680, 140)

                chair.drawImage(435, 250)
                checkIfMaxAmount(chairAmount, "chair", 520, 270)

                pc.drawImage(590, 245)
                checkIfMaxAmount(pcAmount, "pc", 680, 270)

                arcade.drawImage(435, 385)
                checkIfMaxAmount(arcadeAmount, "arcade", 520, 400)

                gamerGirl.drawImage(600, 385)
                checkIfMaxAmount(gamerGirlAmount, "gamerGirl", 680, 400)

                gamingStore.drawImage(435, 520)
                checkIfMaxAmount(gamingStoreAmount, "gamingStore", 520, 530)

                nvidea.drawImage(600, 510)
                checkIfMaxAmount(nvideaAmount, "nvidea", 680, 530)

            if infoButton.num_clickedInfo % 2 and stats["nextLvL"] == 0:
                window.blit(infoFrame, (270, 0))
            elif infoButton.num_clickedInfo % 2 and stats["nextLvL"] != 0:
                window.blit(infoFrame2, (145, 43))

            channel_id = 1 if stats["nextLvL"] == 0 else 2 if stats["nextLvL"] == 1 else 3
            if pauseMusic.num_clickedMute % 2:
                Channel(channel_id).pause()
            else:
                Channel(channel_id).unpause()


            abiliti2xMoney_btn = Button(window, r"assets\buttons\bba1.png", opacity2xMoney, 125, 70, 140, 80, pygame.Rect(945, 440, 140, 70))
            abiliti5min2xMoney_btn = Button(window, r"assets\buttons\bba3.png", opacity5min2xMoney, 125, 70, 140, 80, pygame.Rect(695, 440, 140, 70))
            abiliti50off_btn = Button(window, r"assets\buttons\bba2.png", opacity50Off, 125, 70, 140, 80, pygame.Rect(105, 440, 140, 70))
            abilitiRebirth_btn = Button(window, r"assets\buttons\bba4.png", opacityRebirth, 125, 70, 140, 80, pygame.Rect(380, 440, 140, 70))

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
            mystery_btn = Button(window, r"assets\buttons\lvl2\buttonsMystery.png", opacityMystery, 125*2.2, 100, 140*2.1, 110, pygame.Rect(935, 505, 140, 70))

            if shopButton.num_clickedShop % 2:
                shopScreen.drawShopScreen()
                abiliti2xMoney_btn.drawButton()
                abiliti5min2xMoney_btn.drawButton()
                abiliti50off_btn.drawButton()
                abilitiRebirth_btn.drawButton()

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
                mystery_btn.drawButton()

            infoButton.drawButton()
            shopButton.drawButton()
            pauseMusic.drawButton()

            if nextLvlScreen and stats["eAmount"] != 0:
                titleScreen.drawNextLvlScreen()
                cookie.clickCookie(clickSoundCookie, "off", 0)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

            if stats["mysteryAmount"] != 0:
                titleScreen.drawLvLThreeScreen()
                cookie.clickCookie(clickSoundCookie, "off", 0)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
