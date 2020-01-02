
# Without zsh plugin manager

oh my zsh 같은 zsh plugin manager를 사용하지 않는경우

```sh
git clone https://github.com/gomjellie/zsh-hangul

echo "source ${(q-)PWD}/zsh-hangul/zsh-hangul.plugin.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

# With Plugin Manager

#### [Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

1. custom/plugins/zsh-hangul 에 스크립트를 클론합니다.

```sh
git clone https://github.com/gomjellie/zsh-hangul ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-hangul
```

2. ~/.zshrc에 plugin을 추가합니다.

~/.zshrc 에

```sh
plugins=(
    git
    zsh-hangul
)
```

과 같이 zsh-hangul을 추가해주세요.
