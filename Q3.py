#Task-4
football = {"prince", "Akshay", "Seema", "Rajnish"}
cricket= {"Akshay", "Seema", "Tamanna", "Sarthak"}

both = football & cricket
only_football = football - cricket
only_cricket = cricket - football

students = {"prince", "Akshay", "Seema", "Rajnish", "Tamanna", "Sarthak"}
neither = students - (football | cricket)

print("Students who play both football and cricket:", both)
print("Students who  only play football:", only_football)
print("Students who  only play cricket:", only_cricket)
print("Students who play neither football nor cricket:", neither)
