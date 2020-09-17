# 라이브러리
import cv2, random, os
import numpy as np


while True:

    # 윈도우 cls 명령어.
    os.system('cls')

    # 아스키아트
    print(" _____   _____   _    _   _____   _       _")
    print("|_   _| |_   _| | |  | | |_   _| | |     | | ")  
    print("  | |     | |   | |  | |   | |   | |     | | ")
    print("  | |     | |   | |/\| |   | |   | |     | | ")
    print("  | |_    | |   \  /\  /  _| |_  | |____ | |____")
    print(" \___/    \_/    \/  \/   \___/  \_____/ \_____/")


    # 숫자를 입력받을 때까지 반복
    while True:
        
        try:
            count = int(input("\n뽑을 줄 개수를 입력해주세요. : "))
            i_count = 0
            break

        except ValueError:
            print("Error - 숫자만 입력해주세요.")
            
        
    # 이미지를 불러옴 ( 같은 폴더에 있어야함 )
    image = cv2.imread('jari.jpg')


    # 지정한 횟수 만큼 줄을 긋는다.
    while i_count < count:
        i_count = i_count + 1
        
        # 줄을 그을 랜덤 좌표 생성
        line1 = random.randrange(30,545)
        line2 = random.randrange(30,464)

        line3 = random.randrange(30,545)
        line4 = random.randrange(30,464)

        # 줄의 길이가 300보다 길면
        if line1 - line3 > 300 or line3 - line1 > 300:
            cv2.line(image, (line1, line2) , (line3, line4), (0,0,0), 3)

        # 줄의 길이가 짧으면 횟수증가.
        else :
            i_count = i_count - 1

    # 결과를 표시한다.
    cv2.imshow('random', image)
    cv2.waitKey()


    # 한번더 할래?
    check = input("\n한 번 더 하시겠습니까? (Y/N) : ")
    if check.upper() == 'N':
        break
        
