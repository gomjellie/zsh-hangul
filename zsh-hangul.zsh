autoload -Uz _convert_gksdud
# autoload -Uz _complete_dudgks

ZSH_HANGUL_DIR=$(dirname $0)

_convert_gksdud() {
    # widget to convert korean -> english
    let n_double_quote=$(echo $LBUFFER |grep -o "\"" |wc -l |xargs)
    let n_single_quote=$(echo $LBUFFER |grep -o "'" |wc -l |xargs)
    let n_back_quote=$(echo $LBUFFER |grep -o "\`" |wc -l |xargs)
    
    [[ $(($n_double_quote % 2)) -eq 0 ]] &&
    [[ $(($n_single_quote % 2)) -eq 0 ]] &&
    [[ $(($n_back_quote   % 2)) -eq 0 ]] && {
        BUFFER="${LBUFFER}${gksdud[${KEYS}]}${RBUFFER}"
        CURSOR+=${#gksdud[${KEYS}]}
        return 0
    }
    BUFFER="${LBUFFER}${KEYS}${RBUFFER}"
    CURSOR+=${#KEYS}
}

_complete_dudgks() {
    res=$(python3 $ZSH_HANGUL_DIR/dudgks.py $words[$CURRENT])
    compadd -S "" -U -Q $res
}

zle -N _convert_gksdud

# zle -C _complete_dudgks menu-complete _complete_dudgks

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

# bindkey "^n" _complete_dudgks
