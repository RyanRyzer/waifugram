import bcrypt
from utils.database import cursor, conn


def register_user(username, email, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    existing = cursor.fetchone()

    if existing:
        return False

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users
        (username, email, password)
        VALUES (?, ?, ?)
        """,
        (
            username,
            email,
            hashed
        )
    )

    conn.commit()

    return True


def login_user(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if user:

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):
            return True

    return False