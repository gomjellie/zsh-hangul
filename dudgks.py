"""
Reference

https://github.com/ChalkPE/gksdud
"""
import sys
import re

INITIAL = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
MEDIAL = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
FINAL = [None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
ZI = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
MU = MEDIAL

ALPHABETS = 'qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM'
HANGEUL_JAMOS = 'ㅂㅃㅈㅉㄷㄸㄱㄲㅅㅆㅛㅛㅕㅕㅑㅑㅐㅒㅔㅖㅁㅁㄴㄴㅇㅇㄹㄹㅎㅎㅗㅗㅓㅓㅏㅏㅣㅣㅋㅋㅌㅌㅊㅊㅍㅍㅠㅠㅜㅜㅡㅡ'
KOR_REGEX = re.compile("([ㄱㄲㄴㄷ-ㄹㅁ-ㅃㅅ-ㅎ])([ㅏ-ㅖㅛㅠㅣ]|ㅗ[ㅏㅐㅣ]?|ㅜ[ㅓㅔㅣ]?|ㅡㅣ?)(?:([ㄲㄷㅁㅅ-ㅈㅊ-ㅎ]|ㄱㅅ?|ㄴ[ㅈㅎ]?|ㄹ[ㄱㅁㅂㅅㅌ-ㅎ]?|ㅂㅅ?)(?![ㅏ-ㅣ]))?")
COMPLEX = { 'ㅗㅏ': 'ㅘ', 'ㅗㅐ': 'ㅙ', 'ㅗㅣ': 'ㅚ', 'ㅜㅓ': 'ㅝ', 'ㅜㅔ': 'ㅞ', 'ㅜㅣ': 'ㅟ', 'ㅡㅣ': 'ㅢ', 'ㄱㅅ': 'ㄳ', 'ㄴㅈ': 'ㄵ', 'ㄴㅎ': 'ㄶ', 'ㄹㄱ': 'ㄺ', 'ㄹㅁ': 'ㄻ', 'ㄹㅂ': 'ㄼ', 'ㄹㅅ': 'ㄽ', 'ㄹㅌ': 'ㄾ', 'ㄹㅍ': 'ㄿ', 'ㄹㅎ': 'ㅀ', 'ㅂㅅ': 'ㅄ' }


def combine(chars):
    """
    ["ㅎ", "ㅏ", "ㄴ"] => "한"
    ["ㄱ", "ㅡ", "ㄹ"] => "글"
    """

    if chars[1] in COMPLEX:
        chars[1] = COMPLEX[chars[1]]
    if chars[2] in COMPLEX:
        chars[2] = COMPLEX[chars[2]]

    return chr(INITIAL.index(chars[0]) * 588 + MEDIAL.index(chars[1]) * 28 + FINAL.index(chars[2]) + 44032)


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
    return [INITIAL[ch1], MEDIAL[ch2], FINAL[ch3]]

def dudgks(dud):
    """
    dudgks -> 영한
    """
    cracked_korean = ""
    for _dud in dud:
        # dudgks -> ㅇㅕㅇㅎㅏㄴ
        if _dud not in ALPHABETS:
            continue
        cracked_korean += HANGEUL_JAMOS[ALPHABETS.index(_dud)]

    divided_koreans = KOR_REGEX.findall(cracked_korean)

    ret = ""
    for divided_korean in divided_koreans:
        ret += combine([None if d == '' else d for d in divided_korean])

    if ret == "":
        return cracked_korean

    return ret

if len(sys.argv) == 2:
    ret = ""
    param = sys.argv[1].strip()
    if param[0] == "\"":
        param = param[1:]

    non_alphabetic_regex = re.compile("[^a-zA-Z]")
    non_alphabetics = non_alphabetic_regex.findall(param)
    non_alphabetics.append("")
    alphabetic_groups = non_alphabetic_regex.split(param)
    for idx in range(len(alphabetic_groups)):
        ret += dudgks(alphabetic_groups[idx]) + non_alphabetics[idx]
    print(ret)
