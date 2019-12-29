autoload -Uz _convert_gksdud
autoload -Uz _complete_dudgks

ZSH_HANGUL_DIR=$(dirname $0)

_convert_gksdud() {
    # widget to convert korean -> english
    BUFFER="${LBUFFER}${gksdud[${KEYS}]}${RBUFFER}"
    CURSOR+=${#gksdud[${KEYS}]}
}

_complete_dudgks() {
    res=$(python3 $ZSH_HANGUL_DIR/dudgks.py $words[$CURRENT])
    compadd -S "" -U -Q $res
    compcall -D
}

zle -N _convert_gksdud

zle -C _complete_dudgks menu-complete _complete_dudgks

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

bindkey "^n" _complete_dudgks
