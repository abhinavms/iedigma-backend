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