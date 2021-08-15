# coding=utf8
import telebot as NewtonBot
import json
from random import randint as Newton
from requests import get as GetNewton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
print("+--- Newton\n'|.   '|'                       .                    \n |'|   |    ....  ... ... ... .||.    ...   .. ...   \n | '|. |  .|...||  ||  ||  |   ||   .|  '|.  ||  ||  \n |   |||  ||        ||| |||    ||   ||   ||  ||  ||  \n.|.   '|   '|...'    |   |     '|.'  '|..|' .||. ||. \n+--- Newton")
TOKIN = json.load(open('tokin.json', 'r'))['TOKIN']
bot = NewtonBot.TeleBot(TOKIN)


def Add_ID(ID, VAR):
    with open('ID.json', 'r+') as file:
        data = json.load(file)
        if str(ID)+VAR not in data:
            data.append(str(ID)+VAR)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            file.close()


def Remove_ID(ID, VAR):
    with open('ID.json', 'r+') as file:
        data = json.load(file)
        data.remove(str(ID)+VAR)
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        file.close()


def Add_Name(PATH, VAR):
    with open(PATH+'.json', 'r+', encoding='utf8') as file:
        data = json.load(file)
        data.append(str(VAR))
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        file.close()


def read(Name):
    file = open(Name+'.json', 'r')
    js = json.load(file)
    file.close()
    return js


def write(text, Name):
    file = open(Name+'.json', 'w')
    json.dump(text, file)
    file.close()


def NewtonBows(text):
    bows = ['⌿ '+text+' ⍀', '⦓ '+text+' ⦔', '⦑ '+text+' ⦒', '⋖⊰ '+text+' ⊱⋗', '⸔ '+text+' ⸕',
            '「 '+text+' 」', '꧁ '+text+' ꧂', '⦏ '+text+' ⦐', '⦃ '+text+' ⦄', '❲ '+text+' ❳', '❴ '+text+' ❵', '﴾'+text+'﴿']
    return bows[Newton(0, len(bows)-1)]


def NewtonShapes():
    shapes = ['♱', '✘', '✬', '✯', '❅', '❀', '☘ ', '☀', '☁', '☂', '☃', '☄', '★', '☆',
              '❦', '❧', '⚖', '⚕', '⚔', '⚒', '♯', '♪', '♚', '☽']
    Arrows = ['↝', '↬', '↛ ', '↣', '⎇', '☇', '➜', '➴']
    return Arrows[Newton(0, len(Arrows)-1)]+shapes[Newton(0, len(shapes)-1)]


