from django.shortcuts import render, redirect
from PIL import Image

def index_page(request):
    return render(request, "index.html")
            
def about_page(request):
    return render(request, "about.html")

def rules_page(request):
    return render(request, "rules.html")

# Level One
def playwithme_level1(request):
    context = {
        'level' : 1,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/level 1.png',
        'text': 'This is a test.',
    }
    return render(request, "round.html" , context)

def playwithme_level2(request):
    return redirect("../empty/level2")

# Level 2
def empty_level2 (request):
        context = {
        'level' : 2,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/level 2.png',
        'text': 'This is a test.',
        }
        return render(request, "round.html" , context)

def full_level2 (request):
    return redirect("../googleit/lvl3")

# Level 3
def googleit_lvl3 (request):
    context = {
        'level' : 3,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/level 3.png',
        'text': 'This is a test.',
    }
    return render(request, "round.html" , context)

def googleit_mandymoore (request):
    context = {
        'level' : 3,
        'img_flag' : False,
        'txt_flag' : True,
        'image' : 'images/level/level 3.png',
        'text': 'Not exactly ;P',
    }
    return render(request, "round.html" , context)

def googleit_onlyhope (request):
    return redirect("../z2o/onlyhope/level4")

# Level 4
def z2o_onlyhope_level4 (request):
    context = {
        'level' : 4,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/level 4.jpg',
        'text': '10111100100100001001000110011000100011011001111010001011100010101001001110011110100010111001011010010000100100011000110011010011110111111010011010010000100010101101111110010111100111101000100110011010110111111001001010011110100110111001101011011111100010111001011110010110100011001101111110011001100111101000110111010001110111111011011011011111100101111001000010001111100110101101111110000110100100001000101011011111100110111001011010011011100100011000101111011111100111001001000010010001100010011001101010001101100010111101111110010110100010111101111110010010100111101001000110001010100111101001001110010011100001101101001111011111100010111001011110011110100010111000110011011111100010001001011110011110100010111101111110011100100100001001001010001111100010101000101110011010100011011000110011011111100111101000110110011010110111111001100110010000100011011101000111011111101111001001011110011110100100011001100010011010110111111001000010010001100100111000011010010111100100001000111110011010110111111000101110010000110111111101111110011100100100001001000110011000100100001101111110010110100100011101111110001011100101111001101011011111100010101000110110010011110111111000101110010000110111111000111110001101100100001001110010011010100110101001101111011111100010111001000011011111100010111001011110011010110111111001000110011010100001111000101111011111100011011001000010001010100100011001101111010001',
    }
    return render(request, "round.html" , context)

def z2o_congo_level4 (request):
    return redirect("../../draw/the/line/level5")

# Level 5
def draw_the_line_level5 (request):
    context = {
        'level' : 5,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/level 5.png',
        'text': '<!-- Can you see it? -->',
    }
    return render(request, "round.html" , context)

def draw_the_line_800x600 (request):
    return redirect("../../../anagram/lvl6")

# Level 6
def anagram_lvl6(request):
    context = {
        'level' : 6,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/level 6.png',
        'text': '',
    }
    return render(request, "round.html" , context)

def anagram_thetitanicdisaster (request):
    return redirect("../../listen/to/the/sounds")


# Level 7
def listen_to_the_sounds (request):
    context = {
        'level' : 7,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/level 7.png',
        'text': '<!-- https://drive.google.com/open?id=15bNP_I0Jj_8qsVnqlnB4tIspRogrqNiC --!>',
    }
    return render(request, "round.html" , context)

def listen_to_the_ekac (request):
    return redirect("../../../raseac/reputation")    

# Level 8
def raseac_reputation(request):
    context = {
        'level' : 8,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/level 8.png',
        'text': 'Ndj pgt gtpaan p idjvw lpggxdg X jcstgthixbpits ndj bn ugxtcs Sdci gthi nti iwt ydjgctn xh cdi dktg Gteaprt gtejipixdc lxiw rwpxqtudjgrduutt udg iwt ctmi rwpaatcvt',
    }
    return render(request, "round.html" , context)

def raseac_chaibefourcoffee (request):
    return redirect("../../that/was/awesome")    

# Level 9
def that_was_awesome (request):
    context = {
        'level' : 9,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/levl 9.png',
        'text': '',
    }
    return render(request, "round.html" , context)

def that_was_unexpected (request):
    return redirect("../../../welcometo/thepast")

