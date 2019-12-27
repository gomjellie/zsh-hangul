echo "zsh-hangul loaded"

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
