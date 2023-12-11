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

@click.command(name="list-doctors")
def list_doctors():
    """List all doctors."""
    session = SessionLocal()
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        click.echo(f"Doctor ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}")

@click.command(name="list-patients")
def list_patients():
    """List all patients."""
    session = SessionLocal()
    patients = session.query(Patient).all()
    for patient in patients:
        click.echo(f"Patient ID: {patient.id}, Name: {patient.name}, Age: {patient.age}")

@click.command(name="list-diseases")
def list_diseases():
    """List all diseases."""
    session = SessionLocal()
    diseases = session.query(Disease).all()
    for disease in diseases:
        click.echo(f"Disease ID: {disease.id}, Name: {disease.name}, Severity: {disease.severity}")

cli.add_command(init_db)
cli.add_command(list_doctors)
cli.add_command(list_patients)
cli.add_command(list_diseases)

if __name__ == "__main__":
    cli()
