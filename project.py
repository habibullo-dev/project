<<<<<<< HEAD
# from flask import Flask
# from sqlalchemy import create_engine
# from sqlalchemy import text

# app = Flask(__name__)

# engine = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

# @app.route('/databases')
# def data_bases():
#     result =  '<style>table { border-spacing: 0; } th { text-align: left; } th, td { margin: 0; border: 1px solid black; }</style>'

#     with engine.connect() as db:

#     doctors_data = [
#         {'name': 'Dr. Shin Ho-Chul', 'expertise': 'General Practice', 'type': 'Kangbuk Samsung Hospital', 'address': '108 Pyong-dong, Chung-ku, Seoul', 'phone': '2001-2911, 5100, 5110'},
#         {'name': 'Dr. Yoo Shin-ae', 'expertise': 'General Practice', 'type': 'Samsung Medical Centre', 'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 'phone': '3410-0200'}, 
#         {'name': 'Dr. Kwak', 'expertise': 'General Practice', 'type': 'Seoul Chungang Hospital', 'address': '388-1 Poongnap-dong, Songpa-ku, Seoul', 'phone': '3010-5001/2'}, 
#         {'name': 'Dr. H.S. Rhee', 'expertise': 'General Practice', 'type': 'Seoul Foreign Clinic', 'address': '5-3 Hannam-dong, Yongsan-ku, Seoul', 'phone': '796-1871-2'}, 
#         {'name': 'Dr. John Linton', 'expertise': 'General Practice', 'type': 'Severance Yonsei Hospital', 'address': '134 Shinchon-dong, Sodaemun-ku, Seoul', 'phone': '361-6540'},
#         {'name': 'Dr. Jang', 'expertise': 'General Practice', 'type': 'Soonchunhyang Hospital', 'address': '657-58 Hannam-dong, Yongsan-ku, Seoul', 'phone': '709-9158'},
#         {'name': 'Dr. Ho-wan Han', 'expertise': 'Obstetrics and Gynaecology', 'type': 'Samsung Cheil Hospital', 'address': '1/23 Mukchung-dong, Chung-ku, Seoul', 'phone': '2273-0151'},
#         {'name': 'Dr. Sung Hae-ree', 'expertise': 'Obstetrics and Gynaecology', 'type': 'UN Village Clinic', 'address': 'UN Village, Seoul', 'phone': '790-0802'},
#         {'name': 'Dr. Yoo Shin-ae', 'expertise': 'Paediatrics / Allergy', 'type': 'Samsung Medical Centre', 'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 'phone': '3410-0200'},
#         {'name': 'Dr. Chung Chin-koo', 'expertise': 'Dentist', 'type': 'Unknown', 'address': '135-3 Itaewon-dong, Yongsan-ku, Seoul', 'phone': '795-7726'},
#         {'name': 'Dr. Lee Soo-chan', 'expertise': 'Dentist', 'type': 'Unknown', 'address': '186 Hangang-Ro, 2ga, Yongsan-ku, Seoul', 'phone': '798-0500'},
#         {'name': 'Dr. Kong', 'expertise': 'Opthamologist', 'type': "Dr. Kong's Eye Clinic", 'address': 'Injoo Building, 111-1 Seorin-dong, Chongno-ku, Seoul', 'phone': '733-6890'},
#         {'name': 'Dr. James Lee', 'expertise': 'Chiropractic physician', 'type': 'Itaewon Wellnes', 'address': 'Itaewon Subway Exit #2, Hannam Bldg., 3F', 'phone': '02-794-3536'}
#     ]

#     facilities_data = [
#         {'name': 'Dong-A University Hospital', 'speaker': 'Ms. Kim, Sung-Ah', 'type': 'Hospital', 'address': '1, Dongdaesin-dong 3-ga, Seo-gu', 'phone': '240-2415', 'emergency': '240-5580'},
#         {'name': 'Pusan National Univ. Hospital', 'speaker': 'Ms. Lee, Kyung-Ah', 'type': 'Hospital', 'address': 'Amidong 1-ga, Seo-gu', 'phone': '240-7890', 'emergency': '240-7501'},
#         {'name': 'Baptist Hospital', 'speaker': 'Ms. Song, Jung-Ok', 'type': 'Hospital', 'address': '374-75, Namsan-dong Geumjeong-gu', 'phone': '580-1313', 'emergency': '580-1212'},
#         {'name': 'Baptist Hospital', 'speaker': 'Mr. Lee, Jung-Sang', 'type': 'Hospital', 'address': '374-75, Namsan-dong Geumjeong-gu', 'phone': '580-1251', 'emergency': '580-1212'},
#         {'name': 'Inje Univ.Busan Paik Hospital', 'speaker': 'Mr. Cha, Ji-Hoon', 'type': 'Hospital', 'address': '633-165, Gaegeum 2-dong, Busanjin-gu', 'phone': '890-6220', 'emergency': '890-6221'},
#         {'name': 'Maryknoll General Hospital', 'speaker': 'Mr. Park, Myung-hwan', 'type': 'Hospital', 'address': '12, Daecheong-dong, 4-ga, jung-gu', 'phone': '468-3858', 'emergency': '461-2300'},
#         {'name': 'Kang Internal Medicine Clinic', 'speaker': 'Dr. Kang, Pil-joong', 'type': 'Clinic', 'address': '245-3, Bujeon 2-dong, Jin-Ku, Busan', 'phone': 'NULL', 'emergency': '817-2334'},
#         {'name': 'Ye Dental Clinic', 'speaker': 'Dr. Kim, Byung-Soo', 'type': 'Clinic', 'address': '255-1, Dong-A Bldg., 6th Floor, Bujeon 2-dong, Jin-Ku, Busan', 'phone': 'NuLL', 'emergency': '808-2900'}
#     ]

