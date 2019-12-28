autoload -Uz _convert_gksdud

_convert_gksdud() {
    # widget to convert korean -> english
    BUFFER="${LBUFFER}${gksdud[${KEYS}]}${RBUFFER}"
    CURSOR+=${#gksdud[${KEYS}]}
}

zle -N _convert_gksdud

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

_complete_gksdud() {
    # echo "$words[$CURRENT]"
    compadd -Q "anwp" "wpahr" "$words[$CURRENT]" 
}

zle -C _complete_gksdud menu-complete _complete_gksdud

bindkey "\`" _complete_gksdud
