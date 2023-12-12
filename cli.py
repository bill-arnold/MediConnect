# cli.py
import click
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Doctor, Patient, Disease, DoctorPatient

# Initialize the database
@click.command("init-db")
def init_db():
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized")

# Add a new doctor
@click.command("add-doctor")
def add_doctor():
    name = click.prompt("Doctor's name")
    specialization = click.prompt("Specialization")
    experience = click.prompt("Experience (years)", type=int)
    location = click.prompt("Location")
    contact_number = click.prompt("Contact Number", type=int)

    doctor = Doctor(name=name, specialization=specialization, experience_years=experience, location=location, contact_number=contact_number)
    
    db = SessionLocal()
    db.add(doctor)
    db.commit()
    db.close()

    click.echo("Doctor added successfully")

# Add a new patient
@click.command("add-patient")
def add_patient():
    name = click.prompt("Patient's name")
    age = click.prompt("Age", type=int)
    gender = click.prompt("Gender")
    contact_number = click.prompt("Contact Number", type=int)
    address = click.prompt("Address")

    patient = Patient(name=name, age=age, gender=gender, contact_number=contact_number, address=address)
    
    db = SessionLocal()
    db.add(patient)
    db.commit()
    db.close()

    click.echo("Patient added successfully")

# Add a new disease
@click.command("add-disease")
def add_disease():
    name = click.prompt("Disease name")
    severity = click.prompt("Severity")
    symptoms = click.prompt("Symptoms")
    treatment = click.prompt("Treatment")

    disease = Disease(name=name, severity=severity, symptoms=symptoms, treatment=treatment)
    
    db = SessionLocal()
    db.add(disease)
    db.commit()
    db.close()

    click.echo("Disease added successfully")

# Add a new doctor_patient entry
@click.command("add-doctor-patient")
def add_doctor_patient():
    doctor_id = click.prompt("Doctor's ID", type=int)
    patient_id = click.prompt("Patient's ID", type=int)
    disease_id = click.prompt("Disease's ID", type=int)

    doctor_patient = DoctorPatient(doctor_id=doctor_id, patient_id=patient_id, disease_id=disease_id)
    
    db = SessionLocal()
    db.add(doctor_patient)
    db.commit()
    db.close()

    click.echo("Doctor-Patient entry added successfully")

# List all entries in the doctor_patient table
@click.command("list-doctor-patient")
def list_doctor_patient():
    db = SessionLocal()
    doctor_patient_entries = db.query(DoctorPatient).all()
    db.close()

    for entry in doctor_patient_entries:
        click.echo(entry.__dict__)

# Create the CLI instance and add commands
@click.group()
def cli():
    pass

cli.add_command(init_db)
cli.add_command(add_doctor)
cli.add_command(add_patient)
cli.add_command(add_disease)
cli.add_command(add_doctor_patient)
cli.add_command(list_doctor_patient)

if __name__ == "__main__":
    cli()
