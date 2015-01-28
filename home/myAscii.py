'''
ASCII Art maker
Creates an ascii art image from an arbitrary image
Created on 7 Sep 2009
 
@author: Steven Kay
'''

from PIL import Image
import random
from bisect import bisect

class myAscii():    
    image_path = ''
    
    # greyscale.. the following strings represent
    # 7 tonal ranges, from lighter to darker.
    # for a given pixel tonal level, choose a character
    # at random from that range.
    greyscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
                ]
     
    # using the bisect class to put luminosity values
    # in various ranges.
    # these are the luminosity cut-off points for each
    # of the 7 tonal levels. At the moment, these are 7 bands
    # of even width, but they could be changed to boost
    # contrast or change gamma, for example.
    zonebounds=[36,72,108,144,180,216,252]
    
    #
    size = 100,100
     
    def convert(self): 
        # open image and resize
        # experiment with aspect ratios according to font
        im = Image.open(self.image_path,'r')
#         im = im.thumbnail(self.size, Image.ANTIALIAS)
        im = im.resize(self.size, Image.ANTIALIAS)
        im = im.convert("L") # convert to mono
         
        # now, work our way over the pixels
        # build up str
         
        str=""
        for y in range(0,im.size[1]):
            for x in range(0,im.size[0]):
                lum       = 255-im.getpixel((x,y))
                row       = bisect(self.zonebounds,lum)
                possibles = self.greyscale[row]
                str       = str+possibles[random.randint(0,len(possibles)-1)]
            str=str+"\n"
         
        return str