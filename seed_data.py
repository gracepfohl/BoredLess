from boredless_models import URL_lib, Visit, History



def seed_webs():
    weird1 = URL_lib(feeling="weird", url="http://ninjaflex.com/")
    intuitive1 = URL_lib(feeling="intuitive", url="http://www.puzzles.com/")
    social1 = URL_lib(feeling="social", url="https://www.youtube.com/")
    creative1 = URL_lib(feeling="creative", url="https://www.instagram.com/?hl=en")

    weird2 = URL_lib(feeling="weird", url="http://chihuahuaspin.com/")
    intuitive2 = URL_lib(feeling="intuitive", url="http://www.puzzlesite.nl/index_us.html")
    social2 = URL_lib(feeling="social", url="https://www.facebook.com/")
    creative2 = URL_lib(feeling="creative", url="http://apps.amandaghassaei.com/VortexShedding/")

    weird3 = URL_lib(feeling="weird", url="https://pointerpointer.com/")
    intuitive3 = URL_lib(feeling="intuitive", url="https://www.riddles.com/brain-teasers")
    social3 = URL_lib(feeling="social", url="https://twitter.com/?lang=en")
    creative3 = URL_lib(feeling="creative", url="https://sketch.io/sketchpad/")

    weird1.put()
    weird2.put()
    weird3.put()

    intuitive1.put()
    intuitive2.put()
    intuitive3.put()

    social1.put()
    social2.put()
    social3.put()

    creative1.put()
    creative2.put()
    creative3.put()
