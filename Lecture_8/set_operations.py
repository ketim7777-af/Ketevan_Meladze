frontend_skills = {"HTML", "CSS", "JavaScript", "React"} 
backend_skills = {"Python", "JavaScript", "SQL", "React"}

# გაერთიანება ორი მეთოდით
print(frontend_skills.union(backend_skills))
print(frontend_skills | backend_skills)

# თანაკვეთა ორი მეთოდით
print(frontend_skills.intersection(backend_skills))
print(frontend_skills & backend_skills)

# სხვაობა ორი მეთოდით
print(frontend_skills.difference(backend_skills))
print(frontend_skills - backend_skills)


# სიმეტრიული სხვაობა ორი მეთოდით
print(frontend_skills.symmetric_difference(backend_skills))
print(frontend_skills ^ backend_skills)