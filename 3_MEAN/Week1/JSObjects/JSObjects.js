let students = [
    {name: 'Remy', cohort: 'Jan'},
    {name: 'Genevieve', cohort: 'March'},
    {name: 'Chuck', cohort: 'Jan'},
    {name: 'Osmund', cohort: 'June'},
    {name: 'Nikki', cohort: 'June'},
    {name: 'Boris', cohort: 'June'}
];

for(var i = 0; i < students.length; i++){
    let str = '';
    for(let x in students[i]){
        str += " " + x + ': ' + students[i][x] + ",";
    }
    str = str.slice(0, -1);
    console.log(str)
}


let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
 };

for(let x in users){
    console.log(x)
    for(var i = 0; i < users[x].length; i++){
        let str = '';
        for(let val in users[x][i]){
            str += " " + val + ': ' + users[x][i][val] + ",";
        }
        str = str.slice(0, -1);
        console.log(str)
    }
}