@bot.message_handler()
def start(message):
    msg = message.text
    text = msg.lower()
    Newton1 = text.replace('a', 'Ａ').replace('b', 'Ｂ').replace('c', 'Ｃ').replace('d', 'Ｄ').replace('e', 'Ｅ').replace('f', 'Ｆ').replace('g', 'Ｇ').replace('h', 'Ｈ').replace('i', 'Ｉ').replace('j', 'Ｊ').replace('k', 'Ｋ').replace('l', 'Ｌ').replace('m', 'Ｍ').replace('n', 'Ｎ').replace('o', 'Ｏ').replace('p', 'Ｐ').replace('q', 'Ｑ').replace('r', 'Ｒ').replace('s', 'Ｓ').replace('t', 'Ｔ').replace('u', 'Ｕ').replace('v', 'Ｖ').replace('w', 'Ｗ').replace('x', 'Ｘ').replace('y', 'Ｙ').replace('z', 'Ｚ').replace('ا', 'آ').replace(
        'ب', 'ﭔ').replace('ت', 'ﭥ').replace('ث', 'ﺛ').replace('ج', 'چـ').replace('ح', 'ﺢـ').replace('خ', 'خـ').replace('د', 'ﮈ').replace('ذ', 'ڎ').replace('ر', 'ړ').replace('ز', 'ڒ').replace('س', 'سـّ').replace('ش', 'شًـ').replace('ص', 'ڝـ').replace('ض', 'ڞ').replace('ط', 'طـ').replace('ظ', 'ظـ').replace('ع', 'ﻋ').replace('غ', 'ﻏ').replace('ف', 'ڤـ').replace('ق', 'قـ').replace('ك', 'ﮗ').replace('ل', 'لْـ').replace('م', 'ﻤ').replace('ن', 'ﮢـ').replace('ه', 'ھ').replace('و', 'ۈ').replace('ي', 'ﭜ')
    Newton2 = text.replace('a', 'ａ').replace('b', 'ｂ').replace('c', 'ｃ').replace('d', 'ｄ').replace('e', 'ｅ').replace('f', 'ｆ').replace('g', 'ｇ').replace('h', 'ｈ').replace('i', 'ｉ').replace('j', 'ｊ').replace('k', 'ｋ').replace('l', 'ｌ').replace('m', 'ｍ').replace('n', 'ｎ').replace('o', 'ｏ').replace('p', 'ｐ').replace('q', 'ｑ').replace('r', 'ｒ').replace('s', 'ｓ').replace('t', 'ｔ').replace('u', 'ｕ').replace('v', 'ｖ').replace('w', 'ｗ').replace('x', 'ｘ').replace('y', 'ｙ').replace('z', 'ｚ').replace(
        'ا', 'ا').replace('ب', 'ﺑ').replace('ت', 'ﭠ').replace('ث', 'ﭥ').replace('ج', 'ﭴ').replace('ح', 'פ').replace('خ', 'ﺧ').replace('د', 'ﮃ').replace('ذ', 'ذ').replace('ر', 'ژ').replace('ز', 'ژ').replace('س', 'سـ').replace('ش', 'شـ').replace('ص', 'ﺻ').replace('ض', 'ﺿ').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'ﻋ').replace('غ', 'ﻏ̣̐').replace('ف', 'ﭬ').replace('ق', 'ﻗ̮ـ̃').replace('ك', 'ﮑ').replace('ل', 'ﻟ').replace('م', 'ﻣ̝̚').replace('ن', 'ﻧ').replace('ه', 'ھَہّ').replace('و', 'ۆ').replace('ي', 'ﯾ')
    Newton3 = text.replace('a', '𝐀').replace('b', '𝐁').replace('c', '𝐂').replace('d', '𝐃').replace('e', '𝐄').replace('f', '𝐅').replace('g', '𝐆').replace('h', '𝐇').replace('i', '𝐈').replace('j', '𝐉').replace('k', '𝐊').replace('l', '𝐋').replace('m', '𝐌').replace('n', '𝐍').replace('o', '𝐎').replace('p', '𝐏').replace('q', '𝐐').replace('r', '𝐑').replace('s', '𝐒').replace('t', '𝐓').replace('u', '𝐔').replace('v', '𝐕').replace('w', '𝐖').replace('x', '𝐗').replace('y', '𝐘').replace('z', '𝐙').replace('ا', 'اٌ').replace(
        'ب', 'بّـ').replace('ت', 'تْ').replace('ث', 'ثٌ').replace('ج', 'جِ').replace('ح', 'حٍ').replace('خ', 'خً').replace('د', 'دّ').replace('ذ', 'ذّ').replace('ر', 'رُ').replace('ز', 'زٍ').replace('س', 'سُ').replace('ش', 'شْ').replace('ص', 'صٍـ').replace('ض', 'ضُ').replace('ط', 'طً').replace('ظ', 'ظَ').replace('ع', 'عٍ').replace('غ', 'غَ').replace('ف', 'ّ').replace('ق', 'قْ').replace('ك', 'كُ').replace('ل', 'لِـ').replace('م', 'مِـ').replace('ن', 'ﻧَ').replace('ه', 'هٌ').replace('و', 'وِ').replace('ي', 'يٌـ')
    Newton4 = text.replace('a', '𝐚').replace('b', '𝐛').replace('c', '𝐜').replace('d', '𝐝').replace('e', '𝐞').replace('f', '𝐟').replace('g', '𝐠').replace('h', '𝐡').replace('i', '𝐢').replace('j', '𝐣').replace('k', '𝐤').replace('l', '𝐥').replace('m', '𝐦').replace('n', '𝐧').replace('o', '𝐨').replace('p', '𝐩').replace('q', '𝐪').replace('r', '𝐫').replace('s', '𝐬').replace('t', '𝐭').replace('u', '𝐮').replace('v', '𝐯').replace('w', '𝐰').replace('x', '𝐱').replace('y', '𝐲').replace('z', '𝐳').replace(
        'ا', 'ٱ').replace('ب', 'ﭜ').replace('ت', 'ﭤ').replace('ث', 'ﺛ').replace('ج', 'چ').replace('ح', 'ح').replace('خ', 'ڂـ').replace('د', 'ﮂ').replace('ذ', 'ڎ').replace('ر', 'ږ').replace('ز', 'ژ').replace('س', 'س').replace('ش', 'ش').replace('ص', 'ڝـ').replace('ض', 'ڞـ').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'عـ').replace('غ', 'ڠـ').replace('ف', 'ﭰ').replace('ق', 'ڦـ').replace('ك', 'ڪ').replace('ل', 'ڵـ').replace('م', 'مـ').replace('ن', 'ن').replace('ه', 'ھ').replace('و', 'ۅ').replace('ي', 'ﯾ̃')
    Newton5 = text.replace('a', '𝐴').replace('b', '𝐵').replace('c', '𝐶').replace('d', '𝐷').replace('e', '𝐸').replace('f', '𝐹').replace('g', '𝐺').replace('h', '𝐻').replace('i', '𝐼').replace('j', '𝐽').replace('k', '𝐾').replace('l', '𝐿').replace('m', '𝑀').replace('n', '𝑁').replace('o', '𝑂').replace('p', '𝑃').replace('q', '𝑄').replace('r', '𝑅').replace('s', '𝑆').replace('t', '𝑇').replace('u', '𝑈').replace('v', '𝑉').replace('w', '𝑊').replace('x', '𝑋').replace('y', '𝑌').replace('z', '𝑍').replace('ا', 'ﺂ̲').replace(
        'ب', 'بـ').replace('ت', 'ﺗ̲').replace('ث', 'ﭦ').replace('ج', 'ﺟ̅').replace('ح', 'حَ').replace('خ', 'خ').replace('د', 'ﺩ̲').replace('ذ', 'ذ').replace('ر', 'ږ').replace('ز', 'ژ').replace('س', 'ﺳ̲').replace('ش', 'ﺷ̲').replace('ص', 'ڝ').replace('ض', 'ض').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'ﻋ').replace('غ', 'غ').replace('ف', 'ﻓ̲').replace('ق', 'ق').replace('ك', 'ڳ').replace('ل', 'ﻟ̲').replace('م', 'ﻣ̲').replace('ن', 'ﻧ̲').replace('ه', 'ﮬ̲̌ﮧ').replace('و', 'ۆ').replace('ي', 'يے')
    Newton6 = text.replace('a', '𝑎').replace('b', '𝑏').replace('c', '𝑐').replace('d', '𝑑').replace('e', '𝑒').replace('f', '𝑓').replace('g', '𝑔').replace('h', 'ℎ').replace('i', '𝑖').replace('j', '𝑗').replace('k', '𝑘').replace('l', '𝑙').replace('m', '𝑚').replace('n', '𝑛').replace('o', '𝑜').replace('p', '𝑝').replace('q', '𝑞').replace('r', '𝑟').replace('s', '𝑠').replace('t', '𝑡').replace('u', '𝑢').replace('v', '𝑣').replace('w', '𝑤').replace('x', '𝑥').replace('y', '𝑦').replace('z', '𝑧').replace('ا', 'ٱ').replace(
        'ب', 'ﭓ').replace('ت', 'ٺ').replace('ث', 'ﺛ').replace('ج', 'ﭸ').replace('ح', 'ﺣ̭͠').replace('خ', 'ﺧ').replace('د', 'ﮃ').replace('ذ', 'ڈ').replace('ر', 'ڔ').replace('ز', 'ژ').replace('س', 'ﺳ̭͠').replace('ش', 'ﺷ͠').replace('ص', 'ﺼ').replace('ض', 'ض').replace('ط', 'طَ').replace('ظ', 'ڟ').replace('ع', 'ﻋ̝̚').replace('غ', 'ﻏ̣̐').replace('ف', 'ﻓ̲̣̐').replace('ق', 'ڨ').replace('ك', 'ﮖ').replace('ل', 'ڷ').replace('م', 'ﻣ̝̚').replace('ن', 'ڻ').replace('ه', 'ﮪ').replace('و', 'ۈ').replace('ي', 'ې')
    Newton7 = text.replace('a', '𝑨').replace('b', '𝑩').replace('c', '𝑪').replace('d', '𝑫').replace('e', '𝑬').replace('f', '𝑭').replace('g', '𝑮').replace('h', '𝑯').replace('i', '𝑰').replace('j', '𝑱').replace('k', '𝑲').replace('l', '𝑳').replace('m', '𝑴').replace('n', '𝑵').replace('o', '𝑶').replace('p', '𝑷').replace('q', '𝑸').replace('r', '𝑹').replace('s', '𝑺').replace('t', '𝑻').replace('u', '𝑼').replace('v', '𝑽').replace('w', '𝑾').replace('x', '𝑿').replace('y', '𝒀').replace('z', '𝒁').replace('ا', 'آ').replace(
        'ب', 'بِ').replace('ت', 'تْ').replace('ث', 'ثٌ').replace('ج', 'جَ').replace('ح', 'حْ').replace('خ', 'خِ').replace('د', 'دِ').replace('ذ', 'ڐ').replace('ر', 'رَ').replace('ز', 'زَ').replace('س', 'سُ').replace('ش', 'شٌ').replace('ص', 'صَ').replace('ض', 'ڞ').replace('ط', 'طٌ').replace('ظ', 'ظْ').replace('ع', 'عَ').replace('غ', 'غّ').replace('ف', 'فْ').replace('ق', 'قِ').replace('ك', 'ﻛَ').replace('ل', 'لَ').replace('م', 'مـَ').replace('ن', 'نّ').replace('خ', 'ﮩ').replace('و', 'ۄ').replace('ي', 'يْ')
    Newton8 = text.replace('a', '𝒂').replace('b', '𝒃').replace('c', '𝒄').replace('d', '𝒅').replace('e', '𝒆').replace('f', '𝒇').replace('g', '𝒈').replace('h', '𝒉').replace('i', '𝒊').replace('j', '𝒋').replace('k', '𝒌').replace('l', '𝒍').replace('m', '𝒎').replace('n', '𝒏').replace('o', '𝒐').replace('p', '𝒑').replace('q', '𝒒').replace('r', '𝒓').replace('s', '𝒔').replace('t', '𝒕').replace('u', '𝒖').replace('v', '𝒗').replace('w', '𝒘').replace('x', '𝒙').replace('y', '𝒚').replace('z', '𝒛').replace('ا', 'آ').replace('ب', 'بٍّ').replace(
        'ت', 'تٍّ').replace('ث', 'ثٍّ').replace('ج', 'جِّ').replace('ح', 'حَّ').replace('خ', 'خِّ').replace('د', 'دٍّ').replace('ذ', 'ذ').replace('ر', 'رِ').replace('ز', 'زٍّ').replace('س', 'سَّ').replace('ش', 'شِّ').replace('ص', 'صِّ').replace('ض', 'ِّضِّ').replace('ط', 'طِّ').replace('ظ', 'ظِّ').replace('ع', 'عَّ').replace('غ', 'غَّ').replace('ف', 'فٍّ').replace('ق', 'قٍّ').replace('ك', 'ﮝ').replace('ل', 'لِّ').replace('م', 'مِّ').replace('ن', 'نِّ').replace('ه', 'هِّ').replace('و', 'وٍّ').replace('ي', 'يِّ')
    Newton9 = text.replace('a', '𝒶').replace('b', '𝒷').replace('c', '𝒸').replace('d', '𝒹').replace('e', '𝓮').replace('f', '𝒻').replace('g', '𝓰').replace('h', '𝒽').replace('i', '𝒾').replace('j', '𝒿').replace('k', '𝓀').replace('l', '𝓁').replace('m', '𝓂').replace('n', '𝓃').replace('p', '𝓅').replace('q', '𝓆').replace('r', '𝓇').replace('s', '𝓈').replace('t', '𝓉').replace('u', '𝓊').replace('w', '𝓌').replace('x', '𝓍').replace('y', '𝓎').replace('z', '𝓏').replace('ا', 'ﺂ̣̥̐').replace('ب', 'بّ').replace(
        'ت', 'تٌ').replace('ث', 'ثّـ').replace('ج', 'جّـ').replace('ح', 'حّـ').replace('خ', 'خـّ').replace('د', 'دّ').replace('ذ', 'ﮅ').replace('ر', 'رّ').replace('ز', 'ڗ').replace('س', 'ﺳ̶').replace('ش', 'ﺷ͠').replace('ص', 'صْـ').replace('ض', 'ضّـ').replace('ط', 'طِّ').replace('ظ', 'ظَّ').replace('ع', 'ﻋ̝̚').replace('غ', 'ﻏ̣̐').replace('ف', 'فّـ').replace('ق', 'قّـ').replace('ك', 'ﮗ').replace('ل', 'ﻟ̣̣').replace('م', 'ﻣ̝̚').replace('ن', 'نّ').replace('ه', 'ﮪ').replace('و', 'ۊ').replace('ي', 'ې')
    Newton10 = text.replace('a', '𝓐').replace('b', '𝓑').replace('c', '𝓒').replace('d', '𝓓').replace('e', '𝓔').replace('f', '𝓕').replace('g', '𝓖').replace('h', '𝓗').replace('i', '𝓘').replace('j', '𝓙').replace('k', '𝓚').replace('l', '𝓛').replace('m', '𝓜').replace('n', '𝓝').replace('o', '𝓞').replace('p', '𝓟').replace('q', '𝓠').replace('r', '𝓡').replace('s', '𝓢').replace('t', '𝓣').replace('u', '𝓤').replace('v', '𝓥').replace('w', '𝓦').replace('x', '𝓧').replace('y', '𝓨').replace('z', '𝓩').replace('ا', 'اّ').replace(
        'ب', 'بّ').replace('ت', 'تّ').replace('ث', 'ثّ').replace('ج', 'جّ').replace('ح', 'حّ').replace('خ', 'خّ').replace('د', 'دّ').replace('ذ', 'ذ').replace('ر', 'رّ').replace('ز', 'زّ').replace('س', 'سّ').replace('ش', 'شّ').replace('ص', 'صّ').replace('ض', 'ّضّ').replace('ط', 'طّ').replace('ظ', 'ظّ').replace('ع', 'عّ').replace('غ', 'غّ').replace('ف', 'فّ').replace('ق', 'قّ').replace('ك', 'كّ').replace('ل', 'لّ').replace('م', 'مّ').replace('ن', 'نّ').replace('ه', 'هّ').replace('و', 'وّ').replace('ي', 'يّ')
    Newton11 = text.replace('a', '𝓪').replace('b', '𝓫').replace('c', '𝓬').replace('d', '𝓭').replace('e', '𝓮').replace('f', '𝓯').replace('g', '𝓰').replace('h', '𝓱').replace('i', '𝓲').replace('j', '𝓳').replace('k', '𝓴').replace('l', '𝓵').replace('m', '𝓶').replace('n', '𝓷').replace('o', '𝓸').replace('p', '𝓹').replace('q', '𝓺').replace('r', '𝓻').replace('s', '𝓼').replace('t', '𝓽').replace('u', '𝓾').replace('v', '𝓿').replace('w', '𝔀').replace('x', '𝔁').replace('y', '𝔂').replace('z', '𝔃').replace('ا', 'اٍّ').replace(
        'ب', 'بّْ').replace('ت', 'تُّ').replace('ث', 'ثّْ').replace('ج', 'جٍّ').replace('ح', 'حّْ').replace('خ', 'خٌّ').replace('د', 'دٌّ').replace('ذ', 'ذ').replace('ر', 'رًّ').replace('ز', 'زَ').replace('س', 'سًّ').replace('ش', 'شّْ').replace('ص', 'صُّ').replace('ض', 'ُْضَّ').replace('ط', 'طَّ').replace('ظ', 'ظُ').replace('ع', 'عَّ').replace('غ', 'غٌّ').replace('ف', 'فّْ').replace('ق', 'قِّ').replace('ك', 'كّْ').replace('ل', 'لَّ').replace('م', 'مُّ').replace('ن', 'نِّ').replace('ه', 'هّْ').replace('و', 'وّ').replace('ي', 'يٌّ')
    Newton12 = text.replace('a', '𝔞').replace('b', '𝔟').replace('c', '𝔠').replace('d', '𝔡').replace('e', '𝔢').replace('f', '𝔣').replace('g', '𝔤').replace('h', '𝔥').replace('i', '𝔦').replace('j', '𝔧').replace('k', '𝔨').replace('l', '𝔩').replace('m', '𝔪').replace('n', '𝔫').replace('o', '𝔬').replace('p', '𝔭').replace('q', '𝔮').replace('r', '𝔯').replace('s', '𝔰').replace('t', '𝔱').replace('u', '𝔲').replace('v', '𝔳').replace('w', '𝔴').replace('x', '𝔵').replace('y', '𝔶').replace('z', '𝔷').replace('ا', 'آ').replace(
        'ب', 'بْ').replace('ت', 'تْ').replace('ث', 'ثْ').replace('ج', 'جْ').replace('ح', 'حْ').replace('خ', 'خْ').replace('د', 'دْ').replace('ذ', 'ذْ').replace('ر', 'رْ').replace('و', 'زْ').replace('س', 'سْ').replace('ش', 'شْ').replace('ص', 'صْ').replace('ض', 'ضْ').replace('ط', 'طْ').replace('ظ', 'ظْ').replace('ع', 'عْ').replace('غ', 'غْ').replace('ف', 'فْ').replace('ق', 'قْ').replace('ك', 'ڪْ').replace('ل', 'لْ').replace('م', 'مْ').replace('ن', 'نْ').replace('ه', 'ﮬ̲̣̐').replace('و', 'وْ').replace('ي', 'يْ')
    Newton13 = text.replace('a', '𝔸').replace('c', 'ℂ').replace('b', '𝔹').replace('d', '𝔻').replace('e', '𝔼').replace('f', '𝔽').replace('g', '𝔾').replace('h', 'ℍ ').replace('i', '𝕀').replace('j', '𝕁').replace('k', '𝕂').replace('l', '𝕃').replace('m', '𝕄').replace('n', 'ℕ').replace('o', '𝕆').replace('p', 'ℙ').replace('q', 'ℚ').replace('r', 'ℝ').replace('s', '𝕊').replace('t', '𝕋').replace('u', '𝕌').replace('v', '𝕍').replace('w', '𝕎').replace('x', '𝕏').replace('y', '𝕐').replace('z', 'ℤ').replace('ا', 'اَ').replace(
        'ب', 'بَ').replace('ت', 'تَ').replace('ث', 'ثَ').replace('ج', 'جَ').replace('ح', 'حَ').replace('خ', 'خَ').replace('د', 'دَ').replace('ذ', 'ذ').replace('ر', 'رَ').replace('ز', 'زَّ').replace('س', 'سَ').replace('ش', 'شَ').replace('ص', 'صَ').replace('ض', 'َضَ').replace('ط', 'طَ').replace('ظ', 'ظَ').replace('ع', 'عَ').replace('غ', 'غَ').replace('ف', 'فَ').replace('ق', 'قَ').replace('ك', 'كَ').replace('ل', 'لَ').replace('م', 'مَ').replace('ن', 'نَ').replace('ه', 'هَ').replace('و', 'وًّ').replace('ي', 'يَ')
    Newton14 = text.replace('a', '𝕒').replace('b', '𝕓').replace('c', '𝕔').replace('d', '𝕕').replace('e', '𝕖').replace('f', '𝕗').replace('g', '𝕘').replace('h', '𝕙').replace('i', '𝕚').replace('j', '𝕛').replace('k', '𝕜').replace('l', '𝕝').replace('m', '𝕞').replace('n', '𝕟').replace('o', '𝕠').replace('p', '𝕡').replace('q', '𝕢').replace('r', '𝕣').replace('s', '𝕤').replace('t', '𝕥').replace('u', '𝕦').replace('v', '𝕧').replace('w', '𝕨').replace('x', '𝕩').replace('y', '𝕪').replace('z', '𝕫').replace('ا', 'ּٵ̍').replace('ب', 'بــ').replace(
        'ت', 'ּۛٺــ').replace('ث', 'ۖٽــ').replace('ج', 'ּۛڇۚــ').replace('ح', 'ּحۡــ').replace('خ', 'ۖڅۡــ').replace('د', 'ۖد').replace('ذ', 'ذ').replace('ر', 'ڔ').replace('ز', 'ۖڙ').replace('س', 'ڛۜــ').replace('ش', 'ּڜــ').replace('ص', 'ּڝــ').replace('ض', 'ڞــ').replace('ط', 'ּٹــ').replace('ظ', 'ڟــ').replace('ع', 'ۖ؏ــ').replace('غ', 'ۖڠــ').replace('ف', 'ּۛڣــ').replace('ق', 'ּۛڦــ').replace('ك', 'ڪــ').replace('ل', 'ּڷــ').replace('م', 'ּمۭــ').replace('ن', 'ۖنۨــ').replace('ه', 'هــ').replace('و', 'ﯣ').replace('ي', 'ּيۧۗ')
    Newton15 = text.replace('a', '𝕬').replace('b', '𝕭').replace('c', '𝕮').replace('d', '𝕯').replace('e', '𝕰').replace('f', '𝕱').replace('g', '𝕲').replace('h', '𝕳').replace('i', '𝕴').replace('j', '𝕵').replace('k', '𝕶').replace('l', '𝕷').replace('m', '𝕸').replace('n', '𝕹').replace('o', '𝕺').replace('p', '𝕻').replace('q', '𝕼').replace('r', '𝕽').replace('s', '𝕾').replace('t', '𝕿').replace('u', '𝖀').replace('v', '𝖁').replace('w', '𝖂').replace('x', '𝖃').replace('y', '𝖄').replace('z', '𝖅').replace('ا', 'أ').replace(
        'ب', 'ب').replace('ت', 'تہ').replace('ث', 'ثہ').replace('ج', 'جہ').replace('ح', 'حہ').replace('خ', 'خہ').replace('د', 'د').replace('ذ', 'ذ').replace('ر', 'ر').replace('ز', 'ز').replace('س', 'سہ').replace('ش', 'شہ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طہ').replace('ظ', 'ظ').replace('ع', 'عہ').replace('غ', 'غہ').replace('ف', 'فُہ').replace('ق', 'ق').replace('ك', 'كُہ').replace('ل', 'لہ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هـ').replace('و', 'و').replace('ي', 'يہ')
    Newton16 = text.replace('a', '𝖆').replace('b', '𝖇').replace('c', '𝖈').replace('d', '𝖉').replace('e', '𝖊').replace('f', '𝖋').replace('g', '𝖌').replace('h', '𝖍').replace('i', '𝖎').replace('j', '𝖏').replace('k', '𝖐').replace('l', '𝖑').replace('m', '𝖒').replace('n', '𝖓').replace('o', '𝖔').replace('p', '𝖕').replace('q', '𝖖').replace('r', '𝖗').replace('s', '𝖘').replace('t', '𝖙').replace('u', '𝖚').replace('v', '𝖛').replace('w', '𝖜').replace('x', '𝖝').replace('y', '𝖞').replace('z', '𝖟').replace('ا', 'أ').replace(
        'ب', 'ب̷').replace('ت', 'ت̷').replace('ث', 'ث̷').replace('ج', 'ج̷').replace('ح', 'ح̷').replace('خ', 'خ̷').replace('د', 'د̷ِ').replace('ذ', 'ذ̷').replace('ر', 'ر̷').replace('ز', 'ز̷').replace('س', 'س̷').replace('ش', 'ش̷ُ').replace('ص', 'ص̷').replace('ض', 'ض').replace('ط', 'ط̷ُ').replace('ظ', 'ظ̷ً').replace('ع', 'ع̷ٍ').replace('غ', 'غ̷').replace('ف', 'ف̷َ').replace('ق', 'ق̷').replace('ك', 'گ̷').replace('ل', 'ل̷').replace('م', 'م̷').replace('ن', 'ن̷').replace('ي', 'ہ̷ـ').replace('و', 'ۆ̷').replace('ي', 'ي̷')
    Newton17 = text.replace('a', '𝖠').replace('b', '𝖡').replace('c', '𝖢').replace('d', '𝖣').replace('e', '𝖤').replace('f', '𝖥').replace('g', '𝖦').replace('h', '𝖧').replace('i', '𝖨').replace('j', '𝖩').replace('k', '𝖪').replace('l', '𝖫').replace('m', '𝖬').replace('n', '𝖭').replace('o', '𝖮').replace('p', '𝖯').replace('q', '𝖰').replace('r', '𝖱').replace('s', '𝖲').replace('t', '𝖳').replace('u', '𝖴').replace('v', '𝖵').replace('w', '𝖶').replace('x', '𝖷').replace('y', '𝖸').replace('z', '𝖹').replace('ا', 'أ').replace(
        'ب', 'ب͠').replace('ت', 'ت͠').replace('ث', 'ث͠').replace('ج', 'ج͠').replace('ح', 'ح͠').replace('خ', 'خ͠').replace('د', 'د͠').replace('ذ', 'ذ͠').replace('ر', 'ر').replace('ز', 'ز͠').replace('س', 'س͠').replace('ش', 'ش͠').replace('ص', 'ص͠').replace('ض', 'ض').replace('ط', 'ط͠').replace('ظ', 'ظ͠').replace('ع', 'ع͠').replace('غ', 'غ͠').replace('ف', 'ف͠').replace('ق', 'ق͠').replace('ك', 'گ͠').replace('ل', 'ل͠').replace('م', 'م͠').replace('ن', 'ن͠').replace('ه', 'ه͠ـ').replace('و', 'و͠').replace('ي', 'ي͠')
    Newton18 = text.replace('a', '𝖺').replace('b', '𝖻').replace('c', '𝖼').replace('d', '𝖽').replace('e', '𝖾').replace('f', '𝖿').replace('g', '𝗀').replace('h', '𝗁').replace('i', '𝗂').replace('j', '𝗃').replace('k', '𝗄').replace('l', '𝗅').replace('m', '𝗆').replace('n', '𝗇').replace('o', '𝗈').replace('p', '𝗉').replace('q', '𝗊').replace('r', '𝗋').replace('s', '𝗌').replace('t', '𝗍').replace('u', '𝗎').replace('v', '𝗏').replace('w', '𝗐').replace('x', '𝗑').replace('y', '𝗒').replace('z', '𝗓').replace('ا', 'أ').replace(
        'ب', 'بَ').replace('ت', 'ت').replace('ث', 'ث').replace('ج', 'جٍ').replace('ح', 'حٍ').replace('خ', 'خـ').replace('د', 'دِ').replace('ذ', 'ذَ').replace('ر', 'رٍ').replace('ز', 'زْ').replace('س', 'س').replace('ش', 'شُ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طُ').replace('ظ', 'ظً').replace('ع', 'عٍ').replace('غ', 'غ').replace('ف', 'فُ').replace('ق', 'قٌ').replace('ك', 'ڪ').replace('ل', 'لُِ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هــ').replace('و', 'وُ').replace('ي', 'ي')
    Newton19 = text.replace('a', '𝗔').replace('b', '𝗕').replace('c', '𝗖').replace('d', '𝗗').replace('e', '𝗘').replace('f', '𝗙').replace('g', '𝗚').replace('h', '𝗛').replace('l', '𝗜').replace('j', '𝗝').replace('x', '𝗞').replace('l', '𝗟').replace('m', '𝗠').replace('n', '𝗡').replace('o', '𝗢').replace('p', '𝗣').replace('q', '𝗤').replace('r', '𝗥').replace('s', '𝗦').replace('t', '𝗧').replace('u', '𝗨').replace('v', '𝗩').replace('w', '𝗪').replace('x', '𝗫').replace('y', '𝗬').replace('z', '𝗭').replace('ا', 'أ').replace(
        'ب', 'بٰٰ').replace('ت', 'تہٰ').replace('ث', 'ثہٰـ').replace('ج', 'ج').replace('ح', 'حہٰ').replace('خ', 'خ').replace('د', 'د').replace('ذ', 'ذ').replace('ر', 'ر').replace('ز', 'ز').replace('س', 'سہٰ').replace('ش', 'ش').replace('ص', 'صہٰ').replace('ض', 'ض').replace('ط', 'طہٰ').replace('ظ', 'ظ').replace('ع', 'ع').replace('غ', 'غ').replace('ف', 'فہٰ').replace('ق', 'ق').replace('ك', 'كہٰ').replace('ل', 'لہٰ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هـ').replace('و', 'و').replace('ي', 'يٰ')
    Newton20 = text.replace('a', '𝗮').replace('b', '𝗯').replace('c', '𝗰').replace('d', '𝗱').replace('e', '𝗲').replace('f', '𝗳').replace('g', '𝗴').replace('h', '𝗵').replace('i', '𝗶').replace('j', '𝗷').replace('k', '𝗸').replace('l', '𝗹').replace('m', '𝗺').replace('n', '𝗻').replace('o', '𝗼').replace('p', '𝗽').replace('q', '𝗾').replace('r', '𝗿').replace('s', '𝘀').replace('t', '𝘁').replace('u', '𝘂').replace('v', '𝘃').replace('w', '𝘄').replace('x', '𝘅').replace('y', '𝘆').replace('z', '𝘇').replace('ا', 'أ').replace(
        'ب', 'بَ').replace('ت', 'ت').replace('ث', 'ث').replace('ج', 'جٍ').replace('ح', 'حٍ').replace('خ', 'خـ').replace('د', 'دِ').replace('ذ', 'ذَ').replace('ر', 'رٍ').replace('ز', 'زْ').replace('س', 'س').replace('ش', 'شُ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طُ').replace('ظ', 'ظً').replace('ع', 'عٍ').replace('غ', 'غ').replace('ف', 'فُ').replace('ق', 'قٌ').replace('ك', 'ڪ').replace('ل', 'لُِ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هــ').replace('و', 'وُ').replace('ي', 'ي')
    Newtonboy = ['''❥•َ⚡️͢ֆ⸽
        ⠀

                    ‏ＢΔ S R A ┆17 Y.O ↴   
        ﴿ ‏ ‏ NewtonText 💛ء''', '''⠀
        ⠀
        ⠀



        ⠀                  I R A Q ┆19 Y.O ↴    
                ﴿ NewtonText ️. 💛۽
        ⠀
        ⠀
        ⠀''',

                 '''⠀ ⠀⠀⠀ ⠀⠀⠀ 
        ⠀⠀
        ⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀ ⠀⠀
        ⠀ ⠀⠀⠀⠀- ᗩGE : 17 Y.O
        NewtonText ً.  💛 
        ⠀ ⠀⠀⠀ ⠀⠀⠀ 
        ⠀⠀
        ⠀⠀⠀⠀''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀
        ⠀
        ⠀
        ⠀
        NewtonText . 🥀  
        ⠀⠀⠀⠀- Unfollow Block ♚ֆ 〞 
        ⠀
        ⠀
        ⠀‎
        ‏⠀⠀⠀
        ‎‏⠀''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀

        ⠀
        ⠀
        ‏‏‏NewtonText 🖤ء
        ⠀⠀⠀⠀⠀✗ ᗩGE┊19 ✿‏ֆ
        ⠀
        ⠀
        ⠀‎
        ‏⠀⠀⠀
        ‎‏⠀''',

                 '''⠀⠀


        ⠀⠀
        NewtonText 🥀 🚬 
        ⠀  ⠀   ғollow мe , ғollow вacĸ⠀⠀
        ⠀⠀⠀⠀⠀⠀┄༻☹️༺┄⠀
        ⠀⠀⠀⠀⠀ㅤ⠀‏ ‏⠀⠀''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀

        ⠀
        ⠀
        - ‏NewtonText ☻. 
        ⠀⠀⠀⠀⠀- 🇮🇶|| 19 Y.O ❞
        ⠀
        ⠀
        ⠀‎
        ‏⠀⠀⠀
        ‎‏⠀''',

                 '''⠀
        ⠀
        ⠀



        ⠀            ‏ＢΔ S R A ┆17 Y.O ↴    
        🖤. NewtonText
        ⠀
        ⠀
        ⠀''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀

        ⠀
        ⠀⠀⠀⠀⠀⠀✗ IR‏ΔQ ˛⁽💛₎⇣    
        ﴿ ‏‏NewtonText . 🖤‏ء
        ⠀
        ⠀
        ⠀‎
        ‏⠀⠀⠀
        ‎‏⠀''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀

        ⠀
            ﴿‏ ‏NewtonText🤦🏽‍♀️ً ٰ. 
        ⠀⠀⠀⠀⠀⠀  𖤍 BASRA - iQ ‏
        ⠀‎
        ⠀‎
        ⠀
        ⠀‎
        ''',

                 '''‎‏⠀
        ‎‏⠀
        ‏⠀

        ⠀⠀

        ⠀
        ⠀
        ‏‏‏NewtonText 🖤ء
        ⠀⠀⠀⠀⠀✗ ᗩGE┊19 ✿‏ֆ
        ⠀
        ⠀
        ⠀‎
        ‏⠀⠀⠀
        ‎‏⠀''',

                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀ ֆ ⁽ ♥ ⁾↵
                       

         ⠀          ‹ 🇮🇶 ³¹³ BAGHDAD ›⠀⠀
        NewtonText! 🤷🏽‍♀️
        ⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀
        ⠀''',

                 '''⠀⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ⠀
        ⠀⠀⠀⠀⠀
        ⠀  ⠀⠀                      
        ⠀⠀⠀⠀•┆BΔGHDΔD 🇮🇶 ‏ֆ 
        ‏NewtonText 🖤‏.
        ⠀⠀⠀⠀⠀⠀⠀
        ‏⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀
        ⠀
        ⠀



        ⠀⠀⠀⠀⠀⠀IRΔQ┆19 Y.O ↴    
        ⠀
        ﴿ NewtonText 💚.
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀
        ⠀
        ⠀



        ⠀                  Baghdad ┆15 Y.O ↴    
        ﴿ ‏NewtonText 🖤.
        ⠀
        ⠀
        ⠀''',

                 '''⠀
        ⠀
        ⠀ 

        ⠀
        ⠀
            
        ‏NewtonText  🖤»
        ⠀⠀     ⠀- Bagdad 19Y.O♚ֆ 
        ⠀

        ⠀ ⠀
        ⠀ ⠀''',

                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀          ⠀⠀➝ IR‏ΔQ ˛⁽ 💙 ₎⇣    
        ⠀⠀⠀⠀
        ‏NewtonText 💔.
            ⠀
        ⠀⠀⠀⠀
        ⠀
        ⠀''',

                 '''⠀
        ‏⠀


        ⠀
        ⠀ 
        ⠀⠀⠀⠀⠀❥⁽ AGE┊9 ♚ )
        ⠀
        ﴿ NewtonText ❤️.

        ⠀


        ⠀''',

                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀⠀♛ | ؁ ➝🇮🇶
        ﴿ •  NewtonText 🖤 ֆء
        ⠀♛ | OFFICIAL ACCOANT
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀ 
        ⠀                  ⠀      ↓ ❛
        ⠀
        ⠀    ⠀              ﴾   ⠀ ⠀ 
        ⠀       ♩❥ NewtonText ﴿⠀ ⠀ 
        ⠀       welcome to my profile 
        ⠀ 
        ⠀
        ⠀⠀⠀''',

                 '''⠀⠀


        ⠀⠀‏“🥀 NewtonText “
        ⠀  ғollow мe , ғollow вacĸ⠀⠀
        ⠀⠀⠀⠀⠀┄༻☹️༺┄⠀
        ⠀⠀⠀⠀⠀ㅤ⠀
        ‏
        ''',

                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀♛ | ؁ ➝🇮🇶‏
        ♥️ NewtonText ♯
        ⠀⠀⠀♛ | OFFICIAL ACCOANT
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀ㅤ
        ㅤ 
        ⠀⠀ ㅤ 


        ⠀ ⠀⠀ ㅤ ㅤ ⠀ㅤ ㅤ ؁ ➝🇮🇶   
        NewtonText
        ⠀ㅤ ✿ωєℓ¢σм тσσмуρяσfιℓє✿

        ‏⠀⠀⠀
        ⠀
        ㅤ ㅤ 
        ⠀⠀⠀⠀⠀''',

                 '''
        ⠀
        ⠀
        ⠀⠀⠀ ⠀ ⠀⠀⠀⠀⠀⠀⠀↴⠀
        ⠀⠀❞ᗷᗩS3RAY 🇮🇶|| 21 Y.O ❞
        NewtonText
        ‏﴿ 🌞💧 ﴾

        ⠀ ⠀⠀ 
        ⠀⠀''',

                 '''⠀
        ⠀

        ⠀⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀  ⠀┄༻💠༺┄⠀                      
        ﴿ NewtonText ❤️ء  ﴾ 
        ⠀‏⠀ ⠀ᎳᎬᏞᏟᎾm TO ṃʏ ƿяȏғıʟ
        ⠀⠀⠀⠀⠀⠀⠀┄༻💠༺┄
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀‏⠀

        ⠀‏⠀⠀⠀⠀⠀ ⠀❥ ⁞ ؁  ֆء
        ‏﴿ NewtonText  ..؟⠀
        ⠀ ⠀⠀⠀‏⠀ᴡᴇʟᴄᴏᴍ ᴛᴏ ᴍʏ ᴘʀᴏғɪʟ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀
        ⠀⠀
        ⠀⠀
        ⠀⠀ ⠀ ⠀⠀ ⠀⠀◂◂⠀⠀⠀▮▮⠀⠀⠀▸▸
        ⠀ ⠀⠀ ⠀ ⠀  |◂ ▬▬▬▬●▬▬ ◂|
        ⠀ ⠀⠀ ⠀   ➰ NewtonText ➰ 
        ⠀ ❈⁽ From : IRΔQ➢ＢΔＧḤＤΔＤ ❉
        ⠀''',

                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀❶❽ Ꭹ.Ꭷ
        ⠀⠀⠀⠀⠀⠀⠀❖┊ᖴᖇOᗰ ᗷᗩᔕᖇᗩ
        ‏⠀NewtonText ✘✋🏻 ⠀⠀⠀
        ⠀⠀⠀⠀↬ ❈⁽ шεᴌcσмε тσ мч вяσғ ❁
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''‏⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ⠀⠀⠀⠀⠀ ❈ ⁽💛 ✿ ₎❈↴
        ‏⠀

        ﴿   NewtonText ❤️
        ‏⠀‏ ⠀ᎳᎬᏞᏟᎾm TO ṃʏ ƿяȏғıʟ⠀
        ⠀⠀⠀⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ⠀''',

                 '''⠀⠀


        ⠀⠀
        NewtonText 😴🎷
            ғollow мe , ғollow вacĸ⠀⠀
        ⠀⠀⠀⠀┄༻☹️༺┄⠀
        ⠀⠀⠀⠀⠀ㅤ⠀
        ‏
        ‏ ‏⠀⠀ 

            ⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀''',

                 '''⠀ ⠀ ⠀
        ⠀ ⠀ ⠀

        ‏⠀⠀ ⠀
        ⠀  ⠀❆ＩＱ › ＢΔＧḤＤΔＤ ❉‏⠀
        ‏‏⠀(NewtonText ֆ ☺️!)
                    ※•┈•ʚ♚ɞ•┈‏​•※
        ⠀ ⠀ ⠀
        ⠀ ⠀ ⠀
        ⠀ ⠀ ⠀
        ⠀ ⠀ ⠀''',

                 '''‏⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ⠀⠀⠀⠀⠀⠀ ✿┊Y.O:19  ֆ 
        NewtonText 💔ء﴾
        ‏⠀⠀‏⠀⠀⠀┈┉━❀🚶🏻❀━┅┄⠀
        ‏⠀
        ‏⠀
        ''',
                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀          ⠀⠀➝ IR‏ΔQ ˛⁽ 💙 ₎⇣    
        ⠀⠀⠀⠀
        NewtonText 💚۽
            ⠀
        ⠀⠀⠀⠀
        ⠀
        ⠀''',

                 '''⠀

        ⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀♛؁17♛
        ⠀⠀⠀⠀⠀﴾ IQ ﴿ ��🇶  ❥ᗷᗩᔕᖇᗩ⠀
        “ NewtonText 🏃
        ⠀⠀
        ⠀
        ⠀
        ⠀''',

                 '''‏⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ‏⠀
        ⠀⠀⠀⠀⠀⠀ ✿┊Y.O:19  ֆ 
        ⠀  ⠀❆ＩＱ › ＢΔＧḤＤΔＤ ❉‏⠀
        NewtonText ؟❤️﴾
        ‏⠀⠀‏⠀⠀⠀┈┉━❀🚶🏻❀━┉┄⠀
        ‏⠀
        ‏⠀
        ''',
                 '''⠀
        ⠀
        ⠀
        ⠀
        ⠀⠀⠀ ⠀⠀➝ IR‏ΔQ ˛⁽ ♥ ₎⇣  
        ⠀⠀⠀⠀
        ⠀⠀ NewtonText ⁽✺⃕₎ 
        ↬  ❈⁽ шεʟcσмε тσ мч вяσғ ❁
        ‏⠀⠀⠀⠀┄༻💗༺┄       ⠀
        ⠀⠀⠀⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀
        ⠀

        ⠀
        ⠀
        ⠀⠀⠀⠀⠀⠀⠀◂◄⠀⠀▮▮⠀⠀▸►
        ⠀⠀⠀◂⠀━━━━❊━━━━⠀▸
        NewtonText ء.
        
        ⠀
        ⠀
        ⠀
        ⠀''',

                 '''⠀ ⠀⠀⠀ ⠀⠀⠀ 
        ⠀⠀
        ⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀ ⠀⠀
        ⠀ ⠀⠀⠀        ⠀- ᗩGE : 17 Y.O

        NewtonText
        ؛❤
        ‏
        ⠀ ⠀⠀⠀ ⠀⠀⠀ 
        ⠀⠀''',

                 '''‎‏ㅤ
        ‎‏⠀⠀⠀‏ㅤ⠀⠀⠀
        ‎‏ㅤ
        ⠀‏
        ‎‏ㅤ⠀⠀ ⠀     ⠀ ➝ Y.O:18 ֆ 💭  

        NewtonText 🌸₎
        ‎‏ㅤ
        ‎‏ㅤ
        ‎‏ㅤ⠀⠀⠀''']
