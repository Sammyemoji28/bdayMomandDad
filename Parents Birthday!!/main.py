
import pgzrun

HEIGHT = 800
WIDTH = 1000

pic1 = Actor("momdadimg1")
pic1.pos = (230,175)

pic2 = Actor("momdadimg2")
pic2.pos = (456,234)

pic3 = Actor("momdadimg3")
pic3.pos = (464,654)

pic4 = Actor("momdadimg4")
pic4.pos = (689,354)

pic5 = Actor("momdadimg5")
pic5.pos = (823,493)

pic6 = Actor("momdadimg6")
pic6.pos = (748,605)

star = Actor("starimg2")
star.pos = (347,359)

star2 = Actor("starimg3")
star2.pos = (678,108)

balloon = Actor("balloons")
balloon.pos = (184,634)

balloon2 = Actor("balloon2")
balloon2.pos = (897,234)


def draw():
    pic1.draw()
    pic2.draw()
    pic3.draw()
    pic4.draw()
    pic5.draw()
    pic6.draw()
    star.draw()
    star2.draw()
    balloon.draw()
    balloon2.draw()
    screen.draw.text("happy birthday mom and dad!" ,fontsize = 40, center = (300,450))

def update():
    pass

pgzrun.go()