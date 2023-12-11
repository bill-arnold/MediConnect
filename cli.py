# cli.py
import click
from models import Doctor, Patient, Disease, DoctorPatient
from database import Base, engine, SessionLocal

@click.group()
def cli():
    pass

@click.command(name="init-db")
def init_db():
    """Initialize the database."""
    click.echo("Creating tables...")
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized.")

# ... (your existing commands)

@click.command(name="add-doctor")
@click.option("--name", prompt="Doctor's name", help="Name of the doctor")
@click.option("--specialization", prompt="Specialization", help="Specialization of the doctor")
def add_doctor(name, specialization):
    """Add a new doctor."""
    session = SessionLocal()
    doctor = Doctor(name=name, specialization=specialization)
    session.add(doctor)
    session.commit()
    click.echo(f"Doctor {name} added successfully with ID: {doctor.id}")
    session.close()

@click.command(name="add-patient")
@click.option("--name", prompt="Patient's name", help="Name of the patient")
@click.option("--age", prompt="Patient's age", type=int, help="Age of the patient")
def add_patient(name, age):
    """Add a new patient."""
    session = SessionLocal()
    patient = Patient(name=name, age=age)
    session.add(patient)
    session.commit()
    click.echo(f"Patient {name} added successfully with ID: {patient.id}")
    session.close()

# Similar commands for adding diseases and doctor-patient relationships...

# Add the new commands to the CLI
cli.add_command(init_db)
cli.add_command(add_doctor)
cli.add_command(add_patient)
# Add similar lines for add-disease and add-doctor-patient

if __name__ == "__main__":
    cli()
