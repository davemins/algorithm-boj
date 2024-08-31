email_list = [
    "leetw@hanbat.ac.kr", "kim.sh@hanbat.ac.kr", "parkcomet@hanbat.ac.kr", "pgjoo@hanbat.ac.kr", "ythoo@hanbat.ac.kr",
    "gjinoh@hanbat.ac.kr", "leeeunjin@hanbat.ac.kr", "swkkim@hanbat.ac.kr", "yejiseo@hanbat.ac.kr", "bohyunkim@hanbat.ac.kr",
    "love224@hanbat.ac.kr", "suminoh@hanbat.ac.kr", "topwater@hanbat.ac.kr", "hs.ang@hanbat.ac.kr", "sukim@hanbat.ac.kr",
    "jhyun@hanbat.ac.kr", "hschoi@hanbat.ac.kr", "jieunlee@hanbat.ac.kr", "ytkim@hanbat.ac.kr", "leesa@hanbat.ac.kr",
    "sujinlee@hanbat.ac.kr", "jmjung@hanbat.ac.kr", "forever.kim@hanbat.ac.kr", "mooncw@hanbat.ac.kr", "yoseb.choi@hanbat.ac.kr",
    "kwshin@hanbat.ac.kr", "onlyhwan@hanbat.ac.kr", "mykim@hanbat.ac.kr", "leesunsook@hanbat.ac.kr", "bjoolee@hanbat.ac.kr",
    "jelee@hanbat.ac.kr", "jhgwan@hanbat.ac.kr", "mklee@hanbat.ac.kr", "espark@hanbat.ac.kr", "sykim@hanbat.ac.kr",
    "dbyeom@hanbat.ac.kr", "jh.lee@hanbat.ac.kr", "mkjang@hanbat.ac.kr", "parkts@hanbat.ac.kr", "mhgwon@hanbat.ac.kr",
    "cgchoi@hanbat.ac.kr", "eojinjeon@hanbat.ac.kr"
]

email_without_domain = [email.split('@')[0] for email in email_list]

for i in email_without_domain:
    print(i)
