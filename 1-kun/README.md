FastAPI bilan tanishish
Birinchi API yozish
GET method va path parameter tushunish

FastAPI — bu Python’da backend (API) yozish uchun ishlatiladigan zamonaviy framework.

Request (so‘rov) qabul qiladi
Javob (response) qaytaradi
JSON formatda ishlaydi

⚙️ O‘rnatish
pip install fastapi uvicorn

🚀 Serverni ishga tushirish
uvicorn main --reload

Tekshirish
Brauzerda:
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Endpoint = URL + funksiya

Misol:
@app.get("/")

HTTP methodlar
GET → ma’lumot olish
POST → ma’lumot yuborish
PUT → yangilash
DELETE → o‘chirish

💻 Amaliy mashqlar
1. Salomlashish API:
/hello/{name}
2. Sonni 2 ga ko‘paytirish:
/double/{number}
3. Kvadrat hisoblash:
/square/{number}

🎯 Xulosa

Bugun:

FastAPI nima ekanini o‘rgandim
Birinchi API yozdim
GET method bilan ishladim
Path parameter tushundim