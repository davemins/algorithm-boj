import RPi.GPIO as GPIO  # RPi.GPIO 모듈을 GPIO로 임포트
import time  # 시간 관련 모듈 임포트
import subprocess  # 스트리밍 CCTV uv4l 라이브러리 실행을 위한 모듈 임포트

GPIO.setwarnings(False)  # 불필요한 warning 제거
GPIO.setmode(GPIO.BCM)  # GPIO 핀 번호 모드 설정

TRIG_PIN = 20  # 초음파 센서의 TRIG 핀 번호
ECHO_PIN = 21  # 초음파 센서의 ECHO 핀 번호

def initUltrasonic():
    # 초음파 센서 초기화
    GPIO.setup(TRIG_PIN, GPIO.OUT)  # TRIG 핀을 출력으로 설정
    GPIO.setup(ECHO_PIN, GPIO.IN)  # ECHO 핀을 입력으로 설정

def controlUltrasonic():
    distance = 0.0
    # 초음파 센서로부터 거리 측정
    GPIO.output(TRIG_PIN, False)  # TRIG 핀에 LOW 신호 출력
    time.sleep(0.5)  # 0.5초 대기
    GPIO.output(TRIG_PIN, True)  # TRIG 핀에 HIGH 신호 출력
    time.sleep(0.00001)  # 10 마이크로초 대기
    GPIO.output(TRIG_PIN, False)  # TRIG 핀에 LOW 신호 출력

    while GPIO.input(ECHO_PIN) == 0:  # ECHO 핀이 LOW 상태인 동안 대기
        pulse_start = time.time()  # 시작 시간 기록

    while GPIO.input(ECHO_PIN) == 1:  # ECHO 핀이 HIGH 상태인 동안 대기
        pulse_end = time.time()  # 종료 시간 기록

    pulse_duration = pulse_end - pulse_start  # 초음파가 수신된 시간 계산
    distance = pulse_duration * 17000  # 거리 계산 (음속: 340m/s, 왕복 거리이므로 2로 나누지 않음)
    distance = round(distance, 2)  # 소수점 둘째 자리까지 반올림
    return distance

def main():
    GPIO.setmode(GPIO.BCM)  # GPIO 핀 번호 모드 설정
    distance = 0.0
    initUltrasonic()  # 초음파 센서 초기화
    print("Ultrasonic Operating ...")
    try:
        while True:
            distance = controlUltrasonic()  # 초음파 센서로부터 거리 측정
            print("수위 %.2f cm" % (9.8 - distance))  # 측정된 거리를 수위로 변환하여 출력

            # 수위가 일정 값 이상일 때
            if distance < 5:
                subprocess.run(["sudo", "service", "uv4l_raspicam", "restart"])  # 스트리밍 CCTV uv4l 라이브러리 실행

                GPIO.setup(18, GPIO.OUT)  # 부저를 제어하기 위해 18번 핀을 출력으로 설정
                p = GPIO.PWM(18, 100)  # 18번 핀을 PWM 모드로 설정, 주파수는 100Hz

                Frq = [262, 294, 330, 349, 392, 440, 493, 523]  # 4옥타브 도~시, 5옥타브 도
                speed = 0.5  # 음과 음 사이의 시간 간격 설정
                
                p.start(10)  # PWM 시작, 듀티 사이클 10
                try:
                    for fr in Frq:
                        p.ChangeFrequency(fr)  # 부저의 주파수 변경
                        time.sleep(speed)  # 음과 음 사이의 시간 간격만큼 대기

                except KeyboardInterrupt:  # 사용자가 Ctrl+C를 누르면 종료
                    pass
                p.stop()  # PWM 정지

    except KeyboardInterrupt:  # 사용자가 Ctrl+C를 누르면 종료
        GPIO.cleanup()

# main 실행
if __name__ == '__main__':
    main()