#     # Insert doctors data:
#     with engine.connect() as db:
#         for doctor in doctors_data:
#             db.execute(text("INSERT INTO Doctors (name, expertise, type, address, phone) VALUES (:name, :expertise, :type, :address, :phone)"), doctor)

#     # Insert facilities data:
#     with engine.connect() as db:
#         for facility in facilities_data:
#             db.execute(text("INSERT INTO Facilities (name, speaker, type, address, phone, emergency) VALUES (:name, :speaker, :type, :address, :phone, :emergency)"), facility)


#     res = db.execute(text("SELECT Upper(name) as upper_name, lower(expertise) as lower_expertise FROM phones"))
#     result += '<table><tr><th>Name</th><th>Expertise</th></tr>'
#     for row in res:
#          result += f'<tr><td>{row.upper_name}</td><td>{row.lower_expertise}</td></tr>'


#     return result
=======
from sqlalchemy.sql import text
from website import sql


# def insert_doctor(data):

#     with sql.begin() as db:
        
#     res = db.execute(text("INSERT INTO Doctors (name, expertise, type, address, phone) VALUES (:name, :expertise, :type, :address, :phone)"))


# def insert_facilities(data)




doctors_data = [
    ('Dr. Shin Ho-Chul', 'General Practice', 'Kangbuk Samsung Hospital', '108 Pyong-dong, Chung-ku, Seoul', '2001-2911, 5100, 5110'),
    ('Dr. Yoo Shin-ae', 'General Practice', 'Samsung Medical Centre', '50 Ilwon-dong, Kangnam-ku, Seoul', '3410-0200'), 
    ('Dr. Kwak', 'General Practice', 'Seoul Chungang Hospital', '388-1 Poongnap-dong, Songpa-ku, Seoul', '3010-5001/2'), 
    ('Dr. H.S. Rhee', 'General Practice', 'Seoul Foreign Clinic', '5-3 Hannam-dong, Yongsan-ku, Seoul', '796-1871-2'), 
    ('Dr. John Linton', 'General Practice', 'Severance Yonsei Hospital', '134 Shinchon-dong, Sodaemun-ku, Seoul', '361-6540'),
    ('Dr. Jang', 'General Practice', 'Soonchunhyang Hospital' '657-58 Hannam-dong, Yongsan-ku, Seoul', '709-9158'),
    ('Dr. Ho-wan Han', 'Obstetrics and Gynaecology', 'Samsung Cheil Hospital', '1/23 Mukchung-dong, Chung-ku, Seoul', '2273-0151')
    ('Dr. Sung Hae-ree', 'Obstetrics and Gynaecology', 'UN Village Clinic', 'UN Village, Seoul', '790-0802'),
    ('Dr. Yoo Shin-ae', 'Paediatrics / Allergy', 'Samsung Medical Centre', '50 Ilwon-dong, Kangnam-ku, Seoul', '3410-0200'),
    ('Dr. Chung Chin-koo', 'Dentist', 'Unknown', '135-3 Itaewon-dong, Yongsan-ku, Seoul', '795-7726'),
    ('Dr. Lee Soo-chan', 'Dentist', 'Unknown', '186 Hangang-Ro, 2ga, Yongsan-ku, Seoul', '798-0500'),
    ('Dr. Kong', 'Opthamologist', 'Dr. Kong\'s Eye Clinic', 'Injoo Building, 111-1 Seorin-dong, Chongno-ku, Seoul', '733-6890'),
    ('Dr. James Lee', 'Chiropractic physician', 'Itaewon Wellnes', 'Itaewon Subway Exit #2, Hannam Bldg., 3F', '02-794-3536')
]


facilities_data = [
    ('Dong-A University Hospital','Ms. Kim, Sung-Ah' ,'Hospital', '1, Dongdaesin-dong 3-ga, Seo-gu', '240-2415', '240-5580'),
    ('Pusan National Univ. Hospital', 'Ms. Lee, Kyung-Ah', 'Hospital', 'Amidong 1-ga, Seo-gu', '240-7890', '240-7501'),
    ('Baptist Hospital', 'Ms. Song, Jung-Ok', 'Hospital', '374-75, Namsan-dong Geumjeong-gu', '580-1313', '580-1212'),
    ('Baptist Hospital', 'Mr. Lee, Jung-Sang', 'Hospital', '374-75, Namsan-dong Geumjeong-gu', '580-1251', '580-1212'),
    ('Inje Univ.Busan Paik Hospital', 'Mr. Cha, Ji-Hoon', 'Hospital', '633-165, Gaegeum 2-dong, Busanjin-gu', '890-6220', '890-6221'),
    ('Maryknoll General Hospital', 'Mr. Park, Myung-hwan', 'Hospital', '12, Daecheong-dong, 4-ga, jung-gu', '468-3858', '461-2300'),
    ('Kang Internal Medicine Clinic', 'Dr. Kang, Pil-joong', 'Clinic', '245-3, Bujeon 2-dong, Jin-Ku, Busan', 'NULL', '817-2334'),
    ('Ye Dental Clinic', 'Dr. Kim, Byung-Soo', 'Clinic', '255-1, Dong-A Bldg., 6th Floor, Bujeon 2-dong, Jin-Ku, Busan', 'NuLL', '808-2900')
]
>>>>>>> 0e0c0d0ec9218b58bdda96bc42a085d403e8c1e9
