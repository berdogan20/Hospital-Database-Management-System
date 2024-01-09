export class Patient {
    patientId: number;
    firstName: string;
    lastName: string;
    email: string;
    phoneNumber: string;
    birthDate: Date;
    age: number;
    sex: string;
    address: string;
    insuranceDetails: string;

    constructor(
        patientId: number,
        firstName: string,
        lastName: string,
        email: string,
        phoneNumber: string,
        birthDate: Date,
        age: number,
        sex: string,
        address: string,
        insuranceDetails: string
    ) {
        this.patientId = patientId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.birthDate = birthDate;
        this.age = age;
        this.sex = sex;
        this.address = address;
        this.insuranceDetails = insuranceDetails;
    }
}