# End var
    try:
        if message.chat.type == 'private':
            def ID_Newton(ID):
                with open('BotID.json', 'r+') as file:
                    data = json.load(file)
                    if ID not in data:
                        bot.send_message(
                            read('sudo')['ID_SUDO'], 'قام : '+message.from_user.first_name+'\nبئستعمال البوت')
                        data.append(ID)
                        file.seek(0)
                        json.dump(data, file)
                        file.truncate()
                        file.close()
            if GetNewton('https://api.telegram.org/bot'+TOKIN+'/getChatMember?chat_id='+read('sudo')['CHAT']+'&user_id='+str(message.from_user.id)).json()['result']['status'] == 'left':
                bot.send_message(message.from_user.id, '• اهلا بك، '+message.from_user.first_name+'\n- في بوت الزخرفةالشامل؛\n- استخدام البوت عليك الاشتراك اولاً 🧸💕\n- قناة البوت  ' +
                                 read('sudo')['CHAT']+' 💘🌈 \n\nـ-- -- -- -- - -- -- -- -- -- -- -- -- --')
            else:
                if message.from_user.id == int(read('sudo')["ID_SUDO"]):
                    if message.text and read('BotSendAll'):
                        for i in read('BotID'):
                            bot.send_message(i, message.text)
                        bot.reply_to(message, 'تم الاذاعه الى : ' +
                                     str(len(read('BotID'))))
                        write(False, 'BotImport')
                    elif message.text and read('BotImport') == 'CH':
                        if '@' in message.text:
                            bot.send_message(message.chat.id, 'تم اضاف القناة')
                            files = open('sudo.json', 'r+')
                            data = json.load(files)
                            data['CHAT'] = message.text
                            files.seek(0)
                            json.dump(data, files)
                            files.truncate()
                            files.close()
                            write('Newton', 'BotImport')
                        else:
                            bot.send_message(
                                message.from_user.id, 'المعرف خاطأ')
                            write('Newton', 'BotImport')
                    elif message.text and read('BotImport') == 'ID':
                        try:
                            files = open('sudo.json', 'r+')
                            data = json.load(files)
                            data['ID_SUDO'] = int(message.text)
                            files.seek(0)
                            json.dump(data, files)
                            files.truncate()
                            files.close()
                            bot.send_message(
                                message.chat.id, 'تم تحويل الملكيه بنجاح', reply_markup=ReplyKeyboardRemove(selective=False))
                            markup = ReplyKeyboardMarkup()
                            itembtn1 = KeyboardButton('المشتركين')
                            itembtn2 = KeyboardButton('اذاعة')
                            itembtn3 = KeyboardButton('اضافة اسماء')
                            itembtn4 = KeyboardButton('اضافة نبذات')
                            itembtn5 = KeyboardButton('اضافة اختصارات')
                            itembtn6 = KeyboardButton('تغير قناة الاشتراك')
                            itembtn7 = KeyboardButton('تحويل ملكية البوت')
                            itembtn8 = KeyboardButton('اخفاء الكيبورد')
                            markup.row(itembtn1, itembtn2)
                            markup.row(itembtn3, itembtn4, itembtn5)
                            markup.row(itembtn6, itembtn7)
                            markup.row(itembtn8)
                            bot.send_message(
                                message.text, "مرحباً عزيزي تم تحويل ملكية البوت لك اليك الاوامر", reply_markup=markup)
                            write('Newton', 'BotImport')
                        except Exception as e:
                            bot.send_message(
                                message.from_user.id, 'الايدي خاطأ')
                            write('Newton', 'BotImport')
                    elif message.text and read('BotImport') == 'Boy':
                        bot.send_message(message.chat.id, 'تم اضاف النبذه')
                        Add_Name('Boy', message.text)
                        write('Newton', 'BotImport')
                    elif message.text and read('BotImport') == 'Name':
                        bot.send_message(message.chat.id, 'تم اضاف الاسم')
                        Add_Name('Name', message.text)
                        write('Newton', 'BotImport')
                    elif message.text and read('BotImport') == 'Su':
                        bot.send_message(message.chat.id, 'تم اضاف الاختصار')
                        Add_Name('Su', message.text)
                        write('Newton', 'BotImport')
                    elif message.text == '/start':
                        markup = ReplyKeyboardMarkup()
                        itembtn1 = KeyboardButton('المشتركين')
                        itembtn2 = KeyboardButton('اذاعة')
                        itembtn3 = KeyboardButton('اضافة اسماء')
                        itembtn4 = KeyboardButton('اضافة نبذات')
                        itembtn5 = KeyboardButton('اضافة اختصارات')
                        itembtn6 = KeyboardButton('تغير قناة الاشتراك')
                        itembtn7 = KeyboardButton('تحويل ملكية البوت')
                        itembtn8 = KeyboardButton('اخفاء الكيبورد')
                        markup.row(itembtn1, itembtn2)
                        markup.row(itembtn3, itembtn4, itembtn5)
                        markup.row(itembtn6, itembtn7)
                        markup.row(itembtn8)
                        bot.send_message(
                            message.from_user.id, "مرحباً عزيزي المطور اليك الاوامر", reply_markup=markup)
                    elif message.text == 'تغير قناة الاشتراك':
                        bot.send_message(
                            message.chat.id, 'ارسل معرف القناة الجديده \n قبل ارسال المعرف تئكد ان البوت ادمن في القناة الجديده')
                        write('CH', 'BotImport')
                    elif message.text == 'تحويل ملكية البوت':
                        bot.send_message(
                            message.chat.id, 'ارسل ايدي المطور الجديد')
                        write('ID', 'BotImport')
                    elif message.text == 'المشتركين':
                        bot.send_message(message.from_user.id, 'عدد المشتركين في البوت : ' +
                                         str(len(read('BotID'))))
                    elif message.text == 'اضافة اسماء':
                        bot.send_message(message.from_user.id,
                                         'ارسل الاسم ليتم اضافتة')
                        write('Name', 'BotImport')
                    elif message.text == 'اضافة نبذات':
                        bot.send_message(message.from_user.id,
                                         'ارسل النبذه ليتم اضافتة')
                        write('Boy', 'BotImport')
                    elif message.text == 'اضافة اختصارات':
                        bot.send_message(message.from_user.id,
                                         'ارسل اختصارات ليتم اضافتة')
                        write('Su', 'BotImport')
                    elif message.text == 'اذاعة':
                        bot.send_message(message.from_user.id,
                                         'ارسل النص الذي تريد اذاعتة')
                        write(True, 'BotSendAll')
                    elif message.text == 'اخفاء الكيبورد':
                        bot.send_message(message.from_user.id, 'تم اخفاء الكيبورد لأضهار \n الكيبورد ارسل /start',
                                         reply_markup=ReplyKeyboardRemove(selective=False))
                if message.text == '/start':
                    file0 = open('sudo.json', 'r')
                    filej = json.load(file0)
                    NameChat = bot.get_chat(filej['CHAT']).title
                    keyboard = [[InlineKeyboardButton(message.from_user.first_name, callback_data='#')], [InlineKeyboardButton('زخرفــهـ الاســم', callback_data='ZH'), InlineKeyboardButton('بايو انــستا', callback_data='boy')], [InlineKeyboardButton('رمــوز وارقــام', callback_data='Num And Pass')], [InlineKeyboardButton('اسماء جاهزه', callback_data='Name Completing'), InlineKeyboardButton(
                        'اسماء ببجي', callback_data='Name PUBG')], [InlineKeyboardButton('جمالي من 10', callback_data='%')], [InlineKeyboardButton('نبذه جاهزه', callback_data='boyn'), InlineKeyboardButton('اختصارات', callback_data='Shortcuts')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]
                    bot.send_message(message.from_user.id, '• اهلا بك، '+message.from_user.first_name +
                                     '\n- في بوت الزخرفةالشامل؛)\n- يمكنك الزخرفه باللغه الانكليزيه واللغه العربيه 🧸💕\n- البوت الاول من نوعه في التلكرام  💘🌈 \nـ-- -- -- -- - -- -- -- -- -- -- -- -- --', reply_markup=InlineKeyboardMarkup(keyboard))
                    ID_Newton(message.from_user.id)
                    file0.close()
                elif str(message.from_user.id)+'ZH' in read('ID'):
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton1)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton2)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton3)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton4)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton5)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton6)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton7)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton8)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton9)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton10)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton11)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton12)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton13)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton14)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton15)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton16)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton17)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton18)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton19)+NewtonShapes())
                    bot.send_message(message.from_user.id,
                                     NewtonBows(Newton20)+NewtonShapes())
                    Remove_ID(str(message.from_user.id), 'ZH')
                elif str(message.from_user.id)+'boy' in read('ID'):
                    NewtonNum = 0
                    while True:
                        bot.send_message(message.from_user.id,
                                         Newtonboy[Newton(0, len(Newtonboy)-1)].replace('NewtonText', text))
                        if NewtonNum == 20:
                            break
                        NewtonNum = NewtonNum + 1
                    Remove_ID(str(message.from_user.id), 'boy')
    except Exception as e:
        bot.send_message(read('sudo')['ID_SUDO'], e)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        NameChat = bot.get_chat(read('sudo')['CHAT']).title
        if GetNewton('https://api.telegram.org/bot'+TOKIN+'/getChatMember?chat_id='+read('sudo')['CHAT']+'&user_id='+str(call.from_user.id)).json()['result']['status'] == 'left':
            bot.send_message(call.from_user.id, '• اهلا بك، '+call.from_user.first_name+'\n- في بوت الزخرفةالشامل؛\n- استخدام البوت عليك الاشتراك اولاً 🧸💕\n- قناة البوت  ' +
                             read('sudo')['CHAT']+' 💘🌈 \n\nـ-- -- -- -- - -- -- -- -- -- -- -- -- --')
        else:
            if call.data == 'home':
                keyboard = [[InlineKeyboardButton(call.from_user.first_name, callback_data='#')], [InlineKeyboardButton('زخرفــهـ الاســم', callback_data='ZH'), InlineKeyboardButton('بايو انــستا', callback_data='boy')], [InlineKeyboardButton('رمــوز وارقــام', callback_data='Num And Pass')], [InlineKeyboardButton('اسماء جاهزه', callback_data='Name Completing'), InlineKeyboardButton(
                    'اسماء ببجي', callback_data='Name PUBG')], [InlineKeyboardButton('جمالي من 10', callback_data='%')], [InlineKeyboardButton('نبذه جاهزه', callback_data='boyn'), InlineKeyboardButton('اختصارات', callback_data='Shortcuts')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]
                bot.edit_message_text('• اهلا بك، '+call.from_user.first_name +
                                      '\n- في بوت الزخرفةالشامل؛)\n- يمكنك الزخرفه باللغه الانكليزيه واللغه العربيه 🧸💕\n- البوت الاول من نوعه في التلكرام  💘🌈 \nـ-- -- -- -- - -- -- -- -- -- -- -- -- --', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup(keyboard))
            elif call.data == '#':
                bot.send_message(call.from_user.id, 'you id : ' +
                                 str(call.from_user.id))
            elif call.data == 'ZH':
                bot.send_message(call.from_user.id, 'حسناً عزيزي ' +
                                 call.from_user.first_name+'\nارسل اسمك ليتم زخرفته')
                Add_ID(call.from_user.id, 'ZH')
            elif call.data == 'boy':
                bot.send_message(call.from_user.id, 'حسناً عزيزي ' +
                                 call.from_user.first_name+'\nارسل النص لتحويله الى بايو انستا')
                Add_ID(call.from_user.id, 'boy')
            elif call.data == 'Num And Pass':
                bot.edit_message_text('اختر طلبك من الازرار الموجوده في الاسفل', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('الصفحة الرئيسية', callback_data='home')], [
                    InlineKeyboardButton('رموز', callback_data='pass'), InlineKeyboardButton('ارقام', callback_data='num')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
            elif call.data == 'pass':
                bot.edit_message_text('''
                    ———————×———————
                    - 𖣨 ، ෴ ، 𖡺  ، 𖣐 ، ✜ ، ✘ ، 𖡻 ،
                    - ༄ ، ༺༻ ، ༽༼ ،  ╰☆╮،  
                    - ɵ̷᷄ˬɵ̷᷅ ، ‏⠉̮⃝ ، ࿇࿆ ، ꔚ، ま ، ☓ ،
                    {𓆉 . 𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱 . 𓅓 . 𐂃  . ꕥ  . ⌘ . ♾ .    ꙰  .  . ᤑ .  ﾂ .
                    ———————×———————
                    ✦ ,✫ ,✯, ✮ ,✭ ,✰, ✬ ,✧, ✤, ❅ , 𒀭,✵ , ✶ , ✷ , ✸ , ✹ ,⧫, . 𐂂 }
                    -〘 𖢐 ، 𒍦 ، 𒍧 ، 𖢣 ، 𝁫 ، 𒍭 ، 𝁅 ، 𝁴 ، 𒍮 ، 𝁵 ، 𝀄 ، 𓏶 ، 𓏧 ، 𓏷 ، 𓏯 ، 𓏴 ، 𓏳 ، 𓏬 ، 𓏦 ، 𓏵 ، 𓏱 ، ᳱ ، ᯼ ، 𐃕 ، ᯥ ، ᯤ ، ᯾ ، ᳶ ، ᯌ ، ᢆ ،
                    ᥦ ، ᨙ ، ᨚ  ، ᨔ  ، ⏢ ، ⍨ ، ⍃ ، ⏃ ، ⍦ ، ⏕ ، ⏤ ، ⏁ ، ⏂ ، ⏆ ، ⌳ ، ࿅ ، ࿕ ، ࿇ ، ᚙ ، ࿊ ، ࿈ ، ྿ ،
                    ࿂ ، ࿑ ،  ᛥ ، ࿄ ، 𐀁 ، 𐀪 ، 𐀔 ، 𐀴 ، 𐀤 ، 𐀦 ، 𐀂 ، 𐀣 ، 𐀢 ، 𐀶 ، 𐀷 ، 𐂭 ، 𐂦 ، 𐂐 ، 𐂅 ، 𐂡 ، 𐂢 ، 𐂠 ، 𐂓 ، 𐂑 ، 𐃸 ، 𐃶 ، 𐂴 ، 𐃭 ، 𐃳 ، 𐃣 ، 𐂰 ، 𐃟 ، 𐃐 ، 𐃙 ، 𐃀 ، 𐇮 ، 𐇹 ، 𐇲 ، 𐇩 ، 𐇪 ، 𐇶 ، 𐇻 ، 𐇡 ، 𐇸 ، 𐇣 ، 𐇤 ، 𐎅 ، 𐏍 ، 𐎃 ، 𐏒 ، 𐎄 ، 𐏕 〙.
                    ╔ ╗. 𓌹  𓌺 .〝  〞. ‹ ›  .「  」. ‌‏𓂄‏ ‌‌‏𓂁
                    〖 〗. 《》 .  < > . « »  . ﹄﹃
                    ———————×———————
                    𓅄𓅅𓅆𓅇𓅈𓅉𓅊𓅋𓅌𓅍𓅎𓅏𓅐𓅑𓅒𓅓𓅔𓅕𓅖𓅗𓅘𓅙𓅚𓅛𓅜𓅝𓅞𓅟𓅠𓅡𓅢𓅣𓅤𓅥𓅦𓅧𓅨𓅩𓅫𓅬𓅭𓅮𓅯𓅰𓅱𓅲𓅳𓅴‏𓅵𓅶𓅷𓅸𓅹𓅺𓅻☤𓅾𓅿𓆀𓆁𓆂‏𓀀𓀁𓀂𓀃𓀄𓀅𓀆𓀇𓀈𓀉𓀊𓀋𓀌𓀍𓀎𓀏𓀐𓀑𓀒𓀓𓀔𓀕𓀖𓀗𓀘𓀙𓀚𓀛𓀜𓀝𓀞𓀟𓀠𓀡𓀢𓀣𓀤𓀥𓀦𓀧𓀨𓀩𓀪𓀫𓀬𓀭𓀮𓀯𓀰𓀱𓀲𓀳𓀴𓀵𓀶𓀷𓀸𓀹𓀺𓀻𓀼𓀽𓀾𓀿𓁀𓁁𓁂𓁃𓁄𓁅𓁆𓁇𓁈𓁉𓁊𓁋𓁌𓁍𓁎𓁏𓁐𓁑𓁒𓁓𓁔𓁕𓁖𓁗𓁘𓁙𓁚𓁛𓁜𓁝𓁞𓁟𓁠𓁡𓁢𓁣𓁤𓁥𓁦𓁧𓁨𓁩𓁪𓁫𓁬𓁭𓁮𓁯𓁰𓁱𓁲𓁳𓁴𓁵𓁶𓁷𓁸𓁹𓁺𓁻𓁼𓁽𓁾𓁿𓂀𓂅𓂆𓂇𓂈𓂉𓂊𓂋𓂌𓂍𓂎𓂏𓂐𓂑𓂒𓂓𓂔𓂕𓂖𓂗𓂘𓂙𓂚𓂛𓂜𓂝𓂞𓂟𓂠𓂡𓂢𓂣𓂤𓂥𓂦𓂧𓂨𓂩𓂪𓂫𓂬𓂭𓂮𓂯𓂰𓂱𓂲𓂳𓂴𓂵𓂶𓂷𓂸𓂺𓂻𓂼𓂽𓂾𓂿𓃀𓃁𓃂𓃃𓃅𓃆𓃇𓃈𓃉𓃊𓃋𓃌𓃍𓃎𓃏𓃐𓃑𓃒𓃓𓃔𓃕𓃖𓃗𓃘𓃙𓃚𓃛𓃜𓃝𓃞𓃟𓃠𓃡𓃢𓃣𓃤𓃥𓃦𓃧𓃨𓃩𓃪𓃫𓃬𓃭𓃮𓃯𓃰𓃱𓃲𓃳𓃴𓃵𓃶𓃷𓃸𓃹𓃺𓃻𓃼𓃽𓃾𓃿𓄀𓄁𓄂𓄃𓄄𓄅𓄆𓄇𓄈𓄉𓄊𓄋𓄌𓄍𓄎𓄏𓄐𓄑𓄒𓄓𓄔𓄕𓄖𓄙𓄚𓄛𓄜𓄝𓄞𓄟𓄠𓄡𓄢𓄣𓄤𓄥𓄦𓄧𓄨𓄩𓄪𓄫𓄬𓄭𓄮𓄯𓄰𓄱𓄲𓄳𓄴𓄵𓄶𓄷𓄸𓄹𓄺𓄼𓄽𓄾𓄿𓅀𓅁𓅂𓅃𓏕𓏖𓏗𓏘𓏙𓏚𓏛𓏜𓏝𓏞𓏟𓏠𓏡𓏢𓏣𓏤𓏥𓏦𓏧𓏨𓏩𓏪𓏫𓏬𓏭𓏮𓏯𓏰𓏱𓏲𓏳𓏴𓏶𓏷𓏸𓏹𓏺𓏻𓏼𓏽𓏾𓏿𓐀𓐁𓐂𓐃𓐄𓐅𓐆
                    ———————×———————''', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('الصفحة الرئيسية', callback_data='home')], [InlineKeyboardButton('رموز', callback_data='pass'), InlineKeyboardButton('ارقام', callback_data='num')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
            elif call.data == 'num':
                bot.edit_message_text('''
                    ———————×———————
                    ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀
                    𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 𝟖 𝟗 𝟎
                    𝟭 𝟮 𝟯 𝟰 𝟱 𝟲 𝟳 𝟴 𝟵 𝟬
                    ①②③④⑤⑥⑦⑧⑨⓪
                    ❶❷❸❹❺❻❼❽❾⓿
                    ⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴
                    ———————×———————
                    𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾  𝟿
                    ? 𝟙  𝟚  𝟛  𝟜  𝟝  𝟞  𝟟  𝟠 𝟡
                    𝟬 𝟭  𝟮  𝟯  𝟰  𝟱   𝟲  𝟳  𝟴  𝟵  
                    𝟎  𝟏  𝟐  𝟑  𝟒   𝟓   𝟔  𝟕   𝟖   𝟗
                    ０ １ ２ ３ ４ ５ ６ ７８９
                    ———————×———————''', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('الصفحة الرئيسية', callback_data='home')], [InlineKeyboardButton('رموز', callback_data='pass'), InlineKeyboardButton('ارقام', callback_data='num')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
            elif call.data == 'Name Completing':
                file = open('Name.json', 'r', encoding='utf8')
                array = json.load(file)
                bot.edit_message_text(array[Newton(0, len(array)-1)], call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                    'Newxt', callback_data='Name Completing'), InlineKeyboardButton('Home', callback_data='home')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
                file.close()
            elif call.data == 'Name PUBG':
                file = open('Name PUBG.json', 'r', encoding='utf8')
                array = json.load(file)
                bot.edit_message_text(array[Newton(0, len(
                    array)-1)], call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Newxt', callback_data='Name PUBG'), InlineKeyboardButton('Home', callback_data='home')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
                file.close()
            elif call.data == 'boyn':
                file = open('Boy.json', 'r', encoding='utf8')
                array = json.load(file)
                bot.edit_message_text(array[Newton(0, len(
                    array)-1)], call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Newxt', callback_data='boyn'), InlineKeyboardButton('Home', callback_data='home')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
                file.close()
            elif call.data == 'Shortcuts':
                file = open('Su.json', 'r', encoding='utf8')
                array = json.load(file)
                bot.edit_message_text(array[Newton(0, len(
                    array)-1)], call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Newxt', callback_data='Shortcuts'), InlineKeyboardButton('Home', callback_data='home')], [InlineKeyboardButton(NameChat, url='https://t.me/'+read('sudo')['CHAT'].replace('@', ''))]]))
                file.close()
            elif call.data == '%':
                x = Newton(0, 10)
                if x == 0:
                    bot.edit_message_text('ولله يا '+call.from_user.first_name +
                                          ' اخاف اكلك/ج نسبت الجمال صفر من عشره وتزعل', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 1:
                    bot.edit_message_text(
                        'حبي '+call.from_user.first_name+' جمال/ك/ج اعله من الصفر بواحد', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 2:
                    bot.edit_message_text('اف يا ' +
                                          call.from_user.first_name+' صلوات كمر بس النسبه ثنين من عشره', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 3:
                    bot.edit_message_text('شكلك/ج ' +
                                          call.from_user.first_name+' جمال/ك/ج 3 من 10', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 4:
                    bot.edit_message_text('اكل/ك/ج '+call.from_user.first_name +
                                          ' شني ام/ك/ج متنسيه بفاصوليه وطلعت اشو لا انت من الصاكين ولا من الزرك يعني نسبتك 4 استعمل صابون ركي', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 5:
                    bot.edit_message_text('حياتي '+call.from_user.first_name +
                                          ' انت ازرك عله ابيض يعني رب العالمين خلقك حته يحبوك لزرك ولبيض نسبتك 5 من 10 ', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 6:
                    bot.edit_message_text('هاي شنو ول/ك/ج ' +
                                          call.from_user.first_name+' عابر منطقت الزروكيه يعني 6 من 10', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 7:
                    bot.edit_message_text('هاي شنو ول/ك/ج ' +
                                          call.from_user.first_name+' عابر منطقت الزروكيه يعني 7 من 10', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 8:
                    bot.edit_message_text(call.from_user.first_name +
                                          ' انت يا حلو جمال/ك/ج جمال بزون يعني 8 من 10 فديت ولله', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 9:
                    bot.edit_message_text(
                        call.from_user.first_name+' انت كمر ولله كمر 9 من 10', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
                elif x == 10:
                    bot.edit_message_text(call.from_user.first_name +
                                          ' يحلو ياأبو عيون سود ولله لكعدلك عله الدرب كعود نسبتك 10 من 10 الله يحفظك ويرزقك بالي مثلك بس بتكم الي ', call.from_user.id, call.message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('القائمة الرئيسية', callback_data='home')]]))
    except Exception as e:
        bot.send_message(read('sudo')['ID_SUDO'], e)


@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
    if GetNewton('https://api.telegram.org/bot'+TOKIN+'/getChatMember?chat_id='+read('sudo')['CHAT']+'&user_id='+str(inline_query.from_user.id)).json()['result']['status'] == 'left':
        bot.answer_inline_query(inline_query.id, [InlineQueryResultArticle(1, '• اهلا بك '+inline_query.from_user.first_name+'، \n\n- في بوت الزخرفةالشامل؛\n\n- استخدام البوت عليك الاشتراك اولاً 🧸💕\n\n- قناة البوت  '+read('sudo')['CHAT']+' 💘🌈 \n\n\n-- -- -- -- - -- -- -- -- -- -- -- -- --',
                                InputTextMessageContent('• اهلا بك '+inline_query.from_user.first_name+'، \n\n- في بوت الزخرفةالشامل؛\n\n- استخدام البوت عليك الاشتراك اولاً 🧸💕\n\n- قناة البوت  '+read('sudo')['CHAT']+' 💘🌈 \n\n\n-- -- -- -- - -- -- -- -- -- -- -- -- --'))])
    else:
        msg = inline_query.query
        text = msg.lower()
        Newton1 = text.replace('a', 'Ａ').replace('b', 'Ｂ').replace('c', 'Ｃ').replace('d', 'Ｄ').replace('e', 'Ｅ').replace('f', 'Ｆ').replace('g', 'Ｇ').replace('h', 'Ｈ').replace('i', 'Ｉ').replace('j', 'Ｊ').replace('k', 'Ｋ').replace('l', 'Ｌ').replace('m', 'Ｍ').replace('n', 'Ｎ').replace('o', 'Ｏ').replace('p', 'Ｐ').replace('q', 'Ｑ').replace('r', 'Ｒ').replace('s', 'Ｓ').replace('t', 'Ｔ').replace('u', 'Ｕ').replace('v', 'Ｖ').replace('w', 'Ｗ').replace('x', 'Ｘ').replace('y', 'Ｙ').replace('z', 'Ｚ').replace('ا', 'آ').replace(
            'ب', 'ﭔ').replace('ت', 'ﭥ').replace('ث', 'ﺛ').replace('ج', 'چـ').replace('ح', 'ﺢـ').replace('خ', 'خـ').replace('د', 'ﮈ').replace('ذ', 'ڎ').replace('ر', 'ړ').replace('ز', 'ڒ').replace('س', 'سـّ').replace('ش', 'شًـ').replace('ص', 'ڝـ').replace('ض', 'ڞ').replace('ط', 'طـ').replace('ظ', 'ظـ').replace('ع', 'ﻋ').replace('غ', 'ﻏ').replace('ف', 'ڤـ').replace('ق', 'قـ').replace('ك', 'ﮗ').replace('ل', 'لْـ').replace('م', 'ﻤ').replace('ن', 'ﮢـ').replace('ه', 'ھ').replace('و', 'ۈ').replace('ي', 'ﭜ')
        Newton2 = text.replace('a', 'ａ').replace('b', 'ｂ').replace('c', 'ｃ').replace('d', 'ｄ').replace('e', 'ｅ').replace('f', 'ｆ').replace('g', 'ｇ').replace('h', 'ｈ').replace('i', 'ｉ').replace('j', 'ｊ').replace('k', 'ｋ').replace('l', 'ｌ').replace('m', 'ｍ').replace('n', 'ｎ').replace('o', 'ｏ').replace('p', 'ｐ').replace('q', 'ｑ').replace('r', 'ｒ').replace('s', 'ｓ').replace('t', 'ｔ').replace('u', 'ｕ').replace('v', 'ｖ').replace('w', 'ｗ').replace('x', 'ｘ').replace('y', 'ｙ').replace('z', 'ｚ').replace(
            'ا', 'ا').replace('ب', 'ﺑ').replace('ت', 'ﭠ').replace('ث', 'ﭥ').replace('ج', 'ﭴ').replace('ح', 'פ').replace('خ', 'ﺧ').replace('د', 'ﮃ').replace('ذ', 'ذ').replace('ر', 'ژ').replace('ز', 'ژ').replace('س', 'سـ').replace('ش', 'شـ').replace('ص', 'ﺻ').replace('ض', 'ﺿ').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'ﻋ').replace('غ', 'ﻏ̣̐').replace('ف', 'ﭬ').replace('ق', 'ﻗ̮ـ̃').replace('ك', 'ﮑ').replace('ل', 'ﻟ').replace('م', 'ﻣ̝̚').replace('ن', 'ﻧ').replace('ه', 'ھَہّ').replace('و', 'ۆ').replace('ي', 'ﯾ')
        Newton3 = text.replace('a', '𝐀').replace('b', '𝐁').replace('c', '𝐂').replace('d', '𝐃').replace('e', '𝐄').replace('f', '𝐅').replace('g', '𝐆').replace('h', '𝐇').replace('i', '𝐈').replace('j', '𝐉').replace('k', '𝐊').replace('l', '𝐋').replace('m', '𝐌').replace('n', '𝐍').replace('o', '𝐎').replace('p', '𝐏').replace('q', '𝐐').replace('r', '𝐑').replace('s', '𝐒').replace('t', '𝐓').replace('u', '𝐔').replace('v', '𝐕').replace('w', '𝐖').replace('x', '𝐗').replace('y', '𝐘').replace('z', '𝐙').replace('ا', 'اٌ').replace(
            'ب', 'بّـ').replace('ت', 'تْ').replace('ث', 'ثٌ').replace('ج', 'جِ').replace('ح', 'حٍ').replace('خ', 'خً').replace('د', 'دّ').replace('ذ', 'ذّ').replace('ر', 'رُ').replace('ز', 'زٍ').replace('س', 'سُ').replace('ش', 'شْ').replace('ص', 'صٍـ').replace('ض', 'ضُ').replace('ط', 'طً').replace('ظ', 'ظَ').replace('ع', 'عٍ').replace('غ', 'غَ').replace('ف', 'ّ').replace('ق', 'قْ').replace('ك', 'كُ').replace('ل', 'لِـ').replace('م', 'مِـ').replace('ن', 'ﻧَ').replace('ه', 'هٌ').replace('و', 'وِ').replace('ي', 'يٌـ')
        Newton4 = text.replace('a', '𝐚').replace('b', '𝐛').replace('c', '𝐜').replace('d', '𝐝').replace('e', '𝐞').replace('f', '𝐟').replace('g', '𝐠').replace('h', '𝐡').replace('i', '𝐢').replace('j', '𝐣').replace('k', '𝐤').replace('l', '𝐥').replace('m', '𝐦').replace('n', '𝐧').replace('o', '𝐨').replace('p', '𝐩').replace('q', '𝐪').replace('r', '𝐫').replace('s', '𝐬').replace('t', '𝐭').replace('u', '𝐮').replace('v', '𝐯').replace('w', '𝐰').replace('x', '𝐱').replace('y', '𝐲').replace('z', '𝐳').replace(
            'ا', 'ٱ').replace('ب', 'ﭜ').replace('ت', 'ﭤ').replace('ث', 'ﺛ').replace('ج', 'چ').replace('ح', 'ح').replace('خ', 'ڂـ').replace('د', 'ﮂ').replace('ذ', 'ڎ').replace('ر', 'ږ').replace('ز', 'ژ').replace('س', 'س').replace('ش', 'ش').replace('ص', 'ڝـ').replace('ض', 'ڞـ').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'عـ').replace('غ', 'ڠـ').replace('ف', 'ﭰ').replace('ق', 'ڦـ').replace('ك', 'ڪ').replace('ل', 'ڵـ').replace('م', 'مـ').replace('ن', 'ن').replace('ه', 'ھ').replace('و', 'ۅ').replace('ي', 'ﯾ̃')
        Newton5 = text.replace('a', '𝐴').replace('b', '𝐵').replace('c', '𝐶').replace('d', '𝐷').replace('e', '𝐸').replace('f', '𝐹').replace('g', '𝐺').replace('h', '𝐻').replace('i', '𝐼').replace('j', '𝐽').replace('k', '𝐾').replace('l', '𝐿').replace('m', '𝑀').replace('n', '𝑁').replace('o', '𝑂').replace('p', '𝑃').replace('q', '𝑄').replace('r', '𝑅').replace('s', '𝑆').replace('t', '𝑇').replace('u', '𝑈').replace('v', '𝑉').replace('w', '𝑊').replace('x', '𝑋').replace('y', '𝑌').replace('z', '𝑍').replace('ا', 'ﺂ̲').replace(
            'ب', 'بـ').replace('ت', 'ﺗ̲').replace('ث', 'ﭦ').replace('ج', 'ﺟ̅').replace('ح', 'حَ').replace('خ', 'خ').replace('د', 'ﺩ̲').replace('ذ', 'ذ').replace('ر', 'ږ').replace('ز', 'ژ').replace('س', 'ﺳ̲').replace('ش', 'ﺷ̲').replace('ص', 'ڝ').replace('ض', 'ض').replace('ط', 'ط').replace('ظ', 'ظ').replace('ع', 'ﻋ').replace('غ', 'غ').replace('ف', 'ﻓ̲').replace('ق', 'ق').replace('ك', 'ڳ').replace('ل', 'ﻟ̲').replace('م', 'ﻣ̲').replace('ن', 'ﻧ̲').replace('ه', 'ﮬ̲̌ﮧ').replace('و', 'ۆ').replace('ي', 'يے')
        Newton6 = text.replace('a', '𝑎').replace('b', '𝑏').replace('c', '𝑐').replace('d', '𝑑').replace('e', '𝑒').replace('f', '𝑓').replace('g', '𝑔').replace('h', 'ℎ').replace('i', '𝑖').replace('j', '𝑗').replace('k', '𝑘').replace('l', '𝑙').replace('m', '𝑚').replace('n', '𝑛').replace('o', '𝑜').replace('p', '𝑝').replace('q', '𝑞').replace('r', '𝑟').replace('s', '𝑠').replace('t', '𝑡').replace('u', '𝑢').replace('v', '𝑣').replace('w', '𝑤').replace('x', '𝑥').replace('y', '𝑦').replace('z', '𝑧').replace('ا', 'ٱ').replace(
            'ب', 'ﭓ').replace('ت', 'ٺ').replace('ث', 'ﺛ').replace('ج', 'ﭸ').replace('ح', 'ﺣ̭͠').replace('خ', 'ﺧ').replace('د', 'ﮃ').replace('ذ', 'ڈ').replace('ر', 'ڔ').replace('ز', 'ژ').replace('س', 'ﺳ̭͠').replace('ش', 'ﺷ͠').replace('ص', 'ﺼ').replace('ض', 'ض').replace('ط', 'طَ').replace('ظ', 'ڟ').replace('ع', 'ﻋ̝̚').replace('غ', 'ﻏ̣̐').replace('ف', 'ﻓ̲̣̐').replace('ق', 'ڨ').replace('ك', 'ﮖ').replace('ل', 'ڷ').replace('م', 'ﻣ̝̚').replace('ن', 'ڻ').replace('ه', 'ﮪ').replace('و', 'ۈ').replace('ي', 'ې')
        Newton7 = text.replace('a', '𝑨').replace('b', '𝑩').replace('c', '𝑪').replace('d', '𝑫').replace('e', '𝑬').replace('f', '𝑭').replace('g', '𝑮').replace('h', '𝑯').replace('i', '𝑰').replace('j', '𝑱').replace('k', '𝑲').replace('l', '𝑳').replace('m', '𝑴').replace('n', '𝑵').replace('o', '𝑶').replace('p', '𝑷').replace('q', '𝑸').replace('r', '𝑹').replace('s', '𝑺').replace('t', '𝑻').replace('u', '𝑼').replace('v', '𝑽').replace('w', '𝑾').replace('x', '𝑿').replace('y', '𝒀').replace('z', '𝒁').replace('ا', 'آ').replace(
            'ب', 'بِ').replace('ت', 'تْ').replace('ث', 'ثٌ').replace('ج', 'جَ').replace('ح', 'حْ').replace('خ', 'خِ').replace('د', 'دِ').replace('ذ', 'ڐ').replace('ر', 'رَ').replace('ز', 'زَ').replace('س', 'سُ').replace('ش', 'شٌ').replace('ص', 'صَ').replace('ض', 'ڞ').replace('ط', 'طٌ').replace('ظ', 'ظْ').replace('ع', 'عَ').replace('غ', 'غّ').replace('ف', 'فْ').replace('ق', 'قِ').replace('ك', 'ﻛَ').replace('ل', 'لَ').replace('م', 'مـَ').replace('ن', 'نّ').replace('خ', 'ﮩ').replace('و', 'ۄ').replace('ي', 'يْ')
        Newton8 = text.replace('a', '𝒂').replace('b', '𝒃').replace('c', '𝒄').replace('d', '𝒅').replace('e', '𝒆').replace('f', '𝒇').replace('g', '𝒈').replace('h', '𝒉').replace('i', '𝒊').replace('j', '𝒋').replace('k', '𝒌').replace('l', '𝒍').replace('m', '𝒎').replace('n', '𝒏').replace('o', '𝒐').replace('p', '𝒑').replace('q', '𝒒').replace('r', '𝒓').replace('s', '𝒔').replace('t', '𝒕').replace('u', '𝒖').replace('v', '𝒗').replace('w', '𝒘').replace('x', '𝒙').replace('y', '𝒚').replace('z', '𝒛').replace('ا', 'آ').replace('ب', 'بٍّ').replace(
            'ت', 'تٍّ').replace('ث', 'ثٍّ').replace('ج', 'جِّ').replace('ح', 'حَّ').replace('خ', 'خِّ').replace('د', 'دٍّ').replace('ذ', 'ذ').replace('ر', 'رِ').replace('ز', 'زٍّ').replace('س', 'سَّ').replace('ش', 'شِّ').replace('ص', 'صِّ').replace('ض', 'ِّضِّ').replace('ط', 'طِّ').replace('ظ', 'ظِّ').replace('ع', 'عَّ').replace('غ', 'غَّ').replace('ف', 'فٍّ').replace('ق', 'قٍّ').replace('ك', 'ﮝ').replace('ل', 'لِّ').replace('م', 'مِّ').replace('ن', 'نِّ').replace('ه', 'هِّ').replace('و', 'وٍّ').replace('ي', 'يِّ')
        Newton9 = text.replace('a', '𝒶').replace('b', '𝒷').replace('c', '𝒸').replace('d', '𝒹').replace('e', '𝓮').replace('f', '𝒻').replace('g', '𝓰').replace('h', '𝒽').replace('i', '𝒾').replace('j', '𝒿').replace('k', '𝓀').replace('l', '𝓁').replace('m', '𝓂').replace('n', '𝓃').replace('p', '𝓅').replace('q', '𝓆').replace('r', '𝓇').replace('s', '𝓈').replace('t', '𝓉').replace('u', '𝓊').replace('w', '𝓌').replace('x', '𝓍').replace('y', '𝓎').replace('z', '𝓏').replace('ا', 'ﺂ̣̥̐').replace('ب', 'بّ').replace(
            'ت', 'تٌ').replace('ث', 'ثّـ').replace('ج', 'جّـ').replace('ح', 'حّـ').replace('خ', 'خـّ').replace('د', 'دّ').replace('ذ', 'ﮅ').replace('ر', 'رّ').replace('ز', 'ڗ').replace('س', 'ﺳ̶').replace('ش', 'ﺷ͠').replace('ص', 'صْـ').replace('ض', 'ضّـ').replace('ط', 'طِّ').replace('ظ', 'ظَّ').replace('ع', 'ﻋ̝̚').replace('غ', 'ﻏ̣̐').replace('ف', 'فّـ').replace('ق', 'قّـ').replace('ك', 'ﮗ').replace('ل', 'ﻟ̣̣').replace('م', 'ﻣ̝̚').replace('ن', 'نّ').replace('ه', 'ﮪ').replace('و', 'ۊ').replace('ي', 'ې')
        Newton10 = text.replace('a', '𝓐').replace('b', '𝓑').replace('c', '𝓒').replace('d', '𝓓').replace('e', '𝓔').replace('f', '𝓕').replace('g', '𝓖').replace('h', '𝓗').replace('i', '𝓘').replace('j', '𝓙').replace('k', '𝓚').replace('l', '𝓛').replace('m', '𝓜').replace('n', '𝓝').replace('o', '𝓞').replace('p', '𝓟').replace('q', '𝓠').replace('r', '𝓡').replace('s', '𝓢').replace('t', '𝓣').replace('u', '𝓤').replace('v', '𝓥').replace('w', '𝓦').replace('x', '𝓧').replace('y', '𝓨').replace('z', '𝓩').replace('ا', 'اّ').replace(
            'ب', 'بّ').replace('ت', 'تّ').replace('ث', 'ثّ').replace('ج', 'جّ').replace('ح', 'حّ').replace('خ', 'خّ').replace('د', 'دّ').replace('ذ', 'ذ').replace('ر', 'رّ').replace('ز', 'زّ').replace('س', 'سّ').replace('ش', 'شّ').replace('ص', 'صّ').replace('ض', 'ّضّ').replace('ط', 'طّ').replace('ظ', 'ظّ').replace('ع', 'عّ').replace('غ', 'غّ').replace('ف', 'فّ').replace('ق', 'قّ').replace('ك', 'كّ').replace('ل', 'لّ').replace('م', 'مّ').replace('ن', 'نّ').replace('ه', 'هّ').replace('و', 'وّ').replace('ي', 'يّ')
        Newton11 = text.replace('a', '𝓪').replace('b', '𝓫').replace('c', '𝓬').replace('d', '𝓭').replace('e', '𝓮').replace('f', '𝓯').replace('g', '𝓰').replace('h', '𝓱').replace('i', '𝓲').replace('j', '𝓳').replace('k', '𝓴').replace('l', '𝓵').replace('m', '𝓶').replace('n', '𝓷').replace('o', '𝓸').replace('p', '𝓹').replace('q', '𝓺').replace('r', '𝓻').replace('s', '𝓼').replace('t', '𝓽').replace('u', '𝓾').replace('v', '𝓿').replace('w', '𝔀').replace('x', '𝔁').replace('y', '𝔂').replace('z', '𝔃').replace('ا', 'اٍّ').replace(
            'ب', 'بّْ').replace('ت', 'تُّ').replace('ث', 'ثّْ').replace('ج', 'جٍّ').replace('ح', 'حّْ').replace('خ', 'خٌّ').replace('د', 'دٌّ').replace('ذ', 'ذ').replace('ر', 'رًّ').replace('ز', 'زَ').replace('س', 'سًّ').replace('ش', 'شّْ').replace('ص', 'صُّ').replace('ض', 'ُْضَّ').replace('ط', 'طَّ').replace('ظ', 'ظُ').replace('ع', 'عَّ').replace('غ', 'غٌّ').replace('ف', 'فّْ').replace('ق', 'قِّ').replace('ك', 'كّْ').replace('ل', 'لَّ').replace('م', 'مُّ').replace('ن', 'نِّ').replace('ه', 'هّْ').replace('و', 'وّ').replace('ي', 'يٌّ')
        Newton12 = text.replace('a', '𝔞').replace('b', '𝔟').replace('c', '𝔠').replace('d', '𝔡').replace('e', '𝔢').replace('f', '𝔣').replace('g', '𝔤').replace('h', '𝔥').replace('i', '𝔦').replace('j', '𝔧').replace('k', '𝔨').replace('l', '𝔩').replace('m', '𝔪').replace('n', '𝔫').replace('o', '𝔬').replace('p', '𝔭').replace('q', '𝔮').replace('r', '𝔯').replace('s', '𝔰').replace('t', '𝔱').replace('u', '𝔲').replace('v', '𝔳').replace('w', '𝔴').replace('x', '𝔵').replace('y', '𝔶').replace('z', '𝔷').replace('ا', 'آ').replace(
            'ب', 'بْ').replace('ت', 'تْ').replace('ث', 'ثْ').replace('ج', 'جْ').replace('ح', 'حْ').replace('خ', 'خْ').replace('د', 'دْ').replace('ذ', 'ذْ').replace('ر', 'رْ').replace('و', 'زْ').replace('س', 'سْ').replace('ش', 'شْ').replace('ص', 'صْ').replace('ض', 'ضْ').replace('ط', 'طْ').replace('ظ', 'ظْ').replace('ع', 'عْ').replace('غ', 'غْ').replace('ف', 'فْ').replace('ق', 'قْ').replace('ك', 'ڪْ').replace('ل', 'لْ').replace('م', 'مْ').replace('ن', 'نْ').replace('ه', 'ﮬ̲̣̐').replace('و', 'وْ').replace('ي', 'يْ')
        Newton13 = text.replace('a', '𝔸').replace('c', 'ℂ').replace('b', '𝔹').replace('d', '𝔻').replace('e', '𝔼').replace('f', '𝔽').replace('g', '𝔾').replace('h', 'ℍ ').replace('i', '𝕀').replace('j', '𝕁').replace('k', '𝕂').replace('l', '𝕃').replace('m', '𝕄').replace('n', 'ℕ').replace('o', '𝕆').replace('p', 'ℙ').replace('q', 'ℚ').replace('r', 'ℝ').replace('s', '𝕊').replace('t', '𝕋').replace('u', '𝕌').replace('v', '𝕍').replace('w', '𝕎').replace('x', '𝕏').replace('y', '𝕐').replace('z', 'ℤ').replace('ا', 'اَ').replace(
            'ب', 'بَ').replace('ت', 'تَ').replace('ث', 'ثَ').replace('ج', 'جَ').replace('ح', 'حَ').replace('خ', 'خَ').replace('د', 'دَ').replace('ذ', 'ذ').replace('ر', 'رَ').replace('ز', 'زَّ').replace('س', 'سَ').replace('ش', 'شَ').replace('ص', 'صَ').replace('ض', 'َضَ').replace('ط', 'طَ').replace('ظ', 'ظَ').replace('ع', 'عَ').replace('غ', 'غَ').replace('ف', 'فَ').replace('ق', 'قَ').replace('ك', 'كَ').replace('ل', 'لَ').replace('م', 'مَ').replace('ن', 'نَ').replace('ه', 'هَ').replace('و', 'وًّ').replace('ي', 'يَ')
        Newton14 = text.replace('a', '𝕒').replace('b', '𝕓').replace('c', '𝕔').replace('d', '𝕕').replace('e', '𝕖').replace('f', '𝕗').replace('g', '𝕘').replace('h', '𝕙').replace('i', '𝕚').replace('j', '𝕛').replace('k', '𝕜').replace('l', '𝕝').replace('m', '𝕞').replace('n', '𝕟').replace('o', '𝕠').replace('p', '𝕡').replace('q', '𝕢').replace('r', '𝕣').replace('s', '𝕤').replace('t', '𝕥').replace('u', '𝕦').replace('v', '𝕧').replace('w', '𝕨').replace('x', '𝕩').replace('y', '𝕪').replace('z', '𝕫').replace('ا', 'ּٵ̍').replace('ب', 'بــ').replace(
            'ت', 'ּۛٺــ').replace('ث', 'ۖٽــ').replace('ج', 'ּۛڇۚــ').replace('ح', 'ּحۡــ').replace('خ', 'ۖڅۡــ').replace('د', 'ۖد').replace('ذ', 'ذ').replace('ر', 'ڔ').replace('ز', 'ۖڙ').replace('س', 'ڛۜــ').replace('ش', 'ּڜــ').replace('ص', 'ּڝــ').replace('ض', 'ڞــ').replace('ط', 'ּٹــ').replace('ظ', 'ڟــ').replace('ع', 'ۖ؏ــ').replace('غ', 'ۖڠــ').replace('ف', 'ּۛڣــ').replace('ق', 'ּۛڦــ').replace('ك', 'ڪــ').replace('ل', 'ּڷــ').replace('م', 'ּمۭــ').replace('ن', 'ۖنۨــ').replace('ه', 'هــ').replace('و', 'ﯣ').replace('ي', 'ּيۧۗ')
        Newton15 = text.replace('a', '𝕬').replace('b', '𝕭').replace('c', '𝕮').replace('d', '𝕯').replace('e', '𝕰').replace('f', '𝕱').replace('g', '𝕲').replace('h', '𝕳').replace('i', '𝕴').replace('j', '𝕵').replace('k', '𝕶').replace('l', '𝕷').replace('m', '𝕸').replace('n', '𝕹').replace('o', '𝕺').replace('p', '𝕻').replace('q', '𝕼').replace('r', '𝕽').replace('s', '𝕾').replace('t', '𝕿').replace('u', '𝖀').replace('v', '𝖁').replace('w', '𝖂').replace('x', '𝖃').replace('y', '𝖄').replace('z', '𝖅').replace('ا', 'أ').replace(
            'ب', 'ب').replace('ت', 'تہ').replace('ث', 'ثہ').replace('ج', 'جہ').replace('ح', 'حہ').replace('خ', 'خہ').replace('د', 'د').replace('ذ', 'ذ').replace('ر', 'ر').replace('ز', 'ز').replace('س', 'سہ').replace('ش', 'شہ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طہ').replace('ظ', 'ظ').replace('ع', 'عہ').replace('غ', 'غہ').replace('ف', 'فُہ').replace('ق', 'ق').replace('ك', 'كُہ').replace('ل', 'لہ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هـ').replace('و', 'و').replace('ي', 'يہ')
        Newton16 = text.replace('a', '𝖆').replace('b', '𝖇').replace('c', '𝖈').replace('d', '𝖉').replace('e', '𝖊').replace('f', '𝖋').replace('g', '𝖌').replace('h', '𝖍').replace('i', '𝖎').replace('j', '𝖏').replace('k', '𝖐').replace('l', '𝖑').replace('m', '𝖒').replace('n', '𝖓').replace('o', '𝖔').replace('p', '𝖕').replace('q', '𝖖').replace('r', '𝖗').replace('s', '𝖘').replace('t', '𝖙').replace('u', '𝖚').replace('v', '𝖛').replace('w', '𝖜').replace('x', '𝖝').replace('y', '𝖞').replace('z', '𝖟').replace('ا', 'أ').replace(
            'ب', 'ب̷').replace('ت', 'ت̷').replace('ث', 'ث̷').replace('ج', 'ج̷').replace('ح', 'ح̷').replace('خ', 'خ̷').replace('د', 'د̷ِ').replace('ذ', 'ذ̷').replace('ر', 'ر̷').replace('ز', 'ز̷').replace('س', 'س̷').replace('ش', 'ش̷ُ').replace('ص', 'ص̷').replace('ض', 'ض').replace('ط', 'ط̷ُ').replace('ظ', 'ظ̷ً').replace('ع', 'ع̷ٍ').replace('غ', 'غ̷').replace('ف', 'ف̷َ').replace('ق', 'ق̷').replace('ك', 'گ̷').replace('ل', 'ل̷').replace('م', 'م̷').replace('ن', 'ن̷').replace('ي', 'ہ̷ـ').replace('و', 'ۆ̷').replace('ي', 'ي̷')
        Newton17 = text.replace('a', '𝖠').replace('b', '𝖡').replace('c', '𝖢').replace('d', '𝖣').replace('e', '𝖤').replace('f', '𝖥').replace('g', '𝖦').replace('h', '𝖧').replace('i', '𝖨').replace('j', '𝖩').replace('k', '𝖪').replace('l', '𝖫').replace('m', '𝖬').replace('n', '𝖭').replace('o', '𝖮').replace('p', '𝖯').replace('q', '𝖰').replace('r', '𝖱').replace('s', '𝖲').replace('t', '𝖳').replace('u', '𝖴').replace('v', '𝖵').replace('w', '𝖶').replace('x', '𝖷').replace('y', '𝖸').replace('z', '𝖹').replace('ا', 'أ').replace(
            'ب', 'ب͠').replace('ت', 'ت͠').replace('ث', 'ث͠').replace('ج', 'ج͠').replace('ح', 'ح͠').replace('خ', 'خ͠').replace('د', 'د͠').replace('ذ', 'ذ͠').replace('ر', 'ر').replace('ز', 'ز͠').replace('س', 'س͠').replace('ش', 'ش͠').replace('ص', 'ص͠').replace('ض', 'ض').replace('ط', 'ط͠').replace('ظ', 'ظ͠').replace('ع', 'ع͠').replace('غ', 'غ͠').replace('ف', 'ف͠').replace('ق', 'ق͠').replace('ك', 'گ͠').replace('ل', 'ل͠').replace('م', 'م͠').replace('ن', 'ن͠').replace('ه', 'ه͠ـ').replace('و', 'و͠').replace('ي', 'ي͠')
        Newton18 = text.replace('a', '𝖺').replace('b', '𝖻').replace('c', '𝖼').replace('d', '𝖽').replace('e', '𝖾').replace('f', '𝖿').replace('g', '𝗀').replace('h', '𝗁').replace('i', '𝗂').replace('j', '𝗃').replace('k', '𝗄').replace('l', '𝗅').replace('m', '𝗆').replace('n', '𝗇').replace('o', '𝗈').replace('p', '𝗉').replace('q', '𝗊').replace('r', '𝗋').replace('s', '𝗌').replace('t', '𝗍').replace('u', '𝗎').replace('v', '𝗏').replace('w', '𝗐').replace('x', '𝗑').replace('y', '𝗒').replace('z', '𝗓').replace('ا', 'أ').replace(
            'ب', 'بَ').replace('ت', 'ت').replace('ث', 'ث').replace('ج', 'جٍ').replace('ح', 'حٍ').replace('خ', 'خـ').replace('د', 'دِ').replace('ذ', 'ذَ').replace('ر', 'رٍ').replace('ز', 'زْ').replace('س', 'س').replace('ش', 'شُ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طُ').replace('ظ', 'ظً').replace('ع', 'عٍ').replace('غ', 'غ').replace('ف', 'فُ').replace('ق', 'قٌ').replace('ك', 'ڪ').replace('ل', 'لُِ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هــ').replace('و', 'وُ').replace('ي', 'ي')
        Newton19 = text.replace('a', '𝗔').replace('b', '𝗕').replace('c', '𝗖').replace('d', '𝗗').replace('e', '𝗘').replace('f', '𝗙').replace('g', '𝗚').replace('h', '𝗛').replace('l', '𝗜').replace('j', '𝗝').replace('x', '𝗞').replace('l', '𝗟').replace('m', '𝗠').replace('n', '𝗡').replace('o', '𝗢').replace('p', '𝗣').replace('q', '𝗤').replace('r', '𝗥').replace('s', '𝗦').replace('t', '𝗧').replace('u', '𝗨').replace('v', '𝗩').replace('w', '𝗪').replace('x', '𝗫').replace('y', '𝗬').replace('z', '𝗭').replace('ا', 'أ').replace(
            'ب', 'بٰٰ').replace('ت', 'تہٰ').replace('ث', 'ثہٰـ').replace('ج', 'ج').replace('ح', 'حہٰ').replace('خ', 'خ').replace('د', 'د').replace('ذ', 'ذ').replace('ر', 'ر').replace('ز', 'ز').replace('س', 'سہٰ').replace('ش', 'ش').replace('ص', 'صہٰ').replace('ض', 'ض').replace('ط', 'طہٰ').replace('ظ', 'ظ').replace('ع', 'ع').replace('غ', 'غ').replace('ف', 'فہٰ').replace('ق', 'ق').replace('ك', 'كہٰ').replace('ل', 'لہٰ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هـ').replace('و', 'و').replace('ي', 'يٰ')
        Newton20 = text.replace('a', '𝗮').replace('b', '𝗯').replace('c', '𝗰').replace('d', '𝗱').replace('e', '𝗲').replace('f', '𝗳').replace('g', '𝗴').replace('h', '𝗵').replace('i', '𝗶').replace('j', '𝗷').replace('k', '𝗸').replace('l', '𝗹').replace('m', '𝗺').replace('n', '𝗻').replace('o', '𝗼').replace('p', '𝗽').replace('q', '𝗾').replace('r', '𝗿').replace('s', '𝘀').replace('t', '𝘁').replace('u', '𝘂').replace('v', '𝘃').replace('w', '𝘄').replace('x', '𝘅').replace('y', '𝘆').replace('z', '𝘇').replace('ا', 'أ').replace(
            'ب', 'بَ').replace('ت', 'ت').replace('ث', 'ث').replace('ج', 'جٍ').replace('ح', 'حٍ').replace('خ', 'خـ').replace('د', 'دِ').replace('ذ', 'ذَ').replace('ر', 'رٍ').replace('ز', 'زْ').replace('س', 'س').replace('ش', 'شُ').replace('ص', 'ص').replace('ض', 'ض').replace('ط', 'طُ').replace('ظ', 'ظً').replace('ع', 'عٍ').replace('غ', 'غ').replace('ف', 'فُ').replace('ق', 'قٌ').replace('ك', 'ڪ').replace('ل', 'لُِ').replace('م', 'م').replace('ن', 'ن').replace('ه', 'هــ').replace('و', 'وُ').replace('ي', 'ي')
        try:
            r1 = InlineQueryResultArticle(1, NewtonBows(
                Newton1)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton1)+NewtonShapes()))
            r2 = InlineQueryResultArticle(2, NewtonBows(
                Newton2)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton2)+NewtonShapes()))
            r3 = InlineQueryResultArticle(3, NewtonBows(
                Newton3)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton3)+NewtonShapes()))
            r4 = InlineQueryResultArticle(4, NewtonBows(
                Newton4)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton4)+NewtonShapes()))
            r5 = InlineQueryResultArticle(5, NewtonBows(
                Newton5)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton5)+NewtonShapes()))
            r6 = InlineQueryResultArticle(6, NewtonBows(
                Newton6)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton6)+NewtonShapes()))
            r7 = InlineQueryResultArticle(7, NewtonBows(
                Newton7)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton7)+NewtonShapes()))
            r8 = InlineQueryResultArticle(8, NewtonBows(
                Newton8)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton8)+NewtonShapes()))
            r9 = InlineQueryResultArticle(9, NewtonBows(
                Newton9)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton9)+NewtonShapes()))
            r10 = InlineQueryResultArticle(10, NewtonBows(
                Newton10)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton10)+NewtonShapes()))
            r11 = InlineQueryResultArticle(11, NewtonBows(
                Newton11)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton11)+NewtonShapes()))
            r12 = InlineQueryResultArticle(12, NewtonBows(
                Newton12)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton12)+NewtonShapes()))
            r13 = InlineQueryResultArticle(13, NewtonBows(
                Newton13)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton13)+NewtonShapes()))
            r14 = InlineQueryResultArticle(14, NewtonBows(
                Newton14)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton14)+NewtonShapes()))
            r15 = InlineQueryResultArticle(15, NewtonBows(
                Newton15)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton15)+NewtonShapes()))
            r16 = InlineQueryResultArticle(16, NewtonBows(
                Newton16)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton16)+NewtonShapes()))
            r17 = InlineQueryResultArticle(17, NewtonBows(
                Newton17)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton17)+NewtonShapes()))
            r18 = InlineQueryResultArticle(18, NewtonBows(
                Newton18)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton18)+NewtonShapes()))
            r19 = InlineQueryResultArticle(19, NewtonBows(
                Newton19)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton19)+NewtonShapes()))
            r20 = InlineQueryResultArticle(20, NewtonBows(
                Newton20)+NewtonShapes(), InputTextMessageContent(NewtonBows(Newton20)+NewtonShapes()))
            bot.answer_inline_query(inline_query.id, [
                                    r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20])
        except Exception as e:
            bot.send_message(read('sudo')['ID_SUDO'], e)

try:
    bot.polling(none_stop=False)
except Exception as e:
    print(e)
