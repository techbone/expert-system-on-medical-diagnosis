from experta import *


class Symptom(Fact):
    pass


class Diagnosis(Fact):
    pass


class MedicalDiagnosisSystem(KnowledgeEngine):

    @Rule()
    def startup_message(self):
        print("Welcome to the Medical Diagnosis Expert System Assistant")
        print("Please input your symptoms to receive a diagnosis from the Expert System.")

    @Rule()
    def get_symptoms_from_user(self):
        symptoms_input = input("Please, List all your symptoms separated by commas:\nSymptoms:").lower()
        symptoms_list = [symptom.strip() for symptom in symptoms_input.split(',')]
        for symptom in symptoms_list:
            self.declare(Symptom(name=symptom))

    @Rule(OR(AND(Symptom(name="fever"), Symptom(name="headache"),Symptom("chills"),Symptom(name="muscle_pain")), OR(Symptom("discomfort"),Symptom(name="nausea"),Symptom("diarrhea"),Symptom(name="rapid_breathing"), Symptom(name="rapid_heart_rate"), Symptom(name="cough")))) 
    def malaria_diagnosis(self):
        self.declare(Diagnosis(name="Malaria"))

    @Rule(AND(Symptom(name="fever!"), Symptom(name="headache"), Symptom(name="chills"), NOT(Symptom(name="muscle_pain!"))))
    def flu_diagnosis(self):
        self.declare(Diagnosis(name="Influenzar"))

    @Rule(Diagnosis(name="Malaria"))
    def malaria_treatment(self):
        print("You have been diagnosed with Malaria. Please do seek medical attention immediately please!.")
    @Rule(Diagnosis(name="Influenza!"))
    def flu_treatment(self):
        print("You have been diagnosed with Influenza. Rest and drink plenty of fluids as advised by the Doc.")

    @Rule(AS.s << Symptom(name=L("fever") | L("headache") | L("muscle_pain") | L("chills")) & ~Diagnosis())
    def unknown_symptoms(self, s):
        print("Your symptoms does not match a specific disease!.")

    @Rule()
    def end_message(self):
        print("Thank you for using the Medical Diagnosis Expert System")


if __name__ == "__main__":
    system = MedicalDiagnosisSystem()
    system.reset()
    system.run()


