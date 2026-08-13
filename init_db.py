import sqlite3

DB_PATH = "support.db"


def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM tickets")
    count = cursor.fetchone()[0]

    if count == 0:
        tickets = [
            (
                "John",
                "john@example.com",
                "Payment failed",
                "My payment failed while purchasing the premium plan.",
                "high",
                "open",
                "Alice",
            ),
            (
                "John",
                "john@example.com",
                "Unable to login",
                "I cannot login to my customer portal.",
                "medium",
                "open",
                "Bob",
            ),
            (
                "Sarah",
                "sarah@example.com",
                "Refund request",
                "I would like to request a refund for my subscription.",
                "high",
                "open",
                "Alice",
            ),
            (
                "Michael",
                "michael@example.com",
                "Password reset",
                "Password reset email is not arriving.",
                "low",
                "resolved",
                "Bob",
            ),
            (
                "David",
                "david@example.com",
                "Account locked",
                "My account has been locked after multiple attempts.",
                "high",
                "open",
                "Alice",
            ),
        ]

        cursor.executemany("""
            INSERT INTO tickets (
                customer_name,
                email,
                subject,
                description,
                priority,
                status,
                assigned_to
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, tickets)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_database()