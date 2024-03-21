import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 이메일을 보낼 SMTP 서버 설정
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "MY_USENAME"
smtp_password = "MY_PASSWORD"

# 참가자 목록 및 이메일 주소 설정
participants = {
    "정헌진": "hj.jeong@okestro.com",
    "정헌진2": "hj.jeong@okestro.com",
}

# 무작위로 마니또 할당 생성
def generate_secret_santa(participants):
    santas = list(participants.keys())
    random.shuffle(santas)
    secret_santas = {}
    for i in range(len(santas)):
        if santas[i] == list(participants.keys())[i]:
            return generate_secret_santa(participants)  # 자기 자신과 매칭되면 다시 시도
        else:
            secret_santas[santas[i]] = santas[(i + 1) % len(santas)]
    return secret_santas

# 이메일 보내기 함수
def send_email(sender_email, recipient_email, sender_name, recipient_name, subject):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        html_message = f"""\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html>
          <head>
            <!-- Compiled with Bootstrap Email version: 1.3.1 -->
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <meta http-equiv="x-ua-compatible" content="ie=edge">
            <meta name="x-apple-disable-message-reformatting">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
            <style type="text/css">
              body,table,td{{font-family:Helvetica,Arial,sans-serif !important;}}.ExternalClass{{width:100%}}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{{line-height:150%}}a{{text-decoration:none}}*{{color:inherit}}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}}img{{-ms-interpolation-mode:bicubic}}table:not([class^=s-]){{font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}}table:not([class^=s-]) td{{border-spacing:0px;border-collapse:collapse}}@media screen and (max-width: 600px){{.w-full,.w-full>tbody>tr>td{{width:100% !important}}.w-24,.w-24>tbody>tr>td{{width:96px !important}}.w-40,.w-40>tbody>tr>td{{width:160px !important}}.p-lg-10:not(table),.p-lg-10:not(.btn)>tbody>tr>td,.p-lg-10.btn td a{{padding:0 !important}}.p-3:not(table),.p-3:not(.btn)>tbody>tr>td,.p-3.btn td a{{padding:12px !important}}.p-6:not(table),.p-6:not(.btn)>tbody>tr>td,.p-6.btn td a{{padding:24px !important}}*[class*=s-lg-]>tbody>tr>td{{font-size:0 !important;line-height:0 !important;height:0 !important}}.s-4>tbody>tr>td{{font-size:16px !important;line-height:16px !important;height:16px !important}}.s-6>tbody>tr>td{{font-size:24px !important;line-height:24px !important;height:24px !important}}.s-10>tbody>tr>td{{font-size:40px !important;line-height:40px !important;height:40px !important}}}}
              .table {{width:100%}}
              .table tbody tr, .table tbody td, .table thead th{{border:1px solid;}}
              .table thead th{{background-color: lightgray}}
            </style>
          </head>
          <body class="bg-light" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
            <table class="bg-light body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
              <tbody>
                <tr>
                  <td valign="top" style="line-height: 24px; font-size: 16px; margin: 0;" align="left" bgcolor="#f7fafc">
                    <table class="container" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;">
                      <tbody>
                        <tr>
                          <td align="center" style="line-height: 24px; font-size: 16px; margin: 0; padding: 0 16px;">
                            <!--[if (gte mso 9)|(IE)]>
                              <table align="center" role="presentation">
                                <tbody>
                                  <tr>
                                    <td width="600">
                            <![endif]-->
                            <table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 600px; margin: 0 auto;">
                              <tbody>
                                <tr>
                                  <td style="line-height: 24px; font-size: 16px; margin: 0;" align="left">
                                    <table class="s-10 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;" align="left" width="100%" height="40">
                                            &#160;
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <table class="ax-center" role="presentation" align="center" border="0" cellpadding="0" cellspacing="0" style="margin: 0 auto;">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 24px; font-size: 16px; margin: 0;" align="left">
                                            <img class="w-24" src="https://www.okestro.com/img/logo_up.png" style="height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 96px; border-style: none; border-width: 0;" width="96">
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <table class="s-10 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;" align="left" width="100%" height="40">
                                            &#160;
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <table class="card p-6 p-lg-10 space-y-4" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 6px; border-collapse: separate !important; width: 100%; overflow: hidden; border: 1px solid #e2e8f0;" bgcolor="#ffffff">
                                      <tbody>
                                      <tr>
                                        <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0; padding: 40px;" align="left" bgcolor="#ffffff">
                                          <h1>워크샵 일정 안내</h1>
                                          <h2 class="h3 fw-700" style="padding-top: 0; padding-bottom: 0; font-weight: 700 !important; vertical-align: baseline; font-size: 20px; line-height: 33.6px; margin: 0;" align="left">
                                            안녕하세요 {sender_name} 님.<br>당신의 마니또는 <h>{recipient_name}</h> 님 입니다.
                                          </h2>
                                          <b style="font-size:10px;">*마니또는 자율적인 활동이며 서운해할 필요 1도 없습니다.</b>
                                          <br>
                                          <b style="font-size:10px;">*마니또란? <a href="https://namu.wiki/w/마니또" target="_blank">마니또 - 나무위키</a></b>
                                          <div class="container mt-5">
                                            <div class="row">
                                              <div class="col">
                                                <table class="table">
                                                  <thead>
                                                  <tr>
                                                    <td colspan="2"><h4>- 29일 금요일</h4></td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="col" width="20%">시간</th>
                                                    <th scope="col" width="100%">내용</th>
                                                  </tr>
                                                  </thead>
                                                  <tbody>
                                                  <tr>
                                                    <th scope="row">11:00</th>
                                                    <td>(늦으면 안되는)버스 심팩 빌딩 출발<br>*팀장님 심팩 주간회의 종료 후 출발</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">12:30<br>~13:30</th>
                                                    <td>점심 식사<br>위치 : 다가오는 봄과 함께 봄날 칼국수 보리밥(https://naver.me/FJH6xEJW)<br><b>(자차 이동 인원 시간 맞춰 올것)</b></td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">13:30<br>~14:00</th>
                                                    <td>숙소 이동</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">14:00<br>~15:00</th>
                                                    <td>빠릿빠릿 짐풀기 및 아이스 브레이킹</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">15:00<br>~16:30</th>
                                                    <td>워크샵<br>1.앞으로의 업무 로드맵 및 일정<br>2.조별 협동 과제 해결 시간<br>3.마니또 1등 시상(상금 9만 9000원 + @)</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">16:30<br>~18:00</th>
                                                    <td>게임 및 사진 촬영<br>1.서로 알아가기 시간(https://kahoot.it/)<br>2.레크레이션 및 1등 조 시상(19만 9000원&nbsp;+ @)</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">18:00<br>~21:30</th>
                                                    <td>석식 및 친해지는 시간</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">21:30 ~</th>
                                                    <td>무슨 일이 생길지 모르는 밤</td>
                                                  </tr>
                                                  </tbody>
                                                  <thead>
                                                  <tr>
                                                    <td colspan="2"><h4>- 30일 토요일</h4></td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="col" width="20%">시간</th>
                                                    <th scope="col" width="100%">내용</th>
                                                  </tr>
                                                  </thead>
                                                  <tbody>
                                                  <tr>
                                                    <th scope="row">05:30<br>~07:30</th>
                                                    <td>헌진 정 셰르파와 함께하는 퇴미산 일출 정복시간 (참가 자유)</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">09:30<br>~10:30</th>
                                                    <td>당일 치기한 사람들은 먹을 수 없는 DY.Choi 셰프의 요리 대접</td>
                                                  </tr>
                                                  <tr>
                                                    <th scope="row">11:00</th>
                                                    <td>2차 워크샵을 위한 해산 (버스 다시 여의도 복귀)</td>
                                                  </tr>
                                                  </tbody>
                                                </table>
                                              </div>
                                            </div>
                                          </div>
                                          <table class="s-4 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                            <tbody>
                                            <tr>
                                              <td style="line-height: 16px; font-size: 16px; width: 100%; height: 16px; margin: 0;" align="left" width="100%" height="16">
                                                &nbsp;
                                              </td>
                                            </tr>
                                            </tbody>
                                          </table>
                                          <button class="btn btn-primary p-3 fw-700" role="presentation" border="0" cellpadding="0" cellspacing="0" style="float:right;color: #ffffff; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 6px; line-height: 20px; display: block; font-weight: 700 !important; white-space: nowrap; background-color: #0d6efd; padding: 12px; border: 1px solid #0d6efd;">
                                            <a href="tel:010-8759-8720">문의하기</a>
                                          </button>
                                        </td>
                                      </tr>
                                      </tbody>
                                    </table>
                                    <table class="s-10 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;" align="left" width="100%" height="40">
                                            &#160;
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <table class="ax-center" role="presentation" align="center" border="0" cellpadding="0" cellspacing="0" style="margin: 0 auto;">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 24px; font-size: 16px; margin: 0;" align="left">
                                            <img class="w-40" src="https://www.okestro.com/img/logo_up.png" style="height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 160px; border-style: none; border-width: 0;" width="160">
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                            &#160;
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <div class="text-muted text-center" style="color: #718096;" align="center">
                                      플랫폼서비스 본부<br>
                                      플랫폼서비스 개발 1팀<br>
                                    </div>
                                    <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                            &#160;
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <!--[if (gte mso 9)|(IE)]>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                            <![endif]-->
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </body>
        </html>
        """

        part = MIMEText(html_message, 'html')
        msg.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"이메일이 {recipient_email}으로 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일을 보내는 도중 오류가 발생했습니다: {e}")
    finally:
        server.quit()

# 마니또 할당 생성
secret_santas = generate_secret_santa(participants)

# 이메일 전송
for sender_name, recipient_name in secret_santas.items():
    sender_email = participants[sender_name]
    recipient_email = participants[recipient_name]
    subject = "[플랫폼서비스 개발1팀] 워크샵 일정 공지"
    ret = send_email(sender_email, recipient_email, recipient_name, sender_name, subject)
    print(ret)
