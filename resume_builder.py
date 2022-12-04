class Resume:
    # Define a resume class, whose instance variables will be inputs that user gives  
    def __init__(self, personal_info, skills, work_experience, ) -> None:
        self.personal_info = personal_info
        self.skills = skills
        self.work_experience = work_experience
    def get_info(self):
        # print(self.personal_info)
        return self.personal_info
    def get_skills(self):
        # print(self.skills)
        return self.skills
    def get_work_experience(self):
        # print(self.work_experience)
        return self.work_experience
    
def main():
    personal_info, skills, work_experience = {}, [], {}
    name = input("Enter your full name: ")
    objective = input("Enter your objective: ")
    school = input("Enter your objective: ")
    gpa = input("Enter your objective: ")
    personal_info["name"] = name
    personal_info["objective"] = objective
    personal_info["school"] = school

    personal_info["gpa"] = gpa
    skill_sentence = input("Enter your skills separated by a comma: ")
    skill_sentence = skill_sentence.split(",")
    for skill in skill_sentence:
        skills.append(skill)
    num_experiences = int(input("Enter number of work experiences you would like to add: "))
    for num in num_experiences:
        title = input("Enter your title in work experience: ")
        startDate = input("Enter start date of work (format: mm/yy): ")
        endDate = input("Enter end date of work (format: mm/yy): ")
        desc = input("Enter description of work, separated by commas (example: Functionalized over 400 COVID-19 test kits through use of HPLC and chlorometric assays): ")
        work_experience[num] = [title] + [startDate] + [endDate] + [desc]
    resume = Resume(personal_info=personal_info, skills=skills, work_experience=work_experience)
    resume.get_info()
    resume.get_skills()
    resume.get_work_experience()

if __name__ == "__main__":
    main()