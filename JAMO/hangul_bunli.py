def bunli():
    ##########################################
    chosung = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    jungsung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    jongsung = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', '']
    ##########################################

    a = list(input('글자를 입력해 주세요 >> '))

    for i in a:
        charactorf = ord(i)-0xAC00
        chosung_i = (charactorf) // 21 //28
        if chosung_i == -75:
            print(' spce ', end = ' 🔸 ')
            continue
        else:
            print(chosung[chosung_i], end='')


        jungsung_i = ((charactorf) - (chosung_i * 21 * 28)) //28
        print(jungsung[jungsung_i], end = '')


        jongsung_i = ((charactorf) - (chosung_i * 21 * 28) - ((jungsung_i) * 28) - 1)
        print(jongsung[jongsung_i], end = ' 🔸 ')