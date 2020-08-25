# `zsh-hangul`

영어를 타이핑 해야되는데 한글로 타이핑된경우 자동으로 수정합니다. Auto correct hangul(한글, korean) to english when it was supposed to be typed english.

ex) ㅎㅇ-> gd, ㅣㄴ-> ls

![zsh-hangul.gif](./.github/zsh-hangul.gif)

zsh에서만 동작합니다 bash 사용자는 [bash 버전](https://github.com/gomjellie/bash-hangul)을 사용하세요. 참고로 macOS 는 카타리나 버전부터 zsh이 기본쉘로 변경되었습니다.

# Installation

자세한 설치 가이드는 [INSTALL.md](./INSTALL.md)를 참고해주세요.

# Trouble Shooting

## 한글을 입력하고 싶은데 전부 영어로 바뀌어 버려요

영어로 바뀌는거 무시하고 한글 단어를 끝까지 입력후 ^(ctrl key) 와 함께 n 를 눌러보세요.

해당기능을 사용하기 위해서는 python3 가 설치되어 있어야 합니다.

```sh
cd ./elfprxhfldlfma
#                  ^ 여기까지 입력한 상태에서 ctrl + n 을 누르면 

cd ./디렉토리이름

#로 변경됩니다.
```

문자열안에서는 한글 그대로 입력됩니다.

문자열로 인식하는 경우는 다음 3가지 경우입니다.

- "문자열"

- '문자열'

- \`문자열\`

# Reference

http://zsh.sourceforge.net/Doc/zsh_us.pdf

