autoload -Uz _convert_gksdud
autoload -Uz _complete_dudgks

_convert_gksdud() {
    # widget to convert korean -> english
    BUFFER="${LBUFFER}${gksdud[${KEYS}]}${RBUFFER}"
    CURSOR+=${#gksdud[${KEYS}]}
}

_complete_dudgks() {
    res=$(python3 ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-hangul/dudgks.py $words[$CURRENT])
    # $compstate[insert]=0
    compadd -S "" -U -Q $res
    compcall -D
}

zle -N _convert_gksdud

zle -C _complete_dudgks menu-complete _complete_dudgks

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

bindkey "^n" _complete_dudgks
