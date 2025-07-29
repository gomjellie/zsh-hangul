autoload -Uz _convert_gksdud
# autoload -Uz _complete_dudgks

ZSH_HANGUL_DIR=$(dirname $0)

# 붙여넣기 상태를 추적하는 변수
_zsh_hangul_is_pasting=0

_convert_gksdud() {
    # widget to convert korean -> english
    
    # 붙여넣기 중일 때는 한영변환을 하지 않음
    if [[ $_zsh_hangul_is_pasting -eq 1 ]]; then
        BUFFER="${LBUFFER}${KEYS}${RBUFFER}"
        CURSOR+=${#KEYS}
        return 0
    fi
    
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

# 사용자 정의 bracketed-paste 함수
_zsh_hangul_bracketed_paste() {
    _zsh_hangul_is_pasting=1
    
    # 원본 bracketed-paste 동작 수행
    zle .bracketed-paste
    
    _zsh_hangul_is_pasting=0
}

_complete_dudgks() {
    res=$(python3 $ZSH_HANGUL_DIR/dudgks.py $words[$CURRENT])
    compadd -S "" -U -Q $res
}

zle -N _convert_gksdud

# bracketed-paste 위젯을 커스터마이징
zle -N bracketed-paste _zsh_hangul_bracketed_paste

# zle -C _complete_dudgks menu-complete _complete_dudgks

for key value in ${(kv)gksdud}; do
    bindkey "${key}" _convert_gksdud
done

# bindkey "^n" _complete_dudgks
