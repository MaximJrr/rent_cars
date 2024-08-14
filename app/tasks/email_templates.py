from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_rent_confirmation_template(rent: dict, email_to: EmailStr):
    email = EmailMessage()
    email["Subject"] = f"Hello, dear {rent.get('name')}"
    email["From"] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
        <h1>Confirm the rent</h1>
        You rented car from {rent["date_to"]} to {rent["date_to"]}.
        Total price: {rent["total_price"]}. Total days: {rent["total_days"]}.
        We called you from the number +ХХХХХХХХХ within 30 minutes to confirm the rent.
        """,
        subtype="html"
    )

    return email
