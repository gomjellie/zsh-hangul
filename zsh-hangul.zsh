echo "zeh-hangul loaded"

autoload -Uz _convert_gksdud

typeset -A gksdud # key map for korean-english 2-set array(a.k.a. 두벌식 자판)
gksdud[ㅂ]="q"
gksdud[ㅈ]="w"
gksdud[ㄷ]="e"
gksdud[ㄱ]="r"
gksdud[ㅅ]="t"
gksdud[ㅛ]="y"
gksdud[ㅕ]="u"
gksdud[ㅑ]="i"
gksdud[ㅐ]="o"
gksdud[ㅔ]="p"

gksdud[ㅁ]="a"
gksdud[ㄴ]="s"
gksdud[ㅇ]="d"
gksdud[ㄹ]="f"
gksdud[ㅎ]="g"
gksdud[ㅗ]="h"
gksdud[ㅓ]="j"
gksdud[ㅏ]="k"
gksdud[ㅣ]="l"

gksdud[ㅋ]="z"
gksdud[ㅌ]="x"
gksdud[ㅊ]="c"
gksdud[ㅍ]="v"
gksdud[ㅠ]="b"
gksdud[ㅜ]="n"
gksdud[ㅡ]="m"

_convert_gksdud() {
    # widget to convert korean -> english
    BUFFER="${LBUFFER}${gksdud[${KEYS}]}${RBUFFER}"
    CURSOR+=1
}

zle -N _convert_gksdud

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done
