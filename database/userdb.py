import aiosqlite

DATABASE = 'users.db'

async def setup_database():
    async with aiosqlite.connect(DATABASE) as db:
        # Jadval yaratish: users
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Foydalanuvchi uchun unikal identifikator
                name TEXT NOT NULL,                      -- Ismi
                surname TEXT NOT NULL,                   -- Familyasi
                age INTEGER NOT NULL,                    -- Yoshi
                phone_number TEXT UNIQUE,                -- Telefon raqami
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Jadval yaratish: cards
        await db.execute('''
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Karta uchun unikal identifikator
                user_id INTEGER NOT NULL,                -- `users` jadvaliga tashqi kalit
                card_number TEXT UNIQUE,                 -- Karta raqami
                card_pin TEXT NOT NULL,                  -- Karta PIN kodi
                balance DECIMAL(15, 2) DEFAULT 0.00,     -- Karta balans summasi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        # Jadval yaratish: transactions
        await db.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Transaksiya uchun unikal identifikator
                card_id INTEGER NOT NULL,                 -- `cards` jadvaliga tashqi kalit
                transaction_type TEXT NOT NULL,           -- Amal turi (deposit, withdrawal, payment)
                amount DECIMAL(15, 2) NOT NULL,           -- Transaksiya summasi
                description TEXT,                         -- To'lov izohi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (card_id) REFERENCES cards(id)
            )
        ''')

        # Jadval yaratish: services
        await db.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Xizmat uchun unikal identifikator
                name TEXT NOT NULL,                       -- Xizmat nomi
                provider TEXT,                            -- Xizmat ko'rsatuvchi nomi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Jadval yaratish: payments
        await db.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- To'lov uchun unikal identifikator
                card_id INTEGER NOT NULL,                 -- `cards` jadvaliga tashqi kalit
                service_id INTEGER NOT NULL,              -- `services` jadvaliga tashqi kalit
                amount DECIMAL(15, 2) NOT NULL,           -- To'lov summasi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (card_id) REFERENCES cards(id),
                FOREIGN KEY (service_id) REFERENCES services(id)
            )
        ''')

        # Jadval yaratish muvaffaqiyatli yakunlandi
        print("Database and tables setup complete!")
