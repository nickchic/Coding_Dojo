var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

for(var i = 0; i < students.length; i++){
    console.log(students[i].first_name, students[i].last_name);
}


var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }


for(var x in users){

    console.log(x);
    for(var i = 0; i < users[x].length; i++){

        var nameLength = users[x][i].first_name.length + users[x][i].last_name.length;

        console.log(i + " - " + users[x][i].first_name + " " + users[x][i].last_name + " - " + nameLength);

    }

}
