# cli.py
import click
from models import Doctor, Patient, Disease, DoctorPatient  # Import DoctorPatient model
from database import Base, engine, SessionLocal

@click.group()
def cli():
    pass

@click.command(name="init-db")  # Update the command name
def init_db():
    """Initialize the database."""
    click.echo("Creating tables...")
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized.")

@click.command(name="list-doctors")  # Update the command name
def list_doctors():
    """List all doctors."""
    session = SessionLocal()
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        click.echo(f"Doctor ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}")

@click.command(name="list-patients")  # Update the command name
def list_patients():
    """List all patients."""
    session = SessionLocal()
    patients = session.query(Patient).all()
    for patient in patients:
        click.echo(f"Patient ID: {patient.id}, Name: {patient.name}, Age: {patient.age}")

@click.command(name="list-diseases")  # Update the command name
def list_diseases():
    """List all diseases."""
    session = SessionLocal()
    diseases = session.query(Disease).all()
    for disease in diseases:
        click.echo(f"Disease ID: {disease.id}, Name: {disease.name}, Severity: {disease.severity}")

@click.command(name="list-doctor-patient")  # New command to list doctor_patient table
def list_doctor_patient():
    """List all entries in doctor_patient table."""
    session = SessionLocal()
    doctor_patients = session.query(DoctorPatient).all()
    for dp in doctor_patients:
        click.echo(f"DoctorPatient ID: {dp.id}, Doctor ID: {dp.doctor_id}, Patient ID: {dp.patient_id}, Disease ID: {dp.disease_id}")

cli.add_command(init_db)
cli.add_command(list_doctors)
cli.add_command(list_patients)
cli.add_command(list_diseases)
cli.add_command(list_doctor_patient)  

if __name__ == "__main__":
    cli()
