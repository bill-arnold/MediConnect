# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    experience_years = Column(Integer)
    location = Column(String)
    contact_number = Column(String)

    patients = relationship("DoctorPatient", back_populates="doctor")

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    contact_number = Column(String)
    address = Column(String)

    doctors = relationship("DoctorPatient", back_populates="patient")
    diseases = relationship("DoctorPatient", back_populates="disease")

class Disease(Base):
    __tablename__ = 'diseases'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    severity = Column(String)
    symptoms = Column(String)
    treatment = Column(String)

    patients = relationship("DoctorPatient", back_populates="disease")

class DoctorPatient(Base):
    __tablename__ = 'doctor_patient'
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    disease_id = Column(Integer, ForeignKey('diseases.id'))

    doctor = relationship("Doctor", back_populates="patients")
    patient = relationship("Patient", back_populates="doctors")
    disease = relationship("Disease", back_populates="patients")
