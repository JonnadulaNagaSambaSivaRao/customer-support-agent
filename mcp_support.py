import sqlite3
from mcp.server.fastmcp import FastMCP

DB_PATH = "support.db"

mcp = FastMCP("customer-support")


def get_connection():
    return sqlite3.connect(DB_PATH)


@mcp.tool()
def search_tickets(
    customer_name: str = "",
    status: str = "",
    priority: str = "",
    keyword: str = "",
) -> list[dict]:
    """
    Search support tickets using customer name, status, priority,
    or keyword.
    """

    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """
        SELECT *
        FROM tickets
        WHERE 1=1
    """

    params = []

    if customer_name:
        query += " AND LOWER(customer_name) LIKE LOWER(?)"
        params.append(f"%{customer_name}%")

    if status:
        query += " AND LOWER(status) = LOWER(?)"
        params.append(status)

    if priority:
        query += " AND LOWER(priority) = LOWER(?)"
        params.append(priority)

    if keyword:
        query += """
            AND (
                LOWER(subject) LIKE LOWER(?)
                OR LOWER(description) LIKE LOWER(?)
            )
        """
        params.append(f"%{keyword}%")
        params.append(f"%{keyword}%")

    query += " ORDER BY id DESC"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    results = [dict(row) for row in rows]

    conn.close()

    return results


@mcp.tool()
def get_ticket(ticket_id: int) -> dict:
    """
    Retrieve complete details for a specific ticket.
    """

    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tickets WHERE id = ?",
        (ticket_id,),
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return {
            "success": False,
            "message": f"Ticket {ticket_id} was not found.",
        }

    return {
        "success": True,
        "ticket": dict(row),
    }


@mcp.tool()
def update_ticket(
    ticket_id: int,
    status: str = "",
    priority: str = "",
    assigned_to: str = "",
) -> dict:
    """
    Update a support ticket.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tickets WHERE id = ?",
        (ticket_id,),
    )

    ticket = cursor.fetchone()

    if ticket is None:
        conn.close()

        return {
            "success": False,
            "message": f"Ticket {ticket_id} was not found.",
        }

    updates = []
    params = []

    if status:
        updates.append("status = ?")
        params.append(status)

    if priority:
        updates.append("priority = ?")
        params.append(priority)

    if assigned_to:
        updates.append("assigned_to = ?")
        params.append(assigned_to)

    if not updates:
        conn.close()

        return {
            "success": False,
            "message": "No fields were provided for update.",
        }

    updates.append("updated_at = CURRENT_TIMESTAMP")

    params.append(ticket_id)

    query = f"""
        UPDATE tickets
        SET {", ".join(updates)}
        WHERE id = ?
    """

    cursor.execute(query, params)

    conn.commit()

    cursor.execute(
        "SELECT * FROM tickets WHERE id = ?",
        (ticket_id,),
    )

    updated_ticket = cursor.fetchone()

    columns = [column[0] for column in cursor.description]

    result = dict(zip(columns, updated_ticket))

    conn.close()

    return {
        "success": True,
        "message": f"Ticket {ticket_id} updated successfully.",
        "ticket": result,
    }


@mcp.tool()
def create_ticket(
    customer_name: str,
    email: str,
    subject: str,
    description: str,
    priority: str = "medium",
) -> dict:
    """
    Create a new support ticket.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (
            customer_name,
            email,
            subject,
            description,
            priority,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            customer_name,
            email,
            subject,
            description,
            priority,
            "open",
        ),
    )

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return {
        "success": True,
        "message": "Ticket created successfully.",
        "ticket_id": ticket_id,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")