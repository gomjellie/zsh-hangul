"""
reference

https://frhyme.github.io/python/python_korean_englished
https://github.com/baehyunsol/korean_saying_generator

"""

initial = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
medial = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
final = [None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
zi = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
mo = medial

kor2eng = {
    # zi 자음
    'ㄱ': 'r',
    'ㄲ': 'R',
    'ㄳ': 'rt',
    'ㄴ': 's',
    'ㄵ': 'sw',
    'ㄶ': 'sg', 
    'ㄷ': 'e',
    'ㄸ': 'E',
    'ㄹ': 'f',
    'ㄺ': 'fr',
    'ㄻ': 'fa',
    'ㄼ': 'fq',
    'ㄽ': 'ft',
    'ㄾ': 'fx',
    'ㄿ': 'fv',
    'ㅀ': 'fg', 
    'ㅁ': 'a',
    'ㅂ': 'q',
    'ㅃ': 'Q',
    'ㅄ': 'qt',
    'ㅅ': 't',
    'ㅆ': 'T',
    'ㅇ': 'd',
    'ㅈ': 'w',
    'ㅉ': 'W',
    'ㅊ': 'c',
    'ㅋ': 'z',
    'ㅌ': 'x',
    'ㅍ': 'v',
    'ㅎ': 'g',

    # mo 모음
    'ㅏ': 'k',
    'ㅐ': 'o',
    'ㅑ': 'i',
    'ㅒ': 'O',
    'ㅓ': 'j',
    'ㅔ': 'p',
    'ㅕ': 'u',
    'ㅖ': 'P',
    'ㅗ': 'h',
    'ㅘ': 'hk',
    'ㅙ': 'ho',
    'ㅚ': 'hl',
    'ㅛ': 'y',
    'ㅜ': 'n',
    'ㅝ': 'nj',
    'ㅞ': 'np',
    'ㅟ': 'nl',
    'ㅠ': 'b',
    'ㅡ': 'm',
    'ㅢ': 'ml',
    'ㅣ': 'l',
}

def combine(chars):
    """
    ["ㅎ", "ㅏ", "ㄴ"] => "한"
    ["ㄱ", "ㅡ", "ㄹ"] => "글"
    """
    if len(chars) == 1:
        return chars[0]

    if len(chars) == 2:
        chars.append(None)
    
    return chr(initial.index(chars[0]) * 588 + medial.index(chars[1]) * 28 + final.index(chars[2]) + 44032)

def gksdud(chars):
    ret = []
    for char in chars:
        if char is None:
            continue
        ret.append(kor2eng[char])
    
    return ret

def split_gks(gks):
    """
    가 -> ['ㄱ', 'ㅏ']
    김 -> ['ㄱ', 'ㅣ', 'ㅁ']
    한 -> ['ㅎ', 'ㅏ', 'ㄴ']
    """
    if '가' > gks or gks > '힣':
        raise Exception("split_gks() got wrong parameter {}".format(gks))
    ## 588개 마다 초성이 바뀜. 
    ch1 = (ord(gks) - ord('가')) // 588
    ## 중성은 총 28가지 종류
    ch2 = ((ord(gks) - ord('가')) - (588 * ch1)) // 28
    ch3 = (ord(gks) - ord('가')) - (588 * ch1) - 28 * ch2
    return [initial[ch1], medial[ch2], final[ch3]]

def make_combinations():
    for _zi in zi:
        print('gksdud[{}]="{}"'.format(_zi, "".join(gksdud([_zi]))))
    
    for _mo in mo:
        print('gksdud[{}]="{}"'.format(_mo, "".join(gksdud([_mo]))))
        # print(_medial, "".join(gksdud([_medial])))

    for _initial in initial:
        for _medial in medial:
            res = combine([_initial, _medial])
            print('gksdud[{}]="{}"'.format(res, "".join(gksdud(split_gks(res)))))
    
    for _initial in initial:
        for _medial in medial:
            for _final in final:
                res = combine([_initial, _medial, _final])
                print('gksdud[{}]="{}"'.format(res, "".join(gksdud(split_gks(res)))))

print("typeset -A gksdud")

make_combinations()
