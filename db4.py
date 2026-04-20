
import sqlite3 as sq

with sq.connect("maktab.db") as con:
    cur = con.cursor()


    cur.execute("""CREATE TABLE IF NOT EXISTS oquvchilar (
        id INTEGER PRIMARY KEY,
        ism TEXT NOT NULL,
        familiya TEXT NOT NULL,
        sinf TEXT NOT NULL,           -- masalan: '10-A', '11-B'
        tugilgan_yil INTEGER,
        telefon TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS fanlar (
        id INTEGER PRIMARY KEY,
        nomi TEXT NOT NULL UNIQUE,
        oqituvchi TEXT NOT NULL,
        haftalik_soat INTEGER         -- haftada necha soat o'qitiladi
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS baholar (
        id INTEGER PRIMARY KEY,
        oquvchi_id INTEGER NOT NULL,
        fan_id INTEGER NOT NULL,
        ball INTEGER NOT NULL,        -- 0 dan 100 gacha
        sana TEXT NOT NULL,           -- 'YYYY-MM-DD' formatida
        FOREIGN KEY (oquvchi_id) REFERENCES oquvchilar(id),
        FOREIGN KEY (fan_id)     REFERENCES fanlar(id)
    )""")


    oquvchilar_royxati = [
        (1,  'Bekzod',     'Karimov',     '10-A', 2010, '+998901234567'),
        (2,  'Madina',     'Yusupova',    '10-A', 2010, '+998901234568'),
        (3,  'Aziz',       'Rahimov',     '10-A', 2009, '+998901234569'),
        (4,  'Nilufar',    'Tursunova',   '10-A', 2010, '+998901234570'),
        (5,  'Jasur',      'Nazarov',     '10-B', 2010, '+998901234571'),
        (6,  'Sevara',     'Ismoilova',   '10-B', 2010, '+998901234572'),
        (7,  'Otabek',     'Sharipov',    '10-B', 2009, '+998901234573'),
        (8,  'Dilnoza',    'Karimova',    '11-A', 2009, '+998901234574'),
        (9,  'Alisher',    'Xolmatov',    '11-A', 2008, '+998901234575'),
        (10, 'Gulnora',    'Abdullayeva', '11-A', 2009, '+998901234576'),
        (11, 'Sherzod',    'Mirzayev',    '11-B', 2008, '+998901234577'),
        
        (12, 'Zarina',     'Saidova',     '11-B', 2009, '+998901234578'),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO oquvchilar VALUES (?, ?, ?, ?, ?, ?)",
        oquvchilar_royxati
    )

    fanlar_royxati = [
        # (id, nomi,                  oqituvchi,                          haftalik_soat)
        (1, 'Matematika',             'Karimova Zulfiya Akmalovna',       6),
        (2, 'Fizika',                 'Rahimov Botir Sodiqovich',         4),
        (3, 'Kimyo',                  'Yusupova Mavluda Bahodirovna',     3),
        (4, 'Biologiya',              'Tursunov Sherzod Ravshanovich',    3),
        (5, 'Ona tili va adabiyot',   'Saidova Munira Akromovna',         5),
        (6, 'Ingliz tili',            'Olimova Nargiza Tolibovna',        4),
        (7, 'Tarix',                  'Nazarov Akmal Tursunovich',        2),
        (8, 'Informatika',            'Sharipov Jasur Komilovich',        3),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO fanlar VALUES (?, ?, ?, ?)",
        fanlar_royxati
    )

    baholar_royxati = [

        (1,  1, 1, 92, '2026-04-05'),  (2,  1, 2, 78, '2026-04-08'),
        (3,  1, 3, 85, '2026-04-12'),  (4,  1, 5, 88, '2026-04-15'),
        (5,  1, 8, 95, '2026-04-18'),

        (6,  2, 1, 98, '2026-04-05'),  (7,  2, 2, 95, '2026-04-08'),
        (8,  2, 3, 90, '2026-04-12'),  (9,  2, 4, 96, '2026-04-14'),
        (10, 2, 5, 92, '2026-04-15'),

        (11, 3, 1, 65, '2026-04-05'),  (12, 3, 2, 70, '2026-04-08'),
        (13, 3, 3, 58, '2026-04-12'),  (14, 3, 6, 75, '2026-04-16'),

        (15, 4, 1, 88, '2026-04-05'),  (16, 4, 4, 94, '2026-04-14'),
        (17, 4, 5, 90, '2026-04-15'),  (18, 4, 6, 85, '2026-04-16'),

        (19, 5, 1, 72, '2026-04-05'),  (20, 5, 7, 80, '2026-04-17'),
        (21, 5, 8, 88, '2026-04-18'),

        (22, 6, 3, 95, '2026-04-12'),  (23, 6, 4, 92, '2026-04-14'),
        (24, 6, 6, 89, '2026-04-16'),

        (25, 7, 2, 82, '2026-04-08'),  (26, 7, 8, 91, '2026-04-18'),

        (27, 8, 1, 86, '2026-04-05'),  (28, 8, 5, 94, '2026-04-15'),
        (29, 8, 6, 88, '2026-04-16'),

        (30, 9, 2, 76, '2026-04-08'),  (31, 9, 7, 85, '2026-04-17'),

        (32, 10, 3, 89, '2026-04-12'), (33, 10, 4, 91, '2026-04-14'),
        (34, 10, 5, 87, '2026-04-15'),

        (35, 11, 1, 55, '2026-04-05'), (36, 11, 2, 60, '2026-04-08'),
        (37, 11, 8, 78, '2026-04-18'),
        
        (38, 12, 5, 96, '2026-04-15'), (39, 12, 6, 93, '2026-04-16'),
        (40, 12, 7, 90, '2026-04-17'),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO baholar VALUES (?, ?, ?, ?, ?)",
        baholar_royxati
    )

    con.commit()

    def chiqar(sarlavha, qatorlar):
        print("\n" + "=" * 65)
        print(f"  {sarlavha}")
        print("=" * 65)
        if not qatorlar:
            print("  (natija bo'sh)")
            return
        for q in qatorlar:
            print(" ", q)


    cur.execute("""
        SELECT ism, familiya, tugilgan_yil
        FROM oquvchilar
        ORDER BY tugilgan_yil ASC
    """)
    chiqar("O'quvchilar tug'ilgan yili bo'yicha (kichikdan kattaga)",
           cur.fetchall())

    cur.execute("""
        SELECT familiya, ism, sinf
        FROM oquvchilar
        ORDER BY familiya ASC
    """)
    chiqar("O'quvchilar familiyasi bo'yicha alifbo tartibida",
           cur.fetchall())

    cur.execute("""
        SELECT sinf, familiya, ism
        FROM oquvchilar
        ORDER BY sinf ASC, familiya ASC
    """)
    chiqar("Sinf bo'yicha guruhlangan, ichida familiya tartibida",
           cur.fetchall())


    cur.execute("""
        SELECT oquvchi_id, fan_id, ball, sana
        FROM baholar
        ORDER BY ball DESC
        LIMIT 5
    """)
    chiqar("Eng yuqori 5 ta baho", cur.fetchall())

    cur.execute("""
        SELECT oquvchi_id, fan_id, ball
        FROM baholar
        ORDER BY ball DESC
        LIMIT 5 OFFSET 5
    """)
    chiqar("6-10 o'rindagi baholar (sahifalash)", cur.fetchall())


    cur.execute("""
        SELECT ism, familiya
        FROM oquvchilar
        WHERE familiya LIKE 'K%'
    """)
    chiqar("Familiyasi 'K' bilan boshlanadiganlar", cur.fetchall())

    cur.execute("""
        SELECT ism, familiya, sinf
        FROM oquvchilar
        WHERE familiya LIKE '%ova'
    """)
    chiqar("Familiyasi 'ova' bilan tugaganlar", cur.fetchall())

    cur.execute("""
        SELECT ism, familiya, telefon
        FROM oquvchilar
        WHERE telefon LIKE '+99890%'
    """)
    chiqar("Beeline operatorida telefoni borlar (+99890)",
           cur.fetchall())


    cur.execute("""
        SELECT ism, familiya, tugilgan_yil
        FROM oquvchilar
        WHERE tugilgan_yil BETWEEN 2009 AND 2010
    """)
    chiqar("2009-2010 yillarda tug'ilganlar", cur.fetchall())

    cur.execute("""
        SELECT oquvchi_id, fan_id, ball
        FROM baholar
        WHERE ball BETWEEN 70 AND 89
        ORDER BY ball DESC
    """)
    chiqar("Yaxshi baholar oralig'i (70-89)", cur.fetchall())


    cur.execute("""
        SELECT ism, familiya, sinf
        FROM oquvchilar
        WHERE sinf IN ('10-A', '11-A')
        ORDER BY sinf, familiya
    """)
    chiqar("10-A va 11-A sinf o'quvchilari", cur.fetchall())

    cur.execute("""
        SELECT ism, familiya, sinf
        FROM oquvchilar
        WHERE sinf NOT IN ('11-A', '11-B')
    """)
    chiqar("11-sinflardan tashqari o'quvchilar", cur.fetchall())


    cur.execute("SELECT DISTINCT sinf FROM oquvchilar ORDER BY sinf")
    chiqar("Maktabdagi sinflar ro'yxati", cur.fetchall())

    cur.execute("SELECT DISTINCT sana FROM baholar ORDER BY sana")
    chiqar("Baho qo'yilgan kunlar", cur.fetchall())


    cur.execute("SELECT COUNT(*) FROM oquvchilar")
    print(f"\n  Maktabda jami: {cur.fetchone()[0]} ta o'quvchi")

    cur.execute("""
        SELECT MIN(tugilgan_yil), MAX(tugilgan_yil)
        FROM oquvchilar
    """)
    eng_kichik, eng_katta = cur.fetchone()
    print(f"  Eng kichik tug'ilgan yil: {eng_kichik}")
    print(f"  Eng katta tug'ilgan yil:  {eng_katta}")

    cur.execute("SELECT AVG(ball) FROM baholar")
    print(f"  Maktab bo'yicha o'rtacha ball: {cur.fetchone()[0]:.2f}")


    cur.execute("SELECT MIN(ball), MAX(ball) FROM baholar")
    eng_past, eng_yuqori = cur.fetchone()
    print(f"  Eng past baho: {eng_past},  eng yuqori baho: {eng_yuqori}")


    cur.execute("""
        SELECT sinf, COUNT(*) AS oquvchilar_soni
        FROM oquvchilar
        GROUP BY sinf
        ORDER BY sinf
    """)
    chiqar("Sinflar bo'yicha o'quvchilar soni", cur.fetchall())
    
    cur.execute("""
        SELECT f.nomi, ROUND(AVG(b.ball), 2) AS ortacha_ball,
               COUNT(b.id) AS baholar_soni
        FROM fanlar f
        JOIN baholar b ON f.id = b.fan_id
        GROUP BY f.id
        ORDER BY ortacha_ball DESC
    """)
    chiqar("Fanlar bo'yicha o'rtacha ball va baholar soni",
           cur.fetchall())

    cur.execute("""
        SELECT o.ism || ' ' || o.familiya AS oquvchi,
               o.sinf,
               ROUND(AVG(b.ball), 2) AS ortacha_ball,
               COUNT(b.id) AS fanlar_soni
        FROM oquvchilar o
        JOIN baholar b ON o.id = b.oquvchi_id
        GROUP BY o.id
        ORDER BY ortacha_ball DESC
    """)
    chiqar("O'quvchilar reytingi (o'rtacha ball bo'yicha)",
           cur.fetchall())

    cur.execute("""
        SELECT o.sinf, ROUND(AVG(b.ball), 2) AS sinf_ortachasi
        FROM oquvchilar o
        JOIN baholar b ON o.id = b.oquvchi_id
        GROUP BY o.sinf
        ORDER BY sinf_ortachasi DESC
    """)
    chiqar("Sinflarning o'rtacha bahosi", cur.fetchall())





    cur.execute("""
        SELECT o.ism || ' ' || o.familiya AS oquvchi,
               ROUND(AVG(b.ball), 2) AS ortacha
        FROM oquvchilar o
        JOIN baholar b ON o.id = b.oquvchi_id
        GROUP BY o.id
        HAVING ortacha > 85
        ORDER BY ortacha DESC
    """)
    chiqar("A'lochi o'quvchilar (o'rtacha > 85)", cur.fetchall())

    cur.execute("""
        SELECT sinf, COUNT(*) AS soni
        FROM oquvchilar
        GROUP BY sinf
        HAVING COUNT(*) > 3
    """)
    chiqar("3 dan ortiq o'quvchisi bor sinflar", cur.fetchall())

    cur.execute("""
        SELECT f.nomi, ROUND(AVG(b.ball), 2) AS ortacha
        FROM fanlar f
        JOIN baholar b ON f.id = b.fan_id
        GROUP BY f.id
        HAVING ortacha > 80
        ORDER BY ortacha DESC
    """)
    chiqar("O'quvchilar yaxshi o'zlashtirayotgan fanlar (>80)",
           cur.fetchall())


    cur.execute("""
        SELECT o.ism || ' ' || o.familiya AS oquvchi,
               o.sinf,
               o.tugilgan_yil,
               ROUND(AVG(b.ball), 2) AS ortacha_ball
        FROM oquvchilar o
        JOIN baholar b ON o.id = b.oquvchi_id
        WHERE o.sinf IN ('10-A', '10-B')
          AND o.tugilgan_yil = 2010
        GROUP BY o.id
        HAVING ortacha_ball > 80
        ORDER BY ortacha_ball DESC
    """)
    chiqar("DIREKTOR HISOBOTI: 10-sinf 2010-yil tug'ilganlar reytingi",
           cur.fetchall())



    print("\n" + "=" * 65)
    print("  Dars yakuniga yetdi. Mustaqil vazifalarni bajaring!")
    print("=" * 65)