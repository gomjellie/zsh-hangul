autoload -Uz _convert_gksdud
autoload -Uz _complete_dudgks
autoload -Uz _on_tab_pressed

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

_on_tab_pressed() {
    res=$(python3 $ZSH_HANGUL_DIR/dudgks.py $words[$CURRENT])
    korean_candidate="$(echo $res| sed 's/\.\///')"
    korean_dirs=$(ls -A1|grep ^$korean_candidate)
    compadd -S "/" -P "./" -U $(echo $korean_dirs) # echo makes it array
    # unset POSTDISPLAY
    [[ ${#$(echo $korean_dirs)} -eq 0 ]] || {
        return 0
    }
    compcall -D
}

zle -N _convert_gksdud

zle -C _complete_dudgks menu-complete _complete_dudgks
zle -C _on_tab_pressed menu-complete _on_tab_pressed

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

bindkey "^n" _complete_dudgks
bindkey "\t" _on_tab_pressed
