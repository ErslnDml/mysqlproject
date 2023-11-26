import mysql.connector
    
class Kedi:
    
    def __init__(self):
        pass
    def createdatabase(self):
        self.mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="kedimama"
        )
        self.mycursor= self.mysqldb.cursor()
        # self.mycursor.execute("CREATE DATABASE kedimama")
    
    def createtable1(self):
        self.mycursor.execute("""CREATE TABLE royalcanin (
         icerik CHAR(180) NOT NULL,
         aramo  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def createtable2(self):
        self.mycursor.execute("""CREATE TABLE reflex (
         icerik CHAR(180) NOT NULL,
         aramo  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()
    def ekleroyalcanin(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.icerik=input("İçerik girin :(Tahıllı/Tahılsız/Düşük Tahıllı)")
            self.aroma=input("Aroma girin :(Tavuk,Et,Gurme v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin/Yaşlı)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO royalcanin values('{}','{}','{}','{}')".format(self.icerik,self.aroma,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")

    def eklereflex(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.icerik=input("İçerik girin :(Tahıllı/Tahılsız/Düşük Tahıllı)")
            self.aroma=input("Aroma girin :(Tavuk,Et,Gurme v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin/Yaşlı)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO reflex values('{}','{}','{}','{}')".format(self.icerik,self.aroma,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")

    def silroyalcanin(self):
        self.mycursor.execute("DELETE FROM royalcanin WHERE yas='Yavru' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def silreflex(self):
        self.mycursor.execute("DELETE FROM reflex WHERE icerik='Tahılsız' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def gosterroyalcanin(self):
        self.mycursor.execute("SELECT * FROM royalcanin")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")
    def gosterreflex(self):
        self.mycursor.execute("SELECT * FROM reflex")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")
x=Kedi()
x.createdatabase()
# x.createtable1()
# x.createtable2()
# x.ekleroyalcanin()
# x.eklereflex()
# x.silroyalcanin()
# x.silreflex()
# x.gosterroyalcanin()
# x.gosterreflex()


class Köpek:
    def createdatabase(self):
        self.mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="köpekmama"
        
        )
        self.mycursor= self.mysqldb.cursor()
        # self.mycursor.execute("CREATE DATABASE köpekmama")
    
    def createtable1(self):
        self.mycursor.execute("""CREATE TABLE enjoy(
         icerik CHAR(180) NOT NULL,
         aramo  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def createtable2(self):
        self.mycursor.execute("""CREATE TABLE proplan (
         icerik CHAR(180) NOT NULL,
         aramo  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def ekleenjoy(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.icerik=input("İçerik girin :(Tahıllı/Tahılsız/Düşük Tahıllı)")
            self.aroma=input("Aroma girin :(Tavuk,Et,Gurme v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin/Yaşlı)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO enjoy values('{}','{}','{}','{}')".format(self.icerik,self.aroma,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")

    def ekleproplan(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.icerik=input("İçerik girin :(Tahıllı/Tahılsız/Düşük Tahıllı)")
            self.aroma=input("Aroma girin :(Tavuk,Et,Gurme v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin/Yaşlı)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO proplan values('{}','{}','{}','{}')".format(self.icerik,self.aroma,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")
        
    def silenjoy(self):
        self.mycursor.execute("DELETE FROM enjoy WHERE icerik='tahıllı' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def silproplan(self):
        self.mycursor.execute("DELETE FROM proplan WHERE icerik='tahılsız' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def gosterenjoy(self):
        self.mycursor.execute("SELECT * FROM enjoy")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")
    def gosterproplan(self):
        self.mycursor.execute("SELECT * FROM proplan")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")

x=Köpek()
x.createdatabase()
# x.createtable1()
# x.createtable2()
# x.ekleenjoy()
# x.ekleproplan()
# x.silenjoy()
# x.silproplan()
# x.gosterenjoy()
# x.gosterproplan()

class Kuş:
    def createdatabase(self):
        self.mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="kusyemi"
        
        )
        self.mycursor= self.mysqldb.cursor()
        # self.mycursor.execute("CREATE DATABASE kusyemi")
    
    def createtable1(self):
        self.mycursor.execute("""CREATE TABLE goldwings(
         cins CHAR(180) NOT NULL,
         şekil  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def createtable2(self):
        self.mycursor.execute("""CREATE TABLE jungle (
         cins CHAR(180) NOT NULL,
         şekil  CHAR(180),
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def eklegoldwings(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.cins=input("Cins girin :(Kanarya,Papağan,Muhabbet Kuşu v.b.)")
            self.sekil=input("Şekil girin :(Çubuk,Granül v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO goldwings values('{}','{}','{}','{}')".format(self.cins,self.sekil,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")

    def eklejungle(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.cins=input("Cins girin :(Kanarya,Papağan,Muhabbet Kuşu v.b.)")
            self.sekil=input("Şekil girin :(Çubuk,Granül v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO jungle values('{}','{}','{}','{}')".format(self.cins,self.sekil,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")
        
    def silgoldwings(self):
        self.mycursor.execute("DELETE FROM goldwings WHERE şekil='Çubuk' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def siljungle(self):
        self.mycursor.execute("DELETE FROM jungle WHERE yas='1' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def gostergoldwings(self):
        self.mycursor.execute("SELECT * FROM goldwings")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")
    def gosterjungle(self):
        self.mycursor.execute("SELECT * FROM jungle")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")

x=Kuş()
x.createdatabase()
# x.createtable1()
# x.createtable2()
# x.eklegoldwings()
# x.eklejungle()
# x.silgoldwings()
# x.siljungle()
# x.gostergoldwings()
# x.gosterjungle()

class Balik:
    def createdatabase(self):
        self.mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="balikyemi"
        
        )
        self.mycursor= self.mysqldb.cursor()
        # self.mycursor.execute("CREATE DATABASE balikyemi")
    
    def createtable1(self):
        self.mycursor.execute("""CREATE TABLE ahm(
         tip CHAR(180) NOT NULL,
         yas CHAR(180),
         agirlik INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def createtable2(self):
        self.mycursor.execute("""CREATE TABLE rotifish (
         tip CHAR(180) NOT NULL,
         yas CHAR(180),
         agirlik  INT
        
         )""")
        self.mysqldb.commit()
        self.mysqldb.close()

    def ekleahm(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.tip=input("Tip girin :(Canlı/Tablet/Özel Yem v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO ahm values('{}','{}','{}')".format(self.tip,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")

    def eklerotifish(self):
        sayi=int(input("Kaç adet ürün eklemek istersiniz:"))
        for i in range(sayi):
            self.tip=input("Tip girin :(Canlı/Tablet/Özel Yem v.b.)")
            self.yas=input("Yas  girin :(Yavru/Yetişkin)")
            self.agirlik=int(input("Mama ağırlığını giriniz :"))
            
            sql = "INSERT INTO rotifish values('{}','{}','{}')".format(self.tip,self.yas,self.agirlik)
            self.mycursor.execute(sql)
            self.mysqldb.commit()   
            print(" Veri Eklendi")
        
    def silahm(self):
        self.mycursor.execute("DELETE FROM ahm WHERE yas='Yavru' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def silrotifish(self):
        self.mycursor.execute("DELETE FROM rotifish WHERE agirlik='200' ")
        self.mysqldb.commit()
        print(" Veri Silindi")
    def gosterahm(self):
        self.mycursor.execute("SELECT * FROM ahm")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")
    def gosterrotifish(self):
        self.mycursor.execute("SELECT * FROM rotifish")
        table=self.mycursor.fetchall()
        for i in table:
            print(i)
        print("*******************************************************")

x=Balik()
x.createdatabase()
# x.createtable1()
# x.createtable2()
# x.ekleahm()
# x.eklerotifish()
# x.silahm()
# x.silrotifish()
# x.gosterahm()
# x.gosterrotifish()












while True:
            menu = input("""Menu
            --------------
            1-Kedimaması içerisindeki royal tablosu görüntüle
            2-Kedimaması içerisindeki reflex tablosu görüntüle
            3-Köpekmaması içerisindeki enjoy tablosu görüntüle
            4-Köpekmaması içerisindeki proplan tablosu görüntüle
            5-Kuşyemi içerisindeki goldwings tablosu görüntüle
            6-Kuşyemi içerisindeki  jungle tablosu görüntüle
            7-Balıkyemi içerisindeki  ahm tablosu görüntüle
            8-Balıkyemi içerisindeki  rotifish tablosu görüntüle
            """)
            if menu == "1":
                print("*********Royal Kedi Maması***********")
                a=Kedi()
                a.createdatabase()
                a.gosterroyalcanin()
            elif menu=="2":
                print("*********Reflex Kedi Maması***********")
                a=Kedi()
                a.createdatabase()
                a.gosterreflex()
            elif menu=="3":
                print("*********Enjoy Köpek Maması***********")
                b=Köpek()
                b.createdatabase()
                b.gosterenjoy()
            elif menu=="4":
                print("*********Proplan Köpek Maması***********")
                b=Köpek()
                b.createdatabase()
                b.gosterproplan()
            elif menu=="5":
                print("*********Goldwings Kuş Yemi***********")
                c=Kuş()
                c.createdatabase()
                c.gostergoldwings()
            elif menu=="6":
                print("*********Jungle Kuş Yemi***********")
                c=Kuş()
                c.createdatabase()
                c.gosterjungle()
            elif menu=="7":
                print("*********Ahm Balık Yemi***********")
                d=Balik()
                d.createdatabase()
                d.gosterahm()
            elif menu=="8":
                print("*********RotiFish Balık Yemi***********")
                d=Balik()
                d.createdatabase()
                d.gosterrotifish()
            else:
                print("Yanlış Seçim Yaptınız Ana Menüye Dönünüz!!!!!")