# Level 10
def welcometo_thepast (request):
    context = {
        'level' : 10,
        'img_flag' : False,
        'txt_flag' : True,
        'image' : 'images/level/levl 9.png',
        'text': '☟︎⚐︎⬥︎ 👍︎⚐︎💣︎☜︎ ✡︎⚐︎◆︎ ✌︎☼︎☜︎ 💧︎❄︎✋︎☹︎☹︎ ☟︎☜︎☼︎☜︎✍︎ ✋︎ ❄︎☟︎⚐︎◆︎☝︎☟︎❄︎ ✡︎⚐︎◆︎ ☹︎☜︎☞︎❄︎ ☹︎⚐︎☠︎☝︎ 👌︎☜︎☞︎⚐︎☼︎☜︎📬︎ <br> 💣︎◆︎💧︎❄︎ 💧︎✌︎✡︎📪︎ ✡︎⚐︎◆︎ ✌︎☼︎☜︎ ☼︎☜︎✌︎☹︎☹︎✡︎ 💧︎💣︎✌︎☼︎❄︎📬︎ <br> ❄︎☜︎☹︎☹︎ 💣︎♏︎ ⬥︎☟︎□︎ ✋︎ ✌︎💣︎ ✌︎☠︎👎︎ ✋︎ ⬥︎✋︎☹︎☹︎ ☹︎☜︎❄︎ ✡︎□︎◆︎ ❄︎☟︎❒︎□︎◆︎☝︎♒︎ <br> ✋︎ ☟︎♋︎❖︎♏︎ 💧︎◻︎♋︎♍︎♏︎ ⍓︎□︎◆︎ ♍︎♋︎■︎ ☜︎■︎⧫︎♏︎❒︎📪︎♌︎◆︎⧫︎ ✡︎□︎◆︎ ♍︎♋︎■︎■︎□︎⧫︎ ●︎♏︎♋︎❖︎♏︎📪︎♋︎⬧︎ ❍︎⍓︎ 😐︎♏︎⍓︎⬧︎ ♎︎□︎■︎⧫︎ □︎◻︎♏︎■︎ ●︎□︎♍︎😐︎⬧︎',
    }
    return render(request, "round.html" , context)

def welcometo_keyboard (request):
    return redirect("../../sdrawkcab/lvl11/kfc")

# Level 11
def sdrawkcab_lvl11_kfc (request):
    context = {
        'level' : 11,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/candy.jpg',
        'text': "Hey honey! Do you think KFC's Still open?",
    }
    return render(request, "round.html" , context)

def sdrawkcab_lvl11_marathon (request):
    context = {
        'level' : 11,
        'img_flag' : False,
        'txt_flag' : True,
        'image' : 'images/level/candy.jpg',
        'text': "Try running backwards",
    }
    return render(request, "round.html" , context)

def sdrawkcab_lvl11_nohtaram (request):
    return redirect("../../../take/a/breakn/dance")

# Level 12
def take_a_breakn_dance (request):
    context = {
        'level' : 12,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/levl 12.png',
        'text': "<!-- https://www.youtube.com/watch?v=1iQl46-zIcM -->",
    }
    return render(request, "round.html" , context)

def take_a_breakn_stop (request):
    return redirect("../../../../lvl13/stop/singing")

# Level 13
def lvl13_stop_singing (request):
    context = {
        'level' : 13,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/levl 13.png',
        'text': "<!-- https://drive.google.com/open?id=1AnoqxLzfm99KegzFepinxES6tXKfGLFy -->",
    }
    return render(request, "round.html" , context)

def lvl13_stop_thatwasntthathard (request):
    return redirect("../../../lvl14/now/what")

# Level 14
def lvl14_now_what (request):
    context = {
        'level' : 14,
        'img_flag' : True,
        'txt_flag' : True,
        'image' : 'images/level/levl 14.png',
        'text': "<!-- 3VQ8+R6 -->",
    }
    return render(request, "round.html" , context)

def lvl14_now_newyorkminute (request):
    context = {
        'level' : 14,
        'img_flag' : False,
        'txt_flag' : True,
        'image' : 'images/level/levl 14.png',
        'text': "That's too cliche",
    }
    return render(request, "round.html" , context)

def lvl14_now_mumbaiminute (request):
    return redirect("../../../lvl15/moredots/anddashes")

# Level 15
def lvl15_moredots_anddashes (request):
    context = {
        'level' : 15,
        'img_flag' : True,
        'txt_flag' : False,
        'image' : 'images/level/levl 15.png',
        'text': "That's too cliche",
    }
    return render(request, "round.html" , context)

def lvl15_moredots_8547393808 (request):
    return redirect("../../../success/but/onefinaldetail")

# Sucess
def success_but_onefinaldetail (request):
    context = {
        'level' : "Infinity",
        'img_flag' : False,
        'txt_flag' : True,
        'image' : 'images/level/levl 15.png',
        'text': "Congrats warrior!! <br><br> You have fought against all odds and have reached to the final stage of this long voyage. Are you the first to reach the spot? <br> Find out by texting the number you decoded in the last puzzle in the following manner: <br> “Hello! I am _____________(your nick name). Betty bought a bit of butter. The butter wasn’t bitter. So she sells sea shells on the beach” <br> <br> Thank you for playing. Hope you had a great time cracking as we did making these puzzles!!",
    }
    return render(request, "round.html" , context)