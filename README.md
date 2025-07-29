# `zsh-hangul`

생각해보면 터미널에서는 한글을 쓸 일이 잘 없습니다.

영어를 타이핑 해야되는데 한글로 타이핑된경우 자동으로 수정합니다. 

Auto correct hangul(한글, korean) to english when it was supposed to be typed in english.

ex) ㅎㅇ-> gd, ㅣㄴ-> ls

![zsh-hangul](https://user-images.githubusercontent.com/13645032/182091950-dc93cf86-6b25-466f-8c6c-0ab704d63c13.gif)


zsh에서만 동작합니다 bash 사용자는 [bash 버전](https://github.com/gomjellie/bash-hangul)을 사용하세요. 참고로 macOS 는 카타리나 버전부터 zsh이 기본쉘로 변경되었습니다.

# Installation

자세한 설치 가이드는 [INSTALL.md](./INSTALL.md)를 참고해주세요.

# 한글이 허용되는 경우

## 1. 문자열에서 사용

문자열 안에서는 한글이 그대로 유지됩니다. 다음 3가지 경우에 문자열로 인식합니다.

- `"문자열"` (이중 따옴표)
- `'문자열'` (단일 따옴표)  
- `` `문자열` `` (백틱)

## 2. 복사 붙여넣기

복사 붙여넣기로 입력된 텍스트는 한영변환되지 않습니다. 직접 타이핑한 경우에만 한영변환이 적용되어, 의도하지 않은 변환을 방지합니다.

- ✅ 직접 타이핑: `ㅎㅇ` → `gd`로 자동 변환
- ✅ 복사 붙여넣기: 한글 텍스트가 그대로 유지됨

# Reference

http://zsh.sourceforge.net/Doc/zsh_us.pdf

