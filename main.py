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
    global started
    running = True
    ckClicked = False
    nextLvlScreen = False

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
        "event": 0,
        "nextLvL": 0,
        "playtime": 0,
    }

    pygame.init()
    window = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Cookie Clicker")
    GREEN = 0, 255, 0
    LIGHTBLUE = 0, 255, 255


    if os.path.exists("statsDic.json"):
        with open("statsDic.json", "r") as file:
            stats = json.load(file)

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
            pygame.image.load(r"assets/images/frame2.png"),
            pygame.image.load(r"assets/images/upgradesFrame.png"),
            (300, 100)
        )
        score = Score(window, pygame.image.load(r"assets/images/cookieCount.png"))

    def stone():
        global cookie, gui, score, titleScreen
        cookie = Cookie(
            window, pygame.image.load(r"assets\images\batery.png"), 270, 310
        )
        gui = GUI(
            window,
            pygame.image.load(r"assets\images\backgoundStone.png"),
            pygame.image.load(r"assets\images\shop2_stone.png"),
            (320, 530),
            pygame.image.load(r"assets\images\shop_stone.png"),
            pygame.image.load(r"assets\images\frameLVL2.png"),
            pygame.image.load(r"assets\images\upgrade_stone.png"),
            (300, 75)
        )
        score = Score(window, pygame.image.load(r"assets/images/batteryFrame.png"))

    if stats["nextLvL"] != 0:
        stone()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1100, 570, 30, 30))
        print("stone")
    else:
        wood()
        titleScreen = Title(window)
        playtime = PlaytimeDisplay(window)
        infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1150, 570, 30, 30))
        print("wood")

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

    clickSoundCookie = r"assets/sounds/cookieS.mp3"
    clickSoundBattery = r"assets/sounds/batteryS.mp3"

    InfoFrameImage = pygame.image.load(r"assets/images/info-Frame.png")
    infoFrame = pygame.transform.scale(InfoFrameImage, (600, 600))

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

    def music():
        backgroundMusic = r"assets/sounds/beat.mp3"
        # mixer.music.load(backgroundMusic)
        # mixer.music.set_volume(0.05)
        # pygame.mixer.music.play(loops=100)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(backgroundMusic), loops=-1)
        Channel(1).set_volume(0.1)
        # mixer.music.play()

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
        stats["event"] = 0
        stats["nextLvL"] = 0
        stats["playtime"] = 0

    def onButtonFingerClick():
        stats["cookies"] -= 50
        stats["fingers"] += 1
        # cookie.increaseS = stats["fingers"]
        stats["fingers"] += 1

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

    def get_opacity(cookie_value):
        if stats["cookies"] >= cookie_value:
            return 255
        else:
            return 175

    def onInfoClick():
        infoButton.num_clickedInfo += 1

    def onMuteClick():
        pauseMusic.num_clickedMute += 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("statsDic.json", "w") as file:
                    json.dump(stats, file)
                running = False

            if event.type == timer_event:
                stats["cookies"] += stats["Ck_s"]
                if stats["nextLvL"] != 0 and stats["gAmount"] > 0:
                    cookie.clickCookie(clickSoundBattery)
                elif stats["nextLvL"] == 0 and stats["gAmount"] > 0:
                    cookie.clickCookie(clickSoundCookie)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    started = True
                    music()

                    if stats["event"] == 1:
                        pygame.time.set_timer(timer_event, 1000)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                    music()
                    wood()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    nextLvlScreen = False
                    savedPlaytime = stats["playtime"]
                    reset()
                    stats["playtime"] += savedPlaytime
                    stats["nextLvL"] += 1
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                    stone()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    nextLvlScreen = False
                    stats["cookies"] += 1
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)

            if event.type == pygame.MOUSEBUTTONUP:
                if cookie.is_mouse_on_coockie():
                    ckClicked = True
                    stats["cookies"] += stats["fingers"]
                    if stats["nextLvL"] != 0:
                        cookie.clickCookie(clickSoundBattery)
                    else:
                        cookie.clickCookie(clickSoundCookie)

            if event.type == pygame.MOUSEBUTTONDOWN:
                ckClicked = False
                if stats["cookies"] >= 50:
                    f_btn.buttonClick(onButtonFingerClick)

                if stats["cookies"] >= 500:
                    g_btn.buttonClick(onButtonGrannyClick)

                if stats["cookies"] >= 2000:
                    o_btn.buttonClick(onButtonOvenClick)

                if stats["cookies"] >= 5000:
                    farm_btn.buttonClick(onButtonFarmClick)

                if stats["cookies"] >= 30000:
                    fa_btn.buttonClick(onButtonFactoryClick)

                if stats["cookies"] >= 250000:
                    b_btn.buttonClick(onButtonBankClick)

                if stats["cookies"] >= 1250000:
                    a_btn.buttonClick(onButtonAliensClick)

                if stats["cookies"] >= 6250000:
                    t_btn.buttonClick(onButtonTeslaClick)

                if stats["cookies"] >= 31000000:
                    r_btn.buttonClick(onButtonRocketClick)

                if stats["cookies"] >= 9:
                    nextLvlScreen = True

                infoButton.buttonClick(onInfoClick)
                pauseMusic.buttonClick(onMuteClick)

        if not started:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
            titleScreen.drawScreen()

        if started:
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            window.blit(window, (0, 0))
            stats["playtime"] += playtime.ticks / 10
            gui.drawBackG()
            playtime.run(stats["playtime"])

            if stats["nextLvL"] > 0:
                gui.drawFrame((843, 100), (442, 10))
                score.drawScore(stats["cookies"], (50, 4))
                if not ckClicked:
                    cookie.drawCookie((40, 160))
                else:
                    cookie.drawBigCookies()
            else:
                gui.drawFrame((815, 60), (442, 0))
                score.drawScore(stats["cookies"], (60, 6))
                if not ckClicked:
                    cookie.drawCookie((36, 190))
                else:
                    cookie.drawBigCookies()

            opacityF = get_opacity(50)
            opacityG = get_opacity(500)
            opacityO = get_opacity(2000)
            opacityFarm = get_opacity(5000)
            opacityFa = get_opacity(30000)
            opacityB = get_opacity(250000)
            opacityA = get_opacity(1250000)
            opacityT = get_opacity(6200000)
            opacityR = get_opacity(31000000)
            opacityE = get_opacity(10000000000)

            opacityBattery = get_opacity(150)
            opacityRoboArm = get_opacity(1500)
            opacityBot = get_opacity(6000)
            opacityAi = get_opacity(15000)
            opacitySolar = get_opacity(90000)
            opacityGiga = get_opacity(750000)
            opacityCiber = get_opacity(31000000)
            opacityTwitter = get_opacity(3000000000)

            if stats["nextLvL"] == 0:
                granny.drawImage(430, 117)
                grannyAmount.drawText(": %d" % stats["gAmount"], 520, 140)

                oven.drawImage(600, 117)
                ovenAmount.drawText(": %d" % stats["oAmount"], 680, 140)

                farm.drawImage(425, 245)
                farmAmount.drawText(": %d" % stats["farmAmount"], 520, 270)

                factory.drawImage(600, 245)
                factoryAmount.drawText(": %d" % stats["fAmount"], 680, 270)

                bank.drawImage(435, 385)
                bankAmount.drawText(": %d" % stats["bAmount"], 520, 400)

                alien.drawImage(600, 375)
                aliensAmount.drawText(": %d" % stats["aAmount"], 680, 400)

                tesla.drawImage(430, 515)
                teslaAmount.drawText(": %d" % stats["tAmount"], 520, 530)

                rocket.drawImage(600, 515)
                rocketAmount.drawText(": %d" % stats["rAmount"], 680, 530)
            else:
                battey.drawImage(440, 127)
                batteryAmount.drawText(": %d" % stats["batteryAmount"], 520, 140)

                roboArm.drawImage(600, 117)
                roboArmAmount.drawText(": %d" % stats["roboArmAmount"], 680, 140)

                bot.drawImage(425, 250)
                botAmount.drawText(": %d" % stats["botAmount"], 520, 270)

                ai.drawImage(600, 245)
                aiAmount.drawText(": %d" % stats["aiAmount"], 680, 270)

                solar.drawImage(435, 385)
                solarAmount.drawText(": %d" % stats["solarAmount"], 520, 400)

                giga.drawImage(600, 375)
                gigaAmount.drawText(": %d" % stats["gigaAmount"], 680, 400)

                ciber.drawImage(430, 505)
                ciberAmount.drawText(": %d" % stats["ciberAmount"], 520, 530)

                twitter.drawImage(600, 520)
                twitterAmount.drawText(": %d" % stats["twitterAmount"], 680, 530)

            if infoButton.num_clickedInfo % 2:
                window.blit(infoFrame, (270, 0))

            if pauseMusic.num_clickedMute % 2:
                Channel(1).pause()
            else:
                Channel(1).unpause()


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

            if stats["nextLvL"] == 0:
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
            else:
                battery_btn.drawButton()
                roboArm_btn.drawButton()
                bot_btn.drawButton()
                ai_btn.drawButton()
                solar_btn.drawButton()
                giga_btn.drawButton()
                ciber_btn.drawButton()
                twitter_btn.drawButton()

            infoButton.drawButton()
            pauseMusic.drawButton()

            if nextLvlScreen and stats["cookies"] >= 10:
                titleScreen.drawNextLvlScreen()
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